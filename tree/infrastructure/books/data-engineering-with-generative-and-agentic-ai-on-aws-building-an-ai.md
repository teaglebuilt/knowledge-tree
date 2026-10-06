---
title: Data Engineering with Generative and Agentic AI on AWS Building an AI-Augmented
  Data Practice for the Enterprise (Justin J. Leto)
source: books/pdf/Data Engineering with Generative and Agentic AI on AWS Building
  an AI-Augmented Data Practice for the Enterprise (Justin J. Leto) (z-library.sk,
  1lib.sk, z-lib.sk).pdf
source_type: book
source_hash: 511e2fcb375a35a21616a7cadb87de065d31cb42423c5ae404d2a38a7712a0f9
tags:
- infrastructure
- book
extracted: '2026-10-04'
---

# **with Generative and** **Agentic AI on AWS**

##### Building an AI-Augmented Data Practice for the Enterprise — Justin J. Leto
###### _Foreword by Shreyas Subramanian, PhD_ _Principal Data Scientist, AWS_

## **Data Engineering with** **Generative and Agentic** **AI on AWS**

#### **Building an AI-Augmented Data** **Practice for the Enterprise**

**Justin J. Leto**
**_Foreword by Shreyas Subramanian, PhD, Principal Data Scientist, AWS_**

**_Data Engineering with Generative and Agentic AI on AWS: Building an_**
**_AI-Augmented Data Practice for the Enterprise_**

Justin J. Leto
Apress,
Long Island City, NY, USA

ISBN-13 (pbk): 979-8-8688-2198-1 ISBN-13 (electronic): 979-8-8688-2199-8
[https://doi.org/10.1007/979-8-8688-2199-8](https://doi.org/10.1007/979-8-8688-2199-8)
Copyright © 2026 by Justin J. Leto

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the
material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation,
broadcasting, reproduction on microfilms or in any other physical way, and transmission or information
storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now
known or hereafter developed.

Trademarked names, logos, and images may appear in this book. Rather than use a trademark symbol with
every occurrence of a trademarked name, logo, or image we use the names, logos, and images only in an
editorial fashion and to the benefit of the trademark owner, with no intention of infringement of the
trademark.

The use in this publication of trade names, trademarks, service marks, and similar terms, even if they are not
identified as such, is not to be taken as an expression of opinion as to whether or not they are subject to
proprietary rights.

While the advice and information in this book are believed to be true and accurate at the date of publication,
neither the authors nor the editors nor the publisher can accept any legal responsibility for any errors or
omissions that may be made. The publisher makes no warranty, express or implied, with respect to the
material contained herein.

Managing Director, Apress Media LLC: Welmoed Spahr
Acquisitions Editor: Shaul Elson
Developmental Editor: Laura Berendson
Coordinating Editor: Gryffin Winkler

Cover designed by eStudioCalamar

[Cover image by Freepik (www.freepik.com)](https://www.freepik.com)

Distributed to the book trade worldwide by Springer Science+Business Media New York, 1 New York Plaza,
[New York, NY 10004. Phone 1-800-SPRINGER, fax (201) 348-4505, e-mail orders-ny@springer-sbm.com, or](mailto:orders-ny@springer-sbm.com)
[visit www.springeronline.com. Apress Media, LLC is a Delaware LLC and the sole member (owner) is](https://www.springeronline.com)
Springer Science + Business Media Finance Inc (SSBM Finance Inc). SSBM Finance Inc is a **Delaware**
corporation.

[For information on translations, please e-mail booktranslations@springernature.com; for reprint,](mailto:booktranslations@springernature.com)
[paperback, or audio rights, please e-mail bookpermissions@springernature.com.](mailto:bookpermissions@springernature.com)

Apress titles may be purchased in bulk for academic, corporate, or promotional use. eBook versions and
licenses are also available for most titles. For more information, reference our Print and eBook Bulk Sales
[web page at http://www.apress.com/bulk-sales.](http://www.apress.com/bulk-sales)

Any source code or other supplementary material referenced by the author in this book is available to
[readers on GitHub (https://github.com/Apress). For more detailed information, please visit https://www.](https://github.com/Apress)
[apress.com/gp/services/source-code.](https://www.apress.com/gp/services/source-code)

If disposing of this product, please recycle the paper

_For Elsi and Atlas—believing it is possible lifts up the entire world._

### **Table of Contents**

About the Author xxi

About the Technical Reviewer xxiii

Acknowledgments xxv

Foreword xxvii

Introduction xxix

Chapter 1: Introduction to Data Engineering with Generative and Agentic
AI on AWS 1

What Is Covered 6

What Is Data Engineering? 8

People 9

Process 11

Technology 12

The Future of Knowledge Work 12

AWS Cloud for Business Agility 13

The Rise of Generative and Agentic AI 15

What Is Generative and Agentic AI? 17

The Transformer Architecture 21

Anaphora Resolution 21

Long-Range Dependency 22

Entity Resolution 22

Retrieval-Augmented Generation (RAG) 24

Model Context Protocol (MCP) 24

Agentic AI Development with Kiro 26

Agentic AI for a Modern Data Strategy 26

v

Table of Cont t

The Business of Data 27

Data As a Strategic Asset 28

Data-Driven Decision Making 28

Data-Driven Revenue 29

Dark Data 30

Business Alignment 31

Theoretical Concepts in Data Engineering 33

Distributed Computing 33

The CAP Theorem 35

Consistency 36

Availability 36

Partition Tolerance 36

Scalability 38

Summary 41

Chapter 2: Data Security and Governance 43

Data Governance 44

The Evolving Data Governance Challenge 46

The Growth of Unstructured Data 46

Government Regulations for Data and AI 46

Data Governance for Generative and Agentic AI 46

The Shared Responsibility Model 47

AWS Identity and Access Management (AWS IAM) 48

Principals 48

Entities, Roles, and Policies 49

The Anatomy of an IAM Policy 51

Principle of Least Privilege 52

IAM Authentication for Data Services 54

Encryption for Data Protection 56

Encryption Key Management 57

Encrypting Data-at-Rest 60

Encrypting Data-in-Transit 61

vi

Table of Cont t

Sensitive Data Detection and Redaction 62

Data Governance on AWS 62

Data Governance Roles 64

Fine-Grained Access Control for Data 64

Generative and Agentic AI Security 65

Supply Chain Attack 66

Sensitive Data Leakage 67

Confused Deputy 68

Hallucination 69

Prompt Injection Attack 69

Guardrails 70

Safeguards in Amazon Bedrock 71

AI-Powered Security with the AWS Security Agent 73

Model Context Protocol (MCP) Security 77

Inbound and Outbound Authentication 79

OAuth for MCP 80

MCP Servers As OAuth Resource Server 80

MCP Client-Server Request and Authorization Flows 81

Requesting the Authorization Code 84

Exchange the Authorization Code for the Access Token 86

Request for MCP Resource with Access Token 86

Client Credentials Flow for Private MCP Clients 87

IAM Authentication with SigV4 for MCP 89

Compliance and Auditing 90

AWS Config 90

AWS CloudTrail 91

Amazon S3 Server Logging 91

AWS Security Hub 92

AWS Audit Manager 92

vii

Table of Cont t

Disaster Recovery, High Availability, and Backups 93

Disaster Recovery 93

High Availability 96

Summary 97

Chapter 3: Data Lake Design with Apache Iceberg and S3 Tables 99

Separating Analytical and Operational Workloads 100

Lock-In 100

Scalability 101

Vendor-Agnostic Data 101

The Rise of Data Lakes 101

Separation of Data and Compute 102

Schema-on-Write vs. 103

Serialization Formats 104

Text-Based Serialization 104

Advanced Serialization Formats 104

Components of a Data Lake 108

Storage Layer 110

Security and Governance Layer 110

Metadata Management Layer 111

Data Lifecycle Layer 111

Data Ingestion Layer 111

Data Processing Layer 111

Serving Layer 112

Data Lakes on AWS 112

The Medallion Architecture 113

Landing Zone 115

Audit Stage 115

Raw Stage 115

Optimized Stage 116

Conform Stage 116

viii

Table of Cont t

Unified Analytics Stage 116

Published Stage 117

Data Cataloging with AWS Glue 117

Create a Database 118

Create a Crawler 119

Fine-Grained Access Control with AWS Lake Formation 121

Open Table Formats 125

Time Travel 126

Schema Evolution 127

Partition Evolution 127

Concurrency Control 128

Choosing an Open Table Format 129

Apache Iceberg and S3 Tables 129

Create an S3 Table Bucket 130

Configure IAM Policy for S3 Tables 131

Download and Stage S3 Tables Catalog JAR in S3 132

Configure an S3 Tables Spark Session 132

Write Data to S3 Table 134

Selecting from an S3 Tables Bucket Table 135

Updating an S3 Tables Bucket Table 136

Advanced Iceberg Queries on S3 Table 136

Unmanaged Apache Iceberg in S3 138

Create Apache Iceberg Table 138

Update an Apache Iceberg Table 139

Time Travel Feature in Apache Iceberg 140

Metadata for Apache Iceberg Tables 141

Maintenance for Apache Iceberg Tables 144

Unmanaged Apache Iceberg in AWS Glue 145

AWS Glue Spark Configuration 146

ix

Table of Cont t

Apache Iceberg Operations in Spark 146

Create an Iceberg Table 147

Writing Data to an Iceberg Table 147

Update an Iceberg Table 148

Perform Time Travel Queries 148

Maintenance of Iceberg Tables in Spark 148

Iceberg Table Maintenance Agent 149

Discovery and Inventory Tools 150

Metrics Collection Tools 150

Analysis and Planning Tools 152

Maintenance Actions 153

Summary 154

Chapter 4: Data Mesh Design with Amazon DataZone 155

Limitations of Centralized Data Lakes 156

Introducing the Data Mesh 157

Data Mesh on AWS with Amazon DataZone 158

Data Governance with DataZone 160

Reorganizing for a Data Mesh Strategy 164

Data Domain Owners 165

The Role of the CoE 166

Implement a Data Mesh with Amazon DataZone 167

Account Governance 168

Create and Configure an Amazon DataZone Domain 170

Configure Lake Formation Hybrid Access Mode for Publishers 174

Publishing Data 176

Consuming Data 183

Summary 188

x

Table of Cont t

Chapter 5: Big Data Processing and Transformation with AWS Glue and
AI Agents 191

Big Data Processing in the Cloud 192

Efficiency 192

Scalability 193

Data Solution Development Lifecycle 194

Data Lake Ingestion 196

Change Data Capture 197

API Service 204

SFTP Server with AWS Transfer Family 207

Data Profiling and Analysis 212

Data Structure 212

Data Quality 213

Descriptive Statistics 213

Relationships Between Variables 213

Data Integrity 213

Profiling and Analysis with Glue DataBrew and AI Agents 213

Data Profiling Q&A with Amazon Q for Business 219

ETL Design and Development 221

Visual ETL Design Tools 222

Amazon SageMaker Unified Studio 227

Notebook-Based Development with Glue Interactive Sessions�������������������������������������������228

SageMaker Catalog 231

AI and ML 231

AI-Assisted ETL Development 231

Data Engineering with Kiro 231

Data Quality with Deequ 240

Deequ Analyzers 243

Deequ Profiler 244

Deequ Constraint Suggestion 244

Auto Scaling for Glue ETL Jobs 249

xi

Table of Cont t

Detecting Schema Changes 251

Amazon Bedrock Batch Inference 252

Summary 255

Chapter 6: Data Pipeline Orchestration and Observability 257

Best Practices for Data Pipeline Orchestration 257

Separation of Concerns 258

Encapsulation 258

Interoperability and Control Flow Management 259

Schema Evolution 259

Time to Answer 259

Orchestrating Data Pipelines with AWS 260

AWS Step Functions 261

Standard and Express Workflows 261

Orchestrating Workflows with AWS Step Functions 262

Amazon Managed Workflows for Apache Airflow 265

Amazon MWAA Architecture 266

Amazon MWAA Environment 268

Orchestrating Workflows with Amazon MWAA 270

Observability for Data Pipelines 274

Logging 274

Metrics 278

Traces 281

Enhancing Observability with Generative AI 286

Aggregated Log Insight Reporting 287

Introducing the AWS DevOps Agent 289

Create an Agent Space 289

Managing Agent Access to AWS Resources 290

Enable Web App Access 291

Managing Agent Capabilities 292

Operator Access 292

Summary 294

xii

Table of Cont t

Chapter 7: Multimodal Data Extraction and Enrichment with Amazon
Bedrock and AWS ML Services 297

Amazon Bedrock Data Automation 298

Blueprints for BDA 299

BDA Projects 302

Intelligent Document Processing (IDP) 304

Classification 305

Extraction 309

Image Analysis 320

Object Detection 323

Image Properties 328

Facial and Emotion Recognition 334

Audio Analysis 337

Video Analysis 341

Summary 347

Chapter 8: Retrieval-Augmented Generation (RAG) with S3 Vectors and
Vector Databases 349

Overview of RAG Architecture 350

Managed RAG 351

Amazon Q for Business 352

Amazon Bedrock Knowledge Bases 353

Corpus Collection Process and Storage 355

Amazon S3 Metadata 357

Collection Embeddings Process 362

Amazon Nova Multimodal Embeddings 363

Text Embeddings 364

Image Embeddings 371

Video Embeddings 374

Audio Embeddings 376

Vector Databases and Semantic Search 380

Vector Format and Precision 381

xiii

Table of Cont t

Distance Metrics 383

Euclidean (L2) Distance 383

Cosine Similarity 384

Inner Product 385

Semantic Search Algorithms 385

Hierarchical Navigable Small World (HNSW) 386

Locality-Sensitive Hashing (LSH) 387

Product Quantization (PQ) 388

Similarity Search Libraries 389

Nonmetric Space Library (NMSLib) 389

Facebook AI Similarity Search (FAISS) 390

Common Semantic Search Architectures 390

Vector Databases on AWS 391

Amazon S3 Vectors 392

S3 Vectors Buckets and Indexes 393

Loading and Querying Vectors in S3 Vectors 395

Integrating S3 Vectors with Bedrock Knowledge Bases 398

Integrating S3 Vectors with Amazon OpenSearch 399

Aurora PostgreSQL with Pgvector Extension 401

Install Vector Extension 402

Create Vector Tables 402

Content Metadata Table 403

Text Embeddings Table 403

Create Embeddings Index 405

Insert Embeddings 406

Amazon OpenSearch Serverless with Vector Engine 408

Create Vector Search Collection 408

Install OpenSearch Client Library 409

Create Vector Embeddings Index 409

Semantic Search 410

Generate Embeddings from Query Text 411

xiv

Table of Cont t

Semantic Search in Aurora PostgreSQL 412

Semantic Search in OpenSearch Serverless 415

Construct Search Query 415

Execute Search 416

OpenSearch Neural Search Plugin 417

Summary 420

Chapter 9: Streaming and Real-Time Data Processing with Generative
AI Enrichment 421

What Is Streaming Data? 422

Streaming Ingestion 423

Streaming Ingestion with Amazon Kinesis 424

Kinesis Producer Library (KPL) 424

Kinesis Client Library (KCL) 425

Enrich Streaming Data with Generative AI 425

Latency 429

Scaling Inference 429

Streaming Data into Transactional S3 Tables 430

Create S3Tables Bucket and Managed Iceberg Table 431

Link S3Tables Namespace to Glue Catalog Using a Resource Link 433

Create an IAM Role for Firehose 433

Set Lake Formation Permissions 434

Create Firehose Delivery Stream 435

Trend Analysis Agent 438

Summary 440

Chapter 10: Data Warehousing with Generative AI and Text-to-SQL
Reporting with Amazon Redshift 441

Impact of Generative AI on Data Warehouses 442

Data Warehousing Fundamentals 443

Data Scaling and the JOIN Problem 444

Separating Analytical Workloads 445

Optimized Data Modeling and Organization for Reporting 445

xv

Table of Cont t

OLAP and Star Schema 445

Columnar Storage 446

Amazon Redshift 447

Redshift Architecture 448

Redshift Serverless 450

Redshift Workload Management 450

Redshift Table Design Considerations 450

No Enforceable Constraints 450

Sort Keys 451

Distribution Styles 452

Change Data Capture (CDC) with ZeroETL 453

Automated Batch Loading with Auto-Copy 454

Sales Datamart Demo 454

Redshift Query Editor v2 457

Prompt Engineering for Text-to-SQL 460

Structured Input Formatting 461

Text-to-SQL Solution Architecture 463

Text-to-SQL Agent 465

SQL Evaluation Agent 466

Text-to-SQL Interface 466

Generating Report Suggestions 468

Redshift Integration with Amazon Bedrock 470

IAM Policy to Authorize Bedrock Access 470

Create External Model 471

Generate Sentiment Scores with Bedrock Model 471

Redshift Integration with Amazon SageMaker 472

IAM Role and Policy to Authorize SageMaker Access 472

Create External Model 473

Generate Sentiment Scores with Custom Model 473

Redshift for Retrieval-Augmented Generation (RAG) 473

xvi

Table of Cont t

Redshift ML for Predictive Model Training 475

Create an S3 Bucket for Training Data Export 475

IAM Role and Policy for SageMaker Model Training 476

Grant User Access to Model Creation and Schema 479

Training the Model 479

Model Performance 481

Batch Inference 481

Summary 482

Chapter 11: Generative Business Intelligence with Amazon Quick Suite 483

The Origins of Business Intelligence 484

Amazon Quick Suite for unified intelligence 484

Chat Agents in Quick Suite 485

Quick Spaces in Quick Suite 487

Quick Flows in Quick Suite 489

Quick Research in Quick Suite 490

Quick Automate in Quick Suite 492

Generative BI with Amazon QuickSight 494

Dynamic Reporting with QuickSight Q 494

Prerequisites 495

Datasets in QuickSight 497

Build a Visual with Q 499

Stories in QuickSight 501

Topics in QuickSight 501

Named Entity Feature 506

Administering Amazon Quick Suite 508

Create an Amazon Quick Suite Account and Sign Up 508

Configure Authentication Method and Identity Integration 509

Establish SAML Federation Connection 509

Configure User Provisioning and Role Assignment 509

Implement VPC Integration for Enterprise Security 510

xvii

Table of Cont t

Configure Data Source Connections and Security 510

Implement Hierarchical Permission Structure 510

Configure Data Access Controls and Security Boundaries 510

User Lifecycle Management and Request Approval 511

Summary 511

Chapter 12: Building AI Agents with Bedrock AgentCore, Strands Agents,
and Model Context Protocol (MCP) 513

Strands Agents SDK 514

Model Context Protocol (MCP) 514

Amazon Bedrock AgentCore 517

MCP Server Fundamentals 519

MCP SDKs, Frameworks, and Language Support 520

Local and Remote MCP Transport Mechanisms 520

MCP Message Protocol 522

MCP Message Structure 522

MCP Security 527

MCP Server Deployment on AWS 528

AgentCore Gateway for MCP 530

Lambda Function Target for AgentCore Gateway 531

Lambda MCP Request Entrypoint 532

MCP Request Routing 533

Process the MCP Request 534

AgentCore Gateway Configuration 537

Build and Deploy Agentic AI Solutions on AWS 538

Build and Deploy an HTTP MCP Server 540

Create Redshift HTTP MCP Server Script 541

Deploy and Test Redshift HTTP MCP Server Locally 543

Deploy the Redshift MCP Server to AWS 544

Deploying MCP on AgentCore Runtime 549

Testing the Remote HTTP MCP Server 554

xviii

Table of Cont t

Build and Deploy Sales Reporting AI Agent 557

Create Sales Agent Script 558

Test the Sales Agent Script Locally 567

Deploy Sales Reporting Agent to AgentCore Runtime 568

Testing the Sales Reporting Agent on AgentCore Runtime 571

Observability and Monitoring for AI Agents 572

Summary 575

577

xix

### **About the Author**

**Justin J.** **Leto** is a Global Principal Solutions Architect for
Private Equity at Amazon Web Services. He brings over two
decades of hands-on experience leading data engineering,
machine learning, and AI enterprise transformation. As a
recognized global technology thought leader, author, and
speaker, he has delivered keynote presentations at global
conferences and universities including AWS re:Invent
and Spark+AI Summit, contributed to over 10 AWS blogs,
and was featured in tech magazines. In recognition of
his contributions at the intersection of engineering and
industry, the Pennsylvania State University’s College of Engineering named him one of
13 Outstanding Engineering Alumni in 2026, the highest honor bestowed on its 100,000
living engineering graduates. Justin leads the NYC Generative and Agentic AI Meetup, a
12,000+ member community, and founded Nova Labs, one of the largest member-driven
innovation and fabrication labs in the world. He holds an MBA and a BS in Computer
Engineering from the Pennsylvania State University. He is a licensed Professional
Engineer and certified Project Management Professional. Outside of work, he is a jazz
and blues keyboardist and experienced offshore sailor. He lives in the New York City area
with his wife and two children.

xxi

### **About the Technical Reviewer**

**Naga Santhosh** **Reddy** **Vootukuri** works for Microsoft as a Principal Software
Engineering Manager in the Azure SQL product. He has more than 17 years of
experience in designing and developing several products within Microsoft, ranging
from SSIS to MDS, and currently in Azure SQL DB. He has deep knowledge in cloud
computing, distributed systems, AI, microservice-based architecture, and cloud-native
apps and has experience working in three different Microsoft centers (India, China, and
the United States). Santhosh has authored and published numerous research articles in
peer-reviewed and indexed journals and in major trade publications. He is a core MVB
blogger at DZone and an active senior IEEE member handling various conferences as
technical chair in the Seattle IEEE region. He served as IEEE AI Summit Committee
chair and lightning talk chair and selected some of the best lightning talks for 2024
and 2025. He is in charge of Try Engineering Workshops. He also delivered AI-related
workshops and received an AI innovator award from Washington Senator Lisa Wellman.
Naga served as a judge for the Agent AI hackathon, Fabric AI hackathon, Cosmos DB
AI hackathon, and RAG Hack on Devpost, which further showcased his expertise and
commitment to the advancement of technology. He also manages several open-source
projects on GitHub, which have several stars. He frequently speaks and presents at
various conferences about microservices, AI, and cloud computing. He actively mentors
junior engineers on ADPList and contributes widely to the developer community.
Naga is in the top 1% of developers in the Cloud and AI community. Naga has been
awarded the prestigious Docker Captain membership program and Dapr Meteor for
his outstanding contributions to the Docker, Dapr, and containers community. You
[can reach him on LinkedIn at ­https://www.linkedin.com/in/naga-santhosh-reddy-](https://www.linkedin.com/in/naga-santhosh-reddy-vootukuri-5a67a133/)
[vootukuri-5a67a133/.](https://www.linkedin.com/in/naga-santhosh-reddy-vootukuri-5a67a133/)

xxiii

### **Acknowledgments**

To my wife, Veera, who supported this book through pregnancy, childbirth, and those
chaotic early months with our newborn son and daughter. We did it.

To my parents, Frank and Carole, who built the ship so that I may sail.

xxv

### **Foreword**

The convergence of generative AI and agentic systems represents the most significant
inflection point in enterprise data practice since the advent of cloud computing. We’re
witnessing a paradigm shift where data engineering is evolving from a discipline focused
primarily on pipelines and transformations into one that must also enable intelligent,
autonomous systems capable of reasoning over vast information landscapes. The data
engineers who thrive in this new era will be those who can bridge traditional data
fundamentals with cutting-edge AI capabilities—and that’s precisely what makes this
book so valuable.

AI agents today help orchestrate complex workflows, make intelligent decisions,
and transform how enterprises interact with their data. However, the use of generative
AI and agentic AI for data engineering is evolving quickly and arriving faster than most
organizations anticipated. Every generative AI application, every agentic workflow, and
every intelligent automation depends on a foundation of well-architected, governed, and
accessible data. As AI systems become more sophisticated, the quality, structure, and
availability of enterprise data become even more critical. Time and again, both academic
research and production AI systems prove the same point: investing in high-quality
data for training, context engineering, and evaluation delivers multi-fold returns. The
challenge facing organizations today isn’t whether to invest in data infrastructure, but
how to accelerate and expand their data engineering impact to meet the demands of
AI-driven transformation.

What Justin Leto has accomplished in Data Engineering with Generative and
Agentic AI on AWS is remarkable: he’s created a comprehensive guide for this niche
but very important area that provides a strategic framework for building modern data
architectures that are AI-ready from day one. This book combines the “greatest hits”
of data engineering on AWS—from data lakes and mesh architectures to streaming
pipelines and data warehousing—with practical, actionable guidance on where and how
to apply generative and agentic AI to deliver immediate business value.

Justin brings over 20 years of hands-on experience leading data and AI initiatives,
and it shows on every page. The book strikes a critical balance between theoretical
foundations and pragmatic implementation guidance that you can use in your

xxvii

F

production AI systems today. You’ll find rigorous technical depth alongside businessfocused thought leadership, always grounded in real-world patterns for delivering
solutions that organizations can deploy today.

Whether you’re designing RAG implementations for enterprise search, building
agentic data pipelines that self-optimize, implementing natural language interfaces to
your data warehouse, or architecting the next generation of intelligent data platforms,
you’ll find actionable patterns and proven practices throughout these pages. From
security and governance to observability and orchestration, Justin addresses the full
spectrum of concerns data engineering leaders face when modernizing their data
practice for the generative and agentic AI era.

—Shreyas Subramanian, PhD, Principal Data Scientist, AWS

xxviii

### **Introduction**

Hello, dear reader. This is your author, Justin. If you are thinking about skipping this
section—don’t. I used to skip introductions too. Then one day I actually read an
introduction _after_ finishing the book, and everything about it made much more sense.
Since then I vowed that if I were to ever write a book, I’d write a really good introduction.
You’ll find a lot of value in the next few pages. I explain my thinking about what this book
is intended to represent, how I chose to organize the content, and tips for maximizing
the value you can get from it.

First, let me start off by saying how deeply grateful I am that you chose to spend some
of your hard-earned scratch on a project I spent 18 months developing. Purchasing a
book like this one becomes part of someone’s journey—it can change the course of their
career. This is a responsibility I take extremely seriously. For me, the process required a
lot of late nights, weekends, and vacations at the computer. It required time away from
my wife and two children that I’ll never get back.

**Why I Wrote This Book?**

Why did I write this book? Well, it’s not for the money (trust me, there’s not much in
technical publishing!). I’m sincerely passionate about helping the next generation
of technologists navigate through this disruptive time. The strategies and advice in
this book are the secret to not just surviving but thriving in a technology career. This
guidance will help you get to the next level, whether as an individual contributor or
in people management. That’s why there’s not just data engineering content here, but
business strategy, technology strategy, corporate political strategy, and career advice. To
go even further, I will even help get the word out about your journey. Connect with me
on LinkedIn—linkedin.com/in/justinleto/—and send me a picture of yourself holding
this book in a cool place or next to a cool thing. Tell me a story about your journey.
Maybe it inspires someone else who needs to hear it. Time permitting, I’ll post your
photo and story to my networks!

xxix

Int cti

**Why Is This Book Different?**

Every data engineering book on the market became obsolete the moment generative AI
dropped. Going forward, technical books need to include how generative and agentic
AI have changed their practice. But not everything changed. The tools and strategies
that store, transform, and serve data are not being replaced. They are being enhanced. I
didn’t want to write a book on just the things that changed, leaving out the foundational
aspects that are still required in a modern data strategy. I didn’t want to write a book
about all the things that stayed the same, because people have already seen those ideas.
That didn’t tell the whole story. I concluded that I needed to do both—combine the state
of the art of modern data platform strategy with the new capabilities and enhancements
of generative and agentic AI. AI is a great tool, but it’s a double-edged sword. It helps
you scale your impact, but it can also rob you of agency (no pun intended). In chess,
they have a term for less experienced players called “woodpushers.” A woodpusher
makes moves without a strategy or understanding the deeper “why.” As AI takes on more
responsibility, the risk is that our knowledge and understanding of technology becomes
more abstracted and superficial. I address that challenge head-on with a sizable amount
of ink devoted to the theory and fundamentals of data and data engineering. In many
cases, this includes the historical context and origin and how that technology progressed
over time. It would take you years of senior-level professional experience to accumulate
the knowledge I pulled together in a book that might take you a weekend to read.

**Who Is This Book For?**

There is something to be gained from this book for various roles across the industry.
Whether it’s data engineers, data architects, data product owners, engineering managers,
CTOs or CDOs, or startup founders, this book will help you unlock business value from
data. If done right, it looks like magic to the casual observer. For you, it’s an honest day’s
work. Is this book too advanced for the less experienced? Probably. Will more senior
engineers find some of the content remedial? Absolutely. But will it deliver value for
both? I believe it will!

xxx

Int cti

**How the Book Is Organized**

This book has 12 chapters and covers a wide range of data engineering and AI
topics, from data security and governance to data lake and data mesh design, to data
transformations, data extraction, RAG, streaming and real-time data, data warehousing,
business intelligence, and agentic AI. Each could probably be their own book, but I
took the core concepts and most common use cases from each and combined them
into one book! Some chapters are quite beefy, and you may find it difficult to tackle a
full chapter in one sitting. If you’re goal-oriented to the point where this might frustrate
you, just know that I considered other options but felt that keeping the content together
provided a more seamless flow. Give yourself breaks; use a bookmark. Don’t try to digest
it all at once; give yourself time to fully understand and reflect on what I’m presenting,
and…experiment on your own!

**Use of Generative AI in Writing This Book**

I wrote this book myself with my own two hands. While I consulted many sources and
artifacts as part of my research, everything you read was crafted by me. I missed many
deadlines with my publisher, and perhaps that’s a testament to the level of manual
care and attention I gave to each paragraph and chapter. I liberally use the em dash—
it is not an indication of AI use. Where I used generative AI tools, it was to assist with
minor editing during the writing process. This included offering different words (like a
thesaurus), restructuring sentences and paragraphs, or summarizing content to reduce
space. Whatever came out of these tools was tweaked further to maximize the value,
impact, and clarity for the reader.

**How I Approach Agentic AI**

You may find it odd that I saved the deep dive on building agents for the last chapter of
the book. This was deliberate. I believe the concepts and strategies on where to apply
agentic AI in the data engineering lifecycle are far more valuable than the specifics of
how the tools today implement them. Instead of focusing on the mechanics of how
an agent is deployed, I instead focus on how agents conceptually will be introduced
at different points of the data engineering domain. I use more abstracted solutions
for agents as placeholders. If you are planning to build production-quality multiagent

xxxi

Int cti

systems, be sure to read Chapter 12, “Building AI Agents with Bedrock AgentCore,
Strands Agents, and Model Context Protocol (MCP)”.

**AI Coding for Hands-On Learning**

Along with the book come additional resources (available on GitHub) for each chapter
to help you understand the concepts and services better. These aren’t rinky-dink
code samples (as you might see from other books) that seem like afterthoughts. These
are fully built solutions that you can deploy into your AWS environment with a few
commands. Keep in mind that these solutions will incur costs, so be sure to delete the
resources when not in use. Install Kiro IDE and Kiro CLI. Clone the repository from
GitHub, navigate to any chapter directory, and point Kiro at the code. You can then use
Kiro IDE or Kiro CLI to modify these solutions to your specific use cases or even just ask
questions about them. The new wisdom argues that you need to “use AI or get replaced
by someone who uses AI.”

**Don’t Give Up**

The last thing I’ll tell you is that technology is hard. You’ll be frustrated by bugs and
permissions issues and errors in an ever-changing landscape of solutions, tools, and
frameworks. Most of the successful engineers and architects I know succeeded for one
primary reason: they didn’t give up. Be an underdog and fight like hell. There are no
shortcuts. This is especially true in tech. Even if someone handed you a high position
without merit, you would not earn the confidence of your team to effectively lead
them. Even though AI coding is making it easier than ever to progress quickly with little
knowledge or experience, the risk is that you’ll never gain a deeper understanding.

We all want to succeed and achieve positions of high success and enjoy the benefits
that come with it. But not all of us want to do the work. You’ve taken the first step by
buying this book.

_When God wanted David to be king,_
_He did not give him a crown;_
_He sent him Goliath._

xxxii

**CHAPTER 1**

## **Introduction to Data** **Engineering with** **Generative and Agentic** **AI on AWS**

There is no technological advancement in the modern era that promises to deliver
the transformative value to organizations and society more than Artificial General
Intelligence (AGI) and superintelligence. Today’s generative and agentic AI systems
serve as the harbinger of these revolutionary capabilities, offering organizations
immediate access to intelligent automation, reasoning, and decision-making that
previews the transformative potential ahead. Wherever AI and superintelligence lead
human society, they will trace the watershed moment back to OpenAI’s public release
of ChatGPT3 on November 30, 2022. At no other time in human history did technology
so quickly and completely capture the attention and imagination of the entire world.
This crude mimicry of human intelligence—made accessible via a web-based chatbot
interface—drove global demand from both consumers and businesses for enhanced
AI capabilities. In the years that followed, incremental leaps in the capabilities of large
language models were achieved, and multimodal models for image, video, and audio
generation are disrupting content generation industries. Demand for AI and now agentic
AI for the enterprise is building quickly. Gartner reported in 2025 that 33% of enterprise
software apps will include agentic AI by 2028. They also estimate that by 2028, 15% of
day-to-day work decisions will be made autonomously by AI agents.

1
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_1](https://doi.org/10.1007/979-8-8688-2199-8_1#DOI)

Chapter 1 Introduc i D E i i i G i A ic A AW

As a result, governments and industry are making the largest per-year capital
investment ever (eclipsing the dot-com era in inflation-adjusted dollars). Just the top
tech companies, including Amazon, Google, Microsoft, and Meta, reported 2025 capital
investments totaling $370 billion. They all predict that AI capital expenditures will
_increase_ in 2026. Chip maker Nvidia is investing $100 billion. Anthropic is investing
$50 billion. Governments, including the United States, are injecting billions more as
part of strategic public-private partnerships to accelerate data center build-outs. These
investments are so grand in scale that Harvard economist Jason Furman calculated that
nearly all of US GDP growth in 2025 was attributed to AI investment.

But why are all these investments being made?
If the early results are any indication, we’re in for a wild ride. The pace of innovation
is so severe that just during the time it took me to write this book, models gained
significant capability and were augmented with agentic systems capable of tool use
and sophisticated deep reasoning; model context protocol (MCP) was open-sourced
by Anthropic; and AWS released Strands Agents SDK and its groundbreaking toolkit
of agentic primitives, Bedrock AgentCore. There are even examples of AI contributing
novel solutions for drug discovery and protein folding. Despite these achievements, the
experts concede that what got us here (transformer-based LLM models) won’t get us
to where we want to go (AGI). While no one knows what’s possible, the major players
won’t risk sitting this one out. Will exuberance and FOMO (fear of missing out) lead
to losses for some investors? Undoubtedly there will be investments that don’t pay off.
The magnitude, concentration, and acceleration of discovery and disruption almost
guarantee this. But the risk-adjusted analysis appears to conclude that even without AGI
and superintelligence, there’s plenty of innovation to be discovered along the way, and
enterprises will deem its adoption necessary to stay competitive. This isn’t something
that’s purely speculative or abstract for me. Of the hundreds of engagements I’ve had
with AWS customers on generative and agentic AI, here’s the truth: companies are
creating real value and impact with AI today. Across continents and across industries,
companies of all sizes have already started transforming their business with AI. From the
hard numbers AWS reported in 2025, over 100,000 customers are using Amazon Bedrock
for AI. The demand is real, and it will only continue to grow into the foreseeable future.
Providers who secure the AI inference capacity needed to meet the forecasted demand
will reap the benefits of this unique opportunity. ASICs (Application Specific Integrated
Circuits) are emerging as a lower-cost alternative to GPUs, with Amazon’s Tranium and
Google’s TPUs (Tensor Processing Units) leading the way. The conventional wisdom is

2

Chapter 1 Introduc i D E i i i G i A ic A AW

to assume that Nvidia’s architectures have a significant moat due to the CUDA developer
community. However, if inference cost is the constraint for making AI ubiquitous in
the enterprise, those assumptions won’t hold up. Business needs and competition will
eventually force the commoditization of AI inference.

Over the long term, the promise of AGI and superintelligence is so great that it’s
now perceived not only as the greatest opportunity but also as the greatest threat.
Governments, but also private industry, have no choice but to invest to win the AI
battle. Analysts and economists waxing polemical on whether all this AI investment is
creating a bubble or trying to pinpoint where we are on the hype cycle have misjudged
the new imperative entirely. Whenever there’s a major shift due to the promises of a
breakthrough in technology, it was the early movers who assumed an _asymmetric risk_
to make that breakthrough a reality. Big bets _need to be made_ without the benefit of
knowing it’s possible. AGI and superintelligence are the preeminent existential threats,
and the countries and companies that achieve those breakthroughs in AGI will realign
the world order for decades to come. Imagine looking back and saying out loud (with
a straight face): “microprocessors really didn’t live up to the hype,” or “the internet
never really delivered the value the analysts predicted,” or “mobile never achieved the
transformative value that was promised.” If AGI is fully realized, it’ll eclipse all of these
advancements.

I’ll relay one sobering example. Anthropic released a threat intelligence report
in August 2025, <sup>1</sup> which detailed attempts they detected and neutralized that sought
to weaponize agentic AI systems to perform sophisticated cyberattacks _directly_ . The
realization is that democratized AI significantly lowers the barrier to entry for cybercrime
to include actors with minimal technical skills. This evolution includes the emergence
of “just-in-time” AI malware families that dynamically generate malicious scripts
and obfuscate code during execution. This is just what is possible today, but imagine
the threat posed by a foreign state actor that has achieved AGI or superintelligence
capabilities.

On the business side, the opportunity is immense. The concept of _non-linear revenue_
describes the decoupling of revenue generation from human capital. The metric used to
assess this efficiency is revenue per employee. For digital native businesses that already
enjoy the benefits of efficiency through technology, agentic AI promises to drive an
_asymmetric upside_ (see Figure 1-1).

1 Moix, A., Lebedev, K., & Klein, J. (2025, August). Detecting and Countering AI Misuse: Analysis of
Emerging Cybersecurity Threats [Internal threat intelligence report]. Anthropic.

3

Chapter 1 Introduc i D E i i i G i A ic A AW

**_Figure 1-1._** _Revenue per Employee: Traditional vs. Agentic AI-Powered Business_

What should be clear by now is that we are in the early stages of a major disruption
of markets, labor, and technology. This disruption presents risks and challenges for
technologists and practitioners. As AI takes on more and more tasks in the digital
enterprise, practitioners should be asking: “What skills and competencies will be
relevant in this new AI era and how can I leverage them to future-proof my career?”

To best answer this question, I will first identify the three most limited resources
needed to drive this AI revolution: chips, power, and data. The first two are highly
capital-intensive endeavors that are already receiving the attention needed to meet the
moment. The third constraint, data, has received far less attention. Without data, AI
models would not exist. Without access to clean, curated, and well-governed data, AI
agents would be unreliable and essentially useless. What’s needed is a transformation,
which will require not just superior technical skills but exceptional leadership abilities as
well. Therefore, my answer to the question is unequivocally:

4

Chapter 1 Introduc i D E i i i G i A ic A AW

_Data practitioners_ _who can lead the transformation from a_
_traditional data practice to an AI-augmented data practice at an_
_enterprise to deliver business value at much greater velocity and_
_scale than ever before will thrive in the era of AI disruption._

This is the reason why I wrote this book. In the era of AI and for the foreseeable
future, human data practitioners that can lead the AI-DLC (AI Development Lifecycle)
transformation for their data practice will be needed, in greater numbers, to support this
new gold rush.

As software engineering undergoes significant disruption due to the rapidly
developing capabilities of AI with copilots, vibe coding, and now spec-driven
development and AI-DLC, data engineering will also experience a transformation. But
data solutions are uniquely differentiated from software solutions in several ways. Data
has a criticality to it that demands a higher standard of protection and accuracy. Data is
an asset with gravity that needs to be actively managed and governed. Publicly exposing
a company’s sensitive user data incurs liability, not to mention reputational damage.
Highly specialized domain knowledge is needed to understand a company’s proprietary
data, which may not have extensive documentation or updated metadata. There
are various kinds of data workloads—operational and analytical, batch and
streaming—and they need more care and feeding than software (schema changes,
migrations, dependencies, security). There’s a highly fragmented suite of tools to ingest
it, store it, transform it, and serve it. Getting AI to understand and work seamlessly across
these data domains and tool stacks with high accuracy will just simply take longer to
develop. Since much of traditional software was designed to capture and report data,
will we see a dramatic change in UI/UX strategy generally? As agentic AI becomes
ubiquitous throughout the digital enterprise, will it ultimately converge to the natural
language interface—chat or voice? More complex interfaces, if needed, can now be built
by AI. Over the long term, I believe the backend will rule the day.

Every organization in the world generates and relies on data to make informed
decisions, and the demand for skilled data engineers is skyrocketing. An analysis by
online recruiting firm Zippia revealed a stunning revelation: while there are currently
10,000 data engineers employed in the United States, there are over 300K job openings!
Driving this growth is an explosion of connected devices and—you guessed it—
breakthroughs in artificial intelligence. Transforma Insights predicts that the number
of connected devices will surpass 29 billion by 2030. Market research firm Statista
estimates that the total addressable market for AI could reach $15.72 trillion by 2030.

5

Chapter 1 Introduc i D E i i i G i A ic A AW

Data engineering is expected to play a vital role in unlocking this business growth over
the next quarter century. I believe we can close this skills gap with a mix of AI-assisted
development to help current data engineers scale their impact and enabling displaced
software engineers to transition to AI-assisted data roles.

Throughout the book, I integrate business principles with technology strategy,
focusing on the theory of data engineering, its practical implementation on the AWS
cloud, and where state-of-the-art generative and agentic AI can be applied to add
significant value. Whether you are new to the world of data engineering or a 20-year
practitioner, this book will help you succeed in this rapidly evolving AI-augmented
practice of combining people, process, and technology to transform data into
business value.

**What Is Covered**

This book, _Data Engineering with Generative and Agentic AI on AWS: Building an AI-_
_Augmented Data Practice_, is my contribution to your accelerated journey toward a
successful career in AI-augmented data engineering. Over the next 12 chapters, I will
provide you with the theoretical and practical knowledge of core data engineering topics
fused with the most transformative state-of-the-art technologies of our day: generative
and agentic AI on the AWS cloud.

In this first chapter, I introduce data engineering, generative and agentic AI, and
the AWS cloud. I discuss how data engineering will be impacted by generative and
agentic AI and how data engineering will support generative and agentic AI. I show how
generative AI can unlock hidden value in unstructured data. I discuss the business of
data engineering by defining executive personas, their associated responsibilities, and
examples of hypothetical data projects they might sponsor. Finally, I present theoretical
concepts on the most relevant topics in modern data engineering.

In Chapter 2, “Data Security and Governance,” I present prescriptive guidance for
securing data and provisioning access to consumers and stakeholders in AWS, including
for generative and agentic AI applications. I also demonstrate how to use generative and
agentic AI to enhance the monitoring of one’s security posture and even recommend
enhancements.

In Chapter 3, “Data Lake Design with Apache Iceberg and S3 Tables,” I explain the
theories and concepts of modern data lake design, and I show you the best practices for
how to build a data lake from scratch. I demonstrate how to implement a transactional

6

Chapter 1 Introduc i D E i i i G i A ic A AW

data lake called a “lakehouse” using Apache Iceberg and S3 Tables. I provide coding
examples demonstrating how generative and agentic AI can be used to automate
mundane data engineering tasks like schema matching and field mapping.

In Chapter 4, “Data Mesh Design with Amazon DataZone,” I describe an alternative
to centralized data lakes called the data mesh. I discuss why this is a good scaling
strategy for larger organizations.

In Chapter 5, “Big Data Processing and Transformation,” I delve into core themes of
data engineering, including big data processing and transformation using the distributed
processing engine Apache Spark. I demonstrate how to define and enforce data quality
at scale using the Spark-based data quality framework, Deequ. I also provide real-world
examples of how to use generative and agentic AI to accelerate the development process.

In Chapter 6, “Data Pipeline Orchestration and Observability,” I describe how to
automate and monitor data pipelines with orchestration frameworks and observability. I
present several patterns for using generative and agentic AI to derive high-value insights
from job processing logs and metrics.

In Chapter 7, “Multimodal Data Extraction and Enrichment with Amazon Bedrock
and AWS ML Services,” I showcase how AWS generative AI and ML services can
be integrated into our data pipeline to extract unstructured data and enrich it with
additional insights.

In Chapter 8, “Retrieval-Augmented Generation (RAG) with S3 Vectors and Vector
Databases,” I provide prescriptive guidance for designing and managing RAG systems. I
demonstrate how to use generative AI models to generate text embeddings for corpuses
of unstructured data and how to use vector databases to store these embeddings for
semantic search.

In Chapter 9, “Streaming and Real-Time Data Processing,” I demonstrate how to
design data pipelines for real-time and streaming data use cases and how we can use
generative AI to enhance streaming data analytics.

In Chapter 10, “Data Warehousing with Generative AI and Text-to-SQL Reporting
with Amazon Redshift,” I step you through the process of designing and building
strategic data marts using Amazon Redshift. I present an agentic architecture for
implementing a natural language interface to the data. Along the way, I demonstrate how
ML and generative AI models can be used to enrich data in Redshift. I show how Redshift
integrates with Bedrock Knowledge Bases to implement RAG for structured data.

7

Chapter 1 Introduc i D E i i i G i A ic A AW

In Chapter 11, “Generative Business Intelligence with Amazon Quick Suite,” I
describe how to visualize data from a data lake or data mart using Amazon Quick
Suite, a unified intelligence platform for the enterprise. I demonstrate how to automate
workflows, perform deep research, and use generative AI features in QuickSight to query
data and create visualizations using natural language.

In Chapter 12, “Building AI Agents with Bedrock AgentCore, Strands Agents,
and Model Context Protocol (MCP),” I dive deep into the mechanics of deploying
agentic solutions to production. I demonstrate how to enhance existing APIs, Lambda
Functions, and data sources with MCP to enable agentic integration. I’ll build agents
trained for insights reporting using the Strands SDK and Bedrock AgentCore.

**What Is Data Engineering?**

Data engineering is a practice spanning people, processes, and technology to capture
and convert data into business value by delivering it to the right consumers at the
right time.

Let’s break this down.
The concept of “people, process, and technology” from the above definition
originally comes from Harold Levitt. In 1965, Levitt described a model for creating
change in an organization in his paper entitled “Applied Organization Change in
Industry: Structural, Technological, and Humanistic Approaches.” He defined this model
as a diamond that included _tasks_, _structure_, _people,_ and _technology_ . In the 1990s, this
model was applied to the information technology domain and simplified to a “golden
triangle” of _people_, _process_, and _technology_ depicted in Figure 1-2.

8

Chapter 1 Introduc i D E i i i G i A ic A AW

**_Figure 1-2._** _People, Process, and Technology (PPT) Framework_

I raise this point to emphasize that data engineering isn’t just about technologies or
platforms. It’s people and processes too. And not just the people designing, developing,
and maintaining data pipelines, but the producers and consumers of data in an
enterprise.

Out of the three—and this shouldn’t be controversial—people are the most challenging.
In any company, there are stakeholders and domain experts standing over and behind
the data they generate and analyze. These individuals have an agenda that is personal
to them. They have a vested interest in their own success, which is dependent largely
on how their story is told. This is why giving up control and sharing data with a larger
audience could be viewed as a risk by them. The more experience you accrue as a data
engineer, the more you’ll realize that this role is as much about sales and relationship
management as it is about technology. If you can’t earn the trust of your stakeholders,
then the access to their data, and thus your impact, will be limited. Data engineering
is as much about organizational change management as it is about data. People are
also needed to design, implement, and manage the processes and leverage the latest

9

Chapter 1 Introduc i D E i i i G i A ic A AW

technology to most efficiently drive results. People are needed to lead change. The word
“leadership” is easy to write in a book like this without much thought given to it. To the
casual reader, it might seem easily excusable to gloss over a discussion about leadership,
but to me, it would be unforgivable to leave such an important topic unexamined in this
context. While this isn’t a book about leadership, I can justify a few paragraphs on the
subject.

Let me share a personal experience that should help you remember this leadership
discussion. Sailing has been a major passion of mine. I’ve spent nearly 2 decades
serving as crew (and later captain) for offshore ocean passages. Owners of these vessels
living aboard full-time need to move their boats twice a year (north and south) to avoid
hurricane season in the Atlantic and Caribbean Oceans. What I learned from these
experiences is that in harrowing situations sailing hundreds of miles offshore—at night
through a storm with gale-force winds and 15 ft seas—the actions of the crew can mean
the difference between life and death. My time sailing exposed me to naval history
through a mix of circumstances, storytelling, and natural curiosity. I became interested
in naval war history as a catalyst for leadership lessons I could apply in business. What I
learned is that some of the very same issues facing organizations today with respect to AI
transformation are similar to the challenges facing the United States Navy 80 years ago.

In his famous _Letter to the Naval Committee of Congress, 14 September 1775_, American
Revolutionary War hero and Father of the American Navy, John Paul Jones, emphasized
how important people were despite technological advancement. Jones referenced Alfred
Thayer Mahan, who championed personnel quality and training over material superiority
in his 1890 and 1911 writings on naval strategy. The famous motto attributed to Mahan
declared that “good men with poor ships are better than poor men with good ships.”
A common misconception in modern technology strategy is that superior tools can
compensate for mediocre talent, when the opposite is almost always true.

I came across a book on naval leadership from the World War II era, which contained
the following passage that feels eerily prophetic today:

_In the transition from the Old Navy to the New, with its enormous_
_material development, its complication of machinery and devices,_
_its increases in size and numbers, its watertight subdivisions_
_and its decentralization of authority, its material expansion and_
_contractions, there has been a tendency to lose sight of the man_
_in the machine. No error could be greater than this, no mistake so_
_fraught with disaster._

10

Chapter 1 Introduc i D E i i i G i A ic A AW

In the era of AI, the same holds true. This same book went on to define leadership as
the ability to achieve accomplishment from the crew by virtue of their willingness rather
than by force. Just due to the nature of our work, to be successful, data engineers will
need to influence without formal authority, since they most often are working crossfunctionally across multiple teams and leaders.

As a data practice grows within an organization, smaller decentralized teams will
be needed. These teams will require autonomy to operate effectively. How can leaders
ensure that the decisions made by those teams align with the leadership even in their
absence? This was the critical question Jeff Bezos faced in the early days of Amazon.
He recognized that culture needed to be explicitly defined, which he did through
the concept of Amazon’s Leadership Principles (LPs). <sup>2</sup> However, just publishing LPs
isn’t enough. Culture is developed and reinforced continually through a series of
mechanisms: from the interview process, to onboarding, to day-to-day interactions
with stakeholders, to annual peer and managerial reviews, and the promotion process,
Amazon employees are held accountable for exhibiting the leadership principles. Today,
through a set of 16 leadership principles, which includes “customer obsession,” “bias for
action,” “earns trust,” and “ownership,” among others, Amazonians live the company’s
LPs every day. Amazon has become the case study for scaling a high performing culture
to 1.5 million employees. Organizations looking to scale an AI-augmented data practice
in an enterprise need to consider how they will establish and maintain their own high
performance culture.

Because data engineering is knowledge work that requires inspection to validate, the
business implements processes to manage it. Data governance, data provenance, and
data lineage are topics that describe processes implemented to manage data and data
engineering. What does the data mean? How is the data created, changed, and accessed?
How can producers publish and share data? How can consumers discover and consume
the data? How did the data change from its initial state to its final state?

2 Amazon. “Leadership Principles.” _Amazon Jobs_ [, 2025, amazon.jobs/content/en/our-](http://amazon.jobs/content/en/our-workplace/leadership-principles)
[workplace/leadership-principles. Accessed 4 Dec. 2025.](http://amazon.jobs/content/en/our-workplace/leadership-principles)

11

Chapter 1 Introduc i D E i i i G i A ic A AW

These questions will be no less relevant when AI assumes the role of producer and
consumer. AI will be asked to serve specific business functions within an organization,
just as humans did previously. We will still need processes for managing how data is
produced, shared, and consumed. These processes will be implemented and enforced
using technology.

Technology can enable, simplify, and enforce processes established to ensure quality
or mitigate operational risk. Technology is also critical to how data engineering is
performed today. Despite the encroachment of AI on knowledge work, the digital
tooling needed to create, store, and move data is not likely to fundamentally change in
the near future. Continually seeking and discovering ways to do more with less through
tooling and automation is how data engineers have always differentiated their value
in the market. This is getting significantly easier to achieve, thanks to the features and
capabilities of cloud platforms like AWS, which will greatly accelerate the transition
toward an AI-augmented enterprise.

**The Future of Knowledge Work**

Data engineering is a form of knowledge work. The term “knowledge work” was coined
by famed management consultant Peter Drucker in his 1959 book titled _The Landmarks_
_of Tomorrow_ . In it, Drucker declares that the most valuable asset of an institution will
be its knowledge workers and their productivity. I’ll discuss two of Drucker’s most
important quotes on this topic.

_Knowledge work is not defined by quantity. Neither is knowledge_
_work defined by its costs. Knowledge work is defined by its results._

If this isn’t immediately obvious, consider that a data pipeline could process a
megabyte or a terabyte of data to generate a single data point of significant business
value. Compare this to manufacturing, where the worker produces widgets—the value
of the work is defined by the cost and quantity of widgets produced. Knowledge work
represents a decoupling of direct costs of the inputs determining the value of the output.
This requires higher-level reasoning and analytical ability to process information and
produce an actionable insight.

12

Chapter 1 Introduc i D E i i i G i A ic A AW

_Knowledge workers have to manage themselves. They have to have_
_autonomy._

Because knowledge workers are given a higher-level objective, they need the
freedom and autonomy to seek out new and creative ways to achieve that objective. The
consequence of this is that the specific set of tasks or steps a knowledge worker performs
to produce the output is obfuscated from the external observer. This means that to fully
validate the result, one would need to inspect (or replicate) the full body of work.

If we consider these postulates in the context of AI, we are faced with a daunting
realization—over time more and more knowledge work, including data engineering,
will be performed by AI. Despite this reality, these postulates hold—knowledge work
will still be measured by its results, and it will still require autonomy. The human data
engineer will instead be tasked with managing the complexity and scale that AI enables,
developing relationships with internal and external stakeholders, and aligning data
solutions to business outcomes.

**AWS Cloud for Business Agility**

The AWS cloud is the leading cloud provider in the world. With over 200 fully featured
services across compute, storage, databases, ML/AI, and IoT, builders can rapidly
assemble these services like building blocks to create highly impactful business
outcomes. AWS services are designed to be robust, scalable, resilient, and durable so
developers can focus on solving business problems rather than the technical challenges
of managing IT systems. Among these many services are purpose-built solutions for data
engineering and generative and agentic AI, which we’ll explore extensively in this book.

This is an IT outsourcing strategy to be sure—cloud customers are transferring
the risk of building and operating IT services to AWS. But it’s much more than that.
Technological advancements are accelerating at a faster and faster rate, where we now
have a new term to describe their impact: the acceleration gap.

The acceleration gap is the gap between the number of opportunities presented due
to technological advancement and an organization’s ability to adopt the advancements
to exploit those opportunities. Digital technology and artificial intelligence will continue
to drive this new reality. The general business environment will change rapidly, be more
volatile, and less certain. Businesses are motivated to de-risk and realize value faster. In
that scenario, the only winning strategy is to maximize _agility_ .

13

Chapter 1 Introduc i D E i i i G i A ic A AW

This positions cloud hyperscalers like AWS as highly strategic _partners_ . Not only
are they themselves driving technology innovation _on your behalf_, they’re rapidly
distributing major technology innovations found in open source or third-party providers
as enterprise-ready services. Think PostgreSQL, Apache Spark, Apache Kafka, Apache
Airflow, Apache Iceberg, or OpenSearch. All of these data-centric software projects are
offered by AWS as fully managed, enterprise-ready services.

By leveraging fully managed, enterprise-ready services, customers dramatically
reduce the time-to-value for the solutions they build while mitigating operational risk.
Market research published in 2020 by Salesforce found that for these uncertain times,
customers place time-to-value as top of mind:

_Tight budgets and economic uncertainty mean customers need_
_to realize value from their investments as quickly as possible._
_Accelerating Time to Value (TTV)_ _is top of mind, and new methods_
_are emerging to translate this aspiration to action_ . <sup>3</sup>

Incrementalism is also an effective de-risking strategy. Customer insight
company Gainsight reported that they were able to decrease time-to-value by 66% by
implementing a phased approach.

_Customers want a phased process with multiple value milestones_
_versus waiting for one big rollout with all the value delivered at_
_the end_ . <sup>4</sup>

An analysis by Workday found that the key to business agility was being able to
analyze data across all business systems. They found:

3 Karen Mangia, Mat Sweezey, _Customer Experience Redefined: Insights From Chief Customer_
_Officers on the Frontlines_ [, Salesforce, San Francisco, CA, November, 2020, https://www.](https://www.salesforce.com/news/stories/customer-experience-redefined-insights-from-chief-customer-officers-on-the-frontlines/)
[salesforce.com/news/stories/customer-experience-redefined-insights-from-chief-](https://www.salesforce.com/news/stories/customer-experience-redefined-insights-from-chief-customer-officers-on-the-frontlines/)
[customer-officers-on-the-frontlines/, (accessed May 16, 2022)](https://www.salesforce.com/news/stories/customer-experience-redefined-insights-from-chief-customer-officers-on-the-frontlines/)

4 _How We Decreased Time to Value At Gainsight By 66%_, Gainsight,
[September 21, 2020, San Francisco, CA, https://www.gainsight.com/blog/how-we-decreased-](https://www.gainsight.com/blog/how-we-decreased-time-to-value-at-gainsight-by-66/)
[time-to-value-at-gainsight-by-66/, (Accessed May 17, 2022).](https://www.gainsight.com/blog/how-we-decreased-time-to-value-at-gainsight-by-66/)

14

Chapter 1 Introduc i D E i i i G i A ic A AW

_34% of leaders say that advanced analytics and data visualization_
_skills will ensure that their teams can continuously meet evolving_
_business demands_ . <sup>5</sup>

More and more of data analysis and visualization will be performed dynamically by
agents. The good news is that these agents will need clean, governed, and curated data
to be accurate. If agility is the business imperative where decisions need to be made fast,
then the business will depend heavily on accurate and timely data.

Being fully cloud-adopted is the modern business imperative for maximizing
business agility. The AI-augmented enterprise will inevitably be a cloud-adopted
enterprise.

**The Rise of Generative and Agentic AI**

Generative AI exploded into the global consciousness in November 2022 when OpenAI
released ChatGPT3. It quickly captured the imagination of the entire world, hitting 100
million monthly active users in January 2023. At the time, it was the fastest-growing
application in history. Generative AI existed long before 2022. In fact, the general
purpose transformer (GPT) model that modern generative AI models are based on was
described in a paper published in 2017 by researchers at Google entitled “Attention Is All
You Need.” Since then, the GPT model was further developed and enhanced over several
years by many more contributors. However, we must recognize OpenAI’s breakthrough
and their choice to make it accessible through a chatbot as the moment when generative
AI entered the mainstream.

But the bigger story is how quickly the major cloud platforms adapted to respond to
this competitive threat. Within 5 months of the release of ChatGPT3, all of the top cloud
providers had announced their own generative AI solutions. This timeline is illustrated
in Figure 1-3.

5 Workday. “The Acceleration Gap: Toward Sustainability Digital Transformation.” Workday, 2022,
[https://blog.workday.com/content/dam/web/en-us/documents/reports/workday-](https://blog.workday.com/content/dam/web/en-us/documents/reports/workday-longitude-acceleration-gap-research-project-enus-digital.pdf)
longitude-­ .

15

Chapter 1 Introduc i D E i i i G i A ic A AW

**_Figure 1-3._** _Timeline of Generative AI Announcements from the Launch of_
_ChatGPT3_

This means that cloud-adopted businesses could harness the power of a new
bleeding-edge technology by doing _absolutely nothing_ . You didn’t have to invest any
money into R&D or figure out how to operationally host and manage this complex
technology. You just get the new shiny object, and oh, by the way, it comes with a pay-asyou-go pricing model.

In April of 2023, Amazon announced the launch of Amazon Bedrock, and along with
it, its AI strategy. Rather than support one model or one family of models, Bedrock would
securely host and serve the most compelling first- and third-party models available,
maximizing choice and convenience for customers. This proved to be especially
prescient given the amount of disruption in model supremacy since. As of 2025, Bedrock
supports 53 models across 9 model families. These include first-party model families
built by Amazon, called Nova and Titan. The Nova family of models provides full
multimodal coverage, including text (Nova Lite, Micro, and Pro), images (Nova Canvas),
video (Nova Reel), audio (Nova Sonic), and embeddings (Nova Embeddings). Thirdparty model support in Bedrock features Anthropic Claude (Sonnet, Haiku, and Opus),
Meta’s open-source Llama, DeepSeek’s R1, OpenAI’s open-weights model, Stability AI’s
Stable Diffusion, AI21 Labs, Cohere, and Mistral. The winning strategy long-term will be
to leverage platforms that provide access to the widest selection of models to maximize
agility, cost efficiency, and choice.

AWS is quickly moving beyond model inference to more advanced agentic AI
capabilities. At re:Invent in 2025, AWS announced the release of three fully autonomous
“frontier” agents: a developer agent (Kiro), a security agent (AWS Security Agent), and a
DevOps agent (AWS DevOps Agent). I expect the portfolio of AWS frontier agents to grow
as time goes on.

16

Chapter 1 Introduc i D E i i i G i A ic A AW

Just as everyone started using generative AI to experiment with various use
cases, I experimented with data engineering tasks. I quickly saw an opportunity to
provide practical guidance for how generative and agentic AI could be applied to data
engineering today while also revealing how data engineering will be impacted as AI
advances.

**What Is Generative and Agentic AI?**

Generative AI is a type of artificial intelligence that can creatively generate digital content
that serves some valuable function. It can take as input text, images, audio, or video and
generate content that can include text, images, audio, or video. These generative models
can appear to understand instructions provided in natural language and can apply these
instructions to input content and produce an intelligent output. Generative AI models
differ from machine learning models in that they are considered “open domain” models
trained on vast corpuses of general knowledge data, which can be adapted for many
different tasks merely by changing the instruction provided in the prompt. Traditional
machine learning models are “task-oriented” models that are designed to solve narrowly
defined problems.

Generative AI can “understand” and generate unstructured data like text, images,
video, and audio. It can determine sentiment and summarize or classify documents.
With the assistance of generative AI, the data engineer can work with unstructured
data just as comfortably as they work with structured data. Generative AI also provides
a natural language interface to data, including _Text-to-SQL_ . With this abstraction,
consumers can describe the insights they seek using natural language, and generative
AI models can convert these requests into SQL queries to be run against a data source.
This greatly simplifies reporting and analytics. The days of developing custom reports for
every possible customer request are over.

These are the five main use cases where I see generative AI having the most impact
on data engineering:

1. Extraction, enrichment, and intelligent searching of

unstructured data

2. Generation of synthetic data

3. Development of data solutions

17

Chapter 1 Introduc i D E i i i G i A ic A AW

4. Operations monitoring and observability of data pipelines

5. Analytics and insights reporting

When we operationalize generative AI models as agents, they can perform highly
complex tasks, automate complex workflows, and collaborate with other agents.
Agents can perform higher-level reasoning, decompose complexity, and execute tasks
successfully. Agents can write code for data transformation and orchestrate logic for
much of the data engineering tool stack. It can monitor operational signals and respond
in what will eventually become self-healing data pipelines and systems.

An agent can be defined as an artificially intelligent digital service that can
reason and adapt to perform novel and complex tasks. In practice, the approaches
for implementing agents continue to evolve, and the underlying technology is rapidly
evolving. Therefore, throughout this book, I’ll dissect the data engineering process in
depth and highlight where agents can be implemented to add the most value at different
stages of the process.

To fully understand what an agentic AI system is, consider the conceptual diagram in
Figure 1-4.

**_Figure 1-4._** _Conceptual Diagram of an Agentic AI System_

Agents, like the common definition of the term, are intended to act as delegates,
performing tasks and making decisions _on behalf of_ an authorizing principal. Consider
a familiar example: when you grant someone power of attorney, you’re essentially
appointing them as your agent for specific decisions. You’re giving that person the

18

Chapter 1 Introduc i D E i i i G i A ic A AW

authority to act in your best interest and on your behalf. Similarly, agentic AI ultimately
derives its authority from a human and operates at the direction of humans. In practice,
the agentic AI system is software that implements what is referred to as an agentic
loop. It can receive an input as a prompt, which includes an objective with instructions
defined by the agentic designer for what purpose the agent is to serve. The agent is also
provided access to a set of tools and resources that it can utilize to perform different
tasks in support of completing the overall objective. The agent uses a highly capable
LLM to analyze the request, its instructions, and its tools and resources and breaks down
the objective into a set of tasks. Within the agentic loop, the agent performs the various
tasks that the model has determined necessary. When the tasks are completed, the agent
returns a final response indicating that it has satisfied the objective.

The real value of this architecture is that it can handle novel problems that do
not have to be explicitly defined at design time. When agentic AI first arrived, some
customers wanted to dismiss it as merely “RPA with better marketing.” RPA (Robotic
Process Automation) originated in the early 1990s and rose to prominence in the
2010s as part of larger business process outsourcing (BPO) and digital transformation
movements. The key difference is that RPA automates a _defined_ workflow. With agentic
AI, the specifics of the task or objective are not fully known or defined.

I’ll provide a simplified example from the physical world to help illustrate this point
clearly. Imagine that you are an agent. You are provided access to a highly capable LLM,
say through a web interface. Additionally, you are provided with a large tool chest filled
with all kinds of woodworking tools like saws, hammers, chisels, and instruments of
measurement. You are also provided consumable resources like wood, nails, glue, and
concrete. Now, let’s say that your “boss” is requesting that you build a shed.

You haven’t built a shed before, so you ask the LLM:

“How do I build a shed using these tools and resources?”

The LLM provides you with a step-by-step guide for how to build a shed. One of
the first steps might include asking your boss additional follow-up questions about
the shape, dimensions, and color of the shed. You as the agent continue to report
the completed step to the LLM until all the tasks are complete. You use the LLM to
troubleshoot and solve any challenges you encounter while building the shed. After you
complete the shed, you receive another request from your boss. This time the boss wants
you to build a gazebo. You’ve never built a gazebo before, but once again you ask the
LLM, and it provides a step-by-step set of instructions for building a gazebo.

19

Chapter 1 Introduc i D E i i i G i A ic A AW

From these examples, you should be able to deduce that the robustness or
usefulness of an agent is solely dependent on the sophistication of the generative AI
model powering its reasoning capabilities, the management of its memory and context,
its access to data, and its access to tools that can perform different functions. Figure 1-5
shows an agentic solution conceptually.

**_Figure 1-5._** _High-Level Solution Architecture of an AI Agent_

Agents are not chatbots that just respond to questions (even though that may be one
use case). Agents are given access to data and empowered with tools that can take action
to meet some business objective.

Everything I described above that spans generative and agentic AI has implications
for data engineers. Overall, there are four primary topics in generative and agentic AI
that will require the support of data engineering:

1. Model training, continued pretraining, and model fine-tuning.

2. Curation of knowledge bases from multimodal corpuses and

Retrieval-Augmented Generation (RAG) systems.

20

Chapter 1 Introduc i D E i i i G i A ic A AW

3. Providing agents with secure and privileged access to data and

other resources.

4. Managing AI artifacts like prompts, contexts, memory, caches, and

guardrails.

Now, let’s review what drives generative and agentic AI: the transformer model
architecture.

**The Transformer Architecture**

Generative AI foundation models (FMs) are based on the transformer model
architecture, mentioned earlier. Transformer models first tokenize the input text into
three attention vectors—Query, Keys, and Values—also called projected representations.
Positional embeddings, which indicate where in the original sequence the text is
located, are added. This sequence of vectors is fed into a self-attention mechanism that
determines how much attention it should pay to certain inputs when making decisions
about other inputs. This is referred to as _attention scoring_ . Multihead attention just
means that these attention scores are calculated in parallel for many input tokens
at once.

Through the query vector, a number of different NLP use cases can be specified.
Here are some examples to help illustrate how self-attention works.

Anaphora resolution refers to the NLP task of relating pronouns to their subject. For
example, consider the sentence, “John bought a car. He drives it to work.” The selfattention mechanism should relate “He” as referring to “John” and would score the “He”
token as follows:

**Query** : Looking for the subject it refers to

**Keys** : Match against “John”, “bought”, “a”, “car”, “He”, “drives”

**Values** : Contextual information about each word

**Result** : High attention to “John”, linking the pronoun to its
antecedent

21

Chapter 1 Introduc i D E i i i G i A ic A AW

Relations between words may span long sequences of text. Consider the sentence,
“Although it was raining, Sarah, who loves outdoor activities, decided to go for a hike.”
For the token, “hike”, here’s how the scoring might go:

**Query** : Seeking context for the action

**Keys** : Match against all previous words

**Values** : Semantic content of each word

**Result** : High attention to “Sarah” and “outdoor activities,” lower to
“raining”

Entity resolution is a common NLP use case. Consider the sentence, “The company
is planning to open a new store in New York City.” For the token “York”, the attention
scoring might yield

**Query** : Seeking entity-related information

**Keys** : Match against “Apple”, “planning”, “open”, “new”, “store”,
“in”, “New”

**Values** : Contextual information about each word

**Result** : High attention to “New” and “City”, recognizing them as
part of a location name

Other examples of NLP tasks include semantic disambiguation and sentiment
analysis. The specific queries and NLP tasks are learned at training time and then
specific queries are dynamically generated for each token at inference time.

Figure 1-6 shows a high-level conceptual diagram of a transformer encoder
(decoder) model. Since the architectures between the encoder and decoder are similar,
I attempt to simplify this by indicating decoder variations in parentheses.

22

Chapter 1 Introduc i D E i i i G i A ic A AW

**_Figure 1-6._** _Transformer Model Architecture_

Note that the primary difference between transformer encoders and decoders is that
decoders use masked multihead attention. Multihead attention means that decoders, as
part of output token generation, only score the current and previous tokens as input and
cannot look ahead. Encoders use full attention (bidirectional) for understanding tasks,
whereas decoders are tasked with output token generation.

The high-level takeaway is that transformer models use self-attention mechanisms
to add contextual understanding, whereas other types of neural networks do not. An
easy giveaway of non-transformer-based models is that their inaccuracies look “dumb.”
The tradeoff—and more specifically the risk—is that transformer models are capable
of hallucinating _highly credible-sounding responses_ that, in reality, are completely
nonsensical, making them more difficult to detect.

Foundation models require a significant amount of high-quality data to train.
This data needs to be collected, cleaned, curated, and managed over time. FMs will
be regularly retrained or fine-tuned with new data. Companies lacking the richness
or depth of data for training can generate synthetic data. Due to the data security

23

Chapter 1 Introduc i D E i i i G i A ic A AW

implications, the data engineer will be tasked with determining how to manage
generative AI artifacts like prompts, context, caching, and embeddings to support
generative AI applications.

**Retrieval-Augmented Generation (RAG)**

Retrieval-augmented generation (RAG) is a strategy to enhance the responses of a pretrained foundation model with relevant data the model wasn’t trained on but instead
added to the prompt as context. This strategy requires implementing a fast similarity
search on a corpus of content. This is achieved by generating vector embeddings, or
numerical representations used to perform similarity calculations to compare content.
Text is the most common use case, but images, video, and audio can also be represented
as vectors. This allows for multimodal semantic search—content is retrieved across
corpuses of text, images, video, and audio content based on the request.

Using a text embeddings model and storing these embeddings in a vector database is
shown conceptually in Figure 1-7.

**_Figure 1-7._** _Generating Text Embeddings from a Document Corpus_

Data engineers will manage the corpuses, vector embedding pipelines, and vector
stores to support RAG-based solutions.

**Model Context Protocol (MCP)**

One of the most important enablers of agentic AI for both the product and the enterprise
is model context protocol (MCP). Anthropic released MCP in late 2024 and within
months achieved widespread industry adoption, including Amazon, Google, Microsoft,
and OpenAI, as well as exponential community growth. This success was no accident
since the problem it is solving is a critical one for agentic AI—agents need a standard

24

Chapter 1 Introduc i D E i i i G i A ic A AW

way to integrate with tools, data, and systems. Attempting to directly integrate with
each service or data source is known as an M x N complexity problem. MCP is a unified,
universal natural language API that allows agents to leverage tools and data sources
without needing to know the particulars of how those requests are made. It’s been called
“the USB-C port for AI.” It’s a vital abstraction layer. Figure 1-8 illustrates the difference
architecturally.

**_Figure 1-8._** _Direct Integration vs. MCP for Agent Resource Access_

From its initial success, MCP appears to be on track to become _the_ universal open
standard for AI system connectivity and interoperability.

In Chapter 2, “Data Security and Governance,” I will dive deep into MCP security.
In Chapter 12, “Building AI Agents with Bedrock AgentCore, Strands Agents, and Model
Context Protocol (MCP),” I will step you through the process of selecting an MCP
deployment strategy and deploying MCP servers on Bedrock AgentCore Runtime.

25

Chapter 1 Introduc i D E i i i G i A ic A AW

**Agentic AI Development with Kiro**

The impact of AI copilots on software engineering is already well known. A similar story
can be told for data engineering. Whether profiling data, architecting data models,
unpacking heavily nested JSON, or generating SQL scripts, Spark scripts, Lambda
Functions, or Airflow DAGs, data engineers will be expected to lean heavily on AI
copilots to accelerate the data engineering development process.

In 2025, AWS released the first agentic IDE called Kiro. Kiro takes vibe coding to the
next level with spec-driven development, agentic hooks, and native MCP integration. With
spec-driven development, you iterate on a business and technical specification of what
you want to build and how you want to build it. Once you have the specification refined,
Kiro will create and iterate on a design before finally building the project agentically,
tasking out various parts of the application to be executed by subagents.

Moving beyond the IDE, AWS released a frontier agent, the Kiro autonomous agent,
that monitors every interaction with the developer, then learns and adapts. You can even
assign the Kiro agent tasks from the backlog that it will execute autonomously. This greatly
expands the throughput of a development team where lower priority coding tasks—like
modernization and migrations that pay down technical debt—never get scheduled.
Accenture estimates that tech debt costs US companies $2.4 trillion a year. Gartner estimates
that between 60% and 80% of IT budgets are consumed by maintaining legacy systems.
Not only are teams paying interest on the technical debt that diverts resources from new
products and features, they’re also incurring the opportunity cost of not capturing the value
from the optimizations and features from the latest versions of systems and software.

Accompanying this book is a GitHub repo of solutions demonstrating key concepts,
which were built with the help of Kiro. I highly recommend that readers install Kiro <sup>6</sup> and
use it to perform the various development tasks described in the book and enhance and
customize the solutions provided in the GitHub repo.

**Agentic AI for a Modern Data Strategy**

Generative and agentic AI is evolving so rapidly that it raises serious questions for business
and technology leaders about where to invest. While analysis paralysis and risk aversion
is never a winning strategy in business, this accelerating volatility raises a legitimate cause
for concern. I hope to not only allay those fears for the readers of this chapter but to arm

6

26

Chapter 1 Introduc i D E i i i G i A ic A AW

them with the knowledge and messaging they’ll need to convince their senior leadership
and the board on where to confidently invest in agentic AI. To do this, I’ll channel Amazon’s
customer-centric model that seeks to make long-term strategic decisions based on their
customers’ “durable needs.” Durable needs are consumer needs that do not change over
time. For example, in Amazon’s retail business, the customers’ durable needs were identified
as “price, selection, and convenience.” We can use the same concept of durable needs as our
North Star in the agentic AI era. When evaluating any new technology, consider first what
problem the technology is trying to solve. Determine whether this problem will persist and
produce enough friction to require a solution. Let’s apply this to agentic AI.

We can accept that for AI model inference, cost, latency, and capability are
durable needs.

For AI model inference, we can declare that

     - Customers will always want AI models that are more capable.

     - Customers will always want AI models that cost less.

     - Customers will always want AI models that reduce latency.

When these durable needs are understood, having access to the widest selection of
models that can be chosen to optimize against these durable needs is the imperative. For
MCP, let’s state the obvious: the M × N complexity problem that MCP solves is existential
to agentic AI, and it’s not going away. The solution may change, but the problem won’t.
Data security is a basic requirement. We can say it’s a durable need of agentic AI and
therefore safe to invest in it.

For agentic AI solutions, we can declare that:

     - Customers will always want solutions that increase agentic security

     - Customers will always want solutions to reduce agentic integration
complexity

Let’s discuss the business of data.

**The Business of Data**

Data has become the lifeblood of modern enterprises, transforming the way businesses
operate, compete, and thrive in a rapidly evolving digital landscape. Understanding the
needs of a business and aligning data engineering and AI initiatives to drive the desired
outcomes is one of the most significant ways a data engineer can influence the trajectory
of a business.

27

Chapter 1 Introduc i D E i i i G i A ic A AW

**Data As a Strategic Asset**

Your company data is an asset. Like real estate, it’s a localized monopoly. No other
company has exactly the data you do. But if we take this analogy to its logical conclusion,
we can say that as with any asset, the business goal is to generate some kind of return
from that asset. I will argue that business value derived from data falls into two primary
categories: data-driven decision-making and data-driven revenue. The first focuses on
enhancing decision-making processes and operational efficiencies. The second creates
direct financial value or revenue streams. Keep in mind that machine learning and AI are
derivatives of the data—models are trained on data—therefore, for the purposes of this
discussion, they are included in “data-driven revenue.”

**Data-Driven Decision Making**

It could be said that the success (or failure) of any company is merely a product of their
decisions. Which customers should we serve? What markets should we enter? What
products should we sell? Who should we hire? How should we be organized? What
technology should we leverage? How much capital do we need? Modern enterprises no
longer rely on intuition. They can’t afford to. A study by McKinsey found that companies
that were data-driven reported that data analytics contributed at least 20 percent to
earnings before interest and taxes (EBITA) <sup>7</sup> . They’ve culturally transformed the way
they do business to drive strategic and operational decisions using facts, metrics, and
insights. But not all made the transition gracefully. In an annual survey by NewVantage
Partners, 91.9% of executives cite cultural obstacles as the greatest barrier to becoming
data-driven <sup>8</sup> .

Table 1-1 offers some examples where data-driven decision-making can impact
several business concerns. By understanding these general business concerns, you can
anticipate the needs of the business in your role as a data engineer and be proactive
instead of reactive.

7 Catch them if you can: How leaders in data and analytics have pulled ahead. McKinsey,
[2019. (https://www.mckinsey.com/capabilities/quantumblack/our-insights/](https://www.mckinsey.com/capabilities/quantumblack/our-insights/catch-them-if-you-can-how-leaders-in-data-and-analytics-have-pulled-ahead)
[catch-them-if-you-can-how-leaders-in-data-and-analytics-have-pulled-ahead).](https://www.mckinsey.com/capabilities/quantumblack/our-insights/catch-them-if-you-can-how-leaders-in-data-and-analytics-have-pulled-ahead)

8 Why Becoming a Data-Driven Organization is So Hard. Bean, Randy.
[Harvard Business School. Feb, 2022. (https://hbr.org/2022/02/](https://hbr.org/2022/02/why-becoming-a-data-driven-organization-is-so-hard)
[why-becoming-a-data-driven-organization-is-so-hard)](https://hbr.org/2022/02/why-becoming-a-data-driven-organization-is-so-hard)

28

Chapter 1 Introduc i D E i i i G i A ic A AW

**_Table 1-1._** _Data-Driven Decision Making for Various Business Concerns_

**Business Concern** **Data-Driven Decision Making**

O E U
identifying waste, optimizing processes, and lowering cost.

R U
management, or cybersecurity.

Compliance U

Performance Metrics U
customer satisfaction (CSAT A
market (TT

Investment U
products or features to build or identifying merger or acquisition (M&A

Data-driven revenue is data that is directly supporting the revenue of the company.
Data-driven revenue in this context means data that supports sales and marketing,
data-driven products or services that customers are directly paying to consume, or data
itself as the product. In Table 1-2, I describe what data-driven revenue looks like for key
revenue-side business operations.

**_Table 1-2._** _Data-Driven Revenue Across Different Business Functions_

**Business Function** **Data-Driven Revenue**

Sales and Marketing U
revenue.

P Customers pay directly for data-driven products or services.

D Sell data or data derivatives (A

Both data-driven decisions and data-driven revenue are important, so why is it
necessary to make this distinction? The more directly we can tie data projects to the core
revenue-producing activities of the business, the more political support and investment
these projects will receive.

29

Chapter 1 Introduc i D E i i i G i A ic A AW

How can we be sure the company is fully leveraging ALL the data that the
company owns?

Gartner defines dark data as “the information assets organizations collect, process, and
store during regular business activities, but generally fail to use for other purposes. <sup>9</sup> ”

According to IDC, 90% of a company’s data is unstructured and not being fully
exploited. <sup>10</sup> The 10% of the “visible data” is only the tip of the proverbial iceberg (see
Figure 1-9 below). This typically includes application data, CRMs, ERPs, and data
warehouses.

**_Figure 1-9._** _The Data Iceberg (Image by Freepik)_

[9 Dark Data. Gartner Glossary. Accessed March 26, 2024. (https://www.gartner.com/en/](https://www.gartner.com/en/information-technology/glossary/dark-data)
[information-technology/glossary/dark-data)](https://www.gartner.com/en/information-technology/glossary/dark-data)

10 UNTAPPED VALUE: What Every Executive Needs to Know About Unstructured Data.
[IDC. August 2023. (https://www.box.com/resources/unstructured-data-paper)](https://www.box.com/resources/unstructured-data-paper)

30

Chapter 1 Introduc i D E i i i G i A ic A AW

What types of data make up dark data? It’s the thousands of audio recordings of
customer service calls. It’s 5 years’ worth of support tickets and emails. It’s 10,000
application log files. It’s one million lines of code. It’s surveillance footage. It’s sensor and
geolocation data from fleets of vehicles and edge devices. It’s financial reports, and travel
and expense data.

Business alignment means understanding what priorities the business has identified
and aligning technology use cases like AI-augmented data projects to those priorities.
Business outcomes fall into three general buckets: revenue, cost, and risk management.
Every business wants to increase revenue, reduce cost, and manage risk.

Governance of a company can include its executive leadership and board of
directors. A strategic planning process formalizes and defines business-level goals
and strategic objectives that will enhance competitiveness in the market, increase
profitability, or ensure long-term sustainable growth. If your understanding of business
is limited, the impression you might get is that the business is a monolith. It has one
set of priorities. The reality is more complicated. At the CxO level there will be multiple
senior leaders—each with unique and differentiated responsibilities. Any one of these
leaders could serve as an executive sponsor for data engineering projects that span one
or more domains. Table 1-3 describes a sample of common leadership roles and what
they may need you to build for them.

31

Chapter 1 Introduc i D E i i i G i A ic A AW

**_Table 1-3._** _Executive Roles, Personas, and Use Cases_

**Role** **Persona** **Use Cases**

Chief Financial
O O

Chief
O
O OO

Chief
Information
O O

Chief P
O PO

Chief
Marketing
O O

32

T O
operations, planning, and risk
management strategies for the
company. T O
which strategic investments the
company should make to yield the
highest risk-adjusted return.

T OO
day operational functions of the
company.

T O
IT

T PO
strategy, development, and success
of a company’s products, combining
product innovation with strategic
vision.

T O
strategies that drive growth and
enhance brand value for the
company.

Integrate historical financial data with
external market indicators and operational
data to enhance forecasting models
to anticipate financial challenges and
opportunities and allocate resources
efficiently.

A
performance, inventory levels, and demand
forecasts. P
inventory management, supplier selection,
and logistics, optimizing the supply chain for
cost, speed, and reliability.

A T
documentation, FAQs, and troubleshooting
guides based on historical IT
and resolutions. Monitor and report insights
on the health of IT

A
and competitor products to generate new
product ideas or enhancements. E
prototyping to collect metrics to evaluate and
refine product features to better meet market
demands and customer preferences.

P
scale, including emails, social media posts,
and advertising copy, tailored to the interests
and behaviors of individual customers or
segments. Significantly increase engagement
rates and conversion by delivering more
relevant content to the targeted audience.

Chapter 1 Introduc i D E i i i G i A ic A AW

**Theoretical Concepts in Data Engineering**

Every technical profession is firmly grounded in the foundation of computer
science theory.

I encourage readers to research and understand general data engineering topics that
are fundamental and important for a practitioner to know. As AI takes on more of the
knowledge work in data engineering, the tendency may be to rely more and more on its
capabilities, allowing the abstraction to eventually erode general understanding of how
data systems work. This is the ultimate folly. Practitioners who succumb to laziness are
at risk of being exposed at the moment when AI fails or a use case demands skills that AI
can’t fill.

Readers should familiarize themselves with or review the following list of topics:

     - ACID properties.

     - The three strategies of Redundant Array of Independent
Disks (RAID).

     - The four levels of database normalization.

     - SQL Joins.

     - Star and snowflake schema.

These topics may be referenced in this book, but they will not be examined in depth.
While this book is not intended to be a textbook, the following sections will cover
three of the most important (and related) data engineering concepts in the context of
cloud computing: distributed computing, scalability, and the CAP theorem.

Years before AWS was created, a 1998 Amazon memo titled, “Distributed Computing
Manifesto, <sup>11</sup> ” declared distributed computing as their North Star. The memo described
Amazon’s architecture as tightly coupling the application to the data with a workflow
that depended on a single instance database.

[11 Distributed Computing Manifesto, https://www.allthingsdistributed.com/files/amazon-](https://www.allthingsdistributed.com/files/amazon-distributed-computing-manifesto-1998.pdf)
distributed-­

33

Chapter 1 Introduc i D E i i i G i A ic A AW

Amazon observed:

_As the amount of work increases (a larger number of orders per unit_
_time), the amount of processing against the central instance will_
_increase to a point where it is no longer sustainable._

In the digital age of online retail, distributed computing was now a business
imperative. Amazon’s technical architecture limited the ability of their business to grow
and scale.

They concluded:

_Instead of processes coming to the data, the data would travel to_
_the process._

Five years later in 2003, Google published a research paper describing a distributed
file system they called the Google File System (GFS). The first paragraph makes the case
for horizontally distributing storage across many more lower-cost commodity machines:

_[The Google File System] provides fault tolerance while running on_
_inexpensive commodity hardware, and it delivers high aggregate_
_performance to a large number of clients._

Months later in 2004, a second Google paper, _MapReduce: Simplified Data_
_Processing on Large Clusters_ <sup>12</sup> was published. The founders of Hadoop, Doug Cutting
and Mike Cafarella, credit this research as the basis for Apache Hadoop and the Hadoop
Distributed File System (HDFS).

These innovations were born out of business necessity. The growth in online orders
required Amazon to find technical solutions that scaled to process those orders, or
they risked losing revenue. Google was indexing an exponentially growing internet and
making it instantly searchable for an exponentially growing number of users.

This provides a good backdrop for our discussion of the CAP theorem.

[12 Dean, Jeffrey; Ghemawat, Sanjay (2004). ”MapReduce: Simplified Data Processing on Large](http://research.google.com/archive/mapreduce.html)
[Clusters”. pp. 137–150.](http://research.google.com/archive/mapreduce.html)

34

Chapter 1 Introduc i D E i i i G i A ic A AW

**The CAP Theorem**

A foundational theory in distributed computing is the CAP theorem. CAP is an acronym
representing three competing features in clustered data systems:

     - Consistency

     - Availability

     - Partition tolerance

The CAP theorem is often communicated as a triangle or a Venn diagram (see
Figure 1-10). The theorem posits that only two out of the three features can be
guaranteed in the event of a communication failure between the nodes.

**_Figure 1-10._** _The CAP Theorem_

The CAP Theorem is often misunderstood. During normal operation when all nodes
can communicate, all three features are achievable _with latency_ . Modern systems have
been designed so that the latency is acceptable.

35

Chapter 1 Introduc i D E i i i G i A ic A AW

For example, system designers can minimize latency of a computing cluster in
several ways:

     - Minimize the networking complexity between nodes.

     - Minimize the physical distance between nodes.

     - Use high-performance hardware for networking, storage, computing,
and memory.

     - Optimize software and algorithms for load balancing, concurrency
and parallelism, and caching.

The CAP Theorem requires system designers to choose two of these constraints to
guarantee _only when there’s a communication failure between nodes_, and this decision is
revealing as to their overall strategy. I’ll define each of these constraints and then explain
how they can be applied to AWS services.

Consistency means that a read request is _guaranteed_ to return the most recent data,
regardless of which node is servicing the request. In this context, consistency really
means _strong consistency_ or _read-after-write_ consistency.

Availability means that every read request is _guaranteed_ to receive a functional and nonerror response. Data will be returned no matter what, but no guarantees will be made as
to the version or recency of the data.

Partition tolerance is the third feature, and it describes a system that can continue
operating despite communication loss between nodes. This constraint is a little tricky
because it derives from other fundamental assumptions in IT. Why are multiple nodes
required? Every IT resource (compute, memory, storage, networking) is delivered by
physical hardware made from electromechanical devices.

36

Chapter 1 Introduc i D E i i i G i A ic A AW

**Postulate 1** : every electromechanical device has a nonzero
probability of failure. Mitigating the risk of hardware failure in a
system requires redundancy—i.e., replicating the application and
data across multiple nodes in a cluster. The more nodes added to
a cluster, the lower the probability that hardware failure will result
in data loss.

**Postulate 2** : communication between nodes is never guaranteed
due to the risk of network failure. This is why the constraint
of partition tolerance is _non-negotiable_ for modern systems.
The partition tolerance constraint accepts the possibility that
the nodes of a cluster may be operating normally but cannot
communicate with each other due to a network failure. As a result,
the data in the system cannot maintain consistency. The critical
question for the user is knowing how the system will respond in
this scenario. The answer is determined by which second feature
the designer favors: consistency or availability.

Let’s explore each option to help you think about these tradeoffs.

**Consistency-Partition Tolerance (CP)**

If the designer chooses consistency (CP), the node of the cluster will return an error until
communication is re-established and a consistent version of the data can be reconciled
between the nodes.

**Availability-Partition Tolerance (AP)**

If the designer chooses availability (AP), the node of the cluster will return the most
recent version of the data as known to that node regardless of whether that version of the
data is consistent with the other nodes in the cluster.

As a data engineer leveraging AWS cloud services to build solutions, it is important to
understand how AWS applies these theories when building solutions. Cloud computing
naturally favors distributed computing and thus availability over consistency by default.
The term that is often used is _eventual consistency_ . This means that while the write is
being replicated to all the nodes, a read request to a node that does not have the latest
write will not reflect that write.

37

Chapter 1 Introduc i D E i i i G i A ic A AW

Some AWS services have strong consistency features. Amazon DynamoDB (a
NoSQL database service) delivers “eventually consistent” reads by default but also offers
_strongly consistent_ reads as a feature that can be invoked by setting a parameter for
read operations. Eventually consistent reads are more performant and half the cost of
strongly consistent reads. DynamoDB also supports global tables, which are multiregion,
multiactive databases. Reads from global tables are eventually consistent.

Strong consistency may not include updates or deletes. Strong consistency in
DynamoDB includes read-after-update, read-after-delete, and read-after-write
consistency. Amazon S3 (object storage), by contrast, implements strong consistency as
read-after-write consistency.

In short, it’s important to understand the consistency model of the underlying
services you are using to build your solutions, as it will help you avoid hard-to-debug
errors later in the development cycle.

That brings me to my favorite topic: scalability.

Surprisingly, many senior data engineers misunderstand what scalability means, which
makes it a great interview topic:

_How would you define scalability and can you depict it visually on_
_a graph?_

Many often confuse scalability and performance. They are not the same. I’ll refer
back to the Amazon memo on distributed computing.

They observed:

_As the amount of work increases (a larger number of orders per_
_unit time), the amount of processing against the central instance_
_will increase…_

What they are describing here is scalability. More work (orders that need to be
processed) is being requested in the same span of time. More resources are needed
(processing against the central instance) to perform this work.

38

Chapter 1 Introduction to Data Engineering with Generative and Agentic AI on AWS

Let’s generalize this into a common definition:

_A system can be considered ideally scalable…if for every unit_
_increase in a resource applied, the system will be able to process an_
_equivalent unit increase of work_ _<u>in the same period of time</u>_ _without_
_compromising performance._

If we were to depict the theoretical ideal of a perfectly scaling system, it would look
like Figure 1-11. Time ( _t_ ) remains constant ( _k_ ) as resources and work rise linearly.

**_Figure 1-11._** _Illustration of Ideal Linear Scalability_

Depending on the type of workload and the architecture strategy, real-world
systems may not scale linearly beyond a certain scale primarily due to added overhead
and bottlenecks. For example, adding servers increases network communication and
coordination needs. Shared resources like databases and network bandwidth become
bottlenecks. Instead, real systems may exhibit sublinear scalability, where performance
improvements plateau as resources increase beyond a certain scale. Figure 1-12 shows
how a workload may scale given real-world constraints.

39

Chapter 1 Introduction to Data Engineering with Generative and Agentic AI on AWS

**_Figure 1-12._** _Practical Scaling of Real-World Systems_

For this reason, it’s important to understand—through load testing—the profile of
how your specific workloads scale against peak and forecasted demand. To explain how
this can be confusing, I’ll use a physical world example.

Think about a horse pulling a cart. A normal walking pace for a horse is about 4.5
mph. Let’s say this 1,000 lb horse can pull about 2.5 times its body weight, or 2,500
lbs. When the horse is pulling this load, we’d assume its pace would drop, perhaps to
3 mph. If we add a second 1,000 lb horse but don’t add any more load to the carriage,
we observe that the walking pace is now faster, say 4 mph. From that observation, one
might conclude that scaling capacity led to improved performance since the horses
walked _faster_ after adding a second horse. That’s the wrong interpretation. The correct
way to think about this scenario is that additional capacity was added and the load was
distributed across both, easing the load on the first horse by adding some of the load to
the second horse. If the capacity of these two horses was fully utilized, then 5,000 lbs
(2x the load) could be transported at the same speed (3 mph) that one horse could
achieve with a single load.

The overall message here is to properly distinguish between scalability and
performance. If a system is degraded, ensure that there are no resources constrained
preventing it from scaling to serve the increased load. To improve performance,

40

Chapter 1 Introduc i D E i i i G i A ic A AW

components of the system need to be enhanced to enable it to process the same work
more efficiently. In computing, this means swapping in faster memory, faster compute,
faster storage, or more optimized networking.

In this opening chapter, I establish the transformative moment we’re living through—
one that began with OpenAI’s release of ChatGPT in November 2022 and has since
triggered the largest annual capital investment in history, eclipsing even the dot-com
era in inflation-adjusted dollars. The hundreds of billions of dollars committed by tech
giants reflects, not just opportunity but existential necessity: the race to achieve artificial
general intelligence will determine global power dynamics for decades to come. Yet
while everyone focuses on chips and power—both receiving massive investment—I
argue that data represents the next frontier, as the foundation upon which all AI success
ultimately depends.

This creates an extraordinary opportunity for data practitioners. I explain why
software engineering will be disrupted far more deeply than data engineering. The
unique characteristics of data positions the practice of data engineering to not just
survive AI disruption but to lead the transformation. Data’s inherent criticality demands
specialized governance, complex workloads require deep domain expertise, and
fragmented tool ecosystems need orchestration that AI cannot yet automate. Building
on this foundation, I introduce the core technologies—AWS cloud services, generative
AI, agentic systems, retrieval-augmented generation (RAG), and emerging standards
like Model Context Protocol—that will enable you to build AI-augmented data solutions
and transform data assets into sustainable business value. I introduce Kiro and Kiro
Autonomous Agent, the agentic coding platform that can author high-quality code and
automate many of the development tasks. Toward the end of the chapter, I grounded the
discussion in theoretical data engineering topics, including distributed computing, the
CAP theorem, and scalability.

In the next chapter, I focus on one of the most important topics in data engineering:
data security and governance. No matter what data-enabled agentic AI solutions you
build, keeping your data secure is always job zero!

41

**CHAPTER 2**

## **Data Security** **and Governance**

It’s understandable why data security and governance topics can seem intimidating—
the stakes are high! High profile data breaches can end careers and irreparably damage
brands. Ransomware can bring critical operations to a halt and cost businesses millions
to recover. A 2022 data threat report released by Thales reported that over 60% of
corporate data worldwide is stored in the cloud. <sup>1</sup> In 2023, over 80% of data breaches
involved data stored in the cloud. <sup>2</sup> Every single one of those breaches were due to cloud
misconfiguration by the customer. The National Security Agency (NSA) identified
cloud misconfigurations as the biggest threat to cloud security. <sup>3</sup> Agentic AI is rapidly
transforming how organizations build robust, adaptive security postures that respond
dynamically to evolving threats. AI-enhanced AWS services are also making it easier to
govern, document, share, and operationalize data in an organization.

By the end of this chapter, you’ll understand how to confidently implement
the three core pillars of data governance: ensuring appropriate data discovery and
access, maintaining comprehensive security protections, and implementing robust
audit capabilities. I’ll guide you through the AWS Shared Responsibility Model so you
can clearly distinguish between AWS’s infrastructure security obligations and your
application-level security responsibilities. You’ll learn to implement enterprise-grade

1 Thales Data Threat Report.” Thales, 2022.

2 Why Data Breaches Spiked in 2023. Stuart Madnick. Harvard Business Review. Accessed April
[2024. https://hbr.org/2024/02/why-data-breaches-spiked-in-2023.](https://hbr.org/2024/02/why-data-breaches-spiked-in-2023)

3 Migrating Cloud Vulnerabilities. National Security Agency. January 2020. Accessed Apr 2024.
[https://media.defense.gov/2020/Jan/22/2002237484/-1/-1/0/CSI-MITIGATING-CLOUD-](https://media.defense.gov/2020/Jan/22/2002237484/-1/-1/0/CSI-MITIGATING-CLOUD-VULNERABILITIES_20200121.PDF)
[VULNERABILITIES_20200121.PDF.](https://media.defense.gov/2020/Jan/22/2002237484/-1/-1/0/CSI-MITIGATING-CLOUD-VULNERABILITIES_20200121.PDF)

43
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_2](https://doi.org/10.1007/979-8-8688-2199-8_2#DOI)

Chapter 2 Data Sec d c

security using AWS IAM, key management service, and certificate manager. I then
explore the unique security challenges introduced by generative AI solutions and
how best to mitigate them. I’ll introduce the AWS Security Agent and describe how it
can help customers secure their environment. We’ll examine Model Context Protocol
(MPC) security considerations, as MCP’s ability to connect agentic AI with enterprise
systems creates both opportunities and risks that require careful management.
Additionally, you’ll discover how Amazon DataZone enables comprehensive data
catalog management and lineage tracking while AWS Audit Manager provides the
detailed compliance capabilities essential for generative AI governance. This foundation
will enable you to build AI-augmented data solutions that deliver transformative
business value while maintaining the security standards that enterprises demand.

Data governance is the combination of people, processes, and technology that
organizations use to ensure the quality and security of their data throughout its lifecycle.
Figure 2-1 shows the high-level conceptual operating model of data governance.

44

Chapter 2 Data Sec d c

**_Figure 2-1._** _Operating Model of Data Governance_

From this diagram, we can see the many components of activities and practices
that have to be designed, implemented, and managed over time to ensure robust data
governance.

There are ultimately three goals to data governance:

1) Find, access, and share the right data to the right consumers.

2) Keep data safe and secure.

3) Enable appropriate audits and controls.

45

Chapter 2 Data Sec d c

**The Evolving Data Governance Challenge**

The data governance challenge is evolving, and this evolution is being driven by several
factors.

**The Growth of Unstructured Data**

As Gartner noted, 80–90% of corporate data is unstructured, but it’s also growing _3 times_
_faster_ than structured data. A modern data strategy needs to expand the data lake to
govern and manage unstructured data. New tools are needed to properly manage and
govern unstructured data.

**Government Regulations for Data and AI**

The increase in government regulations for data privacy, data residency, and artificial
intelligence is accelerating. Laws that require companies to enforce certain individual
privacy rights can be onerous. In many countries and jurisdictions, consumers have the
right to see what data a company collected about them. They also have the right to be
forgotten—requiring the company to destroy all data about that person. New regulations
by the European Union on AI add additional restrictions for what use cases AI can be
used for in the workplace.

**Data Governance for Generative and Agentic AI**

Data is the foundation for machine learning and generative AI solutions, and these
capabilities present new challenges for a data engineer to address. Businesses must track
data lineage to understand the source and authenticity of data used in AI models. They’ll
need to implement additional controls to protect LLM training data from accidental or
malicious data poisoning. Additionally, failing to redact or mask sensitive data like PII
in a document corpus can lead to it being inadvertently exposed through generative and
agentic AI applications. AI will also become data producers and consumers of data in the
modern data enterprise, and this will change how we think of data governance.

We’ll explore some of these challenges further in this chapter, but first I’ll provide
the prescriptive guidance you’ll need to confidently and deliberately implement robust
security and governance controls at scale in the AWS cloud.

46

Chapter 2 Data Sec d c

**The Shared Responsibility Model**

Amazon’s Shared Responsibility Model (see Figure 2-2) clearly distinguishes that AWS
is responsible for security _of_ the cloud, and customers are responsible for security _in_
the cloud.

**_Figure 2-2._** _AWS Shared Responsibility Model_

Among these are controls that are fully inherited from AWS, such as the physical
and environmental controls to protect AWS data centers and associated assets from
accidental, intentional, and natural events, including fire, water damage, and power
outages.

Some controls are shared between AWS and customers, like patching. AWS is
responsible for patching bugs and vulnerabilities in the infrastructure, while customers
are responsible for patching vulnerabilities in EC2 instances, guest operating systems,
and applications. The same is true for configuration management.

The controls that are solely the responsibility of the customer to implement might
include IAM, networking access control lists (NACLs), security groups, firewalls,
encryption of data, application security, and backup and disaster recovery policies.

47

Chapter 2 Data Sec d c

The goal for this chapter is to demystify data security and governance in the cloud
and to provide you with a strategy for implementing the necessary controls with
confidence. To do this effectively, I’ll introduce each topic and then illustrate how it is
best used for securing and governing data and where it is limited.

Let’s start with the foundational security service of AWS.

**AWS Identity and Access Management (AWS IAM)**

Implementing strong authentication and authorization controls is the first step to
building a secure cloud environment. If you’re not familiar with AWS IAM, some of the
terminology and concepts may be confusing. My hope is to disambiguate these IAM
concepts for the reader because any confusion or gaps in understanding could lead to a
misconfiguration of these important security controls.

A _principal_ in the context of AWS IAM is an entity that can make an API call in AWS. Any
time an API call is made, it needs to identify the principal, and that principal needs to
be authenticated. IAM users, IAM roles (which can be assumed by trusted entities),
and AWS services can serve as principals. If you enable AWS CloudTrail which logs API
requests to AWS services, and review the logs, you’ll notice a principal specified for each
logged request.

When defining a policy, you can specify any of the following as principals:

     - AWS account and root user

     - IAM roles

     - Role sessions

     - IAM users

     - Federated user sessions

     - AWS services

     - _Anonymous_ users—specified with an asterisk

48

Chapter 2 Data Sec d c

**Entities, Roles, and Policies**

AWS IAM separates the concerns of user management, role assignment, and policies to
create a modular and scalable IAM governance model. The diagram below in Figure 2-3
depicts how these access controls are configured at design time and then validated when
requests are made by authenticated principals to AWS resources.

**_Figure 2-3._** _AWS IAM Configuration and Validation of an Access Request_

Let’s go through each of the numbered labels in the diagram to help eliminate any
confusion.

1. Configuration of IAM roles, policies, and permissions

At design time, roles are defined. These roles encapsulate all of
the policies and permissions an authenticated principal will be
authorized to access. This is shown in Figure 2-4.

49

Chapter 2 Data Sec d c

**_Figure 2-4._** _IAM Policy Definition_

2. Authentication of the principal

The type of principal will determine how the principal
is authenticated. If it is a federated user, the user will be
authenticated through an identity provider (IdP) outside of AWS
and then communicated to AWS using OpenID Connect (OIDC)
or SAML 2.0. The identity will assume a role temporarily. This
can be implemented using AWS IAM Identity Center (formerly
AWS SSO). A non-human principal, like a service account or
application, needs to authenticate programmatically, and it can do
that using IAM access keys.

50

Chapter 2 Data Sec d c

3. An operation is requested from a resource (Amazon S3)

In our example, we are making a request to Amazon S3 to perform
some sort of operation. An example of a valid operation includes
writing an object to a bucket. The API call is made to the service,
which includes the authenticated principal and its associated
temporary credentials.

4. The access request is authorized by AWS IAM

The AWS service validates the authenticated principal’s access via AWS
IAM and either grants or denies execution of the operation requested.

Now that we explored how the authentication and authorization process works, let’s
dive deeper into IAM policies.

**The Anatomy of an IAM Policy**

IAM policies have several sections, which I’ll describe briefly.

**Version** : This section specifies the version of the IAM policy language. It’s typically
set to “2012-10-17” for policies written in the JSON format.

**Statements** : The statement section defines what operations it is allowing or denying
to which resource. Statements themselves have subsections:

     - **Effect** : Allow or Deny

     - **Action** : Operations specific to the service (i.e., s3:PutObject).
Wildcards can be used to specify multiple actions (i.e., s3:*)

     - **Resource** : The ARN of the AWS resources in scope for the
policy. Wildcards can be used to specify multiple resources. (i.e.,
arn:aws:s3:::example-bucket/*)

     - **Condition** : Conditions are optional and can be used to add further
restrictions on access requests to resources. One use may include
IP address allow lists (“IpAddress”) and block lists “NotIpAddress”.
The condition is applied using a CIDR mask for the “aws:SourceIp”
parameter. Setting a “bool” condition for aws:SecureTransport to
“true” will require all requests to be made over secure transport
(HTTPS). Conditions can also be applied to restrict access based on
time of day, resource tags, or the source VPC.

51

Chapter 2 Data Sec d c

**Principle of Least Privilege**

Users and applications should be provided minimal specific access and only that access
needed to accomplish the task or function needed. This security concept is called
the principle of least privilege (PoLP). This allows for the segregation of duties where
responsibilities are divided among multiple users (i.e., developers vs. DevOps).

Creating secure IAM policies from scratch can be intimidating. Luckily, we can call
upon generative AI tools to assist us in creating a very credible _starting point_ .

From the AWS console, we can use the Amazon Bedrock chat playground to generate
our IAM policy for our Amazon S3 example. Alternatively, you could also use Kiro CLI to
create the policy as a JSON file.

Claude Sonnet Prompt:

Create an IAM policy in JSON that implements the principle of
least privilege that allows uploads to S3 for the prefix tenant-1/
upload and bucket example-bucket that limits requests to
192.0.2.0/24 and requires requests over HTTPS.

Figure 2-5 shows the response from the model.

52

Chapter 2 Data Sec d c

**_Figure 2-5._** _Asking Anthropic Claude 3 Sonnet to Generate an IAM Policy_

Here is the full policy created by Anthropic’s Claude 3 Sonnet in Amazon Bedrock:

```json
{

53

Chapter 2 Data Sec d c

}
```

**Caution** A IA AI
be utilized as an assistive technology to provide a starting point for developers. IA
policies should be rigorously reviewed and validated before implementation. Be
sure to use the latest and most capable models for security-related coding
assistance.

There are other important ways to incorporate AWS IAM in your security strategy,
including authenticating user access to AWS data services.

**IAM Authentication for Data Services**

Many AWS services are integrated with AWS IAM, including database services. This
means that administrators can use IAM roles to implement authentication for database
services like Amazon Redshift and Amazon DynamoDB. Amazon RDS offers the option
of “IAM Database Authentication,” which enables authentication using IAM credentials
rather than a username or password. Traffic between the application and the database
is encrypted using SSL/TLS. Authentication is temporary and is valid for 15 minutes.
Figure 2-6 demonstrates the request flow.

54

Chapter 2 Data Sec d c

**_Figure 2-6._** _IAM Authentication to Amazon RDS_

Using IAM-based authentication offers advantages over other traditional methods
like Kerberos, LDAP, or usernames and passwords. The biggest advantage is centralized
management. Rather than managing users at the database level, where an administrator
would need to create or remove users in each database, they can instead manage user
access at the server or cluster level through AWS IAM.

Here are the data services that support IAM Authentication:

     - Amazon S3

     - Amazon RDS (includes IAM Database Authentication)

     - Amazon Redshift

     - Amazon DocumentDB

     - Amazon Athena

     - Amazon EMR

Figure 2-7 describes how AWS IAM authenticates and serves requests from
Amazon S3.

55

Chapter 2 Data Sec d c

**_Figure 2-7._** _IAM Authentication for Requests to Amazon S3_

Using AWS IAM to govern data has its limitations. It’s important to understand where
and when AWS IAM is needed.

**Encryption for Data Protection**

Businesses considering adoption of the AWS cloud are confronted with this question:
“Are we really going to put our most sensitive data in the cloud rather than keep it in our
private on-premises data center?”

The stakes for this decision are extraordinarily high. Choose to adopt the AWS cloud
and bring industry-leading data tools, services, and continuous innovation to fully
secure and exploit the data. Choose to keep the data in an on-premises data center and
incur a significant opportunity cost and data security risks that could imperil the longterm success of the business.

I’ve invested a significant amount of my professional life working to satisfy the
concerns of infosec teams at small and large enterprises when evaluating cloud
platforms and cloud data services. The magic bullet to gaining their approval will be
the seamlessly integrated data protection features that enable strong encryption of the
company’s data both at rest and in transit.

56

Chapter 2 Data Sec d c

The reason? No one—not hackers, not even AWS under court order—can access
the company’s data without the encryption keys that the customer creates and controls.
Without the keys, the data stored in the cloud is useless. From a data engineering
perspective, encryption of the data is the best tool available for safeguarding data from
unauthorized access.

**Encryption Key Management**

The AWS Key Management Service (KMS) is a fully managed service that can generate
encryption keys and help manage their use across more than 45 different AWS services.
KMS is designed to meet a significant swath of customers’ needs.

**AWS-Owned Keys and Customer-Managed Keys**

Data engineers need to be aware of the capabilities and features of AWS-owned keys
compared to customer-managed keys. Be aware that there is a similar term, customer
master keys (CMK), which has since been renamed to AWS KMS key. References to CMK
still exist to avoid breaking changes. Customer-managed keys give the most control to
the customer. Customers create and maintain their key policies, IAM policies, aliases
for the keys, defined key rotation schedules, and enabling and disabling them. Access
to customer-managed keys can be revoked at any time _by the customer_, so in the event
that the key has been compromised, access to the data can be shut down immediately
to reduce the blast radius. This is not the case with AWS-owned keys, which cannot be
revoked.

I’ll demonstrate how to create customer-managed keys using AWS KMS and encrypt
data at rest in Amazon S3.

import boto3
import json

# Initialize a session using Amazon KMS
kms_client = boto3.client('kms')

# Create a CMK with additional parameters
response = kms_client.create_key(

57

Chapter 2 Data Sec d c

)

# Get the key ID from the response
key_id = response['KeyMetadata']['KeyId']

# Define alias name
alias_name = 'my-key'

# Create an alias for the CMK
kms_client.create_alias(

)

print("Key created with ID:", key_id)

For some customers, key creation in KMS is not an option. In the next few sections,
I’ll present options for customers who need more control over key creation and
management.

**Custom Key Store**

For some customers, key creation in KMS is not an option. Instead, keys are created
and stored in single-tenant hardware security modules (HSM). AWS CloudHSM is a
service that supports customers requiring HSMs and is validated at FIPS 140-2 level 3
overall. AWS CloudHSM offers a feature called AWS CloudHSM custom key store that
connects the CloudHSM to KMS so that the services KMS is integrated with can still
do seamless encryption and decryption transparent to client applications. KMS simply
relays the requests to the CloudHSM, and the custom keys never leave the CloudHSM
unencrypted. Figure 2-8 depicts the CloudHSM custom key store service architecture.

58

Chapter 2 Data Sec d c

**_Figure 2-8._** _AWS CloudHSM Custom Key Solution Architecture_

**External Key Store**

For a very small percentage of businesses, compliance requirements will require them
to create and manage encryption keys in an external hardware security module (HSM)
that they operate on-premises (or in a customer-controlled environment outside of
AWS). However, for those that do need that, AWS provides a solution called the AWS
KMS External Key Store (XKS). XKS works in a similar way to the CloudHSM custom key
store except that the connection is made from AWS KMS to an on-premises HSM that is
outside of the AWS environment. Figure 2-9 shows the integration between AWS KMS
and an external HSM via an XKS proxy.

59

Chapter 2 Data Sec d c

**_Figure 2-9._** _XKS Proxy Connected by a Public Endpoint_

**Encryption Across Regions**

Copying or replicating encrypted data, snapshots, backups, and certain types of clusters
across regions could encounter challenges or limitations depending on what types of
keys are used and the method for performing the cross-region transfer. This is needed
when implementing disaster recovery (DR). For instance, a feature called AWS KMS
multiregion keys can facilitate cross-region replication using the same key id and
material. Fully managing backups using AWS Backup makes it easy to move encrypted
backups between regions. There are many other scenarios that might arise, which
are out of the scope of this book. Just be sure to understand how decisions for data
encryption will impact cross-region replication and DR planning.

Encrypting data-at-rest is a euphemism to describe encrypting data where it is stored.
Over 45 AWS services are integrated with KMS, including all major databases and data
storage services. This includes Amazon RDS, Amazon Redshift, Amazon EBS, AWS Glue,
Amazon Kinesis, and Amazon EMR, just to name a few. Encryption of these services
also extends to backups and snapshots. There are a few things to note to avoid any
unpleasantries down the road. Changing the encryption method of a managed Amazon

60

Chapter 2 Data Sec d c

database service will likely require a migration to a new cluster. Encryption services
like CloudHSM and AWS KMS are region-based, and keys cannot be exported—moving
encrypted workloads to different regions might require some additional steps.

AWS services that aren’t integrated with KMS still encrypt customer data, but they
use encryption keys created and managed by that particular service. Some services like
Amazon S3 have default encryption features that implement server-side encryption
using Amazon S3 managed keys (SSE-S3). Since January 2023, all new object uploads
to Amazon S3 buckets are automatically encrypted at no cost and with no impact on
performance.

Encrypting data-in-transit is needed to protect data as it is being sent to and from
services to process and transform the data. AWS network security controls transparently
encrypt data-in-transit at multiple levels. Network traffic between AWS data centers is
encrypted at the physical layer (Layer 1). Traffic within a VPC and between peered VPCs
across regions is encrypted at the network layer (Layer 3). All AWS service endpoints
support TLS and create an HTTPS connection for API requests at the application layer
(Layer 7).

AWS provides solutions to support terminating TLS for customer infrastructure.
Primarily, these include endpoint services like Elastic Load Balancer, Amazon
CloudFront, and Amazon API Gateway. These services enable users to upload their
own digital certificates, establishing a secure cryptographic identity at each endpoint.
Managing digital certificates at scale can be complex due to their expiration and the
need for periodic rotation. To address these challenges, AWS offers the AWS Certificate
Manager (ACM), which streamlines the creation, distribution, and rotation of digital
certificates. ACM provides publicly trusted certificates at no additional cost, which can
be utilized by AWS services to securely terminate TLS connections to the Internet.

Here are the steps to encrypt data-in-transit.

1. Identify an existing domain to use or create one using Route 53.

2. Create a hosted zone in Route 53.

3. Create a CNAME DNS record specifying TTL and routing policy.

4. Create an ACM certificate.

5. Add the domain to the ACM certificate using CNAME.

61

Chapter 2 Data Sec d c

6. Create a load balancer.

a. Choose load balancer type.

b. Scheme and network routing.

c. Choose HTTPS protocol.

d. Define target group.

e. Specify the certificate.

**Note** Due to space constraints, detailed step-by-step instructions for setting
up T AWS load balancer are available at the GitH
this book.

Now that we’ve protected our data at rest and in transit, let’s look at how we will
govern the data at scale.

**Sensitive Data Detection and Redaction**

Sensitive data detection and redaction is an important data security topic that often gets
overlooked. The ability to identify and redact personally identifiable information (PII) in
data lakes and unstructured data sources, such as documents, audio, video, and images,
is becoming a common requirement in retrieval-augmented generation (RAG) use cases.
For this reason, I address this topic in depth in Chapter 8, “Multimodal Data Extraction
and Enrichment with Amazon Bedrock and AWS ML Services.”

**Data Governance on AWS**

Data governance is the methodology, tools, processes, and policies that balance the
competing interests of data privacy, security, and access in a way that maximizes value
to the business while maintaining compliance and minimizing risk. If you want to
create and maintain a data-driven culture, you’ll need to provide the data needed for
business users to analyze and make the right decisions. Inherently, there’s a balancing
act between democratizing data access with governance and control. AWS provides

62

Chapter 2 Data Sec d c

­end-to-­end governance solutions to help you move faster with data by offloading much
of the operational overhead to managed services.

Figure 2-10 shows many of the AWS services mapped to the data governance
function.

**_Figure 2-10._** _Data Governance on AWS_

AWS Glue provides data profiling, data cataloging, data integration, and data
quality capabilities. AWS Entity Resolution is used for schema mapping and matching
records by identifying relationships between datasets. AWS Lake Formation provides
an additional security layer to implement fine-grained access controls to data in the
data lake. AWS Clean Rooms allows you to share data and perform matching operations

63

Chapter 2 Data Sec d c

with third parties without exposing the raw data or PII. Amazon DataZone provides
a business-level data catalog powered by generative AI that allows users to discover,
search, and consume data.

**Data Governance Roles**

Building a business-centric data governance program requires many job functions.
These are the “people” in people, process, and technology.

     - **Executive sponsors** understand many business initiatives on the
corporate roadmap and can help determine priorities for data
governance support.

     - **Data stewards** are from the business and are involved in the details
of projects day to day. They help engineers understand the data
issues that are likely to cause challenges with targeted business
initiatives.

     - **Data owners** make policies about the data, including who should
have access to the data and under what circumstances, how to
interpret and apply regulations, and key terms and definitions.

     - **Data engineers** provide tools that help govern and secure data,
manage data quality, integrate data from a variety of sources, and
find the right data.

Data governance is an expansive topic that could be a book all on its own. What
I hope to accomplish in this section is showcasing the highlights of what an effective
data governance strategy looks like using the purpose-built tools and frameworks AWS
provides. Many of these AWS services and topics we will revisit in later chapters, so this
is just a preview. Amazon DataZone is covered in Chapter 4, “Data Mesh Design with
Amazon DataZone.”

**Fine-Grained Access Control for Data**

Earlier in this chapter, I demonstrated how you can use AWS IAM policies to restrict
access to data in Amazon S3. However, this only reaches a certain level of granularity. To
implement more granular access controls, we can use AWS Lake Formation. I address
this in depth in Chapter 3, “Data Lake Design with Apache Iceberg and S3 Tables.”

64

Chapter 2 Data Sec d c

**Generative and Agentic AI Security**

Solutions that incorporate the use of generative AI foundation models present unique
security risks and challenges. The topics presented in this section may span other
domains and not be pure data security topics. However, it is important to understand
these in the context of data security.

Figure 2-11 shows some of the most common and impactful risks associated with
generative AI model training and inference serving. This list is not intended to be
exhaustive. I finish this section with a discussion on guardrails.

**_Figure 2-11._** _Generative AI Risks_

I’ll discuss many of these briefly and will refer to them in later chapters.

65

Chapter 2 Data Sec d c

**Supply Chain Attack**

A supply chain attack exploits vulnerabilities in the governance and security of
generative AI model training data. Model poisoning is a type of supply chain attack
where data is added to the training set that compromises the quality of the model
(Figure 2-12).

**_Figure 2-12._** _Model Poisoning of the Training Data_

Data engineers can help protect and validate the lineage of training data and its
chain of custody. This attack can also be instigated at the data labeling stage. If a user
assisting with data labeling is providing feedback to a model that is invalid—i.e., it’s a
picture of a dog, but the person labeling the data says it’s a cat (Figure 2-13).

66

Chapter 2 Data Sec d c

**_Figure 2-13._** _Model Poisoning Through Data Labeling_

Waterhole poisoning is another type of supply chain attack where a data source that
is known to be readily used for generative AI model training is compromised with invalid
data. Wikipedia is a good example. Many models are using Wikipedia as a data source,
and a deliberate effort to compromise this open platform could cascade into training
sets that crawl it. A real example is a tool called NightShade, which allows artists to alter
images of art they post online in a way that can severely damage generative AI models. <sup>4</sup>
As a data engineer, it’s important to understand these risks in your role assisting data
scientists and AI specialists with data collection and curation.

**Sensitive Data Leakage**

There are two main ways data can be leaked in generative AI applications. One is via
inference requests served by a model that had sensitive data in the training set. A hard
and fast rule to adopt is to assume that _any data used to train a model could be exposed via_
_inference_ . Data engineers can help ensure that any sensitive data like PII is redacted from
the training set. The other way sensitive data can be leaked is via retrieval-augmented
generation (RAG). Semantic search of a document corpus returns sensitive data that is

4 Dafna Tachover, “Data Poisoning: How Artists Are Fighting Back Against Generative AI,” MIT
[Technology Review, October 23, 2023. https://www.technologyreview.com/2023/10/23/](https://www.technologyreview.com/2023/10/23/1082189/data-poisoning-artists-fight-generative-ai)
[1082189/data-poisoning-artists-fight-generative-ai.](https://www.technologyreview.com/2023/10/23/1082189/data-poisoning-artists-fight-generative-ai)

67

Chapter 2 Data Sec d c

sent to a model in a prompt. The response could return sensitive data
in the response intended for the user. I address redaction later in this chapter and in
Chapter 7, “Multimodal Data Extraction and Enrichment with Amazon Bedrock and AWS
ML Services.”

A confused deputy in the context of AI and RAG is a type of privilege escalation attack
where a user who isn’t authorized to access certain data obtains access via an AI solution
(“the confused deputy”) that has privileged access to the data. Figure 2-14 depicts a
confused deputy request flow.

**_Figure 2-14._** _Confused Deputy Attack via Generative AI Model_

The red arrow shows a bad actor making a direct request to User 1’s data source,
which is rejected. The same bad actor makes a request for User 1’s data through an AI
solution that has privileged access to that data, exposing it in the model’s response.

68

Chapter 2 Data Sec d c

Instances of generative AI model hallucination are reported in the news or regularly
experienced by people using generative AI tools. “Hallucination” refers to a response
produced by a generative AI model that appears plausible and well reasoned but is
actually false or nonsensical. What makes hallucination dangerous is how authoritative
and confident the response can sound. A model’s response is just a probability-chained
sequence of tokens with weights determined by the training data. If you ask a question
that is not supported by the training data, the model returns the sequence with the
highest probability, regardless of whether it’s valid. Hallucination has ramifications
for data engineering and data quality, especially if it is used in pipelines for data
enrichment. The two main ways to mitigate this risk are to implement guardrails and
RAG. I explore the latter in Chapter 8, “Retrieval-Augmented Generation (RAG) with S3
Vectors and Vector Databases.”

**Prompt Injection Attack**

A prompt injection attack exploits vulnerabilities in the input processing mechanism
of a generative AI solution to inject malicious instructions intended to direct the
model to generate harmful responses or leak sensitive data. There are two main types
of prompt injection: direct and indirect. A jailbreak attack is a type of direct prompt
injection that attempts to thwart guardrails to cause the model to generate responses
that are undesirable or harmful. In the early days of ChatGPT, a user would be blocked
from asking how to perform illegal activities like hotwiring a car. The user could adjust
the prompt to claim they were writing a movie script and ask how they should depict
a character hotwiring a car. Discovering and closing gaps has been a cat-and-mouse
game ever since. The crescendo attack <sup>5</sup> is a multiturn jailbreak discovered in 2024 that
was able to successfully evade guardrails in all major providers by gradually escalating
dialogue over many prompts to eventually produce harmful responses.

An indirect prompt injection attack is when instructions are planted in content that
is consumed by generative AI applications that attempt to hijack the model for some
malicious purpose. Email is a great example—malicious content could be sent by a bad

5 Crescendo: A Multimodal Prompt Injection Attack on Large Language Models, ArXiv (2023),
[https://arxiv.org/html/2404.01833v1.](https://arxiv.org/html/2404.01833v1)

69

Chapter 2 Data Sec d c

actor and consumed by an AI copilot authorized to help manage email. The attacker
places an instruction block at the bottom of that email. If the AI copilot has access to
send email, the attacker could ask it to scan the user’s email messages for sensitive data
like credit card and social security numbers and email it to a collection account.

Generative AI models are highly sophisticated and capable, but they have no internal
security mechanism for access control or risk mitigation. This means that whatever
protections organizations want to implement, they must build it as a solution around
the model. Most simply, this means screening what goes into the model and what comes
out. Guardrails are fundamental to mitigating many of the risks presented in this section,
including sensitive data leakage, confused deputy, hallucination, and prompt injection
attacks. Model providers and model hosting services, including Amazon Bedrock,
implement robust and sophisticated guardrails as part of their service. I’ll explore these
features later in this chapter. If you choose to self-host models, including open-source
models, you may need to implement your own guardrails to protect them. Figure 2-15
provides an example of a generalized evaluation service as a guardrail component.

**_Figure 2-15._** _Conceptual Diagram of a Guardrail Service_

In this generalized conceptual example, there is some kind of guarded resource.
The input is first sent to an evaluation service. This service evaluates the input against
specific criteria and generates a score. The score is compared to a defined threshold to
determine if it passes or fails. If it passes, it is sent to the guarded resource. If it fails, it
invokes the guardrail response.

70

Chapter 2 Data Sec d c

Overall, implementing guardrails on your own is a daunting task, luckily Amazon
Bedrock can do much of the heavy lifting for you.

**Safeguards in Amazon Bedrock**

Amazon Bedrock provides a feature called **Guardrails** that helps builders protect their
generative AI applications. These safeguards address prompt attacks, filter harmful
content, topics, PII, and words, and check for hallucination and relevancy. Because these
guardrails are defined as independent entities, each guardrail can be applied to multiple
generative AI solutions. Table 2-1 shows each type of safeguard and what they do.

**_Table 2-1._** _Safeguards in Amazon Bedrock_

**Safeguard** **Scope** **Purpose**

Content filters I
model
responses

Denied topics I
model
responses

Word filters I
model
responses

P
override system instructions. Filter harmful content categories
like hate, insults, sexual content, and violence for text and images

Topic filtering: Block up to 30 topics that are not appropriate or
risk incurring liability for the company. E
tax, medical, or legal advice.

Word filtering: Block up to 10,000 words or phrases, which can
be added manually or uploaded from a local file or S3 object.

PII PII
names, addresses, phone numbers, and SSN
Custom sensitive information filtering: A
patterns to filter custom types of sensitive information.

Grounding and relevance validation: Detect and block
hallucination and irrelevant responses.

71

Sensitive
information
filter

Contextual
grounding

I
model
responses

Model
responses

Chapter 2 Data Sec d c

Let’s take a look at two of these safeguards with fine-grained controls. For content
filtering, there are selectors for applying filters to text or images and a strength threshold
from **None** to **High** . Figure 2-16 shows filtering text for hate and sexual content as well as
images for sexual content.

**_Figure 2-16._** _Content Filtering in Amazon Bedrock Guardrails_

For PII data, we can select whether to block or mask each of the 31 PII types (see
Figure 2-17).

72

Chapter 2 Data Sec d c

**_Figure 2-17._** _Sensitive Information Filters in Amazon Bedrock Guardrails_

Amazon Bedrock makes it easy to quickly define and apply safeguards to mitigate the
unique risks of serving generative AI solutions.

**AI-Powered Security with the AWS Security Agent**

AWS Security Agent is a frontier agent released by AWS in 2025 that provides a number
of proactive and on-demand security services for customers. It reviews your applications
for security vulnerabilities throughout the SDLC, conducts automated security reviews
based on criteria defined by your security team, and can even perform on-demand
penetration testing. AWS Security Agent is designed for application security scanning
and testing; however, it is worth reviewing the capabilities as a quick study in the art of
the possible and perhaps even as a foreshadowing for what’s to come for data security.

Get started by searching for AWS Security Agent from the console. To create an
agent, you’ll need to provide an Agent Space, which you can think of as a specific project
or application. Figure 2-18 shows the creation process from the console.

73

Chapter 2 Data Sec d c

**_Figure 2-18._** _Creating an AWS Security Agent in the Console_

Scoping agents down to this level allows you to customize the security requirements
specific to that project. The AWS Security Agent offers 3 primary services: design review,
code review, and penetration testing (see Figure 2-19).

74

Chapter 2 Data Sec d c

**_Figure 2-19._** _AWS Security Agent Services_

My security agent can connect with Git repositories and analyze documents I upload
to perform its security review. For the design review specifically, I can choose from the
many AWS-managed security requirements shown in Figure 2-20, which includes audit
logging best practices and authorization best practices, or I can create my own custom
security requirements.

75

Chapter 2 Data Sec d c

**_Figure 2-20._** _Managed Security Requirements for Design Reviews_

For code reviews, AWS Security Agent scans for common vulnerabilities such as SQL
injection, cross-site scripting, and inadequate input validation.

The AWS Security Agent can also perform penetration testing. You will need to
configure target domains (ownership verification required), private endpoint VPCs, and
authentication credentials. You can also connect GitHub repositories or S3 buckets for
additional context.

This agent service was newly released and in preview at the time of this writing. It’ll
be interesting to see how the AWS Security Agent evolves over time.

76

Chapter 2 Data Sec d c

**Model Context Protocol (MCP) Security**

Security for MCP is one of the most important topics enabling agentic AI. Without MCP
and secured access to data and tools, agents are far less useful. Understanding how
to secure and authenticate to MCP servers will support important thought exercises
as you read the rest of this book. You’ll be able to conceptualize building out an MCP
strategy for the enterprise as we encounter different data platform strategies and
services. The story of MCP security is a complicated one. MCP’s rollout drew significant
scrutiny over security concerns, with researchers finding that nearly half of MCP
servers contain command injection vulnerabilities, lack proper authentication controls,
and are susceptible to prompt injection attacks that could allow malicious actors to
execute harmful commands or steal sensitive data. Specification changes in June 2025
introduced security improvements, which addressed much of the initial criticism. As late
as August 2025, security researchers discovered a security flaw in Anthropic’s reference
MCP server for PostgreSQL, which allowed read-only restrictions to be bypassed and
arbitrary SQL statements to be executed. Other limitations and gaps will continue to
be identified and addressed as development progresses. However, let’s recognize that
the problem it is solving is a critical one for agentic AI—agents need a standard way to
integrate with tools, data, and business systems. Attempting to integrate directly with
each service or data source can be described as an M x N complexity problem. MCP is
a unified, universal natural language API that allows agents to leverage tools and data
sources without needing to know the particulars of how those requests are made. It’s
been called “the USB-C port for AI.” It’s a vital abstraction layer. Figure 2-21 illustrates
the difference architecturally.

77

Chapter 2 Data Sec d c

**_Figure 2-21._** _Direct Integration vs. MCP for Agentic Resource Access_

The primary inhibitor for enterprise-wide adoption of MCP, and by extension,
agentic AI, is and will continue to be security. Today, most MCP implementations
use local MCP servers over STDIO transport, which do not use OAuth but instead use
environment credentials. This is why coding assistants and IDEs with plugins acting as
MCP hosts that build out local MCP servers have gained faster adoption. Eventually,
standalone remote MCP servers over HTTP will be the transport option that enterprises
will need to adopt to fully realize the transformational value of autonomous multiagent
systems.

These are the best options available right now, but gaps still remain. There is a
spirited debate as to what is needed to implement an autonomous agent mesh securely.
Some of these topics include

     - Cross-agent authorization delegation—Allow agents to delegate tasks
to other agents with their permissions.

     - Headless consent mechanisms—Allow an agent to grant permissions
on behalf of a user.

78

Chapter 2 Data Sec d c

     - Trust framework for multiagent systems—Provide agent identity and
trust chains to track the authorization of an agent and its sub-agents
performing a task.

Stay tuned as MCP project maintainers, the industry, and specifically AWS work to
address these challenges.

**Inbound and Outbound Authentication**

The first important security concept to understand for MCP is that there is both inbound
authentication and outbound authentication (see Figure 2-22).

**_Figure 2-22._** _Inbound and Outbound Authentication for MCP_

An external actor like an agent needs to authenticate to the MCP server. The MCP
server needs to then authenticate to the backend resources defined as tools.

79

Chapter 2 Data Sec d c

While the frameworks and SDKs will abstract away the lower-level details of how this
is implemented, it’s important to know conceptually how it works. The June 2025 MCP
specification requires OAuth 2.1, which adds the following requirements over OAuth 2.0:

     - Proof Key for Code Exchange (PKCE) is required for public client
authorization flows.

     - Redirect URIs must use exact matching (no wildcards or partial
matching).

     - All authorization and token endpoints must use HTTPS.

     - Tokens must be encrypted when stored at rest or in memory.

MCP implementations may employ OAuth 2.0 requirements for the foreseeable
future; however, it’s important to understand the new requirements as they start to be
phased in.

**MCP Servers As OAuth Resource Server**

The MCP specification classifies MCP servers as OAuth resource servers. As an OAuth
resource server, an MCP server acts as a host for protected resources and can accept and
respond to requests for access to those resources using access tokens. There was some
debate early on as to whether an MCP server could also act as an OAuth authorization
server. In the end, the spec remained agnostic (it is not forbidden); however, keeping the
concerns separate is considered the best practice. It minimizes the attack surface and
maximizes flexibility and scalability, as each server can be managed independently. For
an in-depth treatment of this debate, refer to Aaron Parecki’s blog post, _Let’s fix OAuth_
_in MCP_ . <sup>6</sup>

6 Parecki, A. (2025, April 3). Let’s fix OAuth in MCP. _Aaron Parecki_ [. https://aaronparecki.](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol)
[com/2025/04/03/15/oauth-for-model-context-protocol.](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol)

80

Chapter 2 Data Sec d c

**MCP Client-Server Request and Authorization Flows**

Officially, there are 4 grant types supported in OAuth 2.1:

     - Authorization Code Grant (interactive applications)

     - Client Credentials Grant (machine-to-machine authentication)

     - Device Authorization Grant (devices with limited input capabilities)

     - Refresh Token Grant (extend a session without reauthorization)

I’ll focus on the two main authorization grant types most relevant for MCP:
_Authorization Code_ and _Client Credentials_ . To do this right, I’m going to have to go deep
into the technicals. My suspicion is that you’ve been actively avoiding the topic of OAuth
due to its perceived complexity. My hope is that I can demystify this for you. I’ll start
from the very beginning of an MCP client request and explain the flow for each grant
type and do it in a way that’s easy to understand. If you’re a technology leader or dev
lead going into a leadership meeting (with infosec in the room) to advocate for MCP
adoption, you’ll want to speak confidently and authoritatively on security as it relates to
MCP and OAuth.

**MCP Client-Server Initialization and Handshake**

Like any client-server communication, it requires a handshake. The client first
establishes a transport layer connection (STDIO or HTTP). Once established, an
MCP client sends an **initialize** request. As part of the request, the client shares what
MCP protocol version it supports, the client name, the client version, its capabilities
(whether it supports notifications, etc.), and other metadata. The MCP server responds,
confirming the MCP protocol version that will be used for the session. It also provides
the server name, version, metadata, and usage instructions for the client (optional). The
client sends an **initialized** notification to the server to confirm that the handshake is
complete. Figure 2-23 depicts this initialization flow.

81

Chapter 2 Data Sec d c

**_Figure 2-23._** _MCP Client-Server Initialization and Handshake_

**MCP Metadata Discovery**

Since MCP servers are utilizing third-party authorization servers, there needs to be a way
to tell the MCP client which OAuth server endpoints to send authorization and token
requests to. To communicate this, there’s the concept of metadata discovery. As part of
the initialization, the client receives the OAuth server’s metadata discovery endpoint and
queries it to learn the endpoints to send requests to.

If you’re new to OAuth, it’s important to know that there are several different
endpoints to handle different request types:

     - Metadata (/oauth-authorization-server)

     - Client registration (/register)

     - Authorization (/authorize)

     - Access token (/token)

82

Chapter 2 Data Sec d c

The Client Credentials flow, which I present later, is just a simplified version of this
(credentials eliminate the authentication flow). In my authorization flow diagrams in the
next sections, note that there are 4 roles depicted: The client, the authorization server,
the resource owner, and the resource server.

**Dynamic Client Registration (optional, but not really)**

Dynamic client registration (DCR) allows OAuth clients to self-register with OAuth
authorization servers at runtime. During the registration process, client metadata is
saved with the OAuth server, including the client name and grant type—Authorization
Code flow or the Client Credentials flow. The OAuth server generates a unique **client_id**
and returns it to the client. The client will use this **client_id** to identify itself when
sending requests. Redirect URIs are also registered during DCR. The redirect URI is the
client callback endpoint where the OAuth server redirects the client after authorization,
delivering the authorization code or error parameters via URL query parameters. The
redirect URI sent with the authorization request is validated exactly against the URIs
registered for the client during this registration process. Matching redirect URIs exactly
is only a recommended best practice in OAuth 2.1 but required in the June 2025 MCP
specification.

DCR is not required by MCP, but it is a practical necessity for agent-based use cases.
It is simply not feasible to expect to register all MCP clients an agent may interact with
beforehand. Offering dynamic registration has its tradeoffs. For example, the endpoint
must be a public endpoint, and it can’t require authentication. There are security
implications to this, as you might expect. We can imagine that having a public endpoint
that can create clients dynamically is a risk. To mitigate this risk, DCR utilizes Proof Key
for Code Exchange (PKCE), an OAuth security extension, to reduce the risk of crossclient code theft.

Here is how PKCE is used in the authorization flow:

1. The client generates a PKCE code verifier unique to that client that

it keeps secret.

2. A PKCE code challenge is created as a hash of the code verifier.

3. The PKCE code challenge is sent to and saved by the OAuth server

as part of the auth code request.

83

Chapter 2 Data Sec d c

4. When requesting to exchange the auth code for an access token,

the client sends the PKCE code verifier with the auth code. The
auth server recreates the PKCE code challenge from the PKCE
code verifier and compares it to the one it saved in step 3.

Figure 2-24 depicts the PKCE verification as part of the authorization flow.

**_Figure 2-24._** _PKCE Verification as Part of OAuth Authorization Flow_

In this and previous sections, I described the initialization, metadata discovery,
and dynamic client registration flows. With the client registered and a unique client id
generated and returned to the client, a request can be made to obtain the auth code.

**Requesting the Authorization Code**

Whether you want your agents to leverage public MCP servers or the company
itself wants to offer a public MCP server that serves public clients, what I present in
this section will be valuable. I’ll start with a visual. Figure 2-25 shows the complete
Authorization Code flow for MCP resource requests.

84

Chapter 2 Data Sec d c

**_Figure 2-25._** _MCP OAuth 2.1 Authorization Code Flow with Human-in-the-Loop_

Here are the steps in the authorization code request:

1. As part of each and every authorization request, the client

generates a state token. This state token is a security feature to
protect against Cross-Site Request Forgery (CSRF).

2. The client makes an authorization request to the OAuth server.

The authorization request will include the client id, the state,
the PKRE code challenge, and the redirect URI to receive the
generated auth code if the request is successful.

3. The OAuth server validates the client id and the redirect URI

against the URIs stored during the DCR process. The redirect URI
must match exactly. The OAuth server stores the state and PKCE
code challenge.

4. The user and resource owner reviews and approve the request.

5. The OAuth server generates the authorization code and returns it

to the validated redirect URI along with the state.

85

Chapter 2 Data Sec d c

6. The client receives the auth code and the state code. The client

can validate the state code to ensure the response it received
corresponds to the request.

Next, we’ll see how this auth code is exchanged for the access token.

**Exchange the Authorization Code for the Access Token**

The client received the auth code in the previous step, but the auth code is not what’s
used to access a resource. The client now has to send a request to the /token endpoint to
exchange the auth code for the access token.

Here are the steps of the access token request:

1. The client makes a request for the access token. The request

includes the auth code and the PKCE code verifier.

2. The OAuth auth server uses the PKCE code verifier to create the

code challenger and compares it to the one it stored from the
authorization request. It validates the auth code.

3. The OAuth token endpoint generates the access token and returns

it to the client via the redirect URI.

The access token is scoped to the permissions needed to access the resource.

**Request for MCP Resource with Access Token**

Finally, the last stage is to use the access token to request the resource from the MCP
server. The access token (as the bearer token) is most commonly a JWT. When the MCP
server receives the JWT, it can validate it locally using the public JWKS key set it received
from the authorization server and cached during the DCR step. This is often preferred, as
it reduces latency by eliminating one more network request. With the JWT validated, the
resource server requests the resource and returns it to the client, completing the original
request.

86

Chapter 2 Data Sec d c

**Consent Fatigue from the Human-in-the-Loop Approval Flow**

Imagine if every time an agent performs a complex task, you are prompted to approve
every tool or resource needed. After you approve 10 or 15 requests, you start to approve
them without careful consideration. This is called _consent fatigue_, and it’s a problem for
several reasons. When approvals become automatic, it creates a false sense of security.
It adds no security value for the high cost of not allowing autonomous execution in the
first place.

Next, we’ll look at the second option for authorizing MCP access to resources: Client
Credentials.

**Client Credentials Flow for Private MCP Clients**

Client Credentials is a machine-to-machine authorization flow that does not require
user interaction. This allows an MCP server to authenticate with external services on
behalf of an application instead of users. This is an important distinction. Authorization
Code flow enabled user-based permission scope because it supports user-based
authentication. Client Credentials flow authenticates as an application, and permission
is scoped at the application level. Dynamic client registration is possible and supported
for Client Credentials; however, the most common registration process is _pre-_
_registration_ . You’re likely familiar with client pre-registration if you ever generated an
access key and secret access key for CLI access to AWS or GitHub. API keys work similar
to OAuth client credentials with one important difference—API keys are static and longlived, while client credentials are dynamic and short-lived. With registration out of the
way, the flow is much simpler than the Authorization Code flow. Figure 2-26 shows the
Client Credentials flow for pre-registered clients.

87

Chapter 2 Data Sec d c

**_Figure 2-26._** _MCP OAuth 2.1 Client Credentials Flow for Machine-to-Machine_
_Authentication_

After the same initialization and metadata discovery flows, here are the steps for the
pre-registered client credential flow.

1. A request for an access token is made to the /token endpoint using

the client_id and client secret key for authentication.

2. The OAuth server validates the client_id and client_secret,

generates the access token, and returns it as part of the HTTP
response.

3. The client sends the access token (bearer) as part of a resource

request to the MCP server. Like the Authorization Code flow, this
is most commonly a JWT that the MCP server can validate locally
using a public JWKS key set cached from the authorization server.

4. The MCP server requests the resource using the JWT and returns

it to the client.

This concludes my deep dive into MCP security. I’ll demonstrate deploying MCP
servers in Chapter 12, “Building AI Agents with Bedrock AgentCore, Strands Agents, and
Model Context Protocol (MCP).”

88

Chapter 2 Data Sec d c

**IAM Authentication with SigV4 for MCP**

AWS uses a special signing protocol called AWS Signature Version 4 (SigV4) to
authenticate AWS API requests. SigV4 signing uses your AWS credentials to sign requests
without exposing them and proves that you possess a secret key from an associated IAM
identity. Authenticating with AWS IAM is not part of the official MCP specification, but
who cares! SigV4 is a rock-solid, highly secure way to authenticate requests in the AWS
environment. It’s how AWS authenticates all API requests. If you’re not serving MCP
publicly or providing MCP access to agents outside of AWS, then IAM authentication
with SigV4 should be the default choice.

AWS maintains the MCP proxy for AWS <sup>7</sup> package to support IAM authentication for
MCP using SigV4 signing instead of OAuth. This package is needed because standard
MCP clients won’t know how to sign requests with AWS credentials. The package can be
used either as a lightweight proxy or as a library to programmatically connect popular AI
frameworks (e.g., LangChain, LlamaIndex, or Strands) to MCP servers on AWS.

Here’s some sample code for how to implement this library for a streamable HTTP
transport using the Strands framework.

from mcp_proxy_for_aws.client import aws_iam_streamablehttp_client
from strands.tools.mcp import MCPClient

# This creates a streamable HTTP client with SigV4 auth
mcp_client_factory = lambda: aws_iam_streamablehttp_client(

)

# Strands handles the HTTP connection lifecycle
with MCPClient(mcp_client_factory) as mcp_client:

[7 Amazon Web Services. (2024). MCP Proxy for AWS [Computer software]. GitHub. https://](https://github.com/aws/mcp-proxy-for-aws)
[github.com/aws/mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)

89

Chapter 2 Data Sec d c

The AWS credentials are retrieved from environment variables and auto-signed as
part of the MCP client initialization. For more details on how to operationalize SigV4
signing for different frameworks, refer to the AWS documentation.

AWS offers a comprehensive suite of tools and services designed to help organizations
meet regulatory requirements and audit standards. These services automate compliance
checks, monitor security postures, and streamline audit processes.

AWS Config can continuously assess your AWS resource configurations against best
practices and compliance standards defined in predefined conformance packs,
including operational best practices for AWS, CIS (multiple), CISA, NIST (multiple), PCI
DSS, HIPAA, and FedRAMP (low, moderate, high), among others.

In addition, there are various “rules” that can be checked and enforced. In the
example shown in Figure 2-27, I’m implementing a check to detect if Amazon EBS
volumes are encrypted. If a developer unknowingly creates an instance without the
correct encryption required by IT policy, this rule will be triggered and can alert
administrators.

90

Chapter 2 Data Sec d c

**_Figure 2-27._** _AWS Config Rule to Check if Amazon EBS Volumes Are Encrypted_

AWS CloudTrail enables governance, compliance, and operational risk auditing by
logging and monitoring account activity across your AWS accounts. AWS CloudTrail
captures detailed records of AWS API calls made to your AWS account, including the
identity of the caller, time of the call, source IP address, and request parameters. An
additional setting will also capture data events. This comprehensive logging capability
helps in detecting unusual activity, troubleshooting operational issues, and ensuring
compliance with internal policies and regulatory requirements.

**Amazon S3 Server Logging**

Server access logging provides detailed records for the requests that are made to an
Amazon S3 bucket. Server access logs are useful for many applications. For example,
access log information can be useful in security and access audits. By default, Amazon S3
doesn’t collect server access logs. When you enable logging, Amazon S3 delivers access

91

Chapter 2 Data Sec d c

logs for a source bucket to a destination bucket (also known as a target bucket) that you
choose. The destination bucket must be in the same AWS Region and AWS account as
the source bucket.

**AWS Security Hub**

Having one centralized “pane of glass” where all security information flows into is a
critical security requirement. AWS Security Hub can audit your AWS environment
based on several security standards. It provides a scorecard listing the severity of the
vulnerability by resource. Figure 2-28 shows a sample of the security analytics available.

**_Figure 2-28._** _Security Summary in AWS Security Hub_

**AWS Audit Manager**

Customers can use AWS Audit Manager to create and customize audit frameworks
tailored to their specific compliance needs, such as GDPR, HIPAA, or ISO 27001. The
service continuously monitors and records AWS activities, generating audit-ready

92

Chapter 2 Data Sec d c

reports that facilitate efficient and accurate assessment of compliance posture. The
example I’ll use is the AWS Generative AI Best Practices Framework v1, which offers
governance for generative AI applications. Figure 2-29 shows this option.

**_Figure 2-29._** _AWS Generative AI Best Practices Framework v1_

**Disaster Recovery, High Availability, and Backups**

No chapter on data security and governance would be complete without addressing
disaster recovery, high availability, and backups. Beyond access controls and
encryption, what happens when systems fail or service is interrupted? Organizations
(public or private) assess the criticality of their workloads and determine the level of
resiliency needed to meet the requirements of the business. This section explores the
data resiliency topics of disaster recovery (DR), high availability (HA), and backup
strategies in AWS.

Disaster recovery is the practice of preparing for and recovering from catastrophic
events—data center failures, regional outages, cyberattacks, or natural and manmade disasters. DR plans define how to restore operations when entire systems or
regions become unavailable.

93

Chapter 2 Data Sec d c

Every DR strategy begins with two critical metrics that define acceptable downtime
and data loss:

**Recovery Time Objective (RTO)** specifies the maximum
acceptable time to restore service after a disruption. An RTO of
4 hours means your systems must be operational within 4 hours
after the disruption.

**Recovery Point Objective (RPO)** defines the maximum
acceptable age of data that can be lost. An RPO of 15 minutes
means you can tolerate losing up to 15 minutes of data as a result
of service disruption.

These metrics directly drive the architectural decisions and costs associated with
implementing DR. The lower the RTO and RPO, the more sophisticated and costly the
solutions become. Technology leaders can help the business quantify real impact—in
loss of revenue, loss of customers, or loss of reputation—to determine the right level of
protection.

Here’s a closer look at the DR strategies.

Creating and storing backups cross-region is the lowest cost option. AWS Backup is
a fully managed service that centralizes and automates data protection across AWS
services. It provides a unified console for creating backup policies, managing backup
schedules, and monitoring backup activity across Amazon RDS, DynamoDB, EBS
volumes, EFS file systems, S3, and other AWS resources. DynamoDB point-in-time
recovery (PITR) can be enabled in production and provides continuous backups for
35 days. RDS Automated Backups can achieve point-in-time recovery for up to 35
days. Amazon S3 Versioning maintains multiple versions of objects, protecting against
accidental overwrites or deletions. Automate backups with AWS Backup as much as
possible.

AWS Backup Vault Lock implements immutable backups that cannot be deleted
before a specified retention period, even by administrators with full access. This WriteOnce, Read-Many (WORM) protection defends against ransomware that attempts to
delete backups before encrypting production data.

94

Chapter 2 Data Sec d c

Pilot light keeps IaC scripts staged in a secondary region with active and continuous
data replication. During a disruption, infrastructure is quickly deployed to
create a functioning replica of the application scaled to handle the anticipated
production demand.

A warm standby provides a full version of an application without the full
production capacity. When a failover occurs, the workload is quickly scaled up to
meet production demand.

Multiregion active-active requires essentially an active full replica of the workload (with
equivalent capacity) to be deployed into a second region. If a disruption occurs, the
application fails over to the secondary active region in seconds and continues operating.

Table 2-2 shows a matrix of disaster recovery strategies against RTO/RPO
requirements, cost, and complexity.

**_Table 2-2._** _Disaster Recovery Strategy Matrix_

**Strategy** **RTO** **RPO** **Cost** **Complexity**

Backup/R H H $ Low

P 10 minutes Minutes $$ Medium

Warm Standby Minutes Seconds $$$ Medium-H

A A Seconds N $$$$ H

Taking this a step further, Table 2-3 provides some general architectural guidance
based on different RTO/RPO requirements.

95

Chapter 2 Data Sec d c

**_Table 2-3._** _Architecture Strategies for Different Resiliency Metrics_

**Resiliency metrics** **Architecture strategy**

RTO RPO A
replication

RTO RPO Multiregion with asynchronous replication and automated
failover

RTO RPO Single-region HA

RTO RPO Backup and restore strategies

High availability (HA) focuses on minimizing downtime by eliminating single points
of failure through redundancy and automatic failover. HA architectures keep systems
running during component failures, network issues, or planned maintenance. HA and
DR sometimes get confused, but they are altogether different. Yes, HA architectures
can sometimes help you mitigate disaster; however, the requirements for each are not
always aligned. HA in an AWS context can often mean Multi-AZ deployments within a
region. However, this won’t be adequate during an AWS Region failure. If you want to be
highly available amidst a regional outage, you’ll need multiregion HA. HA includes the
availability of the application itself, not just the data.

HA systems typically include the following:

     - Synchronous replication of the data to the standby.

     - Automatic failover.

     - Handles DNS updates and redirects to new primary after failover.

Many AWS services are highly available by default. Amazon S3 has a 99.99%
availability SLA for standard tables. RDS Aurora databases provide a shared storage
system with 6 copies of the data across 3 AZs. Aurora is also capable of subsecond
failover across AZs. Aurora Global Databases is a cross-region replication feature.
DynamoDB Global Tables have a 99.999% availability SLA across multiple regions.

96

Chapter 2 Data Sec d c

In this chapter, we explored the importance of protecting and managing data in the
cloud. I outlined the three primary goals of data governance: finding, accessing, and
sharing the right data to the right consumers; keeping data safe and secure; and enabling
appropriate audits and controls. The chapter also covers the evolving challenges driven
by the growth of unstructured data and increasing government regulations on AI.

I provided a comprehensive overview of the AWS Shared Responsibility Model,
emphasizing the distinction between what is AWS’s responsibility for cloud security
and what is the customer’s responsibility. I explained how authentication and access
are managed in AWS via AWS IAM and the AWS Identity Center. I described how to
implement encryption-at-rest using AWS Key Management Service (AWS KMS) and
encryption-in-transit using TLS and AWS Certificate Manager. I highlighted the use
of Amazon DataZone for data catalog management, data lineage, and compliance. I
discussed the most common generative AI security risks and how to mitigate them with
guardrails. I introduced the AWS Security Agent and demonstrated its key features,
including design reviews, code reviews, and penetration testing. I presented a deep
dive into authentication methods for Model Context Protocol (MCP), including OAuth
and SigV4. I demonstrated how Amazon Bedrock Guardrails makes it easy to apply
safeguards to generative AI solutions. The chapter concludes by describing how to
implement auditing and compliance controls, disaster recovery, high availability, and
backups on AWS.

In the next chapter, I explore data lake design on AWS, including the implementation
of fine-grained access controls using AWS Lake Formation and the use of open table
formats like Apache Iceberg.

97

**CHAPTER 3**

## **Data Lake Design** **with Apache Iceberg** **and S3 Tables**

The most significant data engineering strategy to emerge in the last several decades is
the data lake. According to a study by global marketing and research firm Aberdeen,
organizations that utilize data lakes see a 9% increase in organic revenue growth
compared to their peers. <sup>1</sup> In the AI age, I believe data lakes will be defined more by
what remains the same than what changes. Generative AI models are not capable
of processing large datasets. They still struggle with numerical processing. Data is
the raw material of AI, and as such, the relevance of data lakes will only increase.
Model developers will need data lakes and data engineers to collect and curate model
training data.

In this chapter, I’ll explore modern data lake design theory and practice, including
its evolution to the lakehouse strategy. I’ll present the latest in data lake technology—
advanced serialization formats and open table formats like Apache Iceberg that can
support transactions, upserts, and merges in a data lake. I’ll highlight the strategic
investments by AWS to offer managed Iceberg tables in S3 via a feature called S3 Tables.
Throughout the chapter, I’ll highlight opportunities to support data lake development
with generative AI and how data lakes support generative AI use cases. Data Lake design
is an opinionated practice, and I will certainly be subjecting you to my opinions on the
topic. These opinions were shaped over many years designing and building data lakes
for Fortune 100 customers. By the end of the chapter, you should be able to explain what
a data lake is, how it originated, and why it became a dominant data strategy. You should

1 Angling for Insight in Today’s Data Lake. Michael Lock. October 2017. Aberdeen Group.

99
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_3](https://doi.org/10.1007/979-8-8688-2199-8_3#DOI)

Chapter 3 Data Lake Design with A c Ic d S Tabl

also be able to identify the primary components of a data lake and its transactional
derivative, the lakehouse. You should understand how to map out and define data
quality stages or phases. Finally, you should know which aspects of data lake design are
the most impacted by generative AI.

**Separating Analytical and Operational Workloads**

A best practice in data engineering is to separate analytical workloads from operational
data systems, and some of the reasons might not be obvious. It’s important to know
why this is a best practice because it drives strategic technology decisions that will be
consequential to a business long term. I’ve seen more than a few seasoned technologists
and CTOs get it wrong and pay for it later.

If you’re not separating analytical workloads from operational data systems, where are
you performing analytical processing? In the operational database! Developers use
the imperfect tools and features they know best and are comfortable using to generate
reports—and when they do, they aren’t even aware they’re making consequential
strategic technology decisions. For example, to do this, numerous artifacts are needed.
They’ll need tables to hold the analytical datasets at each stage of processing. These
tables are easy to create, often without contemplating the data’s lifecycle. Perhaps stored
procedures are used to perform ETL and complex analytical calculations. All of this adds
a lot of cost and tech debt when it comes time to migrate. Migration of the table schemas
and data is easy, since this can usually be fully automated. However, migrating the
_business logic_ requires exceptional care and attention. AI tools are becoming more robust
and capable of automating code conversion, but they are still only successful up to 80%.
I’ve seen customer migrations stalled for _years_ because of the millions of lines of legacy
ETL and analytical procedure code. Luckily, I expect AI to improve automation for code
conversion over time.

100

Chapter 3 Data Lake Design with A c Ic d S Tabl

Attempting to scale analytics served from operational databases will encounter
problems, like locking and performance degradation. DBAs will perform disruptive
schema migrations to partition tables or throw more resources at the problem, adding
compute and memory to handle both workloads at peak demand. This is costly
and inefficient. The goal should be to allocate the resources to scale each workload
independently. The general rule: use RDBMS (relational database management
systems) for smaller, structured datasets with limited scale, and data lakes for distributed
processing of structured and unstructured big data at virtually unlimited scale.

No matter what operational database you choose, the business logic and the data types
are living in a product-specific implementation of the ANSI SQL standard. Even the data
types are vendor-specific. This becomes more apparent when attempting to import data
from a third party source into a database. In the process, you’ll be forced to map and
convert data from a data file to the vendor-specific implementation of the data type.
Once you take structured data out of a database and put it into a data lake, the data types
are translated to a universally recognized set of parquet data types: a string, an integer, a
decimal, a date (or timestamp), or a boolean. This is needed when integrating datasets
from various sources.

Now that I’ve made the case for separating these workloads, let’s look at the primary
differentiation between data warehouses and data lakes.

**The Rise of Data Lakes**

From the late 1980s to the 2010s, enterprise data warehouses (EDW) were the dominant
strategy for data centralization. They were favored for their ability to support structured
data and deliver fast query performance with reliable data quality. With the everdiminishing cost of compute and storage and the advent of the internet and mobile,
the 5 “Vs” of big data—volume, velocity, variety, veracity, and value—began to quickly
relegate EDWs to the backseat as data lakes took center stage. If you wanted to pursue
a strategy of centralizing ALL the data in one place—you needed a data platform that
could accommodate _ALL types_ of data.

101

Chapter 3 Data Lake Design with A c Ic d S Tabl

Data Lakes were first implemented as clusters of nodes with compute and block
storage consisting of commodity hardware. This meant that the data could be stored as
files outside of the database tables in an EDW. The ability of data lakes to manage the
increasing _variety_ of data—from structured to semi-structured and unstructured data—
was just one important differentiator. This, combined with its distributed architecture,
meant that data lakes could scale out the number of nodes in the cluster horizontally as
the _volume_ of data grew. The software to manage these clusters was open source (YARN
was distributed with Hadoop), meaning that businesses could build out data lakes for
the cost of the infrastructure and development staff, without incurring millions of dollars
in software licensing fees.

**Separation of Data and Compute**

Early HDFS-based data lakes had a limitation. They tightly coupled the data with the
compute nodes, meaning that it couldn’t scale each resource independently (see
Figure 3-1). If the data grew to a size that exceeded the disk storage available on the
node, the cluster needed to expand to more nodes, even though the cluster was not fully
utilizing its compute capacity. Similarly, if the cluster needed to run compute-intensive
workloads, administrators would need to add more nodes to scale its compute capacity
despite having ample disk capacity. This proved inefficient and costly.

**_Figure 3-1._** _Data and Compute Tightly Coupled_

The first publicly available cloud services that separated data and compute were
Amazon S3 and Amazon EC2, which were released in 2006. While these services weren’t
originally intended for large data processing, customers quickly caught on that they
could spin up large Hadoop clusters on EC2, copy data from S3, process that data in the
cluster, write the data back to S3, and shut down the cluster. This “elastic compute” of the
cloud provided a highly efficient way to process large data sets. Amazon S3 as an object
store provided a distributed storage service that replicated data across multiple devices
and a minimum of 3 AZs, yielding 11 “9s” of durability. Google’s early advancements

102

Chapter 3 Data Lake Design with A c Ic d S Tabl

with distributed architectures included BigTable, which was created in 2004. Google’s
research paper on the topic was published in 2006. <sup>2</sup> BigTable powers many of Google’s
large-scale applications, including the indexing for search, Google Maps, Google
Earth, YouTube, and Gmail. A cloud version of BigTable was released on GCP in 2015.
Figure 3-2 conceptually shows the separation of data and compute and the ability to
independently scale each depending on utilization.

**_Figure 3-2._** _Separation of Data and Compute_

Note that with this architecture, network capacity and throughput became the
critical constraint as large amounts of data needed to transit from the shared storage
system to the compute cluster.

**Schema-on-Write vs. Schema-on-Read**

The fundamental difference between databases (including data warehouses) and data
lakes is that databases are a schema-on-write system and data lakes are a schema-onread system. Schema-on-write means that the schema is defined for a table at design
time before the data can be written to it. The data that is written to the table must
conform to the schema—the table, the columns, the data types, and the constraints.
In a schema-on-read system, the data is written as a file first, with schema information

2 “Bigtable: A distributed storage system for structured data,” Fay Chang, Jeffrey Dean, Sanjay
Ghemawat, Wilson C. Hsieh, Deborah A. Wallach, Mike Burrows, Tushar Chandra, Andrew Fikes,
and Robert E. Gruber, in _Proc. 7th OSDI_ [, Nov. 2006 (Via USENIX, ACM Digital Library, Google](https://db.usenix.org/events/osdi06/tech/chang/chang_html/)
[Research Publications)](http://research.google.com/archive/bigtable.html)

103

Chapter 3 Data Lake Design with A c Ic d S Tabl

embedded with the data. If no schema information is provided, libraries used to read
the data could _infer_ the schema based on the data read from the file. I describe this
difference in more detail later in the chapter.

Data lakes embody the strategic shift away from schema-on-write to schema-onread systems. Knowing fully how the data will be used and constraining the data to that
schema before it is ingested is no longer necessary. Major efficiencies and cost savings
are realized when data can be collected and analyzed to determine business value _before_
committing the resources needed to further refine and process the data.

Writing data as files has its own challenges, which requires sophisticated solutions.
I’ll discuss serialization formats next.

Serialization refers to the ways in which data is stored in a structured, efficient format
that can be easily retrieved and analyzed. In data lakes, data is stored in files. What file
format the data is stored in will determine many factors about how the data lake itself
performs. Choosing the right serialization format is crucial for performance, scalability,
and compatibility.

Text-based file formats, such as CSV, JSON, XML, and YAML, are human-readable.
Most raw data that is ingested into a data lake will arrive in a text-based file format. By
definition of text-based, these formats are uncompressed and verbose and perform
poorly when queried. Generative AI can use text-based data in a number of ways—to
train or fine-tune models or for semantic search as part of a RAG strategy. For structured
data in a data lake, the imperative is to use an advanced serialization format.

**Advanced Serialization Formats**

Advanced serialization formats offer several features that optimize performance for
reading and writing data in a data lake. Examples include Apache Parquet, Apache Avro,
Optimized Row Columnar (ORC), and Google’s IO Protobuf. ORC was the preferred
format for data lakes on Hadoop, but it is not the preferred format for data lakes in AWS,
and this will be the only mention of it in this chapter.

104

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Apache Avro** is a row-based serialization format that is best suited for real-time
processing or when data needs to be ingested rapidly and continuously (i.e., event
logging and message queuing).

**Apache Parquet** is the preferred serialization format for structured data in Amazon
S3 data lakes. Parquet is highly integrated into Apache Spark and many AWS services,
including Amazon Athena, Amazon Redshift Spectrum, and AWS Glue.

Advanced serialization formats like these come with a significant set of features
you may not even think about when writing transformations in Spark; however, it is
critical knowledge all data engineers should possess. Table 3-1 lists several advanced
serialization features and their advantages and trade-offs.

**_Table 3-1._** _Features of Advanced Serialization Formats_

**Feature** **Advantage** **Trade-off**

B S
amount of data physically read from storage and
transmitted over the network, yielding significant
performance benefits.

Compression Compression can further reduce the size of data
on disk and yield performance benefits.

S A
and processed in parallel.

Partitioning A
column row. Queries read only the partitions
needed and ignore the rest of the dataset.

Columnar A
exclude entire columns, reducing the amount of
data accessed and processed.

N

Compression and decompression
operations incur an additional
cost.

H
additional cost to flatten.

R
patterns to be effective.

I
needed.

( _continued_ )

105

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Table 3-1._** ( _continued_ )

**Feature** **Advantage** **Trade-off**

S
describing

S
evolution

Metadata describing the schema is contained in
the data file. Libraries like S
schema and apply it to the data when read.

A
schema while maintaining backwards
compatibility with the schemas of existing data.
T
entire dataset had one schema.

Overhead incurs additional cost
incurred on write.

More limited for columnar data
vs. row-based data. Parquet
(add-only columns)

We need to spend a little more time on compression formats because it’s a critical
decision you want to get right before you start copying lots of data!

**Compression Formats and Throughput**

For analytical “write-once-read-many” workloads, we are optimizing for read
performance. We also need to consider the speed and the throughput of the
compression and decompression operations.

Apache Parquet supports six compression libraries, which are compared in
Table 3-2. Snappy is the default compression for writing Parquet files in Spark because it
balances compression with performance. Using a single i7 core in 64-bit mode, Snappy
compresses at 250 MB/sec and decompresses at 500 MB/sec.

106

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Table 3-2._** _Comparison of Compression Libraries Supported by Apache Parquet_

**Algorithm** **Compression**
**Ratio**

**Compression**
**Speed**

**Decompression**
**Speed**

**Storage Space** **Splittable**
**w/ Parquet?**

G H S Moderate E Yes

S
(default)

Medium Fast Fast Moderate Yes

LZO Medium Fast Fast Moderate Yes

LZ4 Medium **Very Fast** **Very Fast** Moderate Yes

B **Very High** S S **Very Efficient** Yes

ZST H Moderate Fast E Yes

While Snappy has its advantages as a default option, it may not be the best in all
cases. For instance, real-time applications requiring fast reads and writes will achieve
the best performance using LZ4. Zstandard (ZSTD) achieves 2x the compression that
Snappy does with comparable throughput and resource consumption. The tradeoff
is that some writes will take longer using ZSTD vs. Snappy, but this isn’t a concern
for a write-once-read-many dataset. For colder, less frequently accessed data, Brotli
can compress data at a very high ratio, maximizing optimization of storage costs. The
slower performance for both writes and reads may be tolerable for this data’s access
pattern. It’s important to acknowledge that while Brotli support exists in browsers
and AWS CloudFront (for several years now), Athena **_does not_** currently support
Brotli compression. Being able to query data ad hoc in the data lake using Athena is
a major advantage, so unless there’s a very compelling reason to do so, Brotli is not
recommended. If storage costs are a concern, utilize Amazon S3 intelligent tiering to
automatically demote data to colder storage as it ages.

**Note** W
(G S B ST Parquet files.
Parquet’s design format divides the data into row groups and pages, enabling
each to be independently compressed and accessed. T
enables parallel processing.

107

Chapter 3 Data Lake Design with A c Ic d S Tabl

We reviewed the special formats and features for how we store data in a data lake.
Let’s look at the different components that make up a data lake.

**Components of a Data Lake**

A data lake has many components that together make it a functional strategic data
platform. Data lakes serve several data use cases. It can store and serve structured
data. If I had to describe what a data lake was for structured data, I’d say that it was like
a database outside of a database (with some notable differences). I admit I might be
making this analogy because my background includes roles as a database developer
and architect. Databases have nonvolatile storage where the data persists. A data catalog
creates a logical layer for named entities like tables with columns and rows. The catalog
maps the logical tables to where the data is physically stored, enabling me to query these
tables using standard SQL. Similar to databases, there are tools to bulk load data and
interfaces to allow applications and users to connect to and consume the data. There are
security and governance controls managing user access and encryption.

If we break this out into a conceptual diagram (see Figure 3-3), we see from left to
right a flow from data sources to ingestion, data processing, and finally, consumption.

108

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-3._** _Components of a Data Lake_

You can also think about a data lake conceptually as a number of layers (see
Figure 3-4). This is useful for understanding the primary functions of a data lake.

109

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-4._** _Conceptual Layers of a Data Lake_

Let’s quickly review what each of these layers represents in the context of the AWS
cloud and how generative AI is impacting them.

At the storage layer, object storage is the preferred option for modern data lakes.
Compared to block storage, it is much cheaper. Objects in an object store are immutable,
meaning they cannot be changed, only overwritten or deleted. Objects stored in AWS
can be accessed through standard HTTP REST APIs. In terms of management, object
stores carry a significant benefit in that they are stored in flat key spaces, not hierarchical
file structures.

**Security and Governance Layer**

The security and governance layer for the data lake includes the identity and access
management controls, fine-grained access controls, and data protection with advanced
encryption. I covered these topics in Chapter 2, “Data Security and Governance.” AI will
enhance the capabilities for actively monitoring data lakes for compliance and reporting
advanced analysis and insights to help keep data secure.

110

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Metadata Management Layer**

Metadata is data about the data, and it’s an important part of data governance. A feature
called S3 Metadata was released as generally available in 2025. This feature allows you
to store custom metadata about S3 objects along with the object. Amazon DataZone is a
service that manages metadata and provides business users with search and discovery
capabilities for datasets in the data lake. DataZone uses generative AI to automate
metadata management. Historically, performing this task manually was tedious and
didn’t scale. I discuss DataZone in depth in Chapter 4, “Data Mesh Design with Amazon
DataZone.”

**Data Lifecycle Layer**

How an organization manages data over time can be driven by cost management—
moving older data to cheaper and infrequently accessed storage—but it is also subject
to their policies or even external compliance requirements. For example, healthcare
and life sciences companies may need to retain medical records for 7 years. Amazon
S3 has evolved over the years to offer various storage tiers to support data throughout
its lifecycle, including automated demotion of data to less expensive tiers as data gets
colder and finally, deletion.

**Data Ingestion Layer**

The data ingestion layer includes all the services and processes that extract data from the
various sources (external or internal) and lands it into the data lake. A data lake should
support batch, streaming, or microbatching ingestion. Generative AI can profile and
validate new data sets.

**Data Processing Layer**

Operations that are performed on the data to take it from the state it arrived in to the
state the business desires occur in the data processing layer. This includes batch and
streaming data processing, data enrichment, and data quality testing. Generative AI
will write the majority of data processing and testing code. It will analyze logs and help
troubleshoot errors. I dive deeper into these topics in Chapter 5, “Big Data Processing
and Transformation with AWS Glue and AI Agents,” and Chapter 9, “Streaming and RealTime Data Processing with Generative AI Enrichment.”

111

Chapter 3 Data Lake Design with A c Ic d S Tabl

The serving layer includes all the services and processes that serve data to consumers
at scale. Generative AI will make most developed reports obsolete. Instead, users will
be able to query vast amounts of data with natural language and receive dynamically
generated reporting facilitated by agentic workflows. Text-to-SQL takes natural language
and converts it into SQL queries of structured data. I explore this and other topics in
Chapter 11, “Generative Business Intelligence with Amazon Quick Suite.”

**Data Lakes on AWS**

If we overlay AWS services onto our conceptual component diagram, it provides a better
picture as to not only why the data lake is a core strategy in the modern data platform but
why the cloud is the ultimate enabler of the modern data strategy in general. When you
bring your data to the AWS cloud and specifically, a centralized repository of low-cost
object storage like S3, you have a portfolio of premium microservices available to extract
the most business value out of that data for the least amount of effort. Figure 3-5 shows a
high-level data lake design on AWS.

112

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-5._** _Data Lake on AWS_

**The Medallion Architecture**

One core function of a data lake is to define data quality “stages” by which the data
transits on its way to its published state, where it is consumed by the business. In 2020,
cloud-based data and AI company, Databricks, released formal documentation on the
lakehouse strategy that coined the term, “medallion architecture,” which describes the
architectural pattern of organizing data into bronze, silver, and gold stages in a data lake.
The term “medallion” is a metaphor for the Olympic medaling system. This pattern
provides high-level guidance but tends to be too simplistic in practice. I’d expand this
to a larger set of common stages I call “progressive medallion” and explain the purpose

113

Chapter 3 Data Lake Design with A c Ic d S Tabl

for each. By no means am I suggesting that these are the only stages that could exist.
You could augment what I present below further based on business need or preference.
I’d define the criteria for the existence and use of a stage as that which persists the
data at a specific point in the data processing layer that adds a material benefit to the
data engineering process. Practitioners should think hard before adopting or creating
stages—each stage replicates an additional copy of a dataset that will be managed over
time. Additionally, stages could exist for debugging purposes only, where a debug flag
can be set to persist intermediate stages of the data as needed for an investigation.

Figure 3-6 shows the progressive medallion architecture stages followed by the
description of what each stage represents.

**_Figure 3-6._** _Common Data Lake Stages Implemented as Amazon S3 Buckets_

Now I’ll go through each of the stages and describe why you might consider using
each one.

114

Chapter 3 Data Lake Design with A c Ic d S Tabl

The Landing Zone stage is where data is initially ingested into the data lake. It extends
special access to various integration points and services to get the data into the AWS
environment. Rather than a traditional ETL (Extract, Transform, Load) strategy, a data
lake should strictly enforce an ELT (Extract, Load, Transform) strategy. The reason is that
you want to deliver the data with 100% fidelity from the source. It should be understood
that any transformation, no matter how innocuous, alters the data in a way that can
never be recreated as it was when it was extracted directly from the source. This doesn’t
just protect against logic errors, but it also future-proofs the data pipeline—to where
entire data sets dating back to their inception could be reprocessed with entirely new
data pipeline logic if the business case demanded it.

The audit stage takes ELT strategy to the next level by storing the original state of the
data as it arrived in a separate stage that cannot be altered or changed. This stage might
be needed by enterprises operating in highly regulated industries. AWS makes it easy
to implement this stage with Amazon S3 Object Lock. S3 Object Lock can be activated
on general-purpose buckets with versioning enabled and offers two retention modes,
compliance and governance. With compliance mode, object versions cannot be deleted
by any user—including the root user—nor can their retention period. With governance
mode, the object version can be deleted only with special permissions. There’s also
a legal hold feature that prevents deletion of the object version until the legal hold is
released.

The Raw stage preserves flat-file, text-based data as it arrives in the Landing Zone and
organizes the new files so that it can be cataloged and made available for querying. For
semi-structured data like nested JSON, the original file is stored in the Raw stage, but
additional processing is performed to flatten, normalize, and save the data in a textbased format like CSV or flat JSON records. The data is saved as text because even the
conversion to an advanced serialization format like Parquet can alter the data. The
text-based data is then cataloged for querying; however, because it’s text-based, query

115

Chapter 3 Data Lake Design with A c Ic d S Tabl

performance will be poor. The Raw stage is used primarily for troubleshooting data
quality issues where engineers need to trace the transformations back to the data’s
original state.

You may wonder—how is the Raw stage different from the Landing Zone? Separation
of these two stages is critical. The Landing Zone carries significantly higher risk due to
the various integration points and access provided to external producers. The Landing
Zone may also include highly sensitive data like PII or PHI that will be redacted or
masked in later stages.

The Optimized stage converts the text-based datasets in the Raw stage into an optimized
serialization format like Parquet. This conversion greatly enhances the ad hoc query
performance in Amazon Athena as well as any downstream processes that consume this
data as an input. Light transformations like date and time conversion, column splitting,
or numerical formatting may be performed at this stage. The goal of this stage is to make
it easy and efficient for an analyst to perform ad hoc analysis for insights discovery.

The Conform stage applies data validation rules based on the requirements of the
business. This data validation can be implemented using a data quality framework like
Deequ, which I present in Chapter 5, “Big Data Processing and Transformation with
AWS Glue and AI Agents.” In highly regulated industries like finance, this will be a critical
stage for ensuring the data meets reporting and compliance standards before being
published.

The Unified Analytics stage is for integrating and refining the data into its final state.
This may include datasets supplied by multiple third-party vendors that are then unified
into one abstracted dataset. It may also include denormalization, complex calculations,
or aggregations. After processing data in the Unified Analytics stage, the data should
be in its final state, awaiting publication.

116

Chapter 3 Data Lake Design with A c Ic d S Tabl

The Publish stage only includes data that is of the highest quality, prepared for business
reporting. Consumers of this data—either the company or its customers—will have high
confidence in its validity and will use it to make important decisions.

If I were to map these stages to the conceptual bronze, silver, and gold stages of the
medallion architecture, it would be as shown in Figure 3-7.

**_Figure 3-7._** _Stages of a Progressive Medallion Architecture_

**Data Cataloging with AWS Glue**

The data catalog is one of the most important components in a data lake. What good
is having all the data in one place if you can’t find the data you need when you need
it? A data catalog provides a logical abstraction above the storage layer that manages
the metadata for collections of data. Within the AWS Glue context, these collections
are called databases and act as namespaces, which can contain one or more tables.
The catalog primarily links these database and table entities to the storage location in
Amazon S3. In the AWS cloud, the AWS Glue Data Catalog is the centralized metadata
management service of choice.

Within the set of Glue Data Catalog features (see Figure 3-8), I’ll address **Databases**
and **Tables**, **Connections**, and **Crawlers** .

117

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-8._** _AWS Glue Navigation Menu in the AWS Console_

Our sample data will be the “Ordinance Violations (Buildings)” dataset available
from the City of Chicago’s public data portal. <sup>3</sup>

First, I’ll create a database for similar or related datasets for the Raw stage of our data
lake. I recommend separating the data quality stage at the _database level_ for a few
reasons. One, it keeps tables for different stages of data quality separated. Analysts will
have to explicitly reference the stage via the database name to get access to those tables.
Two, it allows the table names to remain the same through each stage. This facilitates
automation through scripting. Append the data quality stage at the end of the database
name so you can easily search by the data provider, product, and stage.

3 Ordinance Violations (Buildings) dataset. City of Chicago Public Data Portal. Accessed
[July 25, 2024. (https://data.cityofchicago.org/Administration-Finance/](https://data.cityofchicago.org/Administration-Finance/Ordinance-Violations-Buildings-/awqx-tuwv/about_data)
[Ordinance-Violations-Buildings-/awqx-tuwv/about_data)](https://data.cityofchicago.org/Administration-Finance/Ordinance-Violations-Buildings-/awqx-tuwv/about_data)

118

Chapter 3 Data Lake Design with A c Ic d S Tabl

Database naming convention:

[provider]-[product]-[stage].[table-name] → chicago-buildingsraw.[table-name]

Figure 3-9 shows the console interface for creating a database.

**_Figure 3-9._** _Creating a Database in AWS Glue Data Catalog_

Next, I’ll create a Glue Crawler. Crawlers can automatically crawl folders and subfolders
in Amazon S3, discover data files, infer the schema from these data files, and then
register the schema in the catalog. Crawlers can also detect partitions on Amazon
S3 when in the Hive-style format (year=YYYY, month=MM, day=DD). Common data
schema formats like CSV are supported without customization. Other formats may

119

Chapter 3 Data Lake Design with A c Ic d S Tabl

require a custom classifier. Refer to the AWS documentation on custom classifiers to
learn more. Tables written in open table formats, including Delta Lake 2.0.X, Apache
Iceberg 1.5, and Apache Hudi 0.14, can also be crawled.

On the **Set output and scheduling** screen, I select the database chicago-buildingsraw that was created earlier. For demonstration purposes, I choose **On Demand** . You
have the option of specifying a prefix to prepend to the table name. Figure 3-10 shows
the table that was created automatically from our Glue Crawler after it successfully
completed.

**_Figure 3-10._** _Table Created Using Glue Crawler_

Clicking on the **Table data** link in the table list launches Amazon Athena, which will
allow us to execute ad hoc SQL queries (see Figure 3-11) against the cataloged table.

120

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-11._** _Querying the Cataloged Table in Amazon Athena_

**Fine-Grained Access Control with AWS**
**Lake Formation**

AWS Lake Formation offers three key benefits to enhance data security and management
in data lakes. Firstly, it centralizes and unifies permissions across the entire data lake
stack, addressing the challenge of split storage, metadata, and compute systems,
each with different permissions. This unification simplifies the synchronization of
permissions, reducing the potential for errors. Secondly, Lake Formation enforces
fine-grained permissions to restrict access, ensuring that users can only access specific
portions of the vast data within data lakes. This capability to slice and dice data into
manageable portions enhances security and data governance. Lastly, it provides scalable
permissions to efficiently manage a large number of databases, tables, and users,
accommodating the continuous addition of new datasets. This scalability is crucial
for organizations dealing with extensive and dynamic data environments, ensuring
seamless data and user management.

121

Chapter 3 Data Lake Design with A c Ic d S Tabl

AWS Lake Formation is needed for implementing fine-grained access control in the
data lake, including column-level and row-level security, which I’ll demonstrate in this
section.

Row-level and column-level permissions are implemented using a feature called
_data filters_ . You can specify both column- and row-level permissions in these filters.
Figure 3-12 shows the **Create data filter** screen. This is where you choose a name for the
filter and select a target database and target table.

**_Figure 3-12._** _Creating Data Filters in AWS Lake Formation_

Under **Column-level access**, select **Include columns** . Figure 3-13 shows how the
columns will be dynamically loaded based on the table selected. In my hypothetical
example, I select the three columns the user will require for their analysis.

122

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-13._** _Column-Level Access Controls in AWS Lake Formation_

The final section shown in Figure 3-14 shows how to implement row-level
permissions using filter row expressions. The filter expression format supports
PartiQL. Let’s say this analyst is researching actors and actresses from films only and
won’t need access to writers or directors.

**_Figure 3-14._** _Row-Level Access Controls in AWS Lake Formation_

123

Chapter 3 Data Lake Design with A c Ic d S Tabl

Of the various values for the category column (actor, actress, writer, director), I filter
by category on the two values I want. Hit **Save** to save the data filter.

Next we’ll need to associate this data filter with a principal. Choose **Data Lake**
**permissions** from the navigation menu. Select **Grant** . Figure 3-15 shows how to select
the database and target tables. Once these are selected, the related data filters can be
selected.

**_Figure 3-15._** _Granting Data Filter to Principal in AWS Lake Formation_

Refer to the GitHub repo for sample code for programmatically creating these filters
using the Boto3 library.

124

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Open Table Formats**

Data lake technology has evolved significantly over the years to now include many
advanced features such as support for ACID (Atomicity, Consistency, Isolation,
Durability) properties of traditional databases. Supporting transactional operations
in a data lake is what inspired the term _lakehouse_, since it combines the flexibility of
a data lake with the transactional capabilities of data warehouses. This feature was
demanded by businesses to handle data merges and reconciliation for late-arriving or
corrected data. Open Table Formats (OTF) emerged to provide an abstraction layer for
table management that adds several capabilities while overcoming the constraints of
advanced serialization file formats like Parquet.

Object stores like Amazon S3 are immutable, meaning that the data cannot be
changed. It can only be entirely replaced or written as new objects. How do you
implement mutability in an immutable system? Well, you write a lot of files. The open
table format manages these files and produces a unified view of the data as one table.
This is accomplished using metadata files and manifest files, which track changes to the
dataset and can produce the current version of the data. This is described conceptually
in Figure 3-16.

125

Chapter 3 Data Lake Design with Apache Iceberg and S3 Tables

**_Figure 3-16._** _Reference Architecture for Apache Iceberg_

**Time Travel**

Because this is a write-only system, previous versions of the data also exist. These
previous versions can be traversed using a feature called “time travel.” Users can query
the data as it was at a certain point in time or observe how the data changes over time.
This is especially valuable for customers requiring full auditability of their data.

126

Chapter 3 Data Lake Design with A c Ic d S Tabl

You’ve been writing a large dataset to the data lake over the last 30 days. But now you
want to add a column, delete a column, and rename two columns. Without robust
support for how its schema might evolve over time, you would need to reprocess 30 days
of data to convert the existing data to the new schema. Schema evolution is a feature
that becomes non-negotiable as the data gets larger. What if a dataset in a data lake has
a _billion_ rows? After a certain size, a full schema migration incurs significant cost—tens
of thousands of dollars! Where software engineering prides itself on agile methodologies
and iterative development, data engineering is much more valuable when it’s well
thought out and designed intelligently. The issue is not that this sort of operation
might be costly, but that schemas change repeatedly over time. Without a strategy to
handle schema changes gracefully, the potential cost incurred would be recurring and
unknown.

Open table formats are well suited to provide advanced schema evolution features.
With their metadata layer, which separates the schema from the data files, changes to
the schema are simply tracked in the metadata files with no change to the underlying
data files. If a column is reordered, just reorder it in the metadata file. If a column is
deleted, just note that in the metadata file and don’t pull that column when the dataset is
queried. And so on.

Partition evolution is an important feature in data systems. At its most basic, it means
that partitions can be dynamically created as new data arrives. Think of a table designed
for a time series dataset that is partitioned by day. As data is collected and inserted each
day, a new partition is created. As the data ages, older partitions need to be deleted as
part of a data lifecycle policy.

Well-designed partitions are determined by query patterns. In fact, the filters used
in queries need to reference partitions properly in order to yield any benefit. Any initial
partitions created may serve its purpose for a while, but as the data grows, new use cases
may be discovered. Query patterns can change, and the partitions must change along
with them. Similar to our schema evolution challenge discussed previously, performing
a migration on the full dataset is either expensive or disruptive to the business. Some
open table formats can manage changes to the partitioning strategy over time using their
metadata management features.

127

Chapter 3 Data Lake Design with A c Ic d S Tabl

Let’s say our sales table (below) was originally partitioned by date.

CREATE TABLE sales (

) PARTITIONED BY (date);

After several months, we determine that most of the sales reporting is being filtered
by region, so we add region as a partition.

ALTER TABLE sales ADD PARTITION FIELD region;

The open table format maintains backward compatibility and allows the data to be
queried as one dataset. Any new data that’s written will use both partitions: date and
region. Existing data will use only the date partition. Although this will result in uneven
performance, it avoids a full migration.

There are other types of partition operations, such as merging, splitting, and
repartitioning, and it will be important to learn about the partition evolution features
supported by your chosen open table format.

Open table formats are designed to manage read and write operations on large datasets
in a distributed architecture to allow multiple users and processes to access and modify
data simultaneously. Concurrency control is needed to ensure consistency and isolation
of transactions, two of the ACID properties. Optimistic concurrency control (OCC) is
the most common mechanism for managing concurrency in a data lake. It assumes that
conflicts are rare and proceeds with operations without locking resources. If it detects a
conflict, the transaction is aborted and retried. It is quite an astute observation to deduce
that open table formats implement optimistic locking because they are limited by the
capabilities of object storage. Database systems utilizing block storage are capable of
more fine-grained locking mechanisms.

128

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Choosing an Open Table Format**

There are several popular open table formats today. These include Apache Hudi, Delta
Lake, and Apache Iceberg. Apache Iceberg has achieved wide adoption and will be the
focus of the rest of this chapter. We can see from Table 3-3 that Apache Iceberg supports
all the major features, including full schema evolution and partition evolution.

**_Table 3-3._** _Feature Comparison of Popular Open Table Formats_

**Open Table Format Feature** **Apache Iceberg** **Delta Lake** **Apache Hudi**

File format Parquet, OR A Parquet Parquet, OR A

Transaction support (A I Yes Yes Yes

S Full Partial Full

Partition evolution Yes Yes Yes

Data versioning (aka “time travel”
queries)

Yes Yes Yes

Concurrency control Optimistic locking Optimistic locking Optimistic locking

Next, I’ll dive deeper into Apache Iceberg and S3 Tables.

**Apache Iceberg and S3 Tables**

In 2024, AWS announced Amazon S3 Tables, the first cloud object store with native
Apache Iceberg support. Think of S3 Tables as the managed service for Apache Iceberg.
This greatly simplifies the overhead required to manage Iceberg tables on S3. By offering
this as a managed service, AWS is able to add optimizations and automate maintenance
to deliver 3x faster query performance and 10x higher transaction throughput. Iceberg
tables require ongoing operational maintenance that normal tables do not require. AWS
is assuming the responsibility of performing maintenance operations like compaction,
snapshot management, and unreferenced file removal—which reduces significant
overhead and risk and is itself an enormous benefit.

129

Chapter 3 Data Lake Design with A c Ic d S Tabl

I’ll spend the rest of this chapter demonstrating how to perform basic operations
with both S3 Tables and self-managed Apache Iceberg tables. I use Glue Spark in these
examples because that is generally the default option for data processing. Table 3-4
shows which Iceberg versions are supported in each AWS Glue version.

**_Table 3-4._** _Iceberg Versions Supported by AWS Glue_

**AWS Glue Version** **Supported Iceberg Version**

5.0 1.7.1

4.0 1.0.0

3.0 0.13.1

For the examples presented, I’ll use the NYC Taxi and Limousine Commission (TLC)
Trip Record Data, <sup>4</sup> a public dataset.

**Create an S3 Table Bucket**

The first thing you’ll notice is that managed Iceberg S3 buckets are referred to as “table
buckets” and are distinguished from normal S3 buckets, which are now referred to as
“general purpose buckets.” They are segregated in the S3 service. The first thing we’ll
need to do is create one of these table buckets. This is the logical location for where data
will be stored using Iceberg.

From the S3 console, choose **Table buckets** from the navigation menu, and then
choose **Create bucket** . Figure 3-17 shows the create table bucket screen. I’ll call the table
bucket “city-data.”

[4 TLC Trip Record Data. https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

130

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-17._** _Table Bucket Creation in the AWS Console_

After creation, the ARN will be viewable from the list of table buckets. You’ll need this
for the Spark configuration in the next section. Incidentally, the way AWS has architected
S3 Tables, they’ve essentially created global addressing down to the table level.

**Configure IAM Policy for S3 Tables**

Permissions for the S3 Tables feature are not included in the standard S3 permissions.
So, for example, if you attached the AWS-managed policy, S3FullAccess, this would not
include S3 Tables access. We need to create a new policy for S3 Tables permissions and
attach it to the service role used in the Glue notebook we’ll use in the next section. For
demonstration purposes, we can create a policy that includes all S3 Tables permissions
restricted to the S3 Tables bucket resource ARN we created in the previous section. I
attached this policy to the IAM role called _GlueServiceRole_, which I am using for my Glue
notebook environment.

131

Chapter 3 Data Lake Design with A c Ic d S Tabl

{

"Resource": "arn:aws:s3tables:us-east-1:{AWS_ACCOUNT}:bucket/

city-data"

}

**Download and Stage S3 Tables Catalog JAR in S3**

The S3 Tables Catalog for Apache Iceberg is distributed as a Maven JAR called s3tables-­catalog-for-iceberg.jar. When connecting to tables, this client catalog JAR is a
dependency when you initialize a Spark session for Apache Iceberg. The current AWS
documentation instructs you to host this JAR file in a general-purpose S3 bucket and
reference it as part of your Spark configuration. This is the guidance for now, which
could change as native support for S3 Tables is added to subsequent Glue versions.

s3://your-bucket/s3tables/jars/s3-tables-catalog-for-icebergruntime-0.1.4.jar

**Configure an S3 Tables Spark Session**

With our IAM policy attached and our client catalog JAR hosted in S3, we can now create
a Spark session in our Glue notebook and perform S3 Tables bucket operations. First,
you can configure the Glue session.

%idle_timeout 2880
%glue_version 5.0
%worker_type G.1X
%number_of_workers 5
%%configure

132

Chapter 3 Data Lake Design with A c Ic d S Tabl

{
"--conf": "spark.sql.extensions=org.apache.iceberg.spark.extensions.

IcebergSparkSessionExtensions",

"--extra-jars" : "s3://your-bucket/s3tables/jars/s3-tables-catalog-for
iceberg-­
}

Similar to non-Iceberg tables, S3 Tables are organized within telescoping logical
containers that include a catalog and a namespace. You can think of a namespace as a
database—it’s simply a collection of tables. This structure is used to reference tables in
SQL queries.

{CATALOG_NAME}.{NAMESPACE}.{TABLE_NAME}

We can use the Spark session builder to method chain the Spark configurations.
If you’re not familiar with how Spark configuration is constructed, I’ll review it before
we move on. In the next several passages, I break out and explain each key-value
configuration setting below.

spark = SparkSession.builder \

For S3 Tables, we designate the catalog as Iceberg-enabled via Spark parameter
values. The catalog name can be customized to whatever you want; however, I would
recommend indicating that it’s an S3 tables bucket catalog. For instance, I’ll define the
catalog name as “s3tablesbucket.”

CONFIG_KEY = “spark.sql.catalog.s3tablesbucket”
CONFIG_VALUE = “org.apache.iceberg.spark.SparkCatalog”
The next lines designate that this Iceberg catalog is implemented using a specific
Amazon software package for S3 Tables.

CONFIG_KEY = “spark.sql.catalog.s3tablesbucket.catalog-impl”
CONFIG_VALUE = “software.amazon.s3tables.iceberg.S3TablesCatalog”
Next, we specify the specific S3 Tables bucket that serves as the warehouse location
for where the data will live. I use the ARN that was created in the previous section.

CONFIG_KEY = “spark.sql.catalog.s3tablesbucket.warehouse”

133

Chapter 3 Data Lake Design with A c Ic d S Tabl

CONFIG_VALUE = “arn:aws:s3tables:us-east-1:{AWS_ACCOUNT}:bucket/city-data”
We then specify the extensions that enable Iceberg table operations.
CONFIG_KEY = “spark.sql.extensions”
CONFIG_VALUE = “org.apache.iceberg.spark.extensions.
IcebergSparkSessionExtensions”

Other general Spark settings like caching can be configured as well, but I’ll exclude
those. To perform operations on this S3 Tables catalog, I can use the Spark SQL API.

spark.sql("CREATE NAMESPACE IF NOT EXISTS s3tablesbucket.nyc_data")

Refer to the Git repository for sample notebooks that include all the proper
configuration commands and settings. With our Spark session configured and
namespace created, we can now perform operations on Iceberg tables.

**Write Data to S3 Table**

First, I’ll load the NYC yellow cab trip dataset into a dataframe.

# Read Parquet file from S3
s3_bucket = "your-bucket"
s3_prefix = "/nyc-taxi/yellow_tripdata_2024-01.parquet"
s3_path = f"s3://{s3_bucket}/{s3_prefix}"

df = spark.read.parquet(s3_path)

With Spark, we can create the table dynamically when writing the dataset. As I
mentioned earlier, parquet is self-describing, so the schema is extracted on read. If
reading from a CSV file, Spark can infer the schema. For testing and prototyping, this
saves us the trouble of defining the table structure and creating the table in advance.

df.writeTo("s3tablesbucket.nyc-data.yellowtrip-data") \
.tableProperty("format-version", "2") \
.createOrReplace()

The format-version designates this as an Iceberg version 2 table. If I need the table
definition, I can display it using this Spark SQL statement.

134

Chapter 3 Data Lake Design with A c Ic d S Tabl

spark.sql("DESCRIBE s3tablesbucket.nyc_data.yellow_tripdata").show()

+--------------------+-------------+-------+
| |  data_type| comment|
+--------------------+-------------+-------+
| |     int|  NULL|
| | timestamp_ntz|  NULL|
| | timestamp_ntz|  NULL|
| | |  NULL|
| | |  NULL|
| | |  NULL|
...

**Selecting from an S3 Tables Bucket Table**

Using the Spark SQL API, we can select from the S3 Tables bucket table as you’d expect.

spark.sql("""
SELECT VendorID, tpep_pickup_datetime, tpep_dropoff_datetime,
passenger_count
FROM s3tablesbucket.nyc_data.yellow_tripdata
""").show()

+-------+-------------------+--------------------+--------------+
|VendorID|tpep_pickup_datetime|tpep_dropoff_datetime|passenger_count|
+-------+-------------------+--------------------+--------------+
| | 2024-01-01 00:57:55| | |
| | 2024-01-01 00:03:00| | |
| | 2024-01-01 00:17:06| | |
| | 2024-01-01 00:36:38| | |
| | 2024-01-01 00:46:51| | |
| | 2024-01-01 00:54:08| | |
| | 2024-01-01 00:49:44| | |
| | 2024-01-01 00:30:40| | |
...

135

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Updating an S3 Tables Bucket Table**

Now let’s perform an update on this table to see how easily this transaction is handled
seamlessly by S3 Tables.

spark.sql("""
UPDATE s3tablesbucket.nyc_data.yellow_tripdata
SET passenger_count = 99
WHERE VendorID = 2
""")

+-------+-------------------+--------------------+--------------+
|VendorID|tpep_pickup_datetime|tpep_dropoff_datetime|passenger_count|
+-------+-------------------+--------------------+--------------+
| | 2024-01-01 00:57:55| | |
| | 2024-01-01 00:03:00| | |
| | 2024-01-01 00:17:06| | |
| | 2024-01-01 00:36:38| | |
| | 2024-01-01 00:46:51| | |
| | 2024-01-01 00:54:08| | |
| | 2024-01-01 00:49:44| | |
| | 2024-01-01 00:30:40| | |
| | 2024-01-01 00:26:01| | |
...

The results confirm that our update transaction was applied successfully.

**Advanced Iceberg Queries on S3 Table**

Now that we have an S3 Table created and populated with data, I can run advanced
queries to view Iceberg artifacts like the individual files comprising the data in the table
and the snapshots of the table.

**Inspecting Data Files**

We’ll first query for the file list. Note that because this is a managed service, the data is
stored in an AWS-managed bucket.

136

Chapter 3 Data Lake Design with A c Ic d S Tabl

spark.sql("""

+------+-----------------------------------------------------+------------+
| content|file_path |file_format |
+------+----------------------------------------------------------+------+

|0    |s3://[AWSGUID]--table-s3/data/00000-27-[FILEGUID]-0-00001.parquet|PARQUET |

|0    |s3://[AWSGUID]--table-s3/data/00001-28-[FILEGUID]-0-00001.parquet|PARQUET |

|0    |s3://[AWSGUID]--table-s3/data/00002-26-[FILEGUID]-0-00001.parquet|PARQUET |
+-------+----------------------------------------------------+-----------+

Similarly, we can query and inspect snapshots of the table.

spark.sql("""

+-------------+----------+---------+--------+----------------------------+
|committed_at |snapshot_id|parent_id|operation |manifest_list        |
+-------------+----------+---------+--------+----------------------------+

|2025-04-17 19:40|27639004... |74363043...|overwrite |[S3Path]/snap-[GUID]-a7d824.avro |

|2025-04-17 19:37|74363043... |NULL    |append  |[S3Path]/snap-[GUID]-612e61.avro|
+-------------+----------+---------+----------+--------------------------+

137

Chapter 3 Data Lake Design with A c Ic d S Tabl

Note that I truncated several fields and used placeholders to abbreviate the
manifest_list results to enhance readability.

You can also query for partitions and manifests by appending “.[query type]” to the
end of the table name. This would be {catalog.namespace.table}.partitions and {catalog.
namespace.table}.manifests. This is left as an exercise for the reader.

**Unmanaged Apache Iceberg in S3**

While managed Iceberg is a great feature to simplify its adoption, it might not be the
best fit for every practitioner or every use case. There may be instances where you
need more control over your Iceberg implementation, including when and how to
perform maintenance of the tables. In the next sections, I’ll also demonstrate how to
implement Apache Iceberg directly on general-purpose S3 buckets, including creating
and partitioning tables, populating the table, updating a table, performing time travel
queries, and performing maintenance operations in Amazon Athena.

**Create Apache Iceberg Table**

First, let’s create our Apache Iceberg table. For our yellow taxi data, we will
partition by day.

CREATE EXTERNAL TABLE IF NOT EXISTS iceberg_yellow_taxi_tripdata(

138

Chapter 3 Data Lake Design with A c Ic d S Tabl

)
PARTITIONED BY (day(tpep_pickup_datetime))
LOCATION 's3://bucket/iceberg_yellow_taxi_tripdata_manipulation/'
TBLPROPERTIES ( 'table_type' ='ICEBERG' );

What differentiates our table definition from a regular table in Athena is the
TBLPROPERTIES setting with parameter 'table_type'='ICEBERG'. Note that Athena
supports merge-on-write and not copy-on-write.

Now let’s populate this table from a regular raw table with data imported from the
data provider.

INSERT INTO "nyc-tlc-trip-records-raw"."iceberg_yellow_taxi_tripdata"
SELECT *
FROM "nyc-tlc-trip-records-raw"."yellow_taxi_tripdata"

**Update an Apache Iceberg Table**

With our Iceberg table populated, let’s perform an update on this table. This statement
will set the trip_distance to 7.44 for all records with a pickup date in the year 2023.

UPDATE "iceberg_yellow_taxi_tripdata"
SET "trip_distance" = 7.44
WHERE year(tpep_pickup_datetime) = 2023;

Figure 3-18 shows the result.

139

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-18._** _Apache Iceberg Table Updated in Place_

**Time Travel Feature in Apache Iceberg**

Next, we’ll use the time travel feature to view the data before our update. The FOR
TIMESTAMP AS OF TIMESTAMP query command restricts the ResultSet based on the state
of the data in the table as of that point in time.

SELECT *
FROM "nyc-tlc-trip-records-raw"."iceberg_yellow_taxi_tripdata"
FOR TIMESTAMP AS OF TIMESTAMP '2024-07-31 11:00:00 UTC'
where year("tpep_pickup_datetime") = 2023;

The results of this query are shown in Figure 3-19.

140

Chapter 3 Data Lake Design with A c Ic d S Tabl

**_Figure 3-19._** _Time Travel Query Showing Data Before Update_

Note that the data appears as it did before our UPDATE statement.

**Metadata for Apache Iceberg Tables**

In addition to our table operations, we can also query to obtain important metadata
about our Iceberg tables. This includes _partitions_, _data files_, _metadata files_, and
_snapshots_ .

We’ll query for partitions first. This not only provides a way to validate that the
partitions were created properly upon table creation but that each subsequent partition
was created after loading new data. You can also view record counts for each partition
to validate data loads and to see how the data is distributed across partitions. You’ll
notice from the query below that the partition list for any table is retrievable in Athena by
simply appending _$partitions_ to the end of the table name.

-- Querying Iceberg Table metadata
SELECT *
FROM

The ResultSet showing each of the partitions is displayed in Figure 3-20.

141

Chapter 3 Data Lake Design with Apache Iceberg and S3 Tables

**_Figure 3-20._** _Apache Iceberg Metadata for Table Partitions_

Next, we’ll look at data files. Similar to partitions, we can view the list of data files for
any table in Athena by appending _$files_ to the table name.

SELECT *
FROM "nyc-tlc-trip-records-raw"."iceberg_yellow_taxi_tripdata$files"

Figure 3-21 lists each individual file where the table data physically resides.

**_Figure 3-21._** _List of Data Files Comprising the Apache Iceberg Table_

142

Chapter 3 Data Lake Design with Apache Iceberg and S3 Tables

Finally, the last query I will demonstrate is the query to list all of the manifest files
that collectively represent the Apache Iceberg table. These files are in the.avro format
and are displayed in Figure 3-22. You can retrieve a list of manifest files in Athena by
appending _$manifests_ to the table name.

SELECT *
FROM "nyc-tlc-trip-records-raw"."iceberg_yellow_taxi_tripdata$manifests"

**_FIgure 3-22._** _List of Manifest Files for the Apache Iceberg Table_

Snapshots are created every time a transaction is committed—adding, updating,
or deleting data—and represent the state of an Iceberg table as a specific point in time.
Snapshots are what enable time travel queries. This is an important detail, as you’ll
discover in the next section. Snapshots are related to manifest files, but they are not the
same. Manifest files describe the data files in each snapshot and store other metadata
like the location, size, and statistics. You can access a list of snapshots for any Iceberg
table by appending _$snapshots_ to the table name in your select query.

SELECT *
FROM "nyc-tlc-trip-records-raw"."iceberg_yellow_taxi_tripdata$snapshots"

The results are shown in Figure 3-23.

**_Figure 3-23._** _Listing Snapshots of an Iceberg Table_

143

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Maintenance for Apache Iceberg Tables**

There are maintenance operations that are regularly required to maintain optimal
query performance of Iceberg tables, and the metadata helps us determine when
these operations are needed. This section discusses the different types of maintenance
operations, including OPTIMIZE and VACUUM, and provides examples for
performing them.

**Note** B PTI I E A
that the I
performed.

**OPTIMIZE Iceberg Tables**

Compaction is the process of merging a number of small data files into larger files for
more efficient processing. Iceberg tables are designed to be append-only, which can
generate small data files naturally over time as more updates are made to the table.
Delete files are created when data is deleted from a table and require an additional
processing step to apply row-level deletes to the query results. Compaction can be
executed manually in Athena using the OPTIMIZE command.

Apache Iceberg supports many compaction strategies and features; however, Athena
only supports two: BIN_PACK and SORT. BIN_PACK is the default option, as it is the fastest
and cheapest. It rewrites the data into larger files without moving or shuffling the data.
SORT will sort the data while it compacts the files.

OPTIMIZE TABLE iceberg_yellow_taxi_tripdata REWRITE DATA USING BIN_PACK

Regular compaction can be automated by scheduling a Glue job to run that executes
the command. This may be needed in situations where many updates are happening
between scheduled vacuum operations.

**VACUUM Iceberg Tables**

Similar to PostgreSQL databases, VACUUM is an important operation for maintaining
Iceberg tables. VACUUM is a more comprehensive process that includes compaction but
also performs additional maintenance tasks that include

144

Chapter 3 Data Lake Design with A c Ic d S Tabl

     - Removing orphan files

     - Cleaning up obsolete metadata entries in manifest files

     - Optimizing partition metadata to facilitate partition pruning

     - Refreshing table statistics

     - Performing consistency checks to ensure the metadata and data are
in a valid state

The VACUUM operation can be executed manually with the following command
in Athena:

CALL vacuum('nyc-tlc-trip-records-raw.iceberg_yellow_taxi_tripdata');

We can customize and fine-tune VACUUM to control how it performs these
functions and to automate its operation. One common scenario is to define the
maximum age for a snapshot, automatically merging and expiring any snapshots that
exceed that age. The command below sets the maximum snapshot age to 3 days.

ALTER TABLE iceberg_yellow_taxi_tripdata SET TBLPROPERTIES (
'vacuum_max_snapshot_age_seconds' = '259200';
);

**Caution** Time travel queries are supported with snapshots. B
expiring snapshots with VA
the ability to time travel to those expired snapshots. T
between performance and data versioning.

**Unmanaged Apache Iceberg in AWS Glue**

Since AWS Glue and Apache Spark are such an integral part of our data lake and data
integration strategy, it’s important to know how to create and manage Apache Iceberg
tables from Spark. In this section, I’ll demonstrate how to create and perform common
operations on Apache Iceberg tables using AWS Glue Spark jobs.

145

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Note** I AWS G
limitation in AWS G T Apache
I AWS G

**AWS Glue Spark Configuration**

There are two configurations that are needed to get Apache Iceberg functional in AWS
Glue. The --datalake-formats parameter that is passed into the Glue job needs to be
set to “iceberg.”

The Spark configuration should be set as follows.

spark.sql.extensions=org.apache.iceberg.spark.extensions.
IcebergSparkSessionExtensions
--conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog
--conf spark.sql.catalog.glue_catalog.warehouse=s3://<your-warehouse-dir>/
--conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.
glue.GlueCatalog
--conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.
s3.S3FileIO

These Spark configurations can be specified in the Glue job or passed in as a spaceseparated string for the job’s --conf parameter. If you’re just starting out and building
your data lake, it makes sense to keep these configurations closer to the code. However,
as you scale your practice, you should consider using a centralized parameter store like
AWS Systems Manager Parameter Store to manage these values. In the event you need to
alter these values, you only have to change it in one place.

**Apache Iceberg Operations in Spark**

Before we can utilize Iceberg tables in Spark, we need to import the relevant Spark
integration modules from the SparkActions class of the Iceberg library. The following
import statement includes the most basic modules.

from iceberg.spark.actions import ScanFiles, SetLocation

146

Chapter 3 Data Lake Design with A c Ic d S Tabl

The ScanFiles action is needed to scan the data files of an Iceberg table. The
SetLocation action is needed to set the location for where the Iceberg table files will be
stored in S3.

**Create an Iceberg Table**

First we need to set the location of where our Iceberg table will live.

# Set the Iceberg table location
iceberg_table_location = "s3://your-bucket/iceberg-tables/nyc-tlc-taxi"

To create the table, we can use a Spark SQL command. Notice that we indicate that
this is an Iceberg table by specifying iceberg as the table format or table provider as
shown below.

# Create the Iceberg table
spark.sql(f"CREATE TABLE IF NOT EXISTS nyc_tlc_taxi_trips USING iceberg
LOCATION '{iceberg_table_location}'")

**Writing Data to an Iceberg Table**

To write data to our table, we first need to load data into a Spark dataframe. In our
example, we can load data from the CSV file of NYC taxi trip data. Since this is just a
demonstration, we will infer the schema from the CSV file.

df = spark.read.format("csv") \

Now that we have a dataframe with data, we will write it out to our Iceberg table
by specifying the format as “iceberg” and the mode as “append.” Append is the most
common write operation for Iceberg tables.

# Write the DataFrame to the Iceberg table
df.write.format("iceberg").mode("append").save(iceberg_table_location)

147

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Update an Iceberg Table**

To update the data in our table, we will first update the data in the dataframe. Our update
will increase the trip distance by 10% when VendorID is 1. To save this data to our table,
we will perform another write operation—this time we will use the “overwrite” mode (as
shown below).

# Update the table by changing the trip_distance for some rows
df_updated = df.withColumn("trip_distance", when(df.VendorID == 1, df.trip_
distance * 1.1).otherwise(df.trip_distance))

# Write the updated data to the iceberg table
df_updated.write.format("iceberg").mode("overwrite").save(iceberg_table_
location)

**Perform Time Travel Queries**

We can also perform time travel queries in Spark. We can set the “as-of-timestamp”
option in Spark to the point in time we want to query. Using the time module, we can do
a quick time calculation to see the state of the data before the update.

Import time

# Perform a time travel query to get the data before the update
df_before_update = spark.read.format("iceberg") \

**Maintenance of Iceberg Tables in Spark**

Knowing how to execute Iceberg table maintenance operations in Spark allows for data
integration pipelines in Glue to include these functions where necessary. One common
scenario is to execute necessary compaction or vacuum after a lot of data operations
have been executed on a table. This binds the maintenance operation to the data
operation, making this much more deterministic and deliberate than some external or
unrelated process.

148

Chapter 3 Data Lake Design with A c Ic d S Tabl

As mentioned previously, the Iceberg API in Spark is accessed through the
SparkActions class.

SparkActions.get()

**Vacuuming an Iceberg Table**

We can use the Boto3 library to create an Athena client and call the vacuum command
for the Iceberg table.

# Requires boto3
client = boto3.client("athena")
client.start_query_execution(

)

This concludes our study of implementing unmanaged Iceberg tables in general
purpose S3 buckets. Let’s see how we can apply agentic AI to help us perform regular
maintenance on Iceberg tables.

**Iceberg Table Maintenance Agent**

Let’s say we want to implement unmanaged Iceberg tables in general purpose S3 buckets
and keep it fully optimized for performance, but we don’t want to do all the work to
maintain the table over time. We could certainly implement Iceberg table maintenance
as a set of deterministic, rules-based operations, with checks scheduled at regular
intervals. However, if we want something more adaptable, intelligent, and dynamic, we
can explore implementing Iceberg table maintenance with agentic AI.

149

Chapter 3 Data Lake Design with A c Ic d S Tabl

This will be a high-level design discussion for a basic hypothetical agent. I will say,
without reservation, that we are still in the experimental phase and that we should
expect to iterate quite a bit. One customer reported deploying the 200th version of
an agent they’ve deployed in production. A good way to approach agentic design is
to consider how a human might approach the problem. In doing so, you’ll quickly
discover that out of all of the conceptual elements of an agent (model, prompt, tools),
the most impactful and enabling are the tools. We can implement the tools in AWS
Lambdas and use Bedrock AgentCore Gateway to “MCPify” it for agentic integration. I
discuss the mechanics of implementing agents in Chapter 12, “Building AI Agents with
Bedrock AgentCore, Strands Agents, and Model Context Protocol (MCP).” Due to space
limitations, I won’t be providing the code for implementing this solution. You can find
full solutions in the GitHub repo provided with the book. The tools for our Iceberg table
maintenance agent will fall into the following categories.

**Discovery and Inventory Tools**

When the agent is first invoked, it will need a way to discover and create an inventory of
the iceberg tables that exist in the catalog.

iceberg_table_discovery: discovers and catalogs all Iceberg tables within a specified
Glue catalog. Creates an inventory list of all Iceberg tables in the catalog.

We can use the AWS Glue API via the Boto3 library in a Python script to discover
databases, tables, and Iceberg tables. Using the get_tables() method in the Boto3 Glue
client, you can retrieve a table object that will include all of its properties. You can
discover Iceberg tables by testing the table property for table_type = “ICEBERG”. Below is
some sample code to retrieve tables and test whether they are Iceberg tables. Searching
via the catalog is far more efficient than any other method.

**Metrics Collection Tools**

Once you have a list of Iceberg tables, the agent will need to know the Iceberg-related
metrics to help it determine the health of the Iceberg table. We can use a Python library
called PyIceberg. The PyIceberg library has the advantage of having direct access to
manifests and data files. It can count the exact number of files and their precise sizes.

150

Chapter 3 Data Lake Design with A c Ic d S Tabl

Use PyIceberg to collect the following metrics:

     - Total number of data files

     - Number of small files (<128MB)

     - Average file size

     - Total table size

     - Number of snapshots

     - Snapshot ages

We can also pull historical query performance from Athena and CloudWatch for
these tables, which can indicate degraded performance over time due to suboptimal
Iceberg table maintenance. These metrics can enhance the analysis and planning the
agent will do to determine what maintenance actions are needed. Here’s how our tool
might be defined.

iceberg_table_metrics_collection: collect key maintenance
metrics of iceberg tables, including historical query performance,
if available.

Using the AWS Athena API via the Boto3 library, we can retrieve query execution
information using an Athena client and using the list_query_executions() method. We
can then filter executions by the Iceberg tables discovered previously. The raw metrics
can be aggregated and averaged to compare recent and older query executions. You
may think, “This is too much information for me to consume, analyze, and understand.”
It is, but it’s not for you! Sure, you’ll want to be frugal with the number of input tokens
consumed, but otherwise, AI doesn’t care! Consider not only how much development
effort a refined set of metrics may require, but also how much effort will be needed to
maintain them over time. Compare this to simply providing the agent with less refined
and verbose metrics from which to derive insights.

Now with the metrics collected, we need to analyze them to determine the best
course of action.

151

Chapter 3 Data Lake Design with A c Ic d S Tabl

**Analysis and Planning Tools**

The analysis and planning tools will use the table configuration, retention settings, and
metrics collected from the Iceberg tables to determine what actions, if any, are needed
for each table.

analyze_iceberg_table_metrics: Analyze the Iceberg table metrics
and historical query performance to determine what Iceberg
maintenance operations should be performed.

The agent will utilize the metrics it collected and its associated generative AI model
to analyze, reason, and provide recommendations for optimizing the Iceberg table.
Here’s what an example analysis report might look like.

## customer_events Table

**Analysis Date:** December 27, 2024, 15:45:00 UTC
**Database:** analytics_prod
**Table:** customer_events
**Analysis Duration:** 47 seconds
**Agent:** Autonomous Iceberg Maintenance Agent v1.0

## Executive Summary

The `customer_events` table requires **IMMEDIATE MAINTENANCE**. Analysis
reveals severe file fragmentation (92% small files) and excessive snapshot
accumulation (178 snapshots) causing significant performance degradation.
Query performance has degraded 38% over the past 30 days, with data scanned
increasing 51%.

**Recommended Actions:**
1. • **CRITICAL:** Compact data files (reduce 2,456 files to ~180 files)
2. • **CRITICAL:** Expire old snapshots (reduce 178 snapshots to ~7)

**Expected Impact:**

- **Performance Improvement:** 45-55% faster queries

- **Cost Savings:** $1,450/month

- **Maintenance Cost:** $32 (one-time)

- **ROI:** 4,531% (payback in 16 hours)

152

Chapter 3 Data Lake Design with A c Ic d S Tabl

This is a very extensive, business-level analysis that—in addition to the technical
recommendations—also includes estimates for cost, ROI, and payback period.

Once it is determined that maintenance is required on an Iceberg table, the agent will
need a way to execute those maintenance operations, whether it be compaction or
snapshot expiration. We can provide the agent two tools to perform general Iceberg table
maintenance.

iceberg_table_perform_compaction: Perform the compaction
operation on an Iceberg table.

iceberg_table_expire_snapshots: Perform the snapshot expiration
operation on an Iceberg table.

We can again use the PyIceberg library, which has specialized functions to perform
these operations. I’ll provide just a snippet with the method call for each.

Compaction with rewrite_data_files:

Snapshot expiration with expire_snapshots:

Refer to Chapter 12, “Building AI Agents with Bedrock AgentCore, Strands Agents,
and Model Context Protocol (MCP),” for implementation strategies and the GitHub repo
for full coding examples. That concludes the design discussion of our Iceberg Table
Maintenance Agent. It also brings us to the end of this chapter.

153

Chapter 3 Data Lake Design with A c Ic d S Tabl

In this chapter, I explored the design of data lakes, a strategic data platform that
centralizes all types of data to drive business insights. I identified and described the key
components of a data lake, including storage, metadata management, data ingestion,
and data processing. I highlighted the best practices for data lake design, such as
separating analytical and operational workloads and the medallion architecture with its
bronze, silver, and gold stages. I took this concept further by presenting the progressive
medallion architecture, which included common practical data quality stages many
practitioners consider when designing their data lake. I described the new capabilities
provided by open table formats, like enabling ACID transactions, schema evolution,
and efficient maintenance. I demonstrated how to implement managed Iceberg tables
in S3 Tables. I also showed how to implement Iceberg in general-purpose S3 buckets in
Athena and Glue Spark. I provided examples for querying Iceberg metadata, including
files, snapshots, partitions, and manifest files, and performing Iceberg maintenance
tasks such as compaction and vacuuming. I provided high-level guidance for
architecting an agentic solution for Iceberg table maintenance.

In the next chapter, we’ll explore the alternative to the centralized data lake strategy:
the data mesh.

154

**CHAPTER 4**

## **Data Mesh Design** **with Amazon DataZone**

In the previous chapter, I explored data lakes as centralized repositories that sought to
consolidate all organizational data to derive new insights. While data lakes solve many
traditional data warehousing limitations, they introduce new challenges around data
ownership, domain expertise, and organizational scalability that become increasingly
apparent as enterprises grow. The data mesh paradigm emerged as a response to
these limitations, proposing a fundamental shift from centralized data platforms to
a distributed, domain-oriented approach that treats data as a product. Rather than
consolidating all organizational data into a single lake managed by a central team,
data mesh advocates for domain teams to own and operate their data products while
maintaining interoperability through standardized interfaces and federated governance.

In this chapter, I’ll describe the differences between a data lake and a data
mesh strategy and explain why a data mesh may be a better architectural strategy
for enterprises. I’ll introduce Amazon DataZone and describe how it simplifies the
implementation and management of a data mesh with features for catalog management,
data product publishing and subscription management, data lineage, and data
discovery. I’ll highlight data governance features, including the integration of generative
AI for metadata management. I’ll address how the organizational structure should
change to support a data mesh strategy. Finally, I’ll dive deep into the design and
implementation of a data mesh with Lake Formation and DataZone.

I’ll start the discussion by highlighting the limitations of a centralized data lake.

155
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_4](https://doi.org/10.1007/979-8-8688-2199-8_4#DOI)

Chapter 4 Data Mesh Design with Am Z

**Limitations of Centralized Data Lakes**

The question of centralization vs decentralization has been a topic of business
management theory debated for over 100 years.

_The CEO’s dilemma—were the gains of centralization worth_
_the pain it could cause?—is a perennial one. Business leaders_
_dating back at least to Alfred Sloan, who laid out GM’s influential_
_philosophy of decentralization in a series of memos during the_
_1920s, have recognized that badly judged centralization can stifle_
_initiative, constrain the ability to tailor products and services_
_locally, and burden business divisions with high costs and poor_
_service._ <sup>1</sup>

In the 1920s, Alfred Sloan was talking about the mass production of cars, but the
same theory holds true for IT services in the digital era. Any centralized service, no
matter how well staffed, will struggle to scale to meet the demand with the desired
responsiveness as enterprises grow beyond a certain size or complexity.

Operationally, a centralized data lake means a centralized data team. For companies
starting their modern data strategy journey, centralization provides many benefits,
including development and enforcement of best practices for design, cost management,
and security, as well as an alignment to top-level business priorities. This can be
formalized as a center of excellence (CoE).

But as the data practice grows, a number of challenges emerge.
The centralized data team struggles to acquire the specialized domain knowledge
of the business, which frustrates domain experts. Security restrictions permit only a few
key individuals to produce and deliver new data to the data lake, creating bottlenecks.
Onerous bureaucratic hurdles develop to manage how consumers request and receive
access to data assets.

1 Andres Campbell, Sven Kunisch, and Günter Müller-Stewens, To centralize or not to centralize,
[McKinsey Quarterly, New York, NY, 2011, https://www.mckinsey.com/business-functions/](https://www.mckinsey.com/business-functions/people-and-organizational-performance/our-insights/to-centralize-or-not-to-centralize)
[people-and-organizational-performance/our-insights/to-centralize-or-not-to-](https://www.mckinsey.com/business-functions/people-and-organizational-performance/our-insights/to-centralize-or-not-to-centralize)
[centralize (accessed May 14, 2024).](https://www.mckinsey.com/business-functions/people-and-organizational-performance/our-insights/to-centralize-or-not-to-centralize)

156

Chapter 4 Data Mesh Design with Am Z

**Introducing the Data Mesh**

A data mesh is a modern data architecture strategy that decentralizes data ownership
and stewardship but provides federated governance across domain-oriented data
systems to enable producers to share governed data. This strategy treats data as a
product within the enterprise and formally separates producers and consumers.
Figure 4-1 shows this conceptually.

**_Figure 4-1._** _Conceptual Diagram of a Data Mesh_

157

Chapter 4 Data Mesh Design with Am Z

For many enterprise businesses, a data mesh offers the best of both worlds: data
producers are empowered to move fast and innovate in their domain, while security and
governance are federated and centralized.

In the next section, I’ll describe the data mesh architecture on AWS.

**Data Mesh on AWS with Amazon DataZone**

If we overlay AWS services onto our conceptual diagram, we will see which AWS
services comprise a data mesh on AWS. In AWS, a data mesh strategy is implemented
as a collection of Amazon S3 data lakes and Amazon Redshift clusters managed across
several AWS accounts. Access to the data is shared with a centralized governance
account, which provides an AWS Glue data catalog that federates the data from each data
source and makes it available for search and consumption from an abstracted business
catalog and web portal. Figure 4-2 shows an AWS data mesh architecture.

158

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-2._** _Data Mesh Architecture on AWS_

159

Chapter 4 Data Mesh Design with Am Z

**Data Governance with DataZone**

Amazon DataZone is a comprehensive data management service designed to simplify
data discovery, governance, and sharing within organizations. DataZone provides an
out-of-console web-based experience that is friendly to business users. Users can search
for and subscribe to specific datasets or data sources, receiving updates and notifications
when changes or new data are available, ensuring they have the latest information
without manual searching. Figure 4-3 shows the core components of the DataZone
service.

**_Figure 4-3._** _Core Components of DataZone_

**Catalog Management with Amazon SageMaker Catalog**

Amazon SageMaker Catalog is built on top of Amazon DataZone and extends its
capabilities specifically for machine learning workflows. SageMaker Catalog offers
discovery and access to both data and AI models through semantic search with
generative AI-created metadata and natural language search through Amazon Q
Developer. It provides seamless integration with the SageMaker platform and workflows,
specifically focusing on the needs of ML engineers, data scientists, and analysts who
require governed access to data and models for their machine learning projects.

160

Chapter 4 Data Mesh Design with Am Z

**Note** A S
layer built on DataZ AI
capabilities for the S S
S S R
in S Z
chapter.

**Catalog Management with Amazon DataZone**

Manual curation of a data catalog is slow and often results in inaccurate and incomplete
metadata. By leveraging generative AI, DataZone simplifies catalog curation by
automatically generating metadata for new and existing datasets. Figure 4-4 shows the
architecture for this highly valuable feature.

**_Figure 4-4._** _Metadata Management with Generative AI in DataZone_

Recommendations can include descriptive summaries, data classifications, and
relationship mappings. It’s exactly this kind of automation using generative AI that
enables large enterprises to manage metadata at scale.

161

Chapter 4 Data Mesh Design with Am Z

**Publishing and Subscription Management**

DataZone allows data owners to publish datasets to a centralized data catalog, making
them available for discovery and access by authorized users across the organization.
Publishers can define access controls and permissions, ensuring that only authorized
users can view or use the published data, maintaining data security and compliance.
DataZone supports versioning, allowing publishers to manage updates and changes
to datasets while maintaining a history of previous versions for reference. Publishing
workflows include approval steps, ensuring that data is reviewed and validated before
becoming available to subscribers. Figure 4-5 describes how the data product model is
implemented.

**_Figure 4-5._** _Publish and Subscribe Data Product Model in DataZone_

Consumers can search for and subscribe to specific datasets or data sources,
receiving updates and notifications when changes or new data are available, ensuring
they have the latest information without manual searching.

Data lineage is the process of tracking and visualizing the flow of data from its origin
through its various stages of transformation to its final destination. It is especially critical
in regulated industries like finance, healthcare, manufacturing, telecommunications,
and the public sector. DataZone’s comprehensive data lineage features are based on
the open-source project, OpenLineage, which provides a common framework for data
lineage collection and analysis. The Amazon DataZone API is OpenLineage-compatible
and extends OpenLineage’s functionality, providing an endpoint for persisting the
output in an extensible object model. OpenLineage can integrate with Apache Spark,
Flink, Airflow, dbt, and popular SQL engines like MySQL, PostgreSQL, Amazon Redshift,
Snowflake, MS SQL, and Google BigQuery.

162

Chapter 4 Data Mesh Design with Am Z

OpenLineage captures data lineage through events, which represent specific
operations in a data pipeline, such as ingestion, transformation, or consumption. It
defines entities like datasets and tables involved in the lineage process and tracks lineage
runs, representing specific executions of data pipelines. Additionally, OpenLineage uses
form types, or facets, to provide extra metadata and context about entities and events,
enhancing the richness and descriptiveness of the lineage information. Figure 4-6 shows
how events, entities, runs, and form types of the lineage data model are related.

**_Figure 4-6._** _Amazon DataZone’s OpenLineage Data Model_

Lineage data is used to generate visualizations that illustrate how data flows from
the source through several transformations to its final state. Visualization features were
released in Amazon DataZone in 2024. Figure 4-7 shows an example of a data lineage
visualization.

**_Figure 4-7._** _Data Lineage Visualization Features in DataZone_

163

Chapter 4 Data Mesh Design with Am Z

In the context of data governance, data discoverability ensures that stakeholders can
easily access relevant, high-quality data while maintaining compliance with regulatory
requirements. Enhanced discoverability supports data democratization, which in turn
drives a data-driven culture built on transparency and accountability. By enabling
users to find and utilize data effectively, organizations can optimize operations, drive
innovation, and maintain a competitive edge. Figure 4-8 shows a sample of the catalog
search and subscribe experience for consumers.

**_Figure 4-8._** _Catalog Search and Subscribe in Amazon DataZone_

Along with these technical capabilities and features, the organization needs to be
aligned to support this strategy. In the next sections, I’ll discuss how to organize your
teams to support a data mesh strategy.

**Reorganizing for a Data Mesh Strategy**

Amazon follows an organizing principle of “two pizza teams,” or in other words, a team
that can be fed by two large (New York–style) pizzas. To move fast, teams need to be
small and nimble, stay close to the customer, make decisions fast, and innovate quickly.
Often when the two-pizza team principle is discussed, it’s in the context of supporting
a microservices architecture strategy. Each AWS service is composed of dozens or even
hundreds of microservices. The same principle could be applied to a data mesh strategy:

164

Chapter 4 Data Mesh Design with Am Z

by aligning data specialists to the business units and product teams, you are able to
establish, develop, and reinforce a data-driven culture that enables high-velocity data
innovation to flourish.

Let’s look at what this means in more detail.

**Data Domain Owners**

The first step in this process is to identify which entities of the business are the closest
to the customer or producing high-value data. From this list, you’ll identify and classify
different data domains. A data domain is a meaningful categorical grouping of the
data. This naturally includes products and functional business units like finance, HR,
marketing, sales, etc. Data producers in the data mesh context are referred to as data
domain owners. As owners of the data, they assume responsibility as the people closest
to the data. These domain owners are the primary stakeholders for the data engineer.
The graphic in Figure 4-9 denotes how data domain ownership spans the creation,
storing, and sharing of the data.

**_Figure 4-9._** _Data Ownership Role and Responsibility_

165

Chapter 4 Data Mesh Design with Am Z

**The Role of the CoE**

For large enterprises, they’ll want to maintain a center of excellence (CoE), but their
role and responsibility will change. They will instead drive policy development and
enforcement for security and auditing, manage federated governance and access, and
provide architectural guidance and best practices to the various data domains.

**Matrixed Organizational Structure**

Decentralizing the data team can be achieved with a matrixed organizational structure.
Figure 4-10 presents how an organizational structure supporting a data lake would
change to support a data mesh strategy.

**_Figure 4-10._** _Organizational Structure for Data Lake vs. Data Mesh_

This changes the engagement model in a fundamental way. Requests sent to
a centralized data team will inevitably encounter poor service over time as that
team juggles business-wide priorities and backlog. Instead, data engineers can be
embedded with the product and business teams to deliver data products based on
that team’s priorities. Formal reporting continues up through technical management,
but their “dotted line” reporting aligns their goals and performance with the business
stakeholders. This will allow data engineers to develop business domain expertise
that will add higher value over time. Inevitably, these data engineers will essentially
become agentic AI engineers as they work to connect and operationalize data to agents.
Additionally, the more senior architects can continue to be organized in the centralized

166

Chapter 4 Data Mesh Design with Am Z

data team or CoE and enforce architectural and security standards and provide guidance
on best practices for new data products. Figure 4-11 shows how the engagement model
changes with this organizational alignment.

**_Figure 4-11._** _Engagement Model for Data Lakes vs. Data Mesh_

Now that we’ve covered the organizational changes needed, let’s step through the
implementation of a data mesh on AWS with DataZone.

**Implement a Data Mesh with Amazon DataZone**

Amazon DataZone provides a unified platform to enable a data mesh approach,
empowering data producers to share their data and data consumers to discover and
access the data they need.

In this section, I’ll highlight the key steps needed to set up a data mesh with
DataZone, including

     - Account governance

     - Lake formation and identity management

167

Chapter 4 Data Mesh Design with Am Z

     - Creating and configuring the DataZone domain

     - Associate accounts with DataZone domain

     - Publishing data assets

     - Discover and consume data assets

**Note** P
given the different variations on identity and access management or use cases
is not practical for this book. R AWS
documentation, blogs, and workshops to ensure they are aware of the most current
features and guidance.

Along with changes to the organization, changes to the AWS account structure will also
be needed to mimic the organization. Early on in your AWS cloud journey, the business
may have only a few AWS accounts: the payer account, development, and production.
This is not the prescriptive guidance provided by AWS, but this reflects the reality for
many based on my experience. Attempting to manage the company’s AWS environment
in three AWS accounts encounters inefficiencies and risks. Moving to a multi-account
strategy and building out the company’s organizational structure in AWS Organizations
is essential to implementing a data mesh strategy on AWS. Figure 4-12 describes a
prototypical multi-account strategy.

168

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-12._** _Multiaccount Strategy for Data Mesh_

Refer to the AWS Organizations documentation to learn how to set up your
organization. Next, let’s take a closer look at each account type.

**DataZone Domain Account**

There will be one centralized DataZone domain account. This account will contain
the DataZone domain, the data portal, and the data catalog for all data producers in
the mesh to publish to. The resource access manager from this account will be used to
provision access between publishers and subscribers. I’ll discuss how to set this up in
more detail in later sections.

**Data Publisher Accounts**

Each team that publishes data may have or receive their own account. Each publisher
account may represent a product, a business unit, or a tenant that generates and stores
data in a data lake. DataZone is integrated with AWS Lake Formation hybrid access
mode. I’ll describe how to enable this feature in later sections.

169

Chapter 4 Data Mesh Design with Am Z

The subscriber accounts represent any consumers of the published data. It makes
sense to designate a specific account, the Analytics account, where power users can
utilize various AWS tools and services to analyze data from across the enterprise, run
experiments, and build out new data projects or products.

You’ll want to create an organization if you haven’t already and create the account
for the DataZone domain before moving on to the next section.

**Create and Configure an Amazon DataZone Domain**

We’ll first create the DataZone domain to generate a domain ID. This is a prerequisite
for future configurations, which is why I’m creating it first. You can locate the DataZone
service by searching from the console. Choosing to create a domain asks you for a
name and a description. If AWS-owned and managed encryption keys are not sufficient
for your requirements, you can choose **Customize encryption settings** and choose a
KMS key.

The **Quick setup** option is intended to support data publishing and subscribing
from the domain account. This is recommended for those starting out or experimenting.
For advanced or production implementations, you’ll avoid operationalizing data in this
account.

Once you’ve created the domain, you’ll want to choose **Enable IAM Identity Center** .
This is needed to integrate with your IdP to support Single Sign-On (SSO). SSO is the
recommended configuration, as it minimizes duplication of work and simplifies and
unifies IAM.

Under **User management**, choose the options **Enable users in IAM Identity Center**
and **Require assignments** as shown in Figure 4-13.

170

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-13._** _Configure User Management for DataZone_

The “require assignments” option will force users to be explicitly granted access to
the DataZone domain and portal.

The next task is to request association with all of the publisher accounts. The second
option, **Connect to data in other accounts** (shown in Figure 4-14), allows you to
associate the AWS accounts where the data assets reside.

171

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-14._** _Connect DataZone to Other Data Publisher Accounts_

You will need the AWS account number for each account you want to associate, but
otherwise this is a straightforward (invite/accept invite) process. Once you specify the
account IDs to associate, you can switch accounts. Navigate to the DataZone console to
view the request (see Figure 4-15).

172

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-15._** _DataZone Requests Sent from Domain Account_

Within the workflow of reviewing the request, you can choose to enable blueprints.
Blueprints (shown in Figure 4-16) are used to determine which services can be deployed
as part of a DataZone environment.

**_Figure 4-16._** _Blueprints for DataZone Environments_

For this example, I’ll choose **Data Lake** because I only have data in S3. The
next section shows that since I only enabled the Data Lake blueprint, only the
**Glue Manage Access role** is added. Luckily, DataZone creates the necessary
role and adds the permissions needed to facilitate cross-account access.

173

Chapter 4 Data Mesh Design with Am Z

Figure 4-17 shows this view from the console and highlights the role that is created
( _AmazonDataZoneGlueAccess-us-east-1-dzd_XXXXX_ ) and the managed policy that’s
attached ( _AmazonDataZoneGlueManageAccessRolePolicy_ ).

**_Figure 4-17._** _Glue Manage Access Role for DataZone in Associated Account_

By clicking **View permission details**, you can view the trust policy that’s added to
the role.

**Configure Lake Formation Hybrid Access Mode**
**for Publishers**

For each of the publisher accounts, you will need to enable hybrid access mode in Lake
Formation to allow DataZone to manage data access for data lakes in each publisher
account. Figure 4-18 shows you where in the Lake Formation console this feature resides.

174

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-18._** _Lake Formation Hybrid Access Mode—Resources and Principals_

Select all the databases and tables you want to share with DataZone. Figure 4-19
shows the Principals section, where you’ll choose the organization you created to
manage your AWS accounts.

**_Figure 4-19._** _Choosing the Organization Used for DataZone_

175

Chapter 4 Data Mesh Design with Am Z

You’ll exclude IAM users and roles from authorized principals. This allows DataZone
to manage permissions.

Now that we have DataZone and our publisher account configured, let’s look at how
data is published.

Before I dive into the details on publishing data in DataZone, it’s important to
acknowledge the high degree of loose coupling and conceptual disambiguation (read:
complexity) in how elements of this service, and specifically the data, are defined and
presented. For instance, there are data products, data sources, and data assets. There are
domains, projects, environments, and environment profiles. As you start developing with
the DataZone service, you’ll realize that this level of complexity is required to support
the more advanced configurations you’ll need as you scale. My advice is to fully acquaint
yourself with how the service defines these terms and their relation to each other. This
will go a long way to eliminating confusion down the road.

**Creating a Data Source**

From the top DataZone menu, you can create a data source. A data source in this context
is a Glue catalog or Redshift cluster in a member account in an organization. A data
source will require an environment to be associated with it. An environment enables
DataZone to connect a specific account's data catalog, crawl and collect metadata, and
provide analytics tools to query this data. Using filters, a data source will define which
database and tables will be included from the associated Glue catalog. Figure 4-20 shows
the data source definition.

176

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-20._** _Data Source Definition_

**Discovering Data Assets**

Once the data source is defined, we can execute a data source “run,” which crawls the
specified database from the data source based on the filter and discovers any entities
that meet the filter condition.

Figure 4-21 shows the results of executing a run of my data source.

177

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-21._** _Executing a Data Source Run to Discover Data Assets_

The discovered entities are referred to as “data assets.” This asset has all the
metadata from the source catalog (table and column names). This is the point where
the generative AI magic happens. For most teams, managing a data catalog or a data
dictionary manually is a nonstarter. Attempting to create and grow a data dictionary
quickly becomes unwieldy. Luckily we now have generative AI to assist us with
these tasks.

**Generating Metadata for Our Data Asset**

If I click on our data asset, which is a public dataset of building ordinance violations
released by the City of Chicago, I see a notice informing me that generative AI has
generated the business metadata content and asking me to accept or reject it. Figure 4-22
shows the AI-generated summary.

178

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-22._** _AI-Generated Metadata for the Data Asset_

This AI-generated context extends into the schema as well. Using AI, each individual
column is also enriched with high-quality descriptions of what that field represents.
Figure 4-23 shows the AI-generated responses for the schema.

179

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-23._** _AI-Generative Field-Level Descriptions_

Each time AI-generated content is introduced, a failsafe _accept_, _edit_, or _reject_ option
is presented to ensure that a human has reviewed and approved the content.

**Creating a Data Product**

Now that we have our data asset populated with the metadata generated, we can create
a new data product. Figure 4-24 shows that under the **Data** section of the top menu, we
will see the option to **Create data product** .

180

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-24._** _Creating a Data Product in DataZone_

From the create new data product screen, you’ll select **Choose assets** to identify
the data assets that comprise the data product. Figure 4-25 shows the data assets
selection screen.

181

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-25._** _Choosing Data Assets for a New Data Product_

**Publishing the Data Product**

After we’ve selected our assets, we can publish this data product to the business
catalog (see Figure 4-26), which makes it discoverable to other DataZone users in our
organization.

**_Figure 4-26._** _Publishing a Data Product_

182

Chapter 4 Data Mesh Design with Am Z

It should be noted that this type of work could be done by a data owner who is a
business user rather than an engineer. The expectation is that the datasets have already
been engineered properly and are just waiting to be collected and productized through
the DataZone platform.

Now that we have a data product to consume, let's look at the process for discovering
and subscribing to data through the DataZone platform.

**Discovering Data Products**

DataZone users can search for data products from the **Inventory data** section of the top
**Data** tab. Figure 4-27 shows the search results screen with our recently published data
product. Note that you can search by both data assets and data products. Data products
include one or more data assets.

**_Figure 4-27._** _Discovering Data Products and Assets Through Data_
_Inventory Search_

We’re not done yet. DataZone allows data owners to control who can access these
products. DataZone provides a subscription request and review model to help facilitate
sharing the data securely.

183

Chapter 4 Data Mesh Design with Am Z

**Subscribing to Data Products**

Now that we’ve found the data product we want. We will submit a request to subscribe
to this dataset. The request screen allows for the submitter to provide a business
justification for the request. Figure 4-28 shows this workflow.

**_Figure 4-28._** _Data Product Subscription Request with Business Justification_

Requesters can create any number of data _projects_ that can discover and submit
subscription requests for data products. This produces a common and well-understood
cost allocation strategy that distributes the cost of analyzing and enriching the data to
the project team rather than the data owner.

**Reviewing the Subscription Request**

On the data owner side, they will be notified when a subscription request is made.
Figure 4-29 depicts what a data owner will see when they view their subscription queue.

184

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-29._** _Viewing Subscription Requests_

Data owners are required to review and approve or deny each request. This provides
an audit trail of provisioned access between publishers and consumers. DataZone even
provides a way to approve data access with row and column filtering! This means that
one dataset can be maintained, and different views of the dataset can be distributed
to subscribers based on their classification access or needs. Figure 4-30 shows the
subscription request review screen with filtering.

185

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-30._** _Reviewing a Subscription Request_

Just this simple workflow is very powerful. Business users are fully empowered
to conduct data market transactions without technical intermediaries. The key to
publishing and consuming data products within an enterprise at scale is removing the
data engineer from the process so they can focus on higher-value activities.

**Create an Asset Filter**

If you choose to filter a data product or asset, you will be required to create an asset
filter. This can be a row filter or column filter. An example of a row filter is shown in
Figure 4-31. This functionality depends on Lake Formation.

186

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-31._** _Creating a Subscription Asset Filter in DataZone_

In your DataZone project and environment, you will have analytics tools depending on
which data sources you configured. Since we chose the Glue Managed Access blueprint
and extended a Lake Formation table to the DataZone environment, we have an Amazon
Athena environment available to us for querying and analyzing the data products for
which we have subscriptions. Figure 4-32 shows the familiar Athena query interface in
the console. This is a managed and isolated Athena environment.

187

Chapter 4 Data Mesh Design with Am Z

**_Figure 4-32._** _Athena Environment for Querying Subscribed Data Products in_
_DataZone_

That completes our tour of data mesh design and implementation with Amazon
DataZone on AWS.

In this chapter, I discussed the limitations of a centralized data lake approach,
highlighting how growing data demands can overwhelm a centralized data team. In
contrast, the data mesh strategy decentralizes data ownership and stewardship while
providing federated governance across domain-oriented data systems. This allows data
producers to move quickly and innovate within their domains while still maintaining
enterprise-wide security and governance. I identified how the organizational structure
would change to support a data mesh, such as establishing domain-oriented data
owners, matrixed data engineering resources, and the policy and advising role of the
central data team. I showed how to implement a data mesh architecture using Amazon
DataZone on AWS while highlighting its generative AI features for automating metadata
generation. This implementation guidance included planning for a multi-­account

188

Chapter 4 Data Mesh Design with Am Z

governance structure, configuring the DataZone domain, and enabling hybrid access
with AWS Lake Formation. I provided examples for creating and publishing data
products, subscribing to these data products, filtering data access, and utilizing the data
in an isolated Athena environment for analysis.

In the next chapter, we'll explore the AWS tools and generative AI techniques for big
data processing and transformation.

189

**CHAPTER 5**

## **Big Data Processing** **and Transformation** **with AWS Glue and AI** **Agents**

The core value that the data engineering practice delivers is the expertise and
competence to convert raw data into business value, whether that takes the form of a
digital product, insights, or the training data that produces ML or AI models that perform
high-value business functions.

In this chapter, I review the fundamental theories of big data processing in the
cloud and the AWS services and tools at your disposal to support and accelerate data
ingestion, profiling, and big data processing and transformation. I also present data
engineering use cases for applying generative and agentic AI to accelerate time-to-value.
I’ll be keeping the agentic architectures presented in this chapter simple to help convey
the conceptual understanding. Complex orchestration could be added to connect
the various parts of the agentic workflows. The strategies for implementing agentic
architectures are evolving rapidly. I present several architectural strategies in Chapter
12, “Building AI Agents with Bedrock AgentCore, Strands Agents, and Model Context
Protocol (MCP).”

191
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_5](https://doi.org/10.1007/979-8-8688-2199-8_5#DOI)

Chapter 5 Big Data P c d T AWS G d AI A

**Big Data Processing in the Cloud**

What makes big data processing in the cloud different from traditional data processing?
In a word: _ELASTICITY_ . The ability to provision resources on demand and then release
them as soon as they are no longer needed while paying for only what was consumed
impacts data processing in two fundamental ways.

The first is _efficiency_ . Efficiency is the ability to maximize the work performed for the
least amount of inputs. Imagine that you’re designing a system to process data. You
procure hardware with a fixed resource capacity. Upon launch, the system operates as
expected. You notice that the system is underutilized, but you’ve built in a margin of
safety for the workload based on expected demand. A large new client is unexpectedly
acquired and onboarded, and the data processing system quickly hits and exceeds the
resource capacity, causing jobs to fail. IT scrambles to procure additional hardware to
meet the new demand. Mitigating this risk means continually overprovisioning capacity.
Figure 5-1 depicts the inefficiency and risk associated with fixed capacity systems.

192

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-1._** _Inefficiency and Risk of Fixed Capacity Data Processing Systems_

The most optimal design would be to provision only the resources needed for each
execution of a workload and release those resources when they are not needed. This not
only maximizes efficiency but enables IT and the business to discover and derive a true
cost of data processing and to shift this cost to the consumer—be it internal or external.
All this is possible due to the elasticity and provisioning model that the cloud provides.

The second is _scalability_ . Elasticity in resources allows choice in how data processing
is performed, and this can greatly impact the throughput. Consider the ideal scenario
where a big data workload can be processed with _x_ resources in time _t_ . Let’s say that
the workload is ideally parallelizable and we can be split the work into 10 tasks and can
process them across a cluster with 10 _x_ the resources. This cluster processes each task

concurrently and completes the job in <sup><u>1</u></sup>

<sup><u>1</u></sup>

10 <sup>_t_</sup> <sup>for the</sup> <sup>_same_</sup> <sup>cost. Because we’re in the cloud,</sup>

you only get billed for the time the resources are consumed. As long as the workload can

193

Chapter 5 Big Data P c d T AWS G d AI A

be split and processed concurrently, there is no penalty and quite a significant benefit for
allocating _more_ resources to process the job in _less_ time. Figure 5-2 shows this theoretical
ideal visually.

**_Figure 5-2._** _Ideal Sequential vs. Concurrent Processing at Constant Cost_

This is true at the workload level, but it’s also true at the job orchestration level. If you
needed to process 10 jobs (with no dependencies), you could process them sequentially
with _x_ resources in time 10 _t_ or concurrently with 10 _x_ resources in time _t_ .

**Data Solution Development Lifecycle**

The development of data solutions evokes analogies with the software development
lifecycle; however, there are a few critical distinctions. For one, data solutions are datacentric and dependent on the data. What does this mean in practice? Well, it means that
the concepts of having separate environments like dev, test, and prod are not applicable
to data. This is not always obvious to technology leaders coming from a software
development background. I’ve seen data teams and even sophisticated CTOs struggle

194

Chapter 5 Big Data P c d T AWS G d AI A

with how to think about data used in solution development. One company I engaged
with years ago was convinced that they needed to replicate their entire data lake as a dev
environment so users could develop data solutions. This would have added significant
cost and no business value! Pursuing such a strategy would have cost them their job.
Understanding that company data is production data from when it is created or ingested
to when it is published and consumed is key to understanding how data differs from
software. This data may be refined through a phased process, but it is still production
data. Once you accept this fact, you’ll realize that using production data for solution
development is a data governance and access management problem, not an SDLC
process problem. The solution developers are consumers of a data product, like any
other consumer. Imagine that a data scientist is tasked with building a probabilistic ML
model. Would they be expected to perform data cleansing, feature engineering, model
training, and testing on dummy data? I hope not because that model will have no value,
and all that work would be wasted.

The second distinction we can make about data solutions is that they incorporate
a process flow that can be represented as a directed graph. This process flow can
include complex dependencies derived from higher-level processing like aggregations,
unification of multiple data sources, or machine learning and AI model training.

Development spans several phases, which I’ll discuss briefly. At AWS, solution
architects learn to work backwards from the business challenge to properly architect
data solutions. Once the business case is defined and the solution is architected, we
identify the relevant source data needed to support the solution. This could include
internal company data and external third party data. For new third party data sources,
data engineers will acquire samples of the data so it can be analyzed and profiled. The
learnings from this analysis are incorporated into the ingestion and data cleansing
stages. Higher level processing may be needed. I’ve illustrated these general phases in
Figure 5-3.

**_Figure 5-3._** _Data Solution Development Lifecycle_

195

Chapter 5 Big Data P c d T AWS G d AI A

In this chapter, I focus on the “Identify and Acquire,” “Profile and Analyze,” and
“Develop and Test” phases of this lifecycle. I’ll explore how generative and agentic AI can
assist in each of these phases. I cover orchestration and observability in the next chapter.
To demonstrate the phases that are in scope for this chapter, we’ll be using a general data
engineering use case. This is a very common business challenge I’ve heard repeatedly
over many years as a data architect, then later as a solutions architect at AWS.

Use Case:

You work for a company that enriches customer data with your
first- and third-party data to deliver valuable insights. Each time
your company acquires a new customer, the data team needs
to integrate and process a data feed from this new customer.
It currently takes weeks of a data engineer’s effort to manually
integrate and process new customer data. Due to the popularity
of this insights product, the company is acquiring customers
faster than the data team has the capacity to serve. This has led
to a backlog of customers waiting to onboard, delaying revenue
realization amid rising opportunity costs. As customers grow
impatient with this lengthy onboarding process, customer
satisfaction (CSAT) scores are impacted as the risk of customer
churn increases. The business has tasked you with developing a
solution that reduces the time it takes to onboard new customers
that can scale to meet customer demand.

I’ll start with the most common data lake ingestion methods.

**Data Lake Ingestion**

As I mentioned previously in Chapter 3, “Data Lake Design with Apache Iceberg and S3
Tables,” data lakes should strictly enforce an extract, load, transform (ELT) policy. This
means that our ingestion processes should be as dumb as possible and simply copy the
data with 100% fidelity from the source. The reason for this is because data solutions
development, like all solutions development, is susceptible to error. The error could
be introduced by the developer or the data source provider. If an error is discovered,
a correction can be made and the affected data can be reprocessed only because the
original source data exists. If the data had been transformed with erroneous logic as

196

Chapter 5 Big Data P c d T AWS G d AI A

part of the ingestion process, it could never be recovered—except from the source—and
that option may no longer be available. Like every “rule,” business requirements could
require a valid exception; however, to date I haven’t encountered one. While most data
ingestion use cases appear to have limited opportunities for leveraging generative and
agentic AI, some opportunities do exist. I’ll explore them in this section.

**Note** For streaming ingestion, see Chapter 9, “S R Time Data
P G AI E

**Change Data Capture**

One of the biggest data lake challenges technology leaders face is ingesting the most
up-to-date data from operational systems. The once-a-day ingestion of data from these
systems cannot deliver current reporting and insights. To deliver up-to-date results,
you need to have a process that initially loads all the existing data from the operational
system to the data lake but then also continually syncs any changes to the data. This
strategy is called change data capture (CDC). There are plenty of CDC tools on the
market, including open-source projects like Debezium. In AWS, CDC into an S3 data lake
is accomplished with AWS Database Migration Services.

**CDC with AWS Database Migration Service**

AWS Database Migration Service (AWS DMS) allows you to easily migrate data to and
from most commercial and open-source databases. This includes migrations between
the same or different databases and synchronizing data. AWS DMS also supports
creating synchronization links between sources and targets to replicate deltas as a
change data capture feature.

**Caution** T
so it is best to refer to the most current AWS MS
migration project.

197

Chapter 5 Big Data P c d T AWS G d AI A

Data engineers choose from a list of supported sources and targets, which includes
Amazon S3. This means that we can implement a CDC process using AWS DMS to
continuously replicate the current state of our operational data into an S3 data lake.
Figure 5-4 shows the architecture for how AWS DMS implements CDC.

**_Figure 5-4._** _CDC with AWS DMS_

You’ll notice from the diagram that the replication task is performed by a compute
instance that runs continuously. This means that you will incur charges continuously
while replication is active. To set this up in AWS DMS, there are a few steps you’ll need
to take. Due to space limitations, this will not be a step-by-step guide, so consult the
documentation and AWS blog content for more details.

1. Create a replication instance

This replication instance will provide the compute to power the
migration task and ongoing replication. You will choose the size
of the instance. Figure 5-5 shows the dms.t3.medium replication
instance I created in the VPC where I’ve provisioned my Amazon
Aurora PostgreSQL cluster.

**_Figure 5-5._** _AWS DMS Replication Instance_

198

Chapter 5 Big Data P c d T AWS G d AI A

**Note** A PostgreS L MS
3.5.3 and above.

I now need to create two endpoints, one for the source and one for
the target.

2. Create source endpoint

When creating the endpoint in DMS, I indicate that it is a
**Source endpoint**, and the source engine is **Amazon Aurora**
**PostgreSQL** . This is shown in Figure 5-6.

**_Figure 5-6._** _Creating the Source Endpoint in AWS DMS_

199

Chapter 5 Big Data P c d T AWS G d AI A

Further down, I provide the database secrets either from AWS
Secrets Manager or directly in the console. I have the option
to test the connection—this creates the endpoint and tests the
connection from the replication instance to the database.

3. Create target endpoint

Before creating the target endpoint, I will need to create an AWS
IAM service role and policy to give DMS access to write to S3. With
RDS we could use database credentials to provide access, but with
S3 that is not an option. This service role will specify a trust policy
that allows DMS to assume the role.

The IAM policy that I’ll attach to this service role will look like this:

{

200

Chapter 5 Big Data P c d T AWS G d AI A

}

I create the role and copy the ARN, which I’ll need when creating
the target endpoint. When I choose Amazon S3 as the **Target**
**engine**, additional options appear (see Figure 5-7) that allow me
to enter the service role ARN, the S3 bucket name, and the folder
where DMS will write the data collected from the source database.

**_Figure 5-7._** _Creating an S3 Target Endpoint in AWS DMS_

201

Chapter 5 Big Data P c d T AWS G d AI A

Just like the source endpoint, I can test access to the S3 location
from the replication instance. After completing the test
successfully, I can create the endpoint and move on to create the
migration task.

4. Create AWS DMS migration task

Creating the migration task brings all the prior steps together.
Figure 5-8 shows how to create the migration task for CDC.

**_Figure 5-8._** _Creating a Database Migration Task in AWS DMS_

I select the replication instance I created, the RDS endpoint for
the source, and the S3 endpoint for the target. I then choose
**Migrate and replicate** for the **Migration type** and **Indefinitely**
as the replication period. Additional configuration allows you to
choose filters for databases and tables to include or exclude in the
migration.

202

Chapter 5 Big Data P c d T AWS G d AI A

Before running the migration task, I need to perform a
**Premigration assessment** . This assessment tests the source
database to validate that it is configured to support migration and
replication. Figure 5-9 shows the results of the initial assessment,
indicating that two tests failed and that I’ll need to change those
configurations before the migration task is executed.

**_Figure 5-9._** _Premigration Assessment for Database Migration Task_

Each database will have different requirements and
configurations, so I will not go through the remediation here.
However, the assessment report details will provide guidance with
references to documentation.

203

Chapter 5 Big Data P c d T AWS G d AI A

Ingesting third-party or first-party data from APIs into the data lake is usually needed
in most organizations. There are few scenarios where I’d advise using AWS Lambda
functions for data ingestion; however, API ingestion is one. The request has to be
properly structured according to the documentation. The request will need to package
valid credentials if the endpoint requires authentication. The response will be
semistructured in JSON, which will need to be unpacked and flattened if we intend to
aggregate key metrics. The good news is that many of these tasks can be accelerated
using generative and agentic AI.

**API Ingestion with AWS Lambda**

Lambda functions are inexpensive, serverless, and can easily scale to process the
requests in parallel. One risk with using AWS Lambda for data ingestion is when the
data size exceeds the allocated memory capacity, causing failures. However, with API
ingestion, the expectation is that the JSON payload will be known in advance and
Lambda resources can be provisioned accordingly to avoid out-of-memory errors. We
can imagine a scenario where we have many APIs we’d like to ingest data from. How
would we design and architect a solution that can scale to a large number of tasks
and be able to execute each in parallel to maximize the efficiency of this ingestion
process? Figure 5-10 shows solution architecture that supports a large number of API
ingestion tasks.

**_Figure 5-10._** _API Ingestion using AWS Lambda_

204

Chapter 5 Big Data P c d T AWS G d AI A

A scheduled event in Amazon EventBridge triggers a Lambda Function that retrieves
the list of API tasks from Amazon DynamoDB and loads them into Amazon SQS. Each
SQS task spawns a Lambda Function that makes the API request and saves the response
as a JSON file in the S3 landing zone.

APIs used in applications have to return a response quickly (usually under 10
seconds) to provide a good customer experience. In contrast, data ingestion via APIs
can run for much longer because it doesn’t have this risk. Up until June 2024, AWS API
Gateway enforced a 29-second API response timeout. Today, this limit can be increased
above 29 seconds. Lambda functions can run for as long as 15 minutes. The maximum
payload for API Gateway is 10MB. The amount of memory Lambda Functions are
allocated is configurable up to 10GB.

From the example above, here is an example of the Lambda Function triggered from
an Amazon SQS queue. The body of the SQS message will contain the parameters that
will be passed to the Lambda Function.

{

}

**Note** T To prepare this L
production, additional logging and exception handling will be needed. T L
F S
M S

Here’s what a simplified Lambda Function servicing the API tasks would look like:

import json
import boto3
import os

205

Chapter 5 Big Data P c d T AWS G d AI A

import requests
from datetime import datetime

def lambda_handler(event, context):

206

Chapter 5 Big Data P c d T AWS G d AI A

This may not fit every use case, as the number of API integrations may not warrant it.
However, once this solution is built, supporting additional API integrations is as easy as
adding tasks to a DynamoDB table. Development of these API integrations and Lambda
functions can be accelerated significantly with the help of AI. I’ll leave it for the reader to
explore the development of an “API integration agent” that accepts API documentation
and the desired dataset as input to produce the full code of the function.

**SFTP Server with AWS Transfer Family**

SFTP stands for secure shell (SSH) file transfer protocol, a network protocol used for
secure data transfer over the internet. The protocol supports the full security and
authentication functionality of SSH. Having customers upload data files to an SFTP site
is operationally more intensive than other methods, but teams may find themselves
needing to support it. Luckily, AWS Transfer Family supports several transfer protocols
as managed services. Figure 5-11 shows the server creation screen in the console.

207

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-11._** _Create SFTP Server in AWS Transfer Family_

**Caution** FTP
information, including usernames and passwords, in plaintext.

AWS Transfer Family enables you to connect your managed SFTP server to a
managed AWS storage service, including Amazon S3 or Amazon EFS. You can refer to the
documentation and the step-by-step setup guide. The service provides a file processing
feature called **Managed workflows** . These multi-step workflows (see Figure 5-12)
provide native processing capabilities that can be applied to full and partial file uploads.

208

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-12._** _Managed Workflows in AWS Transfer Family_

These workflows provide event-driven functionality at the SFTP server level, before it
arrives downstream in AWS storage services. Using workflows to decrypt files using PGP
or tagging files with tenant IDs makes sense here.

There is also a **Custom file-processing step** that invokes a Lambda Function to
process the file, but I would also require that an original version of the data be retained
in durable storage. In this example, I choose S3.

With the SFTP server created, I can now add users. When I add a user, I’m asked to
apply AWS IAM roles and policies. You want to be careful here. The goal is to minimize
the amount of overhead while implementing the principle of least privilege. In this case,
we can create one IAM role with a trust policy authorizing the AWS Transfer Service to
assume the role. The configuration screen offers me the option to apply a session policy
to the user. This is what we want. Figure 5-13 shows these options.

209

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-13._** _Restricting User Access with Dynamic Session Policy_

The session policy uses dynamic variables scoped to the Transfer service, which I
show below. The **Restricted** option restricts user access to just their directory. Here is
the dynamically generated session policy viewable from the **View** button.

{

210

Chapter 5 Big Data P c d T AWS G d AI A

}

This approach minimizes the operational overhead of managing access for many
users while ensuring tenant isolation on the same SFTP server.

The files that are uploaded to the SFTP server are immediately available in S3. The
PutObject event is captured by Amazon EventBridge and can be used to trigger data
pipelines for processing those files. Figure 5-14 describes the solution.

211

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-14._** _AWS Transfer Family SFTP Event-Driven Data Processing_

**Data Profiling and Analysis**

The first step in onboarding new datasets is to perform data profiling and analysis.
Profiling data means learning all about the data to discover opportunities or risks when
converting it into the published version. When profiling data, there are a number of
features to learn more about. Let’s review a few of them.

Understanding the data structure includes the schema of the data and any metadata
that could assist in the creation of a data dictionary, like the data type of each column.
Basic stats on the dataset, like how big (number of rows) and how wide (number of
columns) it is, can assist data engineers with allocating the proper amount of resources
for processing the data.

212

Chapter 5 Big Data P c d T AWS G d AI A

Assessing the quality of the data includes detecting missing values, duplicate rows,
mixed date formats, and invalid values.

Descriptive statistics includes summary statistics like mean, median, mode, standard
deviation, and quartiles for numerical columns. It also includes distributions of the data,
which can be visualized with histograms or box plots. For categorical columns, we can
report the frequency count of each categorical value.

**Relationships Between Variables**

Profiling can also reveal relationships between variables in a dataset by calculating
correlation coefficients. The strength of these correlations can be depicted visually
in a scatter plot. For categorical values, we can create cross tabulations to explore
relationships.

Data integrity analysis can include attempts to identify a unique primary key and
relationships (like foreign keys) between multiple datasets.

Luckily, AWS provides a purpose-built solution called AWS Glue DataBrew to
accelerate data profiling and analysis.

**Profiling and Analysis with Glue DataBrew and AI Agents**

In this next section, I demonstrate the profiling features of AWS Glue DataBrew. I will
then show how to automate these tasks at scale for any new datasets. I’ll then show how
to enhance data profiling reports with generative AI to then be consumed and acted
upon by AI agents.

Glue DataBrew provides a slick user interface via the AWS console (see Figure 5-15),
which is a great option for folks looking for a visual designer.

213

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-15._** _AWS Glue DataBrew Visual Designer_

As with all other services, AWS offers SDKs, APIs, and CLIs for their services
so engineers can access and control these features programmatically, allowing for
automation.

Step 1: Automate and improve the profiling of new datasets.
Not only can we automate the profiling of new datasets with AWS Glue DataBrew,
but we can use an AI agent trained as a “data analyst agent” to help us interpret this
profiling report and derive additional insights. You might ask: Why should we use agents
instead of the LLM directly? We use agents because it provides an extremely valuable
abstraction layer. Agents provide additional functionality but also abstract away the
choice of LLM, tools, data sources, or other configurations. This allows you to change
or augment how the agent is implemented without breaking the application code that
invokes it. Figure 5-16 shows what a potential agent-assisted solution architecture might
look like.

214

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-16._** _New Dataset Profiling by Data Profiling Agent_

This architecture mixes deterministic and probabilistic approaches. It depicts
a special area of our Landing Zone ingestion stage of our data lake. When files are
loaded into this area, an S3 PUT event is captured by EventBridge and invokes our Data
Profiling Agent:

1. The agent utilizes its data_profiling_tool via MCP that creates and

executes an AWS Glue DataBrew profiling job on the dataset.

2. Upon completion of the profiling job, the agent analyzes the

DataBrew profiling report and performs a deeper analysis to
generate insights on the dataset. It optimizes the output structure
to make it easier for the next agent—the Data Architect Agent—to
design the schema for the dataset.

**Creating an AWS Glue DataBrew Profiling Job**

Let’s look at the key parts of the AWS Glue API Boto3 code for these steps. We can
implement this code in AWS Lambdas and use Bedrock AgentCore Gateway to “MCPify”
it for agentic integration. I discuss the mechanics of implementing agents in Chapter 12,

215

Chapter 5 Big Data P c d T AWS G d AI A

“Building AI Agents with Bedrock AgentCore, Strands Agents, and Model Context Protocol
(MCP).” Due to space constraints, I’ll demonstrate the core logic. See the GitHub repo for a
more complete solution. First, I’ll create a DataBrew client.

databrew = boto3.client('databrew')

In order to generate a DataBrew profiling report, we first need to create a DataBrew
dataset. This is effectively an alias for the S3 location of the dataset.

databrew.create_dataset(

)

Next, we create a DataBrew profiling job. Note that this just defines the job; it does
not execute it. We’ll do that in the next step. For the mode, you’ll want to specify “FULL_
DATASET” to ensure the entire dataset is profiled and not just a sample. You’ll also need
to list the column statistics you want to include. The example below provides a common
configuration.

response = client.create_profile_job(

216

Chapter 5 Big Data P c d T AWS G d AI A

)

217

Chapter 5 Big Data P c d T AWS G d AI A

Finally, we start the asynchronous profiling job.

databrew.start_job_run(

)

The profiling report I created using DataBrew is 8,290 lines of JSON! DataBrew
provides a rich set of statistical analysis reporting and visualizations in the console for an
eyes-on-glass experience (see Figure 5-17).

**_Figure 5-17._** _Examples of DataBrew Data Profiling Visualizations_

**Data Profiling Analysis with Agentic AI**

What if we wanted to process and analyze this profiling report without a human? Luckily,
the reasoning capabilities of agentic AI models are well suited for the task.

Here is a set of instructions I used for my agent.

Data Profiling Analysis Instructions:
1. Read the data profiling report and extract table name and column
definitions as structured JSON.
2. For each column, extract key data statistics and data quality insights
like null percentages, value patterns, and statistical outliers.
3. Suggest primary key candidates by identifying unique, non-null columns.
4. Recommend partitioning and indexing strategies based on cardinality and
value distribution.
5. Assess data sensitivity and domain classification based on column names
and content patterns.

218

Chapter 5 Big Data P c d T AWS G d AI A

Output: should be in a structured JSON format and will contain the schema,
data analysis, DDL recommendations, and catalog metadata.

The results look promising. We can get concise analytical value for very little effort.
It’s as if we had a skilled data analyst study the reports in DataBrew and communicate
these conclusions. Below, I list the most interesting part of the agent’s response.

Partition candidates: DATE columns (HEARING DATE, LAST MODIFIED DATE,
VIOLATION DATE)
Index candidates: High-cardinality strings (DOCKET NUMBER, NOV NUMBER,
ADDRESS)

The response also includes structured JSON of the full schema and the column
statistics extracted from the profiling report (not shown for brevity).

From a data modeling perspective, I know which column will serve as the primary
key. I know which columns to potentially partition. I also learn which columns might
include PII. Essentially, everything a junior data engineer might do manually when
onboarding a new dataset.

Up until this point, we have had a fully automated, machine-based process for
profiling and analyzing never-before-seen datasets for onboarding. Use of generative
AI to analyze our profiling report gives a data engineer or data scientist a significant
jumpstart for onboarding datasets. It provides data practitioners with clear direction
on where to focus their time along with a list of tasks to be performed. As agentic
architectures mature and become more sophisticated and error-proof, this task list could
be passed to autonomous agents for processing.

Let’s look at another way to use generative AI to analyze a DataBrew profiling report.

**Data Profiling Q&A with Amazon Q for Business**

We can also use generative AI interactively to interrogate the report with natural
language questions. This saves time. Instead of being forced to read the whole report, I
can ask it just the questions I care about based on my specific use case. Amazon Q for
Business offers an easy way to operationalize our profiling report for interrogation by the

219

Chapter 5 Big Data P c d T AWS G d AI A

data team. I can ingest our profiling report in minutes as part of a managed RAG solution
and ask the report questions through a chatbot interface. Figure 5-18 shows one of the Q
applications setup screens where data is connected via S3.

**_Figure 5-18._** _Amazon Q for Business S3 Connector_

By choosing the S3 location where my data profiling report lives, Q for Business will
ingest the report and prepare it for semantic search by vectorizing the content. When I
ask the chatbot a question, the service searches and retrieves the relevant parts of the
report needed to answer my question, sends it to the model, and returns the answer. To
ensure it is sourcing the content from the right file, it lists the data sources queried as
part of the response. Figure 5-19 shows what this interface looks like.

220

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-19._** _Amazon Q for Business Chatbot for Data Profiling Q&A_

This allows us to free the report from the DataBrew console and provide a natural
language interface to the content. Imagine that at scale, a data profiling chatbot could be
built that ingests the reports for all the datasets. The data team at any time could ask the
chatbot questions about any dataset.

**ETL Design and Development**

Now that we’ve profiled our dataset, I’ll demonstrate how to develop big data processing
and transformation pipelines using AWS Glue. For all our examples, I’ll be choosing to
use Apache Spark, and I’ll write Glue jobs in PySpark. I’ll discuss briefly why I choose
Apache Spark and PySpark for large batch data processing. Spark is an open-source
distributed big data processing engine. It handles the distribution of the workload
across a cluster of nodes, allowing for concurrent processing at scale. Spark enjoys wide
adoption. Similarly, Python is open source and has achieved mass adoption in several

221

Chapter 5 Big Data P c d T AWS G d AI A

application domains. In the realm of machine learning and generative AI, PyTorch is the
clear favorite over similar frameworks like TensorFlow. Greater adoption means more
community support for troubleshooting issues, a larger pool of talent for recruiting, and
a higher-velocity pipeline of bug fixes and features. Being deliberate about choosing a
tool stack realizes a significant return. Forcing consolidation of the tech stack avoids
tool sprawl, which reduces operational overhead and tech debt and increases delivery
velocity.

**Visual ETL Design Tools**

Visual ETL design tools make data engineering more accessible to analytics power
users or data scientists who don’t write code. Business users can prototype solutions,
implementing and transferring high-value domain expertise that technologists might
lack, which can then be handed off and productionalized by engineers. Having business
users utilize visual design tools in this way augments or supplements more traditional
requirements gathering sessions.

There are trade-offs of choosing visual ETL design tools that teams need to keep
in mind:

1. Visual design tools are intended for humans. As generative AI

matures, more and more of the data development workflow will
be automated by AI agents. Building data solutions in executable
code provides current-day generative AI models and future
AI agents high-value artifacts for them to consume and use to
understand and modify solutions.

2. Visual design tools trap and lock the business logic in the visual

artifacts. When maintaining or migrating these artifacts, a
developer needs to visually inspect—with “eyes on glass”—the
process flow in the tool to understand what it’s doing. This is a
serious risk if you want to quickly adapt and migrate to new and
emerging tools and technologies. It should be noted that some
visual design tools are capable of exporting or generating artifacts
that can be consumed and leveraged by generative AI.

222

Chapter 5 Big Data P c d T AWS G d AI A

3. Visual design tools can complicate source control management

(SCM) and configuration management strategies because the
primary artifacts are not executable code. Artifacts from these
tools could be project files or exported descriptor files that
describe the process flow or transformations. If code is exported,
it is autogenerated by the tool and cannot be modified because
changes are not repatriated into the master. Requiring manual
steps to export and track changes just adds risk to it not being
performed consistently. It also complicates the promotion of
changes through environments.

For these reasons, it is recommended that data engineering shops adopt code-based
data pipeline development exclusively. However, I’ll briefly discuss the AWS tooling for
visual ETL design, as it can come in handy for business user prototyping.

**AWS Glue DataBrew**

AWS Glue DataBrew is visual data preparation that reduces the complexity for cleaning
and normalizing data. Users can choose from over 250 prebuilt transformations that
they can apply to their data, offering repeatability and lineage tracking through a feature
called “Recipes.” Recipes describe the specific transformations and the order in which
they are performed on a dataset. Figure 5-20 is a sample of the AWS Glue DataBrew
interface with the recipe displayed on the right.

223

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-20._** _Example DataBrew Transformation_

Behind the scenes, transformations are executed as Spark functions, so the data
processing scales with the size of your data. Recipes are defined as JSON documents,
which mitigates the risk I described in my second point from the previous section.
The benefit is that you can use generative AI to convert DataBrew recipes into lines of
imperative code of your choice.

**AWS Glue Studio**

AWS Glue Studio is a visual ETL designer that enables users to build complex DAGbased data transformation workflows. This visual ETL design tool (see Figure 5-21) is less
friendly to business users and more suited to engineers.

224

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-21._** _AWS Glue Studio Interface for Visual ETL Development_

Similar to recipes, Glue’s visual designer provides an expansive toolkit of
transformations. Figure 5-22 shows only a small sample.

225

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-22._** _Glue Visual ETL Transformations_

The visual designer creates working Glue code as the design is constructed.
While this produces working code, it’s generated one way from the visual design. For
developers looking to stick their fingers in the code, development notebooks in Amazon
SageMaker Unified Studio are a better option, which I talk about in the next section.
The workflow is represented in Glue DAGs that are described in JSON, which can be
imported and exported.

Now that we’ve explored these visual ETL designer options, let’s shift gears to codebased development.

226

Chapter 5 Big Data P c d T AWS G d AI A

**Amazon SageMaker Unified Studio**

AWS brought together several disparate features and functions for ML and analytics into
one unified platform and called it the Amazon SageMaker Unified Studio. By providing
pre-built algorithms, automated model tuning, and seamless integration with AWS’s
broader data and analytics ecosystem, SageMaker Unified Studio accelerates time-tovalue for AI and ML initiatives while maintaining enterprise-grade security, governance,
and scalability. For data and AI developers, this platform will be an important part of the
strategy. This service is accessible from the Amazon SageMaker AI console. You first have
to create a domain (see Figure 5-23).

**_Figure 5-23._** _SageMaker Domain Setup in SageMaker AI_

Let’s take a look at the major features, starting with notebook-based data pipeline
development.

227

Chapter 5 Big Data P c d T AWS G d AI A

**Notebook-Based Development with Glue**
**Interactive Sessions**

Amazon SageMaker Unified Studio’s integrated development environment (IDE)
provides an immersive, browser-based workspace that consolidates all development
activities into a single interface. The IDE features customizable notebooks with support
for multiple kernels (Python, R, Scala), enabling data scientists to seamlessly transition
between exploratory data analysis, feature engineering, and model development without
context switching. The IDE supports these different capabilities as “applications.” The
JupyterLab application is where we can run our notebook environment for data solution
development.

Every data project starts with a prototype and iterative development and testing.
Notebooks provide a great way to incrementally and iteratively test new data processing
code. Notebooks persist variables in a session and structure the code into “cells” that can
be run independently. These notebooks are essentially document versions of a ReadEval-­Print-Loop (REPL) command line. Developing in notebooks was widely practiced
by data scientists for many years before finding its way into data engineering. As data
got bigger, large Hadoop clusters appeared on-prem to help power complex big data
queries and machine learning workflows. Data scientists were able to write code in their
Jupyter Notebook environments and connect remotely over the network to submit jobs
to Hadoop, where jobs were processed across a cluster with Spark. As big data workloads
moved to the cloud, development tools went with them.

To create a notebook environment, open the studio for the domain you created
and choose **Create a JupyterLab space** . You’ll choose the instance size, storage, and
filesystem (optional) and initiate the space by clicking **Run space** . Once the space is
initialized, it’ll allow you to open the environment (see Figure 5-24).

**_Figure 5-24._** _List of JupyterLab Spaces in SageMaker Unified Studio_

228

Chapter 5 Big Data P c d T AWS G d AI A

The most important distinction to make is the difference between a notebook
instance and Spark cluster resources. Just creating a JupyterLab space does not provision
and make available Spark cluster resources. To support big data operations using Spark,
we must leverage AWS Glue and its Glue interactive sessions capability. Figure 5-25
shows the service integration between our JupyterLab space and AWS Glue. The
architecture shows how the SageMaker Unified Studio IDE launches the JupyterLab
space. From the notebook hosted in our JupyterLab environment, we initialize the Glue
interactive session and Spark cluster creation. Once it’s created and connected, Spark
jobs are submitted directly to the Spark cluster for processing.

**_Figure 5-25._** _JupyterLab Space PySpark Notebook with Glue Interactive Sessions_
_Integration_

We first need to change the kernel of our notebook to “Glue PySpark.” This can be
found in the upper right corner of our notebook.

We can initiate Glue Interactive Sessions and our Spark cluster by running a few
system commands using the “%” character from our notebook. Using the following
commands, we can set the Glue version to 3.0, the number of workers to 50, and the
worker type to G.1X and add the Sagemaker Python module.

229

Chapter 5 Big Data P c d T AWS G d AI A

%session_id_prefix my_glue_notebook
%glue_version 5.1
%number_of_workers 50
%worker_type G.1X
%idle_timeout 500
%additional_python_modules sagemaker

You will receive confirmation that the settings have been applied. However, we still
need to initialize the session. We can do that by executing a simple print statement for
the Spark version.

print(spark.version)

This statement will attempt to create a Glue session for the kernel. The response
should look something like this:

Trying to create a Glue session for the kernel.
Session Type: etl
Worker Type: G.1X
Number of Workers: 50
Idle Timeout: 500
Session ID: my_glue_notebook-dfX-XXX-[..]
Applying the following default arguments:
--glue_kernel_version 1.0.9
--enable-glue-datacatalog true
--additional-python-modules sagemaker
Waiting for session my_glue_notebook-dfX-XXX-[..] to get into ready
status...

It’s important to note that the glue interactive sessions project version <sup>1</sup> is not related
to the Glue version. Once the glue interactive session is active, you’ll be connected to a
Spark cluster and will be able to execute Spark-based commands on large datasets.

As you work in these notebooks, you’ll notice that AI assistance provides seamless
code completion for the supported languages and AWS APIs. A built-in AI agent
generates code, SQL, and implementation guides from natural language prompts.

1 Amazon Web Services. “aws-glue-sessions.” Python Package Index, 2024, pypi.org/project/
aws-glue-sessions/.

230

Chapter 5 Big Data P c d T AWS G d AI A

Another key feature of SageMaker Unified Studio is the SageMaker Catalog, built on
Amazon DataZone, which simplifies the discovery, governance, and collaboration
for data and AI across your structured and unstructured data, AI models, business
intelligence dashboards, and applications. The federated catalog and SQL editor allows
you to query across data lakes, data warehouses, databases, and applications.

SageMaker Unified Studio integrates all the capabilities of SageMaker AI, allowing you to
streamline your entire ML workflow. SageMaker AI’s end-to-end managed environment
provides purpose-built capabilities for every stage of model development—data prep,
training, governance, operations, deployment, testing, automation, and performance
tracking. The model section provides quick access to SageMaker Jumpstart base models
for customization. There’s also a SageMaker model customization agent (in preview at
the time of writing) that helps you customize models.

**AI-Assisted ETL Development**

As I mentioned previously, generative and agentic AI has significant promise in helping
to automate or accelerate data solutions development. Despite accuracy over 90%, it
carries risks. Software and data engineering is a craft that is developed over time and
requires ongoing supervision from highly specialized experts. Using coding copilots
like Kiro and Kiro CLI, data engineers can develop highly sophisticated solutions using
natural language. They can more easily discover security risks or vulnerabilities in
their code, including guidance on how to mitigate them. Amazon is moving quickly to
enhance their tooling with generative AI. Let’s take a look at how AI will perform for a
common set of data tasks.

**Data Engineering with Kiro**

To demonstrate the capabilities of AWS’s copilot, Kiro, I put it to the test on a common
data engineering task: onboarding a new dataset and building out a data pipeline
that promotes the dataset through the medallion architecture (bronze, silver, and

231

Chapter 5 Big Data P c d T AWS G d AI A

gold). Using spec-driven development, I provide Kiro with general instructions and
then iterate on the spec. When the spec is acceptable, it moves to the design and
implementation phases.

Here is my initial prompt:

Create a JupyterLab notebook connected to Spark cluster using
Glue interactive sessions. Process a CSV dataset from landing
zone (bronze stage) to GZIP-compressed text-based CSV in raw
(bronze stage) to partitioned tables (silver stage) to fully validated
with Deequ data quality checks in (gold stage) published for the
dataset using a 10-row sample of the dataset. Use the AWSmanaged iceberg service, S3 Tables, as the data storage choice for
the lakehouse strategy.

With this basic prompt, I’m able to generate a very credible first pass that can bring
my never-before-seen dataset from raw to published in my data lake. Kiro creates a
requirement document, a design document, and an implementation task list. Due
to space constraints I’ll only be able to provide excerpts. Refer to the GitHub repo for
the full design documents and resulting notebook. Let’s look at the creation of the
silver stage.

### Requirement 3: Silver Stage

**User Story:** As a data engineer, I want to transform raw CSV data into
a managed Iceberg table using S3 Tables, so that I have ACID transactions,
schema evolution, and time travel capabilities.

#### Acceptance Criteria

1. THE Pipeline SHALL create an S3 Tables namespace for the chicago
violations lakehouse
2. THE Pipeline SHALL write the bronze DataFrame to an Iceberg table in the
silver stage
3. THE Pipeline SHALL partition the Iceberg table by WARD column for
efficient querying
4. THE Pipeline SHALL configure the Iceberg table with appropriate table
properties for S3 Tables

232

Chapter 5 Big Data P c d T AWS G d AI A

5. WHEN duplicate records exist, THE Pipeline SHALL preserve all records in
silver stage
6. THE Pipeline SHALL use the Iceberg catalog integration with AWS Glue
7. WHEN the silver table already exists, THE Pipeline SHALL append or
overwrite based on configuration

In the design stage, we can definitely see the strategy taking shape. The decisions
being depicted in the response demonstrate advanced data engineering reasoning.

## Overview

This design specifies a JupyterLab notebook that implements a medallion
architecture data pipeline for Chicago ordinance violations data. The
pipeline uses AWS Glue interactive sessions to provide managed Spark
compute, processes data through three stages (bronze → silver → gold),
and leverages S3 Tables with Apache Iceberg for lakehouse storage with ACID
guarantees.

The pipeline architecture follows these principles:

- **Separation of concerns**: Each stage has a distinct purpose (ingestion,
transformation, validation)

- **Incremental processing**: Data flows through stages with clear
checkpoints

- **Data quality first**: Deequ validation ensures only quality data
reaches gold stage

- **Cloud-native**: Leverages AWS managed services (Glue, S3 Tables) for
scalability

And finally, in the implementation phase, Kiro created a set of 10 major tasks to
complete. Some tasks, like unit testing, are optional and can be set to be required if
I choose. I’ll provide the major list of tasks and drill down into the details for one to
demonstrate the complexity and sophistication.

233

Chapter 5 Big Data P c d T AWS G d AI A

1. Create notebook structure and Glue session configuration

2. Implement bronze stage—CSV ingestion

2.1 Create bronze stage code cell

2.2 Write unit tests for CSV reading

2.3 Write a property test for column preservation

3. Configure S3 Tables and Iceberg catalog

4. Implement silver stage—schema transformation and Iceberg table

creation

4.1 Create schema transformation logic

4.2 Write transformed data to Iceberg table

4.3 Write unit tests for schema transformation

4.4 Write a property test for data preservation

4.5 Write a property test for schema transformation correctness

4.6 Write unit tests for Iceberg table operations

5. Checkpoint—Verify bronze and silver stages work end-to-end

6. Implement Deequ data quality validation

6.1 Configure the Deequ validation suite

6.2 Execute validation and handle results

6.3 Write unit tests for Deequ validation

6.4 Write property tests for Deequ suite completeness

7. Implement gold stage—validated data publication

7.1 Write unit tests for the gold stage

8. Add pipeline summary and query examples

9. Add comprehensive notebook documentation

10. Final checkpoint—end-to-end pipeline validation

234

Chapter 5 Big Data P c d T AWS G d AI A

Each one of these tasks is well defined with ample detail for what actions will be
taken. Let’s take a look at one of them.

- [x] 4.1 Create schema transformation logic

Cast date columns (hearing_date, last_modified_date, violation_date)
to TimestampType
Cast numeric columns (imposed_fine, admin_costs, latitude, longitude)
to DoubleType

This result was generated without any detailed direction. I then took the generated
Jupyter notebook and uploaded it into my JupyterLab environment for review and
further development. The initial result was not without error—there were certain
variables I did not define in my initial prompt, like S3 locations, nor did I provide JAR
files to enable S3 Tables Iceberg integration. If I want to improve the quality of the initial
pass or customize it to my preferences, I can create Kiro Steering Files and Kiro Powers.
Steering files are reusable artifacts that contain detailed instructions or context to guide
Kiro’s AI agents on project standards, conventions, and best practices.

After a few quick edits and troubleshooting with Kiro, I was able to create a
functional notebook with most of the code already written. Figure 5-26 shows the front
matter as part of the in-notebook documentation.

235

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-26._** _Kiro-Generated Jupyter Notebook for Example Data Pipeline_

Let’s take a quick look at the detailed transformations implemented in Spark for
processing bronze into the silver phase for this dataset. This will provide insight into the
capabilities of Kiro to accelerate data solution development. I’ll present a small block of
code and then add my commentary.

# Start with bronze DataFrame
df_silver = df_bronze

# Step 1: Normalize column names (lowercase, replace spaces with
underscores)
print("\nStep 1: Normalizing column names...")
for col_name in df_silver.columns:

Converting names to lowercase and replacing spaces with underscores makes sense.
However, we may want to add more scenarios, which we can do with a steering file.

236

Chapter 5 Big Data P c d T AWS G d AI A

# Step 2: Cast date columns to TimestampType
date_columns = ["hearing_date", "last_modified_date", "violation_date"]
for date_col in date_columns:

df_silver = df_silver.withColumn(date_col, col(date_col).

cast(TimestampType()))

nulls_after = df_silver.filter(col(date_col).isNull()).count()

if nulls_after > nulls_before:
print(f" ⚠ Warning: {date_col}
before} null after casting")

✓ {date_col} cast to TimestampType")

Converting dates to timestamps does not make sense in many scenarios.
Timestamps are better for auditing fields like when a record was created or updated.
There may be fields that intend to capture both the date and time; however, this is not
assumed. For instance, a hearing date should be assumed to indicate the day only, and
not the time. If the data includes the time, it may not be valid. Understanding the context
and the domain is often required to know which is correct.

I address this in my steering file:

Choose the appropriate temporal type based on your use case:

#### Use DateType When:

- You only need date precision (year, month, day)

- Time of day is not relevant to your analysis

- You want to partition by date

- Examples: birth_date, order_date, event_date

#### Use TimestampType When:

- You need time-of-day precision

- Tracking exact moments in time

237

Chapter 5 Big Data P c d T AWS G d AI A

- Audit trails and event logging

- Examples: created_at, updated_at, transaction_timestamp

The next field transformation is casting numeric fields to double.

# Step 3: Cast numeric columns to DoubleType
numeric_double_columns = ["imposed_fine", "admin_costs", "latitude",
"longitude"]
for num_col in numeric_double_columns:

cast(DoubleType()))

print(f" ⚠ Warning: {num_col}
became null after casting")

✓ {num_col} cast to DoubleType")

Converting these to double is correct for this use case. Some use cases (e.g., financial
services) may require a specific level of precision, which can be implemented using the
DecimalType instead.

For my steering file, I add the following section:

#### Use DecimalType When:

- **Financial data**: Money, prices, costs (exact precision required)

- **Measurements**: Scientific data requiring exact decimal representation

- **Regulatory compliance**: Tax calculations, accounting

- **Avoiding rounding errors**: When precision matters more than
performance

#### Use DoubleType When:

- **Approximate values**: Latitude/longitude, sensor readings

- **Performance critical**: Large-scale analytics where slight imprecision

is acceptable

- **Statistical calculations**: Averages, percentiles, aggregations

238

Chapter 5 Big Data P c d T AWS G d AI A

I may also add examples and explicit use cases for different decimal patterns. Adding
this additional detail will help improve accuracy for how data transformations are
generated by Kiro:

### Common Decimal Patterns

#### Financial Data (Currency)
```python
from pyspark.sql.functions import col
from pyspark.sql.types import DecimalType

# US Dollar amounts (up to $999,999.99)
df = df.withColumn("price", col("price").cast(DecimalType(8, 2)))
df = df.withColumn("tax_amount", col("tax_amount").cast(DecimalType(8, 2)))

# Large financial amounts (up to $999,999,999,999.99)
df = df.withColumn("revenue", col("revenue").cast(DecimalType(14, 2)))

# High-precision financial (4 decimal places for forex, crypto)
df = df.withColumn("exchange_rate", col("exchange_rate").
cast(DecimalType(18, 4)))
```

#### Percentages and Rates
```python
# Percentage with 2 decimal places (0.00% to 100.00%)
df = df.withColumn("interest_rate", col("interest_rate").
cast(DecimalType(5, 2)))

# Basis points (4 decimal places: 0.0000 to 100.0000)
df = df.withColumn("fee_rate", col("fee_rate").cast(DecimalType(6, 4)))
```

You can see that while generative AI is demonstrating extraordinary sophistication
with little direction, it will likely need assistance to produce fully working
production code.

Amazon SageMaker Unified Studio is the recommended option for developing data
solutions. Now let's look at how data quality is enforced at scale.

239

Chapter 5 Big Data P c d T AWS G d AI A

**Data Quality with Deequ**

Data quality for big data is a critical requirement, especially in regulated industries like
financial services (FSI) and healthcare life sciences (HCLS). Data quality needs to be
constantly monitored because a configuration or development change upstream could
introduce data quality problems that you may never detect without a robust data quality
practice.

The conform stage of the data lake is where a dataset is meant to be validated. If the
data succeeds in passing through a strict filter, downstream processes can be confident
that the data is not going to include anomalies or outliers that could generate erroneous
results.

Deequ is an open-source, Spark-based data quality framework originally developed
by Amazon that performs data quality checks on big data, particularly data stored
in data lakes. It leverages Spark’s “method chaining” strategy to chain a sequence of
different constraints together in a compact block of code. This makes it easy for the
reader to understand how the dataset is being evaluated. Incidentally, that reader could
be AI—and this strategy inadvertently provides a valuable artifact for AI to extract data
transformation logic. These tools are also deterministic, producing high-value artifacts
that can then be leveraged by AI agents. LLMs (as they are currently architected) are not
well suited for processing or transforming large structured datasets, nor are they capable
of accurately performing complex calculations, aggregations, or statistical analysis.

In our data transformation pipeline, the data quality checks are performed on the
dataframe prior to writing it to the conform stage. The data quality verification report
that is generated by Deequ can be queried to determine if the dataset passed or failed
the validation. If a constraint verification failure is designated as critical, it should cause
the pipeline to fail. Data validation reports could then be consumed by a “data quality
agent” to assess and summarize the cause to assist a data engineer with a remediation.
Figure 5-27 depicts when the Glue job for data validation is performed and where
agentic AI can assist with data quality analysis.

240

Chapter 5 Big Data P c d T AWS G d AI A

**_Figure 5-27._** _Deequ Data Validation with Agentic Data Quality Analysis_

The glue job depicted in Figure 5-27 is what we’ll focus on next. In order to construct
the Glue job code that applies the Deequ constraints for verification, we first need to
know what constraints should be applied. Determining which constraints to apply is
itself a process. You’d likely profile the dataset to understand the values and distribution.
For example, say a “status” column of a project tracking dataset only contains “pending,”
“completed,” or “cancelled.” I could add a constraint to validate that the column only
contains these values. Any non-standard status value would indicate an error or a
change in business logic that would require the data team to handle downstream. If the
dataset had millions of rows and 100 columns, doing this manually would not scale.
Luckily, Deequ has several methods to automate programmatic execution of these

241

Chapter 5 Big Data P c d T AWS G d AI A

tasks to assist us in this journey. These include analyzers, a profiler, and constraint
suggestions. Before we jump in, there’s some preliminary work that’s needed to enable
Glue to use the Deequ library.

Deequ is natively written in Scala and built on top of Apache Spark, which is why it
scales efficiently with the size of data. It runs on the JVM running in Spark. Using Deequ
in PySpark Glue jobs and notebooks requires some additional steps, which I’ll review
briefly before moving on. You’ll need additional reference files (hosted in S3) that will be
specified to Glue, which are not natively installed—the Deequ Python wrapper and the
Deequ Scala JAR.

Download or clone the PyDeequ project from the public repository and compress
the pydeequ folder (which contains the __init__.py file) into a.zip file. Download the
Deequ JAR file from the Maven repository and upload it to S3.

In a SageMaker Unified Studio notebook, you can use the magic command to specify
additional files and JARs. In a SageMaker Studio or Glue notebook, you can use the
magic command to specify additional files and JARs.

%extra_py_files s3://your-bucket/pydeequ/pydeequ.zip
%extra_jars s3://your-bucket/pydeequ/deequ-2.0.11-spark-3.3.jar

For Glue jobs, you would use the key-value format for setting the --extra_py_files
and --extra-jars flags.

aws glue start-job-run \

You then will need to set the Spark version to a version Deequ supports.

import os
os.environ['SPARK_VERSION'] = '3.3'

If you run this as part of a new session, you should see the following result with
no errors:

_Trying to create a Glue session for the kernel._
_Session Type: glueetl_
_Session ID: ca5aadba-c75b-4f93-a7fe-XXXXXXXX_

242

Chapter 5 Big Data P c d T AWS G d AI A

_Applying the following default arguments:_
_--glue_kernel_version 1.0.8_
_--enable-glue-datacatalog true_
_--extra-py-files s3://your-bucket/pydeequ/pydeequ.zip_
_--extra-jars s3://your-bucket/pydeequ/deequ-2.0.11-spark-3.3.jar_

Now when importing pydeequ as part of a notebook session, we see our extra files
included.

import pydeequ

We can now start using PyDeequ analyzers, profilers, and constraint suggestion
functions in our Glue job. Let’s take a look at each.

The analyze function performs an analysis you explicitly define on column data in
a dataframe. This is a type of data analysis that calculates certain metrics like size,
completeness, distinctness, and data types for each column. For numeric columns, it can
calculate mean, standard deviation, min and max, and distinct count.

To generate this analysis, you can follow the sample code below:

from pydeequ.analyzers import *

analysisResult = AnalysisRunner(spark) \

analysisResult_df = AnalyzerContext.successMetricsAsDataFrame(spark,
analysisResult)
analysisResult_df.show()

For a more complete, full dataset profiling capability, we can use the Deequ profiler.

243

Chapter 5 Big Data P c d T AWS G d AI A

Deequ can perform data profiling, similar to Glue Databrew discussed earlier. Profilers
use analyzers as a foundational module to generate the results. Refer to the sample code
below to learn how to execute profiling jobs with Deequ:

from pydeequ.profiles import *

result = ColumnProfilerRunner(spark) \

And like DataBrew data profiling reports, a Deequ Profiler returns a large JSON
object that details dataset and column-level statistics. Here is an excerpt for a status
column from a hypothetical dataset.

"status": {

**Deequ Constraint Suggestion**

In “smaller” data systems like an RDBMS, constraints are applied and enforced like rowlevel triggers to prevent data from being written to a table. In big data systems like data
lakes, constraints are implemented as data analysis functions executed on the data _after_

244

Chapter 5 Big Data P c d T AWS G d AI A

it is written. This is the mechanism by which we operationalize data quality for big data
scale. Let’s take a look at how suggestions for constraints can be generated with the help
of Deequ.

from pydeequ.suggestions import *

suggestionResult = ConstraintSuggestionRunner(spark) \

Constraint suggestions are returned as JSON, and this allows us to export and import
these rules. The constraint suggestion JSON result object includes a lot of detailed
information, including the actual Spark code.

{

"description": "Values in 'status' should be one of: completed,

pending, cancelled",
"codeForConstraint": ".isContainedIn(\"status\",

Array(\"completed\", \"pending\", \"cancelled\"))",
"constraintCode": "ContainedIn(\"status\", Array(\"completed\",

\"pending\", \"cancelled\"))",

}

You can apply these generated constraints to your dataframe and use it to validate
the data quality of the dataframe. Now we can put it all together.

245

Chapter 5 Big Data P c d T AWS G d AI A

**Create a Glue Job with Constraint Verification Code**

With the profiling and constraint suggestion artifacts that we generated, we can look
to use agentic AI to automate the generation of high-quality constraint verification
code. There is a way to read constraint names and constraint code from a database like
DynamoDB and apply them dynamically using a parameterized Glue job. However,
this approach obfuscates the data quality logic outside of the Glue job code. Instead,
in Figure 5-28, I introduce an architecture for generating Glue job code that performs
Deequ constraint verification using a “Deequ constraint writer” agent.

**_Figure 5-28._** _Deequ Profiling and Constraint Suggestions with Agentic Glue_
_Job Writer_

246

Chapter 5 Big Data P c d T AWS G d AI A

By just providing very basic agent instructions, I can generate very promising (but
not 100% accurate) Glue job code that a junior or mid-level engineer could then polish
and push to the code base. Note that for these examples, I am again using the publicly
available Chicago buildings ordinance violations dataset.

These are the instructions I defined for the Deequ Constraint Writer Agent:

Analyze the Deequ constraint suggestions provided as input and decide
which constraints to apply to ensure high quality data for the referenced
data set.

OUTPUT:
1) Write a glue job that applies the appropriate the Deequ constraints and
output the constraint verification report to S3 and make it available for
querying in Athena
2) Only return the glue job code and nothing else

The agent uses Claude to generate Glue job code that is high quality using just
the Deequ constraint suggestions report. Let’s look at some of the features of the
generated code.

The import statements for Glue and PySpark packages were constructed correctly, as
well as the PyDeequ packages.

# Import Deequ
from pydeequ.analyzers import *
from pydeequ.checks import *
from pydeequ.verification import *
from pydeequ.repository import *

The generated code properly handled Glue job parameters, which included the
database and table name for which to run verification against as well as an output path
for the verification report.

job.init(args['JOB_NAME'], args)

# Get parameters
database_name = args['database_name']
table_name = args['table_name']
output_path = args['output_path']

247

Chapter 5 Big Data P c d T AWS G d AI A

The agent knew how to read a dataset in from the catalog to a Glue-specific dynamic
dataframe. It also knew it had to convert that dynamic dataframe into a Spark dataframe
so that it could be read by Deequ.

# Read data from Glue catalog
dyf = glueContext.create_dynamic_frame.from_catalog(database=database_name,
table_name=table_name )

# Convert to DataFrame for Deequ
df = dyf.toDF()

Things get a bit scary when you see that the agent also created a unique ID for the
verification run and then constructed that unique ID using a concatenated timestamp.

# Create a unique run ID for this verification run
timestamp = int(time.time())
run_id = f"verification-run-{timestamp}"

Things break down a bit when we get to the constraint checks. There are _a lot_   more than is likely needed. The completeness checks are overkill. Unless we expect a
column to never be null, the expected completeness of a column may not be known
or consistent. This type of check does offer a mechanism for defining a threshold for
completeness that Deequ can report on for analysis purposes. On the positive side, I’d
rather have _more_ constraint checks than less. It’s easier to take away than add, which
makes any potential review and modification task go that much faster.

# Define verification
verification = VerificationSuite(spark) \
.onData(df) \
.useRepository(repository) \
.addCheck( Check(spark, CheckLevel.Error, f"Data quality checks for
{database_name}.{table_name}" ) \
.isComplete("ID") \
.isUnique("ID") \
.hasCompleteness("ADDRESS", lambda x: x >= 0.99, "It should be above
0.99!") \
.hasCompleteness("WARD", lambda x: x >= 0.99, "It should be above 0.99!") \

248

Chapter 5 Big Data P c d T AWS G d AI A

.hasCompleteness("RESPONDENTS", lambda x: x >= 0.99, "It should be above
0.99!") \
.hasCompleteness("LATITUDE", lambda x: x >= 0.99, "It should be above
0.99!") \
.hasCompleteness("LONGITUDE", lambda x: x >= 0.99, "It should be above
0.99!") \
.hasCompleteness("VIOLATION DATE", lambda x: x >= 0.99, "It should be
above 0.99!")
...

The results included creating a verification summary, writing the summary results to
S3, and updating the table in the catalog for Athena querying.

While some syntax errors exist in the generated code, it provides a reliable way to put
guardrails on junior developers to complete these lower-value tasks with speed and high
accuracy. You can view the full result in the Git repo accompanying this book.

This raises an important investment decision about generative and agentic AIassisted solution development. It may be possible to make this process more robust with
the goal of fully removing the need for human review. However, the effort needed to
achieve that level of quality given the current state of the art is a risk. If the expectation
is that the quality of the models will improve over time, those hard-fought features may
become obsolete with the next model release. Instead, we should resist the tendency to
over-engineer the logic to compensate for a lack of capability in the models. Remember,
doing so commits the organization to operating, monitoring, and maintaining this
logic. Instead, if we accept these limitations and use humans to review and approve the
working code where it eliminates unnecessary complexity, we can realize significant
productivity gains with a lower-risk investment.

**Auto Scaling for Glue ETL Jobs**

As I mentioned earlier in the chapter, one of the primary benefits of the AWS cloud is
elasticity. Big data workloads may be variable—you may not always know the volume
of the dataset to be processed at execution time. Having a fixed amount of resources
defined at design time will break in production if the size of the data file exceeds the
memory required to process the data. Luckily, AWS Glue ETL jobs have an auto-scaling
feature that allows resources to scale out (and in) based on the size of the workload
encountered at execution time.

249

Chapter 5 Big Data P c d T AWS G d AI A

Auto scaling is available for AWS Glue 3.0 and later for both batch ETL and streaming
jobs. You can enable auto scaling via the console or the CLI.

Figure 5-29 shows the Job details tab in AWS Glue Studio. Under _Worker type_, select
“Automatically scale the number of workers.” You will need to specify a value for the
_Maximum number of workers_, which represents the greatest number of instances of the
specified worker type to spawn if AWS Glue determines it is needed based on the load.

**_Figure 5-29._** _Enabling Auto Scaling Feature in AWS Glue Studio_

You can also enable auto scaling via the start-job-run CLI command using
the –enable-auto-scaling parameter passed when the Glue job is executed. The JSON
parameter enabling the auto-scaling feature is shown below:

{

250

Chapter 5 Big Data P c d T AWS G d AI A

"WorkerType": "G.2X", // G.1X and G.2X are allowed for Auto

Scaling Jobs

}

**Detecting Schema Changes**

As I noted earlier, schema changes in source systems are one of the biggest reasons ETL
pipelines break and require maintenance. One of the most valuable ways to use Glue
Crawlers is to detect and alert on schema changes that were detected in data sources.
And now with generative and agentic AI, we can take it one step further and not just
detect schema changes but modify the current ETL job code to incorporate the latest
schema changes! Figure 5-30 shows this high-level solution architecture.

**_Figure 5-30._** _Automating Schema Change Detection and Glue Code Updates_

251

Chapter 5 Big Data P c d T AWS G d AI A

In the solution architecture above, we can trigger a Glue crawler to run on a schedule
or after an ingestion process runs. That crawler will crawl the data files in S3 and update
the schemas that changed. This will appear as a new table version in AWS Glue. These
table versions are retrievable via the Glue API. The Glue Job Update Writer Agent can
retrieve the new schema and the current Glue job code and use it to generate an updated
Glue job. Depending on how much automation is desired, the agent could write the Glue
code to S3 for manual handling and review, initiate automated testing, and even commit
the code to source control and submit a pull request.

That concludes the discussion of enforcing data quality using the Deequ framework.

**Amazon Bedrock Batch Inference**

Inevitably the question will be asked: how can we apply generative AI to a large
structured dataset? Maybe there is a description field or feedback text as part of a user
review—how could we efficiently run LLM inference at the row level for a large dataset?
Batch inference for Amazon Bedrock is performed asynchronously. Before we jump in
to see how to invoke a batch inference job, we need to first discuss the various limits (see
Table 5-1). AWS is used to manage this feature.

**_Table 5-1._** _Service Limits for Amazon Bedrock Batch Inference_

**Description** **Limit** **Adjustable Upon Request**

M FM I 10 Yes

M 50,000 Yes

M 1,000 N

M 1 G Yes

M 5 G Yes

You’ll notice that _all_ of the upper limits are adjustable and can be increased using
a service quota request. However, due to the overwhelming demand AWS has seen for
this feature, priority is given to requests that fully utilize their service limit allocation.
This means that while it is possible to increase the service limit, the proper strategy
given these constraints is to set the limit for the smallest dataset likely and then use that

252

Chapter 5 Big Data P c d T AWS G d AI A

limit as the chunking size for larger datasets. Another strategy is to distribute the batch
inference load across multiple accounts, based on the size of the data being processed,
and set the limits according to the size of the data. In addition to these considerations,
understand that for most batch inference use cases, latency and cost are typically
primary constraints. So for our example below, we’ll be using Amazon Nova Micro—the
lowest latency model in the Nova family. At $0.04 per million input tokens and $0.14 per
million output tokens, it also delivers the lowest cost per inference on Bedrock.

Let’s take a look at the steps needed to initiate a batch inference request. I assume
you already have created a Bedrock client using the Boto3 library.

1. Prepare the JSONL (JSON lines) file

Each line of the JSONL file is an inference request specifying the
model id and the prompt with context. It requires the “.jsonl”
extension. This file does not contain an entire dataset, just the data
being sent for inference (with an associated record identifier). The
record ID should be the primary key of the source dataset so the
resultset can be joined to the original dataset.

{

"text": "Provide sentiment analysis on the

following social media post:..."

}

253

Chapter 5 Big Data P c d T AWS G d AI A

2. Define the input file configuration object

The location of the JSONL file that was prepared in step 1 needs to
be defined in a configuration parameter that we can pass in when
the invoke method is called.

inputDataConfig=({

})

3. Define the output file configuration object

The results of our inference requests need to go somewhere. Since
this is an asynchronous request, Bedrock needs an S3 location to
write the results.

outputDataConfig=({

})

4. Create a model invocation job

With our configuration parameters defined, we can create the
batch inference job to start processing inference on our dataset.

response=bedrock.create_model_invocation_job(

)

254

Chapter 5 Big Data P c d T AWS G d AI A

5. Check job status

jobArn = response.get('jobArn')
job_status = bedrock.get_model_invocation_job(jobIdentifier=jobArn)

['status']

6. Check for errors

We can also check for any errors that might have occurred. This
returns the list of records that failed during processing.

error_list = bedrock.list_model_invocation_jobs(

)

This concludes our odyssey into big data processing and transformation with
generative and agentic AI.

In this chapter, I explored big data processing and transformation using AWS Glue
and agents, while leveraging cloud computing’s fundamental benefit: elasticity. I
demonstrated how AWS Glue DataBrew can be used for initial dataset profiling, showing
how to enrich these profiles through the deep reasoning and analytical capabilities of
LLM-powered agents. Throughout the chapter, I illustrated the integration of AI agents
at various stages of the data engineering workflow—from generating PySpark code and
Deequ constraints to writing complete AWS Glue jobs. I also provided a comprehensive
look at data quality solutions using the open-source Deequ library, demonstrating
how it can be used to analyze data, suggest constraints, and generate verification code.
I presented a solution for dynamically managing schema changes in source systems
with agentic automation. I also demonstrated how to perform AI model inference at
scale using the batch inference feature in Amazon Bedrock. By combining traditional
data engineering practices with emerging AI capabilities, I showed how to accelerate
development while maintaining robust data quality standards. I sought to emphasize
practical, hands-on approaches, providing concrete examples and architectural patterns
that data engineers can implement in their own workflows today.

In the next chapter, I explore data pipeline orchestration and observability.

255

**CHAPTER 6**

## **Data Pipeline** **Orchestration** **and Observability**

Converting raw data into business value can require a complex, multi-step process
with various dependencies. There can be several data loading processes running
concurrently, with the outputs being the inputs to more data processing that eventually
serves reporting, analytics, or AI model training. The business (or its customers)
depends on this process to be completed successfully on time every time to yield the
value they expect. They are relying on you as the data engineer to ensure these processes
are robust and resilient.

In this chapter, I present best practices for implementing complex data pipeline
orchestration and observability in the AWS cloud. I discuss the criteria for choosing
an orchestration solution and provide examples for orchestrating data pipelines with
Amazon Managed Workflows for Apache Airflow (MWAA) and AWS Step Functions. I
describe how to implement observability for data pipelines in the context of the three
pillars of observability: logging, metrics, and traces. I’ll also demonstrate strategies for
using generative AI to write our orchestration code and to help us observe and analyze
these complex pipelines.

**Best Practices for Data Pipeline Orchestration**

The best practices that I present here are my biased opinions based on criteria I’ve
developed from my experience. It’s not intended to be an exhaustive list addressing
every possible use case. As a data engineer, you will work backwards from the business

257
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_6](https://doi.org/10.1007/979-8-8688-2199-8_6#DOI)

Chapter 6 Data P c - d

and data requirements and adapt the tooling to meet those requirements. What follows
are principles that likely will not change over time, given the current generation of
tooling.

There should be a clear separation of concerns between the orchestration logic and the
data processing and transformation logic. This is complicated when the capabilities
of the tooling overlap. For instance, AWS Glue can schedule jobs and perform basic
orchestration. Apache Airflow can scale out workers using its Celery Executor to perform
distributed data processing and transformation. By keeping these concerns separate,
it narrows the scope of migration in the event you decide to swap in a new tool to
perform a specific function. The easiest way to ensure this is to choose and enforce the
use of different tools for each responsibility. If you violate this rule, you’ll need to be
exceptionally diligent and deliberate in maintaining this separation.

Applying the general principle of encapsulation encourages us to break up our data
processing code into logical chunks to make it easier to maintain. With the logic
separated into multiple jobs, we can quickly identify which part of the pipeline has failed
and work to correct and rerun the pipeline from that task rather than rerunning the
entire pipeline from the beginning. Two characteristics drive the division of work:

**Duration** : Long-running tasks that involve the extraction and

transformation of large datasets are good candidates for isolation.
If an error later in the same job requires a retry of this longrunning task, it will cause delays and incur unnecessary cost. You
should separate long-running tasks into their own job.

**Complexity** : Highly complex analytical calculations that require

many dependent steps should be scrutinized to determine where
checkpoints can be defined. Developing and maintaining this
logic as one job will exacerbate debugging and experience higher
rates of regression.

258

Chapter 6 Data P c                  - d

My last piece of advice is: don’t overdo it. Excessive job-splitting adds unnecessary
delays to processing and should be considered an anti-pattern.

**Interoperability and Control Flow Management**

The primary responsibility of an orchestration tool is to control the flow of execution—
including complex dependencies—of the data pipeline from start to finish. The control
flow is enabled by the orchestration tool’s ability to natively interoperate with the various
data systems and services that perform tasks in the data pipeline. What interoperability
means in this context is the ability for the orchestration tool to not just trigger and
execute a task in another system but then continuously monitor that system for status
updates. Once the orchestrator is notified that the task is completed, it advances the flow
to the next step in the pipeline. Without this interoperability, you would need to write
custom logic to continuously poll for status. At scale, you could find yourself writing
custom logic for dozens of data sources, which you’ll need to maintain over time.

One of the primary reasons for data pipeline failures and rework is the evolution of
schemas over time. Where the data team controls the data sources and the systems
they are managed in, schema changes can be governed with strict rules to enable the
system to minimize the impact of these changes downstream. For instance, Parquet can
gracefully manage schema changes if column names and ordering are consistent and
new columns are only added to the end of the data set. However, for data sources the
data team doesn’t control, schemas can change unexpectedly. A robust data pipeline
must monitor data sources for unexpected schema changes and alert data engineers to
intervene to mitigate the risk of failure downstream.

Time to answer is one of the most critical nonfunctional requirements of the business
that drives the design of data pipelines. Time to answer (aka time to insight or time to
decision) is a business-level SLA indicating when the business determines it needs
to deliver insights from when the data is created or acquired. The business may not
naturally understand this metric or define it, but it is the responsibility of the data

259

Chapter 6 Data P c - d

engineer to ensure that these metrics are defined for each pipeline. While some
applications may require near real-time delivery, this is often not the case with most
data-driven applications. Many batch workloads, particularly in sales and marketing or
even customer insights, may only require a time to answer of 12–24 hours. The data team
should consider this time period as a hard deadline for which breaching it will incur
some financial impact or loss of trust with the business or customers. While a full day to
deliver may seem generous, consider that pipelines may take hours to run and failures
can and will occur. This means that any technical challenges need to be investigated
and resolved, and the full data pipeline then needs to be processed successfully within
that time frame. Other constraints could be imposed. For instance, data extraction
from source systems often occurs overnight or after peak business hours when any
performance impact on business users is minimized. Any delay to this schedule could
cause data processing to spill over into the following business day.

**Orchestrating Data Pipelines with AWS**

AWS provides several services for orchestrating data pipelines. AWS Glue Workflows is
an orchestration feature within Glue that can schedule, trigger, and orchestrate crawlers
and Glue jobs. I do not cover AWS Glue Workflows in this book, but if you are interested
in learning more about its capabilities to see if it is right for your use case, refer to the
user guide. The two orchestration solutions I will cover in depth are Amazon Managed
Workflows for Apache Airflow (Amazon MWAA) and AWS Step Functions. Table 6-1
describes the key differences between them. Data teams should choose the one best for
their needs.

260

Chapter 6 Data P c                  - d

**_Table 6-1._** _Comparison of Amazon MWAA and AWS Step Functions_

**Feature** **Amazon Managed Workflows for**
**Apache Airflow**

**AWS Step Functions**

L P JS N

L Open S Vendor-specific

P I Declarative

S Persistent service S AWS L

Control Flow Directed A A S

I I AWS
AWS

I AWS

S Moderate H

I’ll cover AWS Step Functions first, then Amazon MWAA.

**AWS Step Functions**

AWS Step Functions is a fully managed service that enables you to coordinate the
components of distributed applications and microservices using visual workflows. Like
Airflow, it simplifies the orchestration of complex processes. Step Functions use state
machines to define workflows. Each state machine is a collection of states, tasks, and
transitions that define the flow of your process. Since it does not adhere to a DAG-based
control flow, waiting steps and loops can be implemented. The service provides built-in
error handling, including automatic retry of failed tasks, error catching, and a timeout
feature to stop tasks that are taking too long to execute.

**Standard and Express Workflows**

AWS Step Functions offers two types of workflows: Standard Workflows and Express
Workflows. Each type is suited for different use cases based on the requirements for
execution duration, rate, and cost. Table 6-2 shows a detailed comparison between the
two offerings.

261

Chapter 6 Data P c - d

**_Table 6-2._** _AWS Step Functions: Standard Workflows vs. Express Workflows_

**Feature** **Standard Workflows** **Express Workflows**

E R H T

S Transition
R

Up to 25,000 transitions per second Up to 100,000 transitions per second

Durability Durable execution history H

E
S

L
Tracing

E A

Detailed, step-by-step in CloudWatch
L

S
L

H
effective

Use Cases L
auditing

P B B

**Standard Workflows** are ideal for applications requiring long execution times, high
reliability, and detailed logging. **Express Workflows** are best suited for high-frequency,
short-duration tasks where cost efficiency and high throughput are paramount.

**Orchestrating Workflows with AWS Step Functions**

I’ll implement the same data pipeline with an AWS Step Functions Standard Workflow.
I will demonstrate how generative AI can be used to assist us in creating this Step
Functions workflow.

**Create IAM Policies and Roles**

I’ll start first with the AWS IAM roles and policies that will be needed to authorize the
Step Function workflow to execute, monitor, and stop AWS Glue jobs. Using the principle
of least privilege, we can use the IAM policies to specify the specific AWS Glue jobs that
this Step Function workflow has access to execute. This provides an additional layer of
protection to prevent the inadvertent referencing of Glue jobs that are not intended to
be part of the workflow. As the workflow changes and new Glue jobs are added, the IAM
policy will need to be updated to explicitly authorize new Glue jobs.

262

Chapter 6 Data P c                  - d

This is the IAM policy:

{

}

I’ll attach this policy to an IAM role that has a trust relationship to assume the AWS
Step Functions service role.

{

}

263

Chapter 6 Data P c - d

**Create AWS Step Functions Workflow**

Using Kiro CLI, I can use agentic AI to produce a Step Functions Workflow, including
highly complex workflows with concurrent processing and dependencies. Let’s take a
look at how effective Kiro is at producing orchestration code.

Here is the prompt I used:

Create an AWS Step Functions workflow to orchestrate a series of
Glue jobs with the following dependencies:

glue-job-extract1 and glue-job-extract2 are dependencies for
glue-job-transform but can run concurrently.

glue-job-transform is a dependency for glue-job-validate.

glue-job-validate is a dependency for glue-job-publish.

For any errors detected, send a message to the SNS Topic “glueworkflow-­

Write only JSON and output it to a JSON file.

The result from Kiro CLI is a valid JSON artifact (refer to the Git repo associated with
this book for complete code). Figure 6-1 shows the steps that Kiro completed.

**_Figure 6-1._** _Kiro CLI Reporting the Creation of the AWS Step Function_

I then instructed Kiro to deploy this in my AWS environment, which it did
successfully. I was then able to view the Step Function from the AWS console. The
**Definition** tab includes a visual workflow diagram (see Figure 6-2) to validate that the
orchestration logic has been implemented successfully.

264

Chapter 6 Data P c                  - d

**_Figure 6-2._** _Visual Diagram of the Example Step Function_

The advantage of using Kiro to help us is that it added exception and retry logic,
whereas a junior developer doing this infrequently may not think or know to do that.
Without rigorous testing, this may not have been discovered before getting deployed to
production, potentially causing unnecessary outages.

We just created a functional AWS Step Function process flow using generative
AI. Now let’s see how to use Amazon’s managed Apache Airflow service for
orchestration.

**Amazon Managed Workflows for Apache Airflow**

Amazon Managed Workflows for Apache Airflow (Amazon MWAA) is a fully managed,
enterprise-grade service that runs open-source Apache Airflow. Announced in 2025,
there is now a fully serverless version of the MWAA. Apache Airflow is a popular tool for
orchestrating and managing complex workflows. Data teams that choose Apache Airflow
and particularly Amazon MWAA typically do so for three primary reasons:

265

Chapter 6 Data P c - d

**Apache Airflow Is Pythonic**

Apache Airflow, being Python-based, offers the benefits of an
imperative programming paradigm. This allows developers to
programmatically define the steps for tasks to be executed. Defining
the orchestration logic as code makes it possible to implement
robust configuration management and DevOps practices.

**Directed Acyclic Graph (DAG) Workflow Management**

Apache Airflow provides a DAG interface that simplifies defining
and running intricate workflows with dependencies. Apache
Airflow visualizes these DAG workflows through a GUI, allowing
for an “eyes on glass” operations management experience that can
oversee the execution of pipelines in real time.

**Extensibility**

Apache Airflow’s operators provide a structured method for
executing common tasks using reusable modules. This feature
is highly extensible, allowing the Apache Airflow open-source
community to develop and maintain operators that integrate AWS
services such as Amazon S3, Amazon Redshift, Amazon EMR,
AWS Batch, and Amazon SageMaker. With many cloud-based
services supported, these operators offer useful abstraction,
repeatability, and an API. In the realms of big data and AI, these
operators are especially valuable for orchestrating long-running
asynchronous AI processes like model training.

**Amazon MWAA Architecture**

It’s important to understand the way the Amazon MWAA service is architected because it will
impact your strategy for how you manage MWAA environments as part of your development
process. For instance, the Amazon MWAA service cannot be stopped and started by design.
It runs continuously. Although the cost incurred to run the environment is minimal, it’s
important to consider this as part of your selection process. A fully serverless deployment
option for MWAA was launched in late 2025. Refer to the AWS docs for more information.
For the purposes of this section, I’ll be presenting the provisioned deployment option.

The service is operated from both an AWS service account and in the customer’s
VPC. Figure 6-3 depicts the Amazon MWAA architecture.

266

Chapter 6 Data P c                  - d

**_Figure 6-3._** _Amazon MWAA Architecture_

The _Web Server_ runs in AWS Fargate containers from an AWS service account.
The Airflow _Scheduler_ and _Workers_ are served from AWS Fargate containers in the
customer’s VPC.

AWS creates an Amazon Aurora PostgreSQL meta database for each MWAA
environment, which it manages from the service account. This metadata includes things
like the history of DAG runs and user roles and permissions.

**Caution** Deleting an A AA
associated metadata. T A A PostgreS L
AWS AA
A AWS 1 details how to export the metadata prior
to deletion of the environment.

1 Automating stopping and starting Amazon MWAA environments to reduce cost. Beswick,
[James. May 11, 2023. (https://aws.amazon.com/blogs/compute/automating-stopping-](https://aws.amazon.com/blogs/compute/automating-stopping-and-starting-amazon-mwaa-environments-to-reduce-cost/)
[and-starting-amazon-mwaa-environments-to-reduce-cost/)](https://aws.amazon.com/blogs/compute/automating-stopping-and-starting-amazon-mwaa-environments-to-reduce-cost/)

267

Chapter 6 Data P c - d

The DAGs are consumed from a specific Amazon S3 bucket. DAGs are stored
independent of the MWAA environment, which means they will persist if the MWAA
environment is terminated.

Next, I’ll demonstrate how to set up an Amazon MWAA environment.

**Amazon MWAA Environment**

To create the Amazon MWAA environment, complete the following steps:

1. On the Amazon MWAA console, choose **Create environment** .

2. Choose a **Name** for the environment.

3. Choose the **Airflow version** to use.

4. Choose the day and hour for the **Weekly maintenance window**

**start (UTC)** .

5. In the **DAG code in Amazon S3** section, you’ll choose the S3

bucket to load your DAGs and supporting files.

For this example, I’ve created an Amazon S3 bucket for all of
my Airflow environments using a standard naming convention.
I created a root folder with the name of the environment,
_MyAirflowEnvironment_ . Inside that folder, I create the folder
structure depicted in Figure 6-4.

268

Chapter 6 Data P c                  - d

**_Figure 6-4._** _Amazon S3 Folder Structure for a Managed Airflow Environment_

6. To use the AWS Boto3 SDK in our DAGs, I create a requirements.txt

file with boto3==1.34.138 as an entry, and I upload it to the
requirements folder. This was the current version of Boto3 at the
time of writing.

7. I choose the **DAGs folder** and **Requirements file** from my S3

bucket. Additionally, you can provide a plugins.zip file with
additional plugins and a shell script for a customized image. Both
are optional. Figure 6-5 shows these configurations.

269

Chapter 6 Data P c - d

**_Figure 6-5._** _Specifying S3 Folder and File Locations for Airflow Artifacts_

To complete the creation of the managed Airflow environment, you will choose
configurations for networking, security, compute sizing, and monitoring based on your
preferences. For brevity, I have omitted these steps.

Now that we have our managed Airflow environment created, I will demonstrate how
to construct our DAG using generative AI for our data lake.

**Orchestrating Workflows with Amazon MWAA**

The best way to demonstrate the capabilities of Amazon MWAA is to implement a
workflow. In this example, we will process several related datasets from the _Landing_
_Zone_ phase all the way to the _Published_ phase in our data lake. I will again use Kiro CLI
to help us construct our Airflow DAG.

I used the same prompt from my Step Functions example with instructions to create
an Apache Airflow (MWAA) DAG.

The result from Kiro CLI is a valid Airflow DAG .py file artifact (see glue_workflow_
dag.py in Chapter 6 of the Git repo associated with this book). Figure 6-6 shows the steps
that Kiro completed.

270

Chapter 6 Data P c                  - d

**_Figure 6-6._** _Kiro CLI Reporting the Creation of the Airflow DAG_

We can then ask Kiro to upload the DAG to the designated S3 bucket location.

**Validating the DAG with an MWAA Test Environment**

There’s a way to know if our AI-generated DAG file is valid. The Amazon MWAA
environment is connected to the S3 bucket and continuously polling for new DAG files.
The DAG processor will validate that each file contains a properly formed DAG and then
add them to the “DAG bag.” To generate logs for the DAG processor, you will need to
enable CloudWatch logs for each option desired. You have the option of choosing a base
reporting level (INFO, WARNING, ERROR, or CRITICAL), which will send Airflow logs
for that level and above. Logs can be enabled when creating or editing the environment
(see Figure 6-7).

271

Chapter 6 Data P c - d

**_Figure 6-7._** _Enabling DAG Processing Logs_

The AWS CloudWatch log group will be named according to the convention:

_airflow-YourEnvironmentName-DAGProcessing_

If you set the minimum **Log level** to **INFO**, every DAG file will appear in CloudWatch
as a log stream, including the DAGs that are processed successfully (see Figure 6-8).

272

Chapter 6 Data P c                  - d

**_Figure 6-8._** _Log Stream for DAG_

With our non-production Airflow environment with CloudWatch logs enabled, we
have a test bench for automating DAG testing as part of our generative AI workflow. With
our example DAG loaded successfully, we can visualize the graph as shown in Figure 6-9.

**_Figure 6-9._** _DAG Tasks Visualized in Amazon MWAA_

The MWAA scheduler environment is offered at very low cost. At the time of writing,
the smallest MWAA environment, which supports 50 DAGs, was priced at $0.49 per hour.
This is just over $350 per month. This cost could be optimized further by making the
environment creation dynamic and ephemeral as part of DAG testing.

We successfully used generative AI to create our Airflow DAG. Now, let’s add
observability to these pipelines.

273

Chapter 6 Data P c - d

**Observability for Data Pipelines**

Observability is the practice of measuring the state of a system by its outputs. In practice,
observability depends on three types of telemetry data: _logging_, _metrics_, and _traces_ . These
are referred to as the “three pillars of observability.” Observability is often confused with
monitoring, and they’re casually used interchangeably, but they are not the same.

Monitoring is used to assess the health of a system. It will be able to detect when
the system is not operating normally. Observability, on the other hand, seeks to achieve
a holistic view and understanding of how the system is operating by providing deeper
insights. If monitoring is the _what_, observability is the _why_ .

Workloads in production require observability. Too often, data teams are guilty
of developing and deploying a data pipeline to production without ever considering
observability, and by that time it’s too late. As failures occur, data teams are then reactive in
addressing those failures—adding observability to prevent the failures they encounter. Why
risk experiencing preventable failures and losing the trust of the business when you can
implement observability from the start and proactively mitigate risks that are detected? For
these reasons, observability needs to be considered at design time. The implementation of
observability is part of the solution that will be iterated on and managed over time.

In this section, I’ll demonstrate how to implement observability for data pipelines,
including logging, metrics, and traces. I’ll also explore how generative AI can be
used to summarize, interpret, enhance, and troubleshoot the data gathered from this
telemetry data.

Logs provide a detailed, timestamped record of discrete events that occur within a
system. They capture what happened, when it happened, and the relevant context or
details about the event. Logs typically include error messages, information messages,
debugging information, and other significant events. Each log entry is a standalone piece
of information.

Logs are used to troubleshoot specific issues, audit activities, and gain insights into
the operations of individual components within the system. They help answer questions
like “What went wrong?” and “What actions were taken?”

In the next sections, I lay out the various logging features relevant for our data
pipelines and how to activate them if they are optional.

274

Chapter 6 Data P c                  - d

To enable logging in MWAA via the AWS Management Console or using AWS CLI.

aws mwaa update-environment --name MyAirflowEnvironment --loggingconfiguration file://logging-config.json

The contents of the logging-config.json file are below. Since we are only using
MWAA for DAG orchestration, we want to enable the DAG processing logs, task logs,
and webserver logs at a minimum. However, if you want to enforce restricting the use
of MWAA to these functions, you can enable all logs and trigger alerts if a developer
unknowingly attempts to utilize these features.

{

}

Next, we’ll look at what standard logging we have available in AWS Glue.

275

Chapter 6 Data P c - d

**AWS Glue Logs**

In the configuration of AWS Glue jobs, you can elect to have more detailed logging of
your Glue jobs. Figure 6-10 shows options for **Continuous logging** and **Spark UI** logs.

**_Figure 6-10._** _Enabling Continuous Logging and Spark UI Logs in AWS Glue_

The continuous logs are available from the Glue job **Runs** menu, as shown in
Figure 6-11.

276

Chapter 6 Data P c                  - d

**_Figure 6-11._** _Continuous Logging in AWS Glue_

CloudWatch offers many metrics specific to Glue Spark jobs. These metrics make it
easier to troubleshoot Spark-based data processing.

This concludes a review of most of the standard logging. Next, I’ll discuss custom
logging.

Logging in Glue Jobs can include additional information to track the progress of the job.
In the event of failure, this will help narrow down the section in the code that requires
attention.

# In your Glue job script (PySpark)
import logging
logger = logging.getLogger('glueLogger')
logger.setLevel(logging.INFO)

277

Chapter 6 Data P c - d

logger.info("Starting Glue job...")
# Your job logic
logger.info("Finished Glue job.")

Metrics are quantitative measurements that reflect the performance, health, and
behavior of a system or its components. They provide a high-level view of how a system
is functioning and help identify trends, anomalies, and potential issues. In order to
identify trends and anomalies, a common set of metrics needs to be tracked for the same
processes over time.

Amazon MWAA provides standard metrics in AWS CloudWatch. For example, the metric
task_failures will track the number of Airflow tasks that failed. Since this is a metric,
we can create a CloudWatch alarm and alert the data team when an Airflow task fails.

aws cloudwatch put-metric-alarm --alarm-name "AirflowTaskFailures"
--metric-name "task_failures" --namespace "AWS/Airflow"
--statistic "Sum" --period 300 --threshold 1 --comparison-operator
"GreaterThanOrEqualToThreshold" --evaluation-periods 1 --alarm-actions
arn:aws:sns:us-east-1:123456789

**AWS Glue Metrics**

AWS Glue provides several features to assist us in capturing and reporting observability
metrics. Figure 6-12 shows the various Spark metrics available in AWS Glue, including

     - **Memory Profile** : Utilization of drivers and executors (%)

     - CPU load (%)

     - Worker utilization (%)

     - Active executors, completed stages

278

Chapter 6 Data P c                  - d

**_Figure 6-12._** _Metrics for AWS Glue Spark Jobs_

I’ll provide examples of each metric and log type and how they might be used to
troubleshoot challenges. There’s ample documentation online for how to troubleshoot
Spark logs, but as you might have guessed, AI is well suited for deriving insights from a
large haystack of observability data.

To implement robust observability for our AWS Glue jobs, we may need to create our
own metrics specific to our use case that give us the visibility into our pipelines that will
help provide insights to aid our understanding.

If you navigate to the **Metrics** section of the AWS Glue console, you’ll notice that they
are read-only. To create custom metrics, AWS provides a CloudWatch feature called the
_embedded metric format_ .

**The Embedding Metric Format**

The CloudWatch embedded metric format enables you to create custom metrics
asynchronously by writing logs to CloudWatch. The specification allows you to embed
custom metrics alongside detailed log event data. Custom metrics allow you to add

279

Chapter 6 Data P c - d

application- or business-level metrics to CloudWatch. CloudWatch then automatically
extracts these metrics, enabling visualization and alarm setup for real-time incident
detection. The associated detailed log events can be queried using CloudWatch Logs
Insights, offering deep insights into the root causes of operational events.

In this section, I’ll demonstrate how to create a custom metric using the embedded
metric format, then visualize and alert on anomalies for this metric using AWS
CloudWatch. For our example, we’ll keep things light by tracking business-level metrics
inspired by Chicago’s building code violations dataset:

     - total_imposed_fine

     - average_imposed_fine

     - total_violations

     - unique_violation_types

Let’s assume we’re running Spark in EMR and have our dataset loaded into a Spark
dataframe. Below are the Spark methods to aggregate each metric:

# Aggregate the metrics
total_imposed_fine = df.agg(F.sum("IMPOSED FINE")).first()[0]
average_imposed_fine = df.agg(F.avg("IMPOSED FINE")).first()[0]
total_violations = df.count()
unique_violation_types = df.select("VIOLATION CODE").distinct().count()

Custom metrics require a specialized format. For instance, “_aws” must be at the
root. The embedded data is automatically captured by CloudWatch as we watch.

# Prepare EMF log data
emf_data = {

"Timestamp": int(time.time() * 1000),

milliseconds

280

}

Chapter 6 Data P c                - d

CloudWatch can display any metric on a dashboard. See Figure 6-13.

**_Figure 6-13._** _Custom Metrics Dashboard_

These are business-level metrics. Operational metrics include the failure rate,
latency, and volume of the data processed.

Traces provide an end-to-end view of a single transaction or request as it moves through
various components and services within a system. They capture the path and duration
of the request, highlighting how different parts of the system interact. Traces include
detailed information about each segment of the transaction, such as entry and exit

281

Chapter 6 Data P c - d

timestamps, the services involved, and any errors or latency encountered. Each trace
represents a flow or journey through the system. Traces are used to understand the
performance and behavior of distributed systems, identify bottlenecks, and diagnose
latency issues. They help answer questions like “Where did the request spend the most
time?” and “Which service caused the delay?”

Logs provide granular, event-specific information, while traces offer a
comprehensive view of the lifecycle of a request across the system, making both logs and
traces essential for a complete observability strategy.

**Traces in AWS Glue**

Implementing traces in AWS Glue is not straightforward, but it can be accomplished
with some custom logging. This is due to the fact that while Airflow schedules the
execution of tasks in a pipeline, the services performing those tasks vary depending
on the use case. In distributed data pipelines where traceability is desired, there is the
concept of a correlation_id. This correlation_id provides a unique identifier that can
be distributed throughout each of the tasks and can be used to link all the logs specific
to an execution of a pipeline. Analysis of these disparate logs can describe a sequence of
events through that pipeline execution. There’s no need to generate this ID on your own.
In Airflow, the run_id is a unique identifier assigned for each execution of a DAG.

**Distributing the Trace Variables**

In this section, I’ll demonstrate how to distribute the tracing variables for two common
data processing services: Glue and EMR jobs. First, I need to define three variables in my
Airflow DAG. These variables will uniquely identify the DAG, the DAG execution, and
the S3 bucket where these logs can be aggregated in one place. I will assign the run_id
system variable to the correlation_id.

The trace variables defined in the DAG file will be:

correlation_id = "{{ run_id }}"
dag_name = "airflow-data-pipeline"
S3_BUCKET_NAME = "data-pipeline-logs"

Now, let’s see how to pass these to our data processing services.

282

Chapter 6 Data P c                  - d

**AWS Glue Jobs**

I’ll pass the trace variables to the Glue job using Airflow’s Glue operator. As mentioned
earlier, Airflow operators are specialized integrations into external services. Airflow tasks
are defined in relation to these operators, which define how the tasks are performed.

The trace variables can be passed as arguments to the Glue job.

glue_task = AwsGlueJobOperator(

)

The Glue job script can retrieve these parameters, retrieve the Glue job logger, and
inject this identifier into the logs for the Glue job.

# Parse arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME','dag_name','task_
id','correlation_id'])

# Spark and Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Retrieve the job object from the Glue context
job = Job(glueContext)

# Initialize the job with the parameters
job.init(args['JOB_NAME'], args)

# Get logger
logger = glueContext.get_logger()

# Create composite key

283

Chapter 6 Data P c - d

correlation_id = args['dag_name'] + "." + args['task_id'] + " " +
args['correlation_id']

# Add log entry with identifier
logger.info("Correlation ID from GLUE job: " + correlation_id)

Any logging statements made from the Glue script can add the composite identifier
indicating which DAG, which task, and which execution the statement was executed
from. From the Airflow UI, I can retrieve the execution ID and reconstruct the composite
key. With the composite key, I can query the relevant CloudWatch log groups using
CloudWatch Logs Insights.

**Amazon EMR Jobs**

Amazon EMR is another popular AWS service. There may be heavier data processing
jobs where teams may choose EMR. An Airflow data pipeline can create an ephemeral
EMR cluster and submit a job to it, then shut it down to optimize for costs.

In EMR, I define a configuration object called JOB_FLOW_OVERRIDES to set the
cluster parameters. I pass the trace variables to the Name parameter to create a composite
key that can be parsed later.

emr_task_id = "create_emr_cluster"
JOB_FLOW_OVERRIDES = {

"LogUri": "s3://{}/logs/emr/{}/{}/{}".format(S3_BUCKET_NAME, dag_name,

emr_task_id, correlation_id),

284

}}

Chapter 6 Data P c                - d

I will pass this configuration object into the Airflow EMR create job flow operator.

emr_cluster_creator = EmrCreateJobFlowOperator(

)

Similarly, I can use a configuration object that defines the steps the EMR cluster will
perform and then pass that into the EMR add steps operator.

EMR_STEPS = [{

's3://{}/data/unified-analytics/your-table'.format(S3_

BUCKET_NAME),

}]

285

Chapter 6 Data P c - d

In order to retrieve the job_flow_id, which is created and returned as part of the cluster
creation task, you can use Airflow XComs. Airflow XComs ­(Cross-Communication) is
a feature that enables communication and data sharing between tasks within a DAG,
allowing for more complex and dynamic workflows since the output of one task can be
used as input for another task.

step_adder = EmrAddStepsOperator(

job_flow_id="{{ task_instance.xcom_pull('create_emr_cluster',

key='return_value') }}",

)

Within my sample EMR analytics.py processing script, we unpack the parameters
and construct the identifiers needed to retrieve and submit events to the logger.

input_path = sys.argv[1]
output_path = sys.argv[2]
dag_task_name = sys.argv[3] + "." + sys.argv[4]
correlation_id = dag_task_name + " " + sys.argv[5]
spark = SparkSession\

sc = spark.sparkContext
log4jLogger = sc._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(dag_task_name)
logger.info("Spark session started: " + correlation_id)

This concludes our look at how to implement distributed tracing in data pipelines
orchestrated by Amazon Managed Airflow.

**Enhancing Observability with Generative AI**

Creating high-quality logs, metrics, and traces adds a lot of value on its own, as it
accelerates traditional troubleshooting to detect and resolve errors in the pipeline.
However, the big advantage now is that AI agents can quickly ingest and analyze these

286

Chapter 6 Data P c                  - d

raw inputs to deliver more meaningful analysis and actionable intelligence. These
capabilities can scale well beyond what a human operator can achieve. This means that
more insights can be collected from these inputs that can help improve performance,
resiliency, and scalability.

Let’s look at two scenarios.

**Aggregated Log Insight Reporting**

By enlisting the help of agentic AI to assist us in analyzing logs immediately when
they’re created, they can provide a jumpstart on troubleshooting errors and discovering
optimizations. We can automate log aggregation and analysis with agents and include
this as a mechanism that reports back to technical and business stakeholders.
Figure 6-14 shows the Log Analysis Agent solution architecture.

**_Figure 6-14._** _Log Aggregation and Analysis with Agentic AI_

287

Chapter 6 Data P c - d

We can use DAG-level callbacks to send events to EventBridge when an Amazon
Managed Airflow DAG completes (success or failure). We define these callbacks in our
DAG definition:

# Define your DAG with callbacks
dag = DAG(

Centrally routing events through EventBridge allows us to manage in one place
any and all actions we may want to trigger off of our DAG completion event. In the
referenced send_dag_completion_event function, we retrieve the DAG context,
construct an event message, and send the event using a Boto3 EventBridge client.

We start by creating our Boto3 EventBridge client:

events_client = boto3.client('events')

Then we retrieve the DAG context:

dag_run = context.get('dag_run')
dag = context.get('dag')

Now we construct the event message that includes all the job details that we want
to send:

event_detail = {

}

We now send the event to EventBridge. I reference the default bus in this example,
but you can create a custom airflow-specific bus.

288

Chapter 6 Data P c                  - d

events_client.put_events(

)

From EventBridge we can use a Lambda target to invoke our Log Analysis Agent. The
agent can retrieve and analyze all the relevant logs for that specific pipeline execution
and provide insights and analysis. The agent writes its analysis to S3 and sends a
notification to the data engineer using Amazon SNS.

As capabilities improve, data teams could take this further to implement self-healing
workflows, which at this point are still highly experimental. For teams that prefer not to
build and manage their own observability agent, there is an alternative.

**Introducing the AWS DevOps Agent**

The AWS DevOps Agent is a managed agent service that remediates existing issues and
anticipates potential problems before they occur, driving ongoing enhancements to
system stability and efficiency. The agent builds a comprehensive understanding of your
infrastructure components and their interdependencies, leveraging observability and
telemetry data, runbooks, code repositories, and CI/CD pipelines. Similar to the AWS
Security Agent featured in Chapter 2, “Data Security and Governance,” the AWS DevOps
Agent was announced in 2025 and was still in preview at the time of writing. Let’s take a
look at how we can adapt this powerful capability for data pipeline observability.

**Create an Agent Space**

You can quickly find the AWS DevOps Agent service by searching for it in the console.
You’ll first create a DevOps agent space (shown in Figure 6-15).

289

Chapter 6 Data P c - d

**_Figure 6-15._** _Creating an AWS DevOps Agent Space_

It is aptly named a “space” because you’re creating more than just the agent. There’s
also a web app and portal that you can use to monitor and instruct your agent.

**Managing Agent Access to AWS Resources**

You can choose to auto-create a new DevOps agent role that you can use to manage
agent access to AWS resources. Figure 6-16 shows the options for role creation.

290

Chapter 6 Data P c                  - d

**_Figure 6-16._** _Managing Agent Access to AWS Resources_

Access to AWS resources is managed like any IAM role. The types of resources it may
need access to could include CloudWatch logs, the Glue jobs themselves, or S3.

**Enable Web App Access**

There’s a web app that provides visibility including the agent’s capabilities and
configuration, and allows for users to direct the agent to perform investigations and
recommend preventive measures. Figure 6-17 shows how to connect our web app to an
IAM Identity Center instance.

291

Chapter 6 Data P c - d

**_Figure 6-17._** _Manage User Access to the Web App with IAM Identity Center_

The role that’s created is the user role that will be used to authenticate and authorize
access to the DevOps agent web app. This is different from the role we created previously
that gave the agent access to AWS resources to perform investigations.

**Managing Agent Capabilities**

You can navigate to the agent space after the agent space is created. From this console
screen, you can view the topology graph of the account’s resources (as a graph) and
define capabilities for the agent, including multiple AWS accounts, webhooks to allow
external applications to trigger the agent, CI/CD pipelines, and SIM ticket queues.

Clicking “operator access” from the agent space launches the web app. It provides a
portal into three main features: DevOps Center, Incident Response, and Prevention. The
console view is shown in Figure 6-18.

292

Chapter 6 Data P c                  - d

**_Figure 6-18._** _Operator Access to AWS DevOps Agent Web App_

I injected a syntax error in a Glue job and ran it. I then asked my DevOps Agent to
investigate any failed Glue jobs in the past 3 hours. It performed about 27 steps that
included retrieving information, including logs and job codes, planning, and analysis to
identify the Glue job that failed and the reason for the failure. Figure 6-19 shows a brief
excerpt of the long record of its investigation.

293

Chapter 6 Data P c - d

**_Figure 6-19._** _AWS DevOps Agent Incident Response Investigation_

Just like agents generally, the more artifacts that are created, including logs, metrics,
and traces, but also alarms in CloudWatch, the more data points the DevOps agent can
consume and provide actionable intelligence on for your AWS workloads. We can expect
managed agents to get more capable and robust as time goes on.

In this chapter, I presented best practices for evaluating and implementing data
pipeline orchestration, including separating concerns, interoperability, and control flow
management, managing schema evolution, and understanding and defining timeto-­answer SLAs from the business. I demonstrated how to implement data pipeline
orchestration using AWS Step Functions and Amazon Managed Workflows for Apache
Airflow (MWAA). I demonstrated how to use Kiro CLI to generate valid definition files

294

Chapter 6 Data P c                  - d

for Step Functions and Airflow DAGs that can implement complex orchestration logic.
I described how to implement the three pillars of observability—logging, metrics, and
traces—for data pipelines in an AWS context. I presented solution architecture for a Log
Analysis Agent that can ingest and analyze Airflow and Spark logs to troubleshoot errors
and discover optimizations. I also demonstrated the major features of the AWS DevOps
Agent, a frontier agent that applies DevOps expertise in your AWS environment.

In the next chapter, we’ll explore how to extract and enrich unstructured data with
generative and agentic AI.

295

**CHAPTER 7**

## **Multimodal Data** **Extraction and Enrichment** **with Amazon Bedrock** **and AWS ML Services**

When humans process unstructured data the old-fashioned way, we employ a cadre
of sophisticated capabilities our brain has learned and refined since birth. Eventually,
a human’s ability to identify objects, faces, and text from images or words and sounds
from audio is automatic, effortless, and implicit. Machines attempt to mimic these
capabilities with deep learning neural network models iteratively trained on very large
datasets. This may seem obvious, but it’s worth reiterating: AI that synthesizes human (or
above-human) capabilities as digital solutions can instantly scale to meet the needs of a
business, where the challenges of hiring and managing a human workforce are no longer
the limiting factor.

Extracting data is a critical step in any complex data pipeline that processes unstructured
data. What are we extracting from unstructured data? We’re extracting structure and
meaning from the unstructured data. Digital images as data are just pixels. What do the pixels
represent? They represent objects, entities, the setting or context, and how it all relates to one
another. Facial expressions can reveal sentiment. Audio is a representation of waveforms
that we interpret as sounds, music, or speech. Videos are just frames of images composed of
pixels that change through time. What is being communicated? Does it have meaning? Can
we extract this meaning and derive insights that add value to our business? In this section,
I’ll break down the data extraction methods for each type of modality, demonstrating where
generative AI augments and enhances the capabilities of traditional machine learning.

297
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_7](https://doi.org/10.1007/979-8-8688-2199-8_7#DOI)

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

I’ll explore both the newest AWS services that provide a fully managed and abstracted
experience as well as other AWS generative AI and machine learning services. It’s
important to note some universal differences. The first is that AWS ML services are
purpose-built and provide an API with a response object that is highly structured, domainspecific nested JSON. The response includes confidence scores for the inferences made.
Using Amazon Bedrock multimodal generative AI models directly, we may discover new
insights from the source content, but it will not produce a deterministic or domain-specific
output as the corresponding AWS ML service. The combination of the two together
presents an opportunity to exploit the best of both technologies. Amazon Bedrock Data
Automation is a more managed service that attempts to bridge this gap. For general AI
enrichment in Amazon Redshift data warehouses, see Chapter 10, “Data Warehousing with
Generative AI and Text-to-SQL Reporting with Amazon Redshift.”

In this chapter, I’ll demonstrate the capabilities of Amazon Bedrock Data
Automation for multimodal data extraction. I’ll discuss and compare the capabilities of
other AWS services utilizing both probabilistic and generative AI approaches for each
of the modalities: images, video, audio, and text. I’ll dive deep on Intelligent Document
Processing (IDP), a very common use case spanning many industries. IDP consists of
processing documents—as scanned images or PDFs—to extract data from form elements
like key-value pairs, tables, or even visual elements like charts and graphs.

**Amazon Bedrock Data Automation**

Amazon Bedrock Data Automation (BDA) provides developers with tools to process and
analyze unstructured multimodal content through a unified API. The service provides
advanced extraction capabilities for various content types, including documents, images,
audio, and video files, to enable the automation of three specific data-centric workflows:

1) Retrieval-augmented generation (RAG)

2) Intelligent document processing (IDP)

3) Media analysis

By addressing common challenges in content processing—from document splitting
and classification to data extraction, output normalization, and validation—BDA
can help organizations scale their data processing operations by abstracting away
the complexity. This section examines the service’s key capabilities and its role in
streamlining multimodal content processing workflows.

298

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

One of the challenges with incorporating generative AI into data pipelines is ensuring
a structured and deterministic output. Blueprints in BDA address this challenge.
Blueprints are pre-configured templates that provide standardized workflows and a
defined output structure for data processing tasks. Figure 7-1 shows the console view for
the 41 sample blueprints that are available to use.

**_Figure 7-1._** _Console View of Amazon BDA Sample Blueprints_

Using the bank statement blueprint and a sample bank statement, we can see the
power of this template in Figure 7-2.

299

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

**_Figure 7-2._** _AWS Console View of BDA Blueprint Extraction of a Bank Statement_

The blueprint provides the list of fields, instructions, field types, and names for
each. “Table” fields capture tables embedded in the document. The results I can retrieve
include a JSON file with all the fields and extracted data, but also bounding boxes and
confidence scores for each. This provides “best of both worlds” capabilities for document
extraction. Additional CSV files for table and non-table fields are also generated.
Utilizing this service from the SDK requires that you perform a number of steps to define
parameters that are then passed into the invocation method.

First, we’ll start by creating clients for the service API and runtime.

import boto3
bda_client = boto3.client('bedrock-data-automation')
bda_runclient = boto3.client('bedrock-data-automation-runtime')

You’ll use the client to create a BDA project and the runtime client to invoke
extraction jobs. Project creation requires metadata such as name, description, and
deployment stage. You’ll also specify standard and custom output configurations.

300

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Standard configuration is defined in a JSON object that includes general extraction
settings for each modality. Here’s a configuration snippet for the document modality:

output_config = {

}

Refer to the BDA documentation for details on the JSON format for additional
modalities and their corresponding parameters.

Next, define the custom configuration to specify which blueprints to apply to your
documents. The “xx_blueprint_arn” variables would contain the Amazon Resource
Name (ARN) of the blueprints you choose or create.

custom_config = {

You can use the override configuration parameter to enable page splitting of multipage documents. I’ll show this in the next section.

301

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

BDA supports the concept of a project, which allows you to define data extraction
preferences for workflows involving multi-document PDFs. When document splitting is
enabled, BDA can take a PDF containing multiple logical documents (such as an employee
onboarding package) and automatically split them into separate documents for independent
processing. Each document is then matched to the appropriate blueprint for field extraction.

For example, consider automating an employee onboarding process where a single
PDF contains identity documents, an I-9 form, a direct deposit form, a W-4, and other
company-specific forms. With document splitting enabled, BDA will:

1. Split the PDF into individual logical documents based on semantic

boundaries

2. Match each document to the appropriate blueprint

3. Extract all configured fields from each document

4. Write the structured data to your specified S3 output location

First, define the override configuration to enable document splitting:

override_config = {

}

With all the configuration parameters defined, we can create the BDA project:

response = bda_client.create_data_automation_project(

)

project_arn = response['projectArn']

302

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Next, construct the BDA profile ARN. Replace {region} and {account_id} with your
AWS region and account ID:

dataAutomationProfileArn = 'arn:aws:bedrock:{region}:{account_id}:dataautomation-­

With your S3 bucket locations defined, invoke the asynchronous BDA job using the
project:

response = bda_runtime_client.invoke_data_automation_async(

)

Once the job is launched, poll for completion status:

invocation_arn = response['invocationArn']
in_progress = True

while in_progress:

303

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

BDA provides valuable abstraction for document processing workflows, particularly
when handling multi-document PDFs or standardized forms. For use cases requiring
more granular control over the extraction specifications, Amazon Textract may be more
appropriate. I’ll explore these alternatives and their specific capabilities later in the
chapter.

**Intelligent Document Processing (IDP)**

A special use case of image analysis that is relevant across many industries and
especially generative AI is intelligent document processing (IDP). Highly regulated
industries or the government still collect or report information via forms and
documents—IRS tax forms, financial reports and statements, insurance claim forms,
patient health intake forms, work orders in facilities maintenance, compliance, and audit
reporting. These forms are the mechanism for how information is communicated by and
between people and organizations. While originally intended to be read and processed
by humans, in modern cloud-native architectures, intelligent services are doing this
work. In the generative AI context, data extracted from documents are the lifeblood of
LLMs. The ability to automate the extraction of data from documents at scale is a critical
support function data engineers serve for generative AI model development.

IDP is a well-worn topic that I won’t be covering comprehensively. Instead, I’ll
focus just on the key integration points and differentiators between AWS ML services
and transformer-based models. In this section, I’ll present the AWS ML services for
document processing, Amazon Textract and Amazon Comprehend, and compare their
capabilities to transformer-based models like Amazon Nova or Anthropic Claude.

To set the context, it’s important to understand the key functions of an IDP workflow,
including classification, extraction, and enrichment, which I depict in Figure 7-3. There
might be other stages for IDP in a business workflow context, such as human-in-theloop review and validation, which are not included for this example.

304

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

**_Figure 7-3._** _Data Processing Stages for Documents_

From a data engineering standpoint, validating the document type ensures that the
input is as expected and the right document processing pipeline is being invoked.
Classification of documents is performed extremely well using generative AI models.
Amazon Comprehend also offers the option of creating a custom classifier and providing
a training data set to train a probabilistic model to perform a similar function. In
the interest of space, I won’t be presenting this option but instead will focus on the
classification capability that generative AI can deliver.

For this and other demos in this chapter, I use sample documents published as part
of the open-source aws-samples/amazon-textract-code-samples project, available on
GitHub. Figure 7-4 shows the patient intake form I’ll use for this example.

305

Chapter 7 MULTIMODAL DATA EXTRACTION AND ENRICHMENT WITH AMAZON BEDROCK AND

AWS ML SERVICES

**_Figure 7-4._** _Sample Patient Intake Form_

The prompt I used simply specified an exclusive set of classification categories. I also
specified that I wanted the response in JSON composed of two parts, the classification,
and the explanation. Retaining the explanation provides auditability in the event a
document was misclassified.

_Classify the following document as one of the following categories:_

_[Medical, Employment, Tax, Lending, Expense, Insurance] and_
_only provide the classification and explanation in a JSON object in_
_this format {“classification”: “[Category]”, “explanation”:”[Explan_
_ation]”}._

306

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

The response from Claude:

{
"classification": "Medical",
"explanation": "This is a medical intake form containing patient
information, emergency contacts, and COVID-19 screening questions. It
includes personal health information and symptoms assessment, which is
typical of medical documentation used in healthcare settings."
}

My other tests included a mortgage document, a pay stub, a vaccination card,
an insurance claim form, and an expense report. Claude classified each document
according to my custom classification set with 100% accuracy. No special model training
or data set curation was needed to achieve this. The conclusion you should draw is
that for many classification use cases, industry leading generative AI models perform
extremely well.

**Note** A
with high accuracy but at a fraction of the cost. A E
managed service that makes it easy to test multiple models against defined tasks
to identify which models perform with acceptable accuracy at the lowest cost.

I want to take this a step further to understand how much control I have over the
model if my classification task is very detailed, domain-specific, or beyond general
knowledge. To perform this experiment, I provided as context examples that were
deliberately mislabeled. The goal here is to see if the model would follow my instructions
for classification over its own general knowledge training.

I provide this prompt to the model, which included mislabeled category examples:

Consider the following category classifications based on the
examples provided only when evaluating the document text below
and determining a category classification.

Categories = {

"The new smartphone features a powerful processor and

advanced camera technology.",

307

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

"Artificial intelligence is revolutionizing various

industries.",
"Cloud computing offers scalable solutions for businesses

of all sizes.",
"The latest software update includes improved security

features.",
"5G networks promise faster data speeds and lower latency."

"The team won the championship after an intense final

match.",
"The athlete broke the world record in the

100-meter dash.",
"Football fans eagerly await the upcoming World Cup

tournament.",
"The basketball player scored a triple-double in last

night's game.",
"Tennis enthusiasts are excited about the Grand Slam

tournament."

"The new movie received critical acclaim for its

innovative storytelling.",
"The pop star's latest album topped the charts in multiple

countries.",
"The streaming service announced several new original

series.",
"The actor won an award for their outstanding performance

in the drama.",
"The highly anticipated video game sequel will be released

next month."

}

Evaluate the following document text and provide a category
classification only with no explanation:

308

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

“The cutting-edge smartwatch combines state-of-the-art health
monitoring sensors with seamless integration to cloud-based
artificial intelligence, leveraging 5G connectivity for real-time data
analysis and personalized insights, all protected by robust security
protocols and powered by an energy-efficient microprocessor.”

The model classified the input as “Sports,” which is consistent with the examples I
provided in the prompt. This confirms that the model followed my instructions instead
of relying on its own training. By utilizing prompt engineering best practices, for
example, including detailed and specific instructions with examples in the context, it will
perform custom classification with high accuracy.

Now that we’ve confirmed how generative AI will perform on classification tasks, let’s
explore data extraction from documents.

**Note** Many generative A A
accept images as part of the input. H
the service cannot accept as inputs directly. A
convert the document into a supported format. T

Using machines to extract data from documents was always a daunting task for data
engineers to solve. Documents and forms can have various elements that are easily
readable by humans but a significant challenge for machines. Imagine all the ways a form
could be constructed to capture and communicate information! It might include formbased key-value pairs, tables, checkboxes, free text boxes, or circled items. It could include
numerical or monetary values. The input could be typed or handwritten. Luckily, these
tasks are getting easier thanks to the capabilities of AWS ML services like Amazon Textract
and multimodal generative AI models like Amazon Nova and Anthropic Claude. In this
section, I’ll explore the data extraction from forms using these two approaches.

Complex document types like MS Word are not supported as inputs. PDF is the most
widely supported by many leading models hosted in Bedrock. Depending on how your
documents are generated, you may need to perform some preprocessing to convert
documents to a supported format for ingestion by your chosen method. Document
conversion tools are readily available, but this is out of the scope of the book.

309

Chapter 7 MULTIMODAL DATA EXTRACTION AND ENRICHMENT WITH AMAZON BEDROCK AND

AWS ML SERVICES

Figure 7-5 shows a sample document sourced from a collection of public documents
available from Kaggle <sup>1</sup>, which I’ll use for our comparison.

**_Figure 7-5._** _Sample of a Completed Form_

Reviewing this document, we see that it has several field prompts with entered
values, a section with multiple options with affirmative choices marked with “X,” free text
areas with long narrative text, and a table with rows and columns with values entered
in some of the cells. There’s also a document ID number printed vertically in the lower
right margin.

Processing this document through Amazon Textract’s analyze document API yields
a highly verbose and detailed JSON response that includes confidence scores, bounding

1 [https://www.kaggle.com/](https://www.kaggle.com/)

310

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

boxes for all detected values, and parent and child identifiers for keys and associated
values. All this detail and structure would require a lot of effort to parse. Luckily there
is a robust helper tool to assist us. The project _Textractor_ <sup>2</sup> performs a number of tasks,
including parsing, overlaying the bounding boxes on the image, pretty printing the
response, and simplifying navigation of the document using geometric information and
relations to identify hierarchical key-value pairs. Overlaying the bounding boxes onto
the image is an important feature of a human-in-the-loop review. Amazon Augmented
AI (Amazon A2I) is a managed service that provides an overlay of bounding boxes for
extracted fields for reviewers to confirm or change. Amazon A2I can be seamlessly
integrated into an enterprise IDP workflow.

As I mentioned in the previous section, Textract offers synchronous and
asynchronous operations. Because I am building data pipelines and not integrating
these services into applications that serve customer experiences, I’m going to
exclusively use the asynchronous operations. With my Boto3 Textract client, I will
use the start_document_analysis method and specify the parameters in the JSON
configuration object.

Here is the sample Boto3 Python script to analyze our sample document:

import boto3

textract_client = boto3.client('textract')

# S3 bucket and file details
bucket_name = 'data-engineering-with-generative-ai'
file_name = 'textract/demo-documents/2025325926.png'
out_file_name ='textract/demo-documents/processed/'
response = textract_client.start_document_analysis(

2 [https://github.com/aws-samples/amazon-textract-textractor](https://github.com/aws-samples/amazon-textract-textractor)

311

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

)

The response includes the JobId and other metadata:

{'JobId': '6d6a7043f713d1a78f7fb0b1c17582aca330417da758fa7edd5878XXXXXXX',
'ResponseMetadata': {'RequestId': '3b930fb5-9520-4cf2-bfc3-2f6XXXXXX',
'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid':
'3b930fb5-9520-4cf2-bfc3-2f6XXXXXX', 'content-type': 'application/x-amzjson-1.1', 'content-length': '76', 'date': 'Sun, 05 Jan 2025 20:20:00
GMT'}, 'RetryAttempts': 0}}

**Note** T
is to specify an S3 location in the OutputConfig parameter. T
get_document_analysis method using the JobId created by the start_document_
analysis method.

You can use Textractor to read the response document and extract the features
needed. The documentation provides a step-by-step guide for running the library in a
Lambda function, making it well-suited for scalable and serverless data pipelines.

Because Textract has been trained on many different types of documents, it’s able
to process documents it’s never seen before with high accuracy due to a concept called
transfer learning. Transfer learning in machine learning is when a model is able to
apply what it learned from its training set to perform better on similar tasks it has not
been trained on. For our example document, the “justification category” was extracted
correctly, indicating that “STRAIGHT REPLACEMENT” was the only one selected.

Similarly, Textract performed with 100% accuracy on the similar “indicate ‘yes’ or
‘no’ as appropriate” section. Table 7-1 shows the results.

312

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

**_Table 7-1._** _Extracted Table for “Indicate Yes or No As Appropriate”_
_Section of Document_

**Key** **Value**

IS PR E T PR AR R E P RT PR T No

DOE PR E T PR E A R AVINGS?: No

NUMBER H R PE P E AVE NOT E E TE

NUMBER A AR E PE P E AVE NOT E E TE

DOE PR E T RE RE RE RRE No

DOE PR E T RE RE E EER PP RT Yes

DOE PR E T RE RE PP RT No

DATE T E TTE T PERAT A A Feb-95

DATE RE RE A APPR A May-95

Textract performed well even for the table at the bottom of the form, properly
determining rows and columns and the populated values in the cells.

Now let’s see how Anthropic Claude performs on the same document. I instructed
Claude to analyze the image of the document and structure its response in JSON. My
simple prompt accompanying the image as input was the following:

_Analyze this document, extract all the content, and format the_
_response in JSON._

The response is clean, simple, and human-readable. Note that I’ve skipped some of
the response for brevity, which is indicated by an ellipsis.

{

313

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

...

}

Claude’s response shows differences from Textact. The title value is misreported
by Claude as “Four-trialer” instead of “Fourdrinier.” However, it did find and report the
document number. The key values for the tabular options are accurate. The identifiers
in the JSON are inferred from the document’s extracted keys and are reported in lower
CamelCase. These are pretty good results that require a lot less work.

Since we have great results from both but also some gaps from both, the optimal
strategy to yield the most accuracy could be to combine the results from both. Using

314

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Claude to arbitrate, I got an updated JSON response that corrected the title value using
Textact’s result and kept other features it detected that Textract missed.

_{_
_"documentMetadata": {_
_"pageNumber": 3,_
_"documentType": "PLANNED PROJECT DATA SHEET"_
_},_
_"projectDetails": {_
_"appropriationNumber": "PLANNED",_
**_"title": "Fourdrinier Stock Delivery",_**
_"date": "9/1/94",_
_"originator": "W._
_"location": "Park 500",_
_"coordinator": "E._
_"department": ""_
_}_

[Truncated for space]

Claude provided a summary of its findings:

_This combined JSON output incorporates the structured information from both_
_Claude's and Textract's analyses, using Textract's output to validate and_
_provide additional details where applicable. The structure largely follows_
_Claude's output, with some modifications and additions based on Textract's_
_analysis:_

_Added a documentMetadata section with page number and_

_document type._

_Kept the detailed structure of project details, justification_

_categories, and project questions from Claude's analysis._

_Retained the spending forecast structure from Claude's_

_analysis, as it was more detailed._

_Included the document ID from Textract's analysis._

315

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

This combined output provides a comprehensive representation of the document’s
content, leveraging the strengths of both analyses.

If we were to express this as solution architecture, it would look like Figure 7-6.

**_Figure 7-6._** _Combining Data Extraction Results from Textract and Claude_

In summary, Amazon Textract offers a highly sophisticated and robust toolset for
accurate OCR and data extraction of complex forms. Textract requires more effort and a
few different pieces to help process the result but may provide a decent complement to
generative AI extraction. You may find that combining these capabilities (if the budget
allows) can achieve a superior result.

In our final document processing section, we’ll explore data enrichment.

I’ll define enrichment broadly to mean any augmentation or redaction of extracted data.
There are many use cases where post-processing is required. It could be redacting PII
or PHI, moderating offensive content, identifying important entities like companies or
people, or summarizing or interpreting the extracted content to provide sentiment or
topic analysis.

316

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

For our sample document, I’ve created 2 fake customer reviews with an exaggerated
amount of PII and saved it in a file called customer_review.txt. Here is the text of the file.

Review 1:
"I purchased this deluxe beach chair from Seaside Supplies last month and
had it shipped to my home at 742 Ocean View Dr, Miami FL 33139. While the
quality seems decent, I had issues with delivery and had to call customer
service at 888-555-0123 multiple times. My account rep Sarah Johnson wasn't
very helpful when I explained the problems. At least my AMEX card ending in
4567 was refunded promptly."
Review 2:
"This is the worst chair ever! I took it to North Shore Beach in Honolulu
and it broke on day one. Had to go to Dr. Michael Williams at Beachside
Urgent Care (patient #12345) after it collapsed and hurt my back. My email
is jsmith1985@email.com if anyone wants details about this dangerous
product. My cell is (305) 555-8989. Don't waste your money like I did
stick with chairs from BeachMaster Pro instead."

First, we need to detect entities with potential PII. Using the Boto3 library, the
Amazon Comprehend method we’ll call is detect_pii_entities. I’ll provide the
function calls directly; you will want to structure this code as helper functions.

import boto3
import json

comprehend = boto3.client('comprehend')

response = comprehend.detect_pii_entities(

The JSON response object includes a confidence score, the entity type, and
beginning and ending offsets. These offsets can be used by a script to replace the text of
an entity with redaction text.

Here’s what our response object looks like for our sample text:

[{'Score': 0.9999951720237732, 'Type': 'ADDRESS', 'BeginOffset': 113,
'EndOffset': 146}, {'Score': 0.9999759197235107, 'Type': 'PHONE',

317

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

'BeginOffset': 243, 'EndOffset': 255}, {'Score': 0.9996626377105713,
'Type': 'NAME', 'BeginOffset': 287, 'EndOffset': 300}, {'Score':
0.9999651908874512, 'Type': 'CREDIT_DEBIT_NUMBER', 'BeginOffset': 384,
'EndOffset': 388}, {'Score': 0.9902966022491455, 'Type': 'ADDRESS',
'BeginOffset': 468, 'EndOffset': 485}, {'Score': 0.9990436434745789,
'Type': 'ADDRESS', 'BeginOffset': 489, 'EndOffset': 497}, {'Score':
0.999915599822998, 'Type': 'NAME', 'BeginOffset': 540, 'EndOffset':
556}, {'Score': 0.9999971389770508, 'Type': 'EMAIL', 'BeginOffset':
648, 'EndOffset': 668}, {'Score': 0.9998790621757507, 'Type': 'PHONE',
'BeginOffset': 734, 'EndOffset': 748}]

The following Python script will replace the text of the detected entities from our
sample customer reviews using the offsets in our detected entities response object.

for entity in sorted(entities, key=lambda x: x['BeginOffset'],
reverse=True):

You can customize this further to reflect the requirements of the business. For
instance, you may want to redact customer names but retain account manager names.
You could achieve this by filtering entities to exclude account managers from the
redaction. There are over 30 entities that Comprehend will detect, and not all of them
may be relevant depending on the use case.

After running the redaction script on our original text, we see the redacted version:

Review 1:
"I purchased this deluxe beach chair from Seaside Supplies last month and
had it shipped to my home at [REDACTED-ADDRESS]. While the quality seems
decent, I had issues with delivery and had to call customer service at

[REDACTED-PHONE] multiple times. My account rep [REDACTED-NAME] wasn't
very helpful when I explained the problems. At least my AMEX card ending in

[REDACTED-CREDIT_DEBIT_NUMBER] was refunded promptly."

318

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Review 2:
"This is the worst chair ever! I took it to [REDACTED-ADDRESS] in

[REDACTED-ADDRESS] and it broke on day one. Had to go to Dr. [REDACTEDNAME] at Beachside Urgent Care (patient #12345) after it collapsed and hurt
my back. My email is [REDACTED-EMAIL] if anyone wants details about this
dangerous product. My cell is [REDACTED-PHONE]. Don't waste your money like
I did

Now let’s try the same using Anthropic Claude. I’ll provide it with the same sample
customer reviews and direct it to identify and redact entities using the following prompt:

Analyze the following customer reviews, detect any PII entities, redact
the entities using the format "[REDACTED-TYPE]" where TYPE is the type of
entity (i.e. ADDRESS, NAME, BANK-ACCOUNT-NUMBER, PHONE-NUMBER, EMAIL)

The result showed some differences with the Comprehend result. Here is Claude’s
response:

Here are the reviews with PII entities redacted:

Review 1:
"I purchased this deluxe beach chair from Seaside Supplies last month and
had it shipped to my home at [REDACTED-ADDRESS]. While the quality seems
decent, I had issues with delivery and had to call customer service at

[REDACTED-PHONE-NUMBER] multiple times. My account rep [REDACTED-NAME]
wasn't very helpful when I explained the problems. At least my AMEX card
ending in [REDACTED-BANK-ACCOUNT-NUMBER] was refunded promptly."

Review 2:
"This is the worst chair ever! I took it to North Shore Beach in Honolulu
and it broke on day one. Had to go to [REDACTED-NAME] at Beachside Urgent
Care (patient #[REDACTED-BANK-ACCOUNT-NUMBER]) after it collapsed and hurt
my back. My email is [REDACTED-EMAIL] if anyone wants details about this
dangerous product. My cell is [REDACTED-PHONE-NUMBER]. Don't waste your
money like I did

319

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

It provided an explanation for its determination of PII and what it chose to redact.
Entities detected and redacted:

     - Addresses

     - Phone numbers

     - Names

     - Bank/Account numbers

     - Email addresses

Business names (like Seaside Supplies, Beachside Urgent Care, and BeachMaster
Pro) and location names (like North Shore Beach, and Honolulu) were left intact, as they
are public business/location information rather than PII.

Claude’s response correctly identifies that the business names of the seller and a
competitor were not PII and thus not redacted. It misidentified the patient number as a
bank account number. Comprehend did not detect the patient number as PII (or likely
privileged). Similar to the Textract result, by combining the two results, each result can
act as validation and error correction for the other.

There are many other ways to enrich extracted data from documents that I didn’t
have the space to include. Additional topics include sentiment analysis and data
cleansing and validation, which I’ll leave to the reader to explore on their own.

Let’s now explore image analysis.

Before generative AI, text extraction from images was performed using Convolutional
Neural Networks (CNNs) and Optical Character Recognition (OCR) models. CNNs
extract features at different levels of abstraction. At the lowest level, it identifies edges,
corners, and textures. At the next level, the model detects shapes, patterns, and parts of
objects. At the highest level, the model is extracting complete objects and interpreting
relationships between those objects to discern meaning in complex scenes. OCR uses
feature extraction and pattern recognition.

Transformer models divide the image into non-overlapping patches. It leverages
CNNs to extract higher-level features and transform patch vectors into feature vectors
that encapsulate the visual information. Positional embeddings, which indicate where
on the original image the patch is located, are added to the feature vector. This sequence

320

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

of vectors is fed into a self-attention mechanism. This is a lot of technical jargon that
means essentially that the model has a mechanism to determine how much attention it
should pay to certain inputs when making decisions about other inputs. This is called
_attention scoring_ . Figure 7-7 depicts this basic vision transformer architecture.

**_Figure 7-7._** _Transformer Architecture_

For each patch of the image, three specialized vectors are created as
described below:

     - **Query (Q)** : Features from the patch that is being searched (edge,
color, texture, etc.). It represents “what we’re looking for” or “what
we’re searching with.”

     - **Key (K)** : Features from all patches that can be matched against
queries.

     - **Value (V)** : Learned representations created through linear
projections of the patch data that will be aggregated based on
attention weights.

321

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

The attention score indicates the importance of each patch in relation to the query
word. The model calculates the attention score by taking the dot product of the Query
vector and the Key vector of each word for every other word. Finally, these scores are
normalized using the Softmax function, and the Value vector is multiplied by these
normalized scores to yield a weighted sum. The weighted sum determines the output
returned to the user.

To aid in your understanding of the differences of these model architectures, I’ve
highlighted the differences between these model architectures in Table 7-2.

**_Table 7-2._** _Comparison of CNN and OCR Models vs. Transformer Models_

**Aspect** **CNNs and OCR Models** **Transformer-Based Models**

A Layered structure with convolutions and
pooling (CNNs); specialized pipeline for text
extraction (OCR

Unified, end-to-end transformer
architecture with self-attention
mechanisms

Learned representations from
entire input data; captures global
dependencies through self-attention

E
handles feature extraction, positional
encoding, and context modeling

H
parallel through self-attention layers

Vision Transformers (ViT ETR
(Detection Transformer), CLIP
(Contrastive Language–Image P
training)

Feature
E

Focuses on small patches or regions of the
image; spatial hierarchies; CNNs extract
features at multiple levels (edges, textures,
shapes, objects)

Training R
separate training for different components
(CNN for features, OCR

Inference Limited parallelism; processes data
sequentially through layers

E A R Tesseract
(OCR

What you’ll notice about the two types of models is that transformer-based models
can achieve high parallelism due to its self-attention layer architecture. Traditional
CNNs and OCR models process data sequentially through layers. This is an important
distinction when scalability and throughput are constraints.

322

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

In the next several sections, I’ll compare the capabilities and features of AWS ML
services and AWS-hosted generative AI services for image-based data extraction tasks.
We’ll look at image processing for object detection and facial recognition.

In this section, I’ll demonstrate how to perform object detection using Amazon’s image
recognition service, Amazon Rekognition, its document extraction service, Amazon
Textract, and the multimodal capabilities of Anthropic Claude, hosted on Bedrock.

First, we’ll need to set up a testbench to run our experiments. In AWS, we can use
JupyterLab notebooks in SageMaker Unified Studio. In our notebook, we will create
Boto3 clients for Amazon Rekognition and Amazon Bedrock. We’ll also need libraries to
handle images and base64 encoding.

import time
import json
import boto3
import base64

from PIL import Image
from IPython.display import display

bedrock_client = boto3.client('bedrock-runtime')
rekognition_client = boto3.client('rekognition')

For the first image, I’ll use the stock photo of a skateboarder performing a kickflip
(see Figure 7-8), which is provided in the label detection demo section of the AWS
console.

323

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

**_Figure 7-8._** _Amazon Rekognition Label Detection Demo in the AWS Console_

First, I create three helper functions to prepare the image and parameters for
invoking the two services for our comparison.

Helper function 1 generates a base64 encoded string of the image to pass into the
Bedrock API:

def encode_image (label_image_path : str ):

encoded_string = base64.b64encode(image_file.read()).

decode('utf-8')

Helper function 2 creates the JSON object we will use as an input for the
Bedrock API:

def claude_v2_request (base64_img, prompt):

324

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

}

Now with these helper functions, we can invoke the services and get responses. For
Anthropic Claude, I can invoke the model through Bedrock’s common API:

For Rekognition, I’ll need a 3rd helper function that reads the image as bytes to pass
into the Rekognition service API:

def get_image_bytes(label_image_path):

325

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Now with our image converted to bytes, we can invoke the Rekognition service:

You’ll notice that the Rekognition API provides some additional features like setting
the maximum number of labels to detect and defining a confidence level threshold.

I can write some printer-friendly display code to show the response. First the
Rekognition response object, then Bedrock.

for label in labels:
print(f"Label: {label['Name']}, Confidence:

{label['Confidence']:.2f}%")

Rekognition Response:

Label: Neighborhood, Confidence: 100.00%
Label: City, Confidence: 99.98%
Label: Road, Confidence: 99.97%
Label: Street, Confidence: 99.97%
Label: Urban, Confidence: 99.97%
Label: Person, Confidence: 98.33%
Label: Car, Confidence: 97.39%
Label: Wheel, Confidence: 96.63%
Label: Building, Confidence: 95.27%
Label: Metropolis, Confidence: 93.71%

The output here just shows labels and confidence levels, but the nested JSON
response object provides much more, including label categories, aliases of labels, and
detailed object positioning defined as bounding boxes.

Rekognition’s response doesn’t identify the skateboarder as the main subject of the
photo. Since I limited the number of labels detected to 10, it returned 10 labels with the
highest confidence scores, and the skateboarder wasn’t one of them. Higher accuracy
and confidence are driven by how complete and robust the training set is. If we assume

326

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

that the training set likely included fewer images of skateboards and skateboarders than
buildings, cars, and people, it explains why the label for skateboard might return a lower
confidence score. If I increase the label limit to 20, the label “Skateboard” appears at
number 18 with an 80.9% confidence.

The lesson here is to be sure to set the label limit and confidence thresholds
appropriately to capture less common labels.

Now let’s take a look at Claude’s response:

Here are the key elements I can label in this image:

1. Skateboarder
2. Skateboard
3. City street
4. Parked cars
5. Buildings
6. Trees
7. Crosswalk
8. Sidewalk
9. Shadow
10. Clear sky

The image captures an urban scene with a person performing a skateboard
trick in the middle of a city street lined with parked cars and buildings.

This response demonstrates the power of the transformer architecture. Not only
do we detect the label “skateboard,” but “skateboarder,” which is the core subject of the
photo, and it appears first. The positional embeddings and the multi-head attention
layer were able to determine not just the objects in the photo but what was important.
Instead of “Car,” the label reported is “Parked cars.” Instead of “City” and “Street”
separately, the label is “City street.”

The sentence at the end of the labels provides rich analytical context describing
accurately, from the human interest perspective, what is being portrayed in the photo.

To summarize, Rekognition provides label detection with confidence values, which
can be valuable depending on the business case. Rekognition also supports custom
labels, where you can define your own labels and train a custom version of the service
using training images you provide. The most capable transformer models can provide
human-quality image analysis with context, with the ability to determine the importance
of elements in a complex composition.

327

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Images have a lot of other information that you might not be thinking of but may have
value depending on the industry or use case. For instance, you could replicate the color
palette of a real photo for a client’s branding proposal. Similar to the previous section,
I’ll present the image properties extraction capabilities of Amazon Rekognition and
compare it to a transformer-based model via the Amazon Bedrock service.

Figure 7-9 shows the stock photo of a green car available as a demo in the Amazon
Rekognition console, which I’ll use for our image properties example.

**_Figure 7-9._** _Amazon Rekognition Image Properties Demo in the AWS Console_

In the code examples provided in the Git repository, we have a helper function for
extracting image properties from Rekognition.

def get_rekognition_image_properties(label_image_path):

328

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

The invocation function is detect_labels; however, we indicated it with the _IMAGE__
_PROPERTIES_ value in the _Features_ parameter list. We can also set a limit for the number
of dominant colors we want to extract.

I’ve truncated the results to conserve space. A helper function (not shown) prints the
response with the following format:

Quality:

Dominant Colors:

Color: dimgrey (Hex: #696969, RGB: (105, 105, 105), Pixel

Percent: 13.98%)
Color: darkseagreen (Hex: #8fbc8f, RGB: (143, 188, 143), Pixel

Percent: 12.58%)
Color: blanchedalmond (Hex: #ffebcd, RGB: (255, 235, 205), Pixel

Percent: 11.95%)

Foreground Quality:

Foreground Dominant Colors:
Color: darkseagreen (Hex: #8fbc8f, RGB: (143, 188, 143), Pixel

Percent: 29.97%)
Color: cadetblue (Hex: #5f9ea0, RGB: (95, 158, 160), Pixel

Percent: 24.14%)

329

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Color: darkolivegreen (Hex: #556b2f, RGB: (85, 107, 47), Pixel

Percent: 5.57%)

Background Quality:

Background Dominant Colors:
Color: dimgrey (Hex: #696969, RGB: (105, 105, 105), Pixel

Percent: 20.11%)
Color: darkgrey (Hex: #a9a9a9, RGB: (169, 169, 169), Pixel

Percent: 15.03%)

Color: blanchedalmond (Hex: #ffebcd, RGB: (255, 235, 205), Pixel

Percent: 12.91%)
Color: darkslategrey (Hex: #2f4f4f, RGB: (47, 79, 79), Pixel

Percent: 12.59%)

Again, we see more structured, standardized data with percentages of pixel coverage.
Now let’s test the same image with a transformer-based model in Bedrock using the
following prompt:

Give information about image quality (sharpness, brightness, and contrast)
for the entire image. Also give sharpness and brightness for the foreground
and background of the image
colors of the entire image, foreground, background. Along with textual
descriptions, it gives hex values of the colors with a breakdown of the RGB
values and the percentage of the amount of pixels they occupy in the image.

Once again, I used Anthropic Claude for this example, and this was the response:

Overall Image Quality:

- Sharpness: High, with clear details visible

- Brightness: Medium to high, well-lit scene

- Contrast: Medium, good distinction between elements

330

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Foreground (Car):

- Sharpness: Very high, crisp details on the car

- Brightness: Medium-high, car is well-illuminated

Background (Street):

- Sharpness: Medium, slight blur for depth effect

- Brightness: Medium, balanced lighting on buildings

Dominant Colors:
Entire Image:
1. Mint Green: #A4C5B4

2. Asphalt Gray: #5A5A5A

3. Beige (buildings): #D2C8B6

Foreground (Car):
1. Mint Green: #A4C5B4

2. Chrome Silver: #C0C0C0

Background:
1. Beige: #D2C8B6

331

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

2. Dark Gray: #4A4A4A

3. Sky Blue: #87CEEB

The image has a vintage feel due to the classic car and the color grading,
which emphasizes the mint green of the vehicle against the urban backdrop.

While each of these services provides good detailed quality and color information,
including dominant colors overall and foreground and background colors, they differ
substantially. The transformer-based model can identify what is contextually important
(i.e., “Foreground (Car)”) and choose pixels from the object rather than just the
foreground. To make the differences between each output easier to detect, I listed a
subset of the most notable colors detected along with a sample of the color in Table 7-3.

332

Chapter 7 MULTIMODAL DATA EXTRACTION AND ENRICHMENT WITH AMAZON BEDROCK AND

AWS ML SERVICES

**_Table 7-3._** _Comparison of Image Properties Analysis of Rekognition and Claude_
_Sonnet 3.5_

**Service** **Name** **HEX** **RGB** **Color**

Rekognition dimgrey 696969 105, 105, 105

darkgrey A9A9A9 169, 169, 169

blancedalmond FFEBCD 255, 235, 205

darkseagreen 8FBC8F 143, 188, 143

cadetblue 5F9EA0 95, 158, 160

Claude Asphalt Gray 5A5A5A 90, 90, 90

Chrome Silver C0C0C0 192, 192, 192

Beige D2C8B6 210, 200, 182

Mint Green A4C5B4 164, 197, 180

Sky Blue 87CEEB 135, 206, 235

Amazon Rekognition and Claude Sonnet detect image properties differently, and
if there’s value in capturing more, it may make sense to combine the results from both
depending on the use case and budget.

333

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

**Facial and Emotion Recognition**

Facial recognition is a tricky subject for commercially available transformer models
because of privacy issues and guardrails. This makes Amazon Rekognition better
suited for most facial recognition use cases. As part of its general service, Rekognition
recognizes the faces of celebrities.

Rekognition offers the capability to scan through still images, archived videos, and
live video streams to identify faces that correspond to those stored in a user-managed
database called a face collection. This collection serves as a repository of facial data
under your control. To effectively utilize the system for identifying individuals based
on their facial features, it’s necessary to first create an index of the faces you want to
recognize and then perform searches against that index.

For our example, I’ll use a sample image from the Rekognition console, shown in
Figure 7-10.

**_Figure 7-10._** _Amazon Rekognition—Facial Analysis Console_

So send a request to the Rekognition service for facial analysis; we can use the
detect_faces method.

334

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

The DEFAULT parameter value includes the facial attributes BoundingBox,
Confidence, Pose, Quality, and Landmarks, which will always be returned. The other
facial attributes returned by ALL include AGE_RANGE, BEARD, EMOTIONS, EYE_
DIRECTION, EYEGLASSES, EYES_OPEN, GENDER, MOUTH_OPEN, MUSTACHE,
FACE_OCCLUDED, SMILE, and SUNGLASSES.

A helper function (not shown) prints the response with the following format:

Bounding Box:

Age Range:

Smile:

Eyeglasses:

Sunglasses:

Gender:

Beard:

Mustache:

335

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Eyes Open:

Mouth Open:

Emotions:

Additional attributes that were not shown due to space included pose, quality,
confidence, face occluded, and eye direction. As we see from this response, there’s
a detailed set of attributes reported on with associated confidence scores. This is a
structured and deterministic set of attributes, which differs from what we get from a
transformer-based model.

Using Claude again for consistency, I’ll use the following prompt:

Tell me about the mood and sentiment of the person in the image and perform
a facial analysis.

As you’ll see from the response below, responsible use guardrails kick in, but it then
continues with what the Bedrock service and model’s policy allows.

Claude Response:

I apologize, but I’m not able to perform facial analysis or identify
specific individuals in images. However, I can describe what I observe in
the photo:

The image shows a person driving a bright yellow vintage-style car. They
appear to be smiling broadly, suggesting a cheerful, happy mood. The driver
is wearing large sunglasses and has long blonde hair. They’re holding onto
a white steering wheel and seem relaxed and at ease.

336

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

The overall sentiment conveyed by the scene is one of carefree enjoyment
it has a summery, road trip vibe. The yellow color of the car and the sunny
outdoor setting contribute to the upbeat, positive atmosphere of the image.
The person’s posture and expression indicate they’re likely having an
enjoyable driving experience.

The response is verbose and descriptive and delivered in natural language. It is a
sophisticated response that depicts the person’s sentiment in graphic detail.

The takeaway is that purpose-built services deliver different results than
transformer-based multimodal models; however, the results may complement each
other. In terms of achieving a more structured output, Bedrock Data Automation could
address this with its blueprint feature.

Now let’s look at audio processing.

Many businesses generate or consume audio data. This includes recorded customer
service calls, meeting recordings, or audio from videos or media content. Being able to
accurately transcribe audio into text for further processing is just another skill a modern
data engineer is expected to perform competently. I’ll demonstrate the capabilities of a
purpose-built AWS ML service that performs transcription, Amazon Transcribe, as well
as an open-source transformer model, Whisper.

Amazon Transcribe is an ASR service launched by AWS in 2017 that supports batch
or streaming audio transcription. The service supports dozens of languages and can
identify different speakers in a conversation. Transcribe also allows customization via
a feature called “custom vocabulary,” which is designed to increase the accuracy of
domain-specific words. Transcribe also supports redaction of sensitive PII data.

Whisper is a transformer-based ASR model that was created by OpenAI and
released as open source in 2022. Since its release, it’s achieved significant adoption for
its capabilities. Whisper was trained on 680,000 hours of diverse audio, supports over
100 languages, and achieves human-level performance for English speech recognition
benchmarks. It utilizes an encoder-decoder architecture but includes convolutional
layers for processing raw audio. Another open-source transcription model is Parakeet,
released as open source by Nvidia. Parakeet originally only supported English
transcription but more recently has expanded its multilingual support. Parakeet was not
included in this analysis.

337

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

**Caution** A
frequency and severity that adds risk in safety- or mission-critical settings where
transcriptions require high accuracy. Given these limitations, ensure that the
Whisper model is appropriate for the intended use case.

A Michigan University study <sup>3</sup> released in May of 2024 found that 1.4% of audio
segments transcribed by Whisper included hallucinations. Out of those hallucinations,
38% included “explicit harms such as perpetuating violence, making up inaccurate
associations, or implying false authority.” Researchers and observers reported that the
hallucinations tended to occur amid pauses, background sounds, or music playing or
when the speaker had an accent or language disorder or used broken speech.

Before transformer architecture featuring attention mechanisms, ASR model
architectures included Convolutional Neural Networks (CNNs), Recurrent Neural
Networks (RNNs), Hidden Markov Models (HMMs), or Pretrained Audio Neural
Networks (PANNs). Algorithms like Mel-frequency Cepstral Coefficients (MFCCs) extract
features from audio by mimicking how human ears process sound. Discussion of these
model architectures and algorithms is out of the scope of the book but is mentioned here
for background. Table 7-4 summarizes the differences between traditional ASR models
and transformer-based ASR models.

**_Table 7-4._** _Comparison of Traditional ASR Models vs. Transformer-Based_
_ASR Models_

**Aspect** **Traditional ASR Models** **Transformer-Based ASR Models**

Feature
E

Dependency
Modeling

Mel-frequency Cepstral Coefficients (MFCCs)
or spectrograms

H H
R R
temporal modeling

Learned representations, often
directly from raw audio

Self-attention mechanism for
capturing long-range dependencies

Training Multiple stages and components E

Scalability Sequential processing Parallel processing

3 Koenecke A, Choi ASG, Mei KX, et al. Careless whisper: speech-to-text hallucination harms. In:
_The 2024 ACM conference on fairness, accountability, and transparency_, 2024, pp. 1672–1681.

338

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Like any transformer model, the self-attention mechanism provides generally better
accuracy as words are tested against other words as part of a context-aware capability.
For my audio sample, I simply recorded myself reading the fake customer reviews I
created for the entity detection and PII redaction demo in the previous section.

Here is the raw output of the transcription generated by Amazon Transcribe:

Review one.
I purchased this deluxe beach chair from Seaside Supplies last month and
had it shipped to my home at 742 Ocean View Drive, Miami, Florida 33139.
While the quality seems decent, I had issues with delivery and had to call
customer service at 888-555-0123 multiple times. My account rep Sarah
Johnson wasn't very helpful when I explained the problems. At least my Amex
card ending in 4567 was refunded promptly.

Review too.
This is the worst chair ever. I took it to North Shore Beach in Honolulu,
and it broke on day one. Had to go to Doctor Michael Williams at Beachside
Urgent Care, patient number 12345 after it collapsed and hurt my back. My
email is jsmith1985@email.com. If anyone wants details about this dangerous
product. My cell is 305-555-8989. Don't waste your money like I did. Stick
with chairs from Beachmaster Pro instead.

I notice some minor inaccuracies, like “too” instead of “two.” Transcribe has the
ability to detect and redact PII as part of the transcription process, and there’s an option
to return both the unredacted and redacted transcription.

This was the result of the redacted transcription for the first review:

Review one.
I purchased this deluxe beach chair from Seaside Supplies last month and had
it shipped to my home at [PII]. While the quality seems decent, I had issues
with delivery and had to call customer service at [PII] multiple times. My
account rep [PII] wasn't very helpful when I explained the problems. At
least my Amex card ending in [PII] was refunded promptly. Review too. This
is the worst chair ever. I took it to [PII] in [PII], and it broke on day
one. Had to go to Doctor [PII] at Beachside Urgent Care, patient number
12345 after it collapsed and hurt my back. My email is [PII]. If anyone
wants details about this dangerous product. My cell is [PII]. Don't waste
your money like I did. Stick with chairs from Beachmaster Pro instead.

339

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

This yielded similar results compared to Comprehend or Claude; however, it did
not redact the patient number. As a software engineer, the inherent choice evokes
similarities to the Single Responsibility Principle (SRP), where the optimal design is for
software functions to do only one thing. This means that we would use Transcribe for
transcription and Comprehend or Claude for PII detection and redaction. Even though
we introduce an additional component, we know the capabilities and functionality of
the component rather than having 2 different services performing the task differently. A
reference solution architecture is presented in Figure 7-11.

**_Figure 7-11._** _Solution Architecture for Audio Transcription and Redaction_

Now let’s transcribe the same audio using the Whisper model. Setting up Whisper for
online or batch inference is out of the scope of the book. For online inference, refer to the
AWS blog, _Host the Whisper Model on Amazon SageMaker: exploring inference options_ .
For asynchronous and on-demand inference, refer to the blog I co-authored, _Whisper_
_audio transcription powered by AWS Batch and AWS Inferentia_ .

340

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Using the Whisper model to transcribe my audio generated the following output:

<|startoftranscript|><|en|><|transcribe|><|notimestamps|> Review 1. I purchased
this deluxe beach chair from Seaside Supplies last month and had it shipped
to my home at 742 Ocean View Drive, Miami, Florida 33139. While the quality
seems decent, I had issues with delivery and had to call customer service
at 888-555-0123 multiple times. My account rep, Sarah Johnson, wasn't very
helpful when I explained the problems. At least my Amex card ending in 4567
was refunded promptly.<|endoftext|>

<|startoftranscript|><|en|><|transcribe|><|notimestamps|> Review 2. This is
the worst chair ever. I took it to North Shore Beach in Honolulu and it
broke on day one. Had to go to Dr. Michael Williams at Beachside Urgent
Care, patient number 12345, after it collapsed and hurt my back. My email
is jsmith1985 at email.com if anyone wants details about this dangerous
product. My cell is 305-555-8989. Don't waste your money like I did. Stick
with chairs from Beachmaster Pro instead.<|endoftext|> <|startoftranscript|><|
en|><|transcribe|><|notimestamps|> Thank you.<|endoftext|>

The Whisper model autodetected the spoken language based on its training,
and the transcription includes tags, which can be used to extract chunks of text. The
context-aware self-attention mechanism was able to correctly transcribe the second
review as “review 2” instead of “review too.” It missed an opportunity to transcribe the
email address “jsmith1985 at email.com” correctly and the “Thank you.” at the end is a
hallucination!

The last type of analysis I’ll explore is video analysis.

Video analytics, or video content analysis, uses advanced algorithms and machine
learning techniques to automate analysis of video footage and derive valuable insights.
Video analysis is used to identify objects, recognize faces, track movement, transcribe
speech, and/or interpret complex scenes or interpret emotional states. Applying
generative AI for video analysis is a bit tricky. Even multimodal generative AI models do
not support video formats as an input, so some preprocessing is needed.

341

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Amazon Rekognition Video is a powerful machine learning service that automates
the analysis of video content, which was launched by AWS in 2017. Rekognition Video
uses deep learning algorithms to detect and recognize objects, activities, text, and
people in videos, both in real-time streaming and batch processing modes. The service
can identify thousands of objects (such as vehicles or animals), detect inappropriate
content, recognize celebrities, and track the movement of people throughout a video.
As of 2024, it has found widespread adoption in various industries, including media and
entertainment for content moderation, law enforcement for investigations, and retail for
shopper behavior analysis.

For the video extraction demonstration, I’ll use a 12-minute documentary video
in the public domain called “This is Coffee,” <sup>4</sup> published in 1961 and available at The
Internet Archive. This video has scenes without speech, scenes with written text on
screen, and scenes with a narrator speaking. I’m going to preprocess the video using two
AWS services to generate two data inputs. First, I’ll use Amazon Rekognition to analyze
the video and provide timestamped lists of detected labels. This will capture the change
of scenes through the video and extract objects and entities in these scenes.

Here is simplified Python code to generate time-stamped labels:

import boto3
import time
import json

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

# S3 location of the video file
bucket_name = 'my-bucket'
video_name = 'rekognition/ThisisCo1961_512kb.mp4'

# start the asynchronous detect labels job
response = rekognition.start_label_detection(

[4 This is Coffee. Vision Associates. 1961. Accessed Jan 7, 2025 (https://archive.org/details/](https://archive.org/details/ThisisCo1961)
[ThisisCo1961).](https://archive.org/details/ThisisCo1961)

342

)

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

I used a helper script to print a list of detected labels. Here is a sampling:

Label: Alarm Clock, Confidence: 95.45%
Label: Clock, Confidence: 95.45%
...
Label: Sink, Confidence: 97.88%
Label: Sink Faucet, Confidence: 97.88%
...
Label: Face, Confidence: 97.20%
Label: Head, Confidence: 97.22%
Label: Person, Confidence: 97.64%
Label: Adult, Confidence: 97.70%

_[Truncated for brevity]_

A thousand lines of output are generated, consisting of detected labels with time
stamps and confidence scores. It’s too much for a human to make sense of, but it doesn’t
matter because the generative AI model will be the one to make sense of it all for us!

Now let’s look at the other key piece of data, human speech, to help us with our video
analysis. A narrator starts talking 1 minute and 9 seconds into the video. By transcribing
the words the narrator is saying and adding timestamps, we generate an important
input for video analysis. I demonstrated in the previous audio analysis section how to
use Amazon Transcribe to generate transcriptions. We need to alter this slightly to add
timestamps to the transcription.

response = transcribe_client.start_transcription_job(

MediaFormat=file_uri.split('.')[-1],

to your file format

343

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

To parse the JSON and inject timestamps into the transcription, I’ll modify the
for loop.

# Extract and print transcription with timestamps
items = transcript_data['results']['items']
current_sentence = []
for item in items:

current_sentence.append(f"{word} ({word_start_time:.0f}-{word_end_

time:.0f}ms)")

With the script modified to add timestamps, I rerun the job to create the new
transcription. Here is a sample of the output:

This (73500-74449ms) is (74739-75260ms) coffee (75260-75940ms) .
Our (90459-90739ms) story (90739-91339ms) begins (91339-91779ms) here
(91779-92370ms) with (92660-93220ms) coffee (93220-93660ms)..

_[Truncated for brevity]_

This transcription with the timestamps is very verbose and not easily readable, but
that doesn’t matter because we’re just going to feed it into the generative AI model!
Industry-leading LLMs support large context windows so you can add long text inputs to
the prompt. LLM pricing is metered by input and output token consumption, so at scale
this may not make sense.

Here’s the prompt I used to generate the video analysis:

344

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

Describe the whole video scene by scene that includes a short
concise description. Include timestamps in minutes for each
scene. Use the detected labels and the audio transcription
generated to generate this video analysis.

Detected labels generated by Amazon Rekognition:

_[Detected labels with timestamps output_

Transcription with timestamps generated by Amazon Transcribe:

_[Transcription with timestamps output_

Claude generates a very compelling and credible video analysis using the detected
labels and transcription of the narration:

Here’s a scene-by-scene analysis of the video with timestamps:

0:00-0:15
0:15-0:30
0:30-0:45
enjoyment and satisfaction
0:45-1:30
narrator introduces coffee's significance in daily life and its cultural
importance
1:30-2:30
various processing stages
2:30-4:30
three key elements: water, coffee, and time
4:30-5:30
and bringing it to a boil
5:30-7:00
showing different measuring tools
7:00-9:30
and vacuum) with specific timing instructions:

- Percolator: 6-8 minutes

- Drip: 4-6 minutes

- Vacuum: 3 minutes
9:30-10:30
brewing process

345

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

10:30-11:30
11:30-12:30
day

The video appears to be an instructional film about proper coffee brewing
techniques, with a focus on precision and care in the process.

This approach is formalized in a solution architecture shown in Figure 7-12.

**_Figure 7-12._** _Solution Architecture for Video Analysis_

We were able to generate a highly accurate analysis of a complex, long-running
video by combining the capabilities of AWS ML services like Amazon Rekognition and
Amazon Transcribe to provide the prompt and context for generative AI models hosted
on Amazon Bedrock. Amazon Rekognition can segment the video by scene and detect
labels from a series of images, and Amazon Transcribe can transcribe speech in the
video’s audio. I provided coding examples and reference solution architectures to help
you easily experiment with these approaches.

346

Chapter 7 MULT A ATA E TRA T A E R H E T TH A A E R A
AWS ML SER E

In this chapter, I explored the application of AWS generative AI and machine learning
services for extracting, classifying, redacting, and enriching unstructured data. I
compared traditional deep learning models like CNNs with transformer-based
generative AI approaches across various data processing tasks, including image
analysis, document processing, audio analysis, and video analysis. I demonstrated how
combining purpose-built AWS services like Amazon Rekognition, Textract, Transcribe,
and Comprehend with generative AI models like Amazon Nova and Anthropic Claude
can often yield optimal results. Throughout the chapter, I offered practical guidance
on implementing these hybrid approaches by providing code examples and reference
architectures to help readers implement these solutions.

In the next chapter, we explore one of the most important data engineering topics in
generative AI—retrieval-augmented generation (RAG) and vector databases.

347

**CHAPTER 8**

## **Retrieval-Augmented** **Generation (RAG) with S3** **Vectors and Vector** **Databases**

Retrieval-augmented generation (or RAG) is an advanced technique for augmenting
the capabilities of a generative AI model by integrating external knowledge bases that
contain up-to-date, task- or domain-specific information. Through this approach, RAG
improves the accuracy and relevance of generated content, reduces hallucinations, and
enables more context-aware responses.

Due to the resources required (cost and time) to train robust generative AI models,
there will always be a lag between the most current information available and the data
used to train a model at some time in the past. It is my belief that the responsibility
for implementing and managing RAG will naturally gravitate to the data engineering
domain. The primary reason for this expanding role to now include RAG is that the
company’s data, now represented as text embeddings, will also be stored in a vector
store. This database will persist and inherit all the risks and opportunities that a
corporate data system holding privileged information will incur. The collection and
preprocessing of these documents is not a one-time task that occurs at a point in time,
but a continual process where updates or additions to the current data collection need
to be managed and monitored. This is an exciting time for data engineers and the
opportunity to grow and expand your skills to meet the moment has arrived!

349
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_8](https://doi.org/10.1007/979-8-8688-2199-8_8#DOI)

Chapter 8 R A G RAG V c s V c D s s

In this chapter, I dive deep into the solution architecture and data flow of a general
RAG solution. I’ll discuss the various options for implementing RAG in AWS, from the
most managed (and abstracted) to the least managed (and least abstracted) solutions.
I’ll describe and demonstrate using text and multimodal embedding models in Amazon
Bedrock to create embeddings from text, images, video, and audio. I’ll then explore
vector-supported data systems used for storing vectors, including cost-optimized
options like S3 Vectors and more performant options like Aurora PostgreSQL with the
PgVector extension and Amazon OpenSearch with the Vector plugin.

**Overview of RAG Architecture**

The primary objective of RAG is to enhance the capability of generative AI models
by dynamically retrieving additional knowledge or data at query time and serving
it to the model as part of the prompt context. This additional knowledge could
include proprietary or confidential company information or recently collected public
information that is first processed and stored in a knowledge base. Figure 8-1 shows the
conceptual process flow for RAG.

**_Figure 8-1._** _Retrieval-Augmented Generation (RAG) Conceptual Diagram_

350

Chapter 8 R A G RAG V c s V c D s s

I’ll discuss each component conceptually, then we’ll overlay the AWS services that
can help us implement them. When a request is submitted to a generative AI model in
natural language (by a human or service), the request is first converted to numerical
representations as a high-dimensional array, which captures the semantic associations
of the text. This allows a semantic search to be performed on a vector database.
A semantic search in practical terms is a “similarity search” where stored vector
embeddings are compared against query embeddings to determine which content in
a knowledge collection is likely related to the request. Similarity can be determined
by different types of vector math, which we’ll explore later in this chapter. The vector
embeddings that are the most semantically similar are returned and converted back into
text and integrated as part of the prompt. That RAG-enhanced prompt is what is sent to
the generative AI model, with the model’s response being returned to the requester.

**Note** Vector embeddings are used in other machine learning use cases such as
classification, clustering, and recommendation engines.

Before I delve into the AWS services and architectures that are used to implement RAG,
it’s worth noting that there are a number of what I’ll call “managed RAG” solutions in the
AWS ecosystem. I define a managed RAG solution as one that abstracts key functions of
the RAG process. These may include one or more of the following:

1) Automated data collection process

The data collection process to build a corpus of content is
abstracted using data connectors, a synchronization process,
scheduling, and a way to dynamically update the corpus with
updated data.

2) The generation and storage of vector embeddings

In managed RAG systems, the generation of vector embeddings
is performed internally without any additional effort by the
user. This is true for both the document ingestion process and
converting the search query text to vectors for semantic search.

351

Chapter 8 R A G RAG V c s V c D s s

3) Computing similarity and returning relevant content

A managed RAG system will perform semantic search without
exposing the mechanics of computing similarity between vectors.

The advantage of leveraging managed RAG is the simplicity and speed that a readymade solution can deliver to accelerate time-to-value for a business. The disadvantage is
that the abstracted system makes many decisions for you, and these decisions may not
be right for your use case. Let’s look at a few managed RAG solutions in AWS.

**Amazon Q for Business**

Amazon Q for Business is a fully managed RAG-enabled enterprise chatbot service. It’s
easily configurable from the console—so easy that a power user could set one up without
a data engineer.

Amazon Q for Business connects to over 40 popular enterprise applications and
document repositories, including Amazon S3, Salesforce, Google Drive, Microsoft 365,
ServiceNow, Gmail, Slack, Atlassian, and Zendesk. Amazon Q will ingest and index the
data from those data sources and enable an intelligent search as part of a generative AI
chatbot. Figure 8-2 shows a small sampling of the connectors supported by Amazon Q
for Business.

**_Figure 8-2._** _A Sample of Amazon Q for Business Connectors_

352

Chapter 8 R A G RAG V c s V c D s s

Once you choose data sources in Q for Business, you can choose how the data is
synced—on demand or on a schedule. You can also choose whether to sync the full
dataset or only new or modified data. Figure 8-3 shows an example of these options from
the Q for Business console.

**_Figure 8-3._** _Syncing and Scheduling Options for Amazon Q for Business_

In Amazon Q for Business, the vector embeddings model is chosen for you. In
addition, a number of important data security features are included to help manage
user access to RAG corpus data. These permissions “passthrough,” meaning that the
authenticated user only retrieves additional content from the knowledge base for which
they have direct access.

**Amazon Bedrock Knowledge Bases**

Amazon Bedrock Knowledge Bases provides an enterprise-ready RAG with more
configurable options for how RAG is implemented than more managed solutions like
Amazon Q for Business. Knowledge bases for unstructured data can be created using
OpenSearch Serverless collections, Amazon Aurora Serverless PostgreSQL, or Amazon
Neptune for GraphRAG. Knowledge bases for structured data can also be created using
Amazon Redshift.

353

Chapter 8 R A G RAG V c s V c D s s

Knowledge Bases integrates with a number of data sources and collection tools,
including Amazon S3, a managed web crawler service, or a custom collector. It also
integrates natively with third-party content platforms like Confluence, Salesforce, and
SharePoint.

Knowledge Bases also allows you to choose an embedding model from Amazon
and Cohere to use to generate vector embeddings. Figure 8-4 shows this model
selection screen.

**_Figure 8-4._** _Embedding Model Selection in Bedrock Knowledge Bases_

Unless you’ve procured a provisioned throughput instance of the embedding model,
the only inference option available will be **on demand** .

Builders can choose from several chunking strategies, as shown in Figure 8-5. This
determines how the content is organized in the vector store.

354

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-5._** _Chunking Strategies in Knowledge Bases_

Besides these configurations, Knowledge Bases handles everything else behind
the scenes. It ingests the content from the data sources specified, it chunks the content
using the chosen chunking strategy, and it generates embeddings using the selected
embeddings model. It then stores the embeddings in the selected vector store.

For implementing RAG with Bedrock Knowledge Bases using structured data in
Amazon Redshift, see Chapter 10, “Data Warehousing with Generative AI and Text-toSQL Reporting with Amazon Redshift.”

Now, let’s shift gears to discuss how a builder would implement RAG without
abstraction.

**Corpus Collection Process and Storage**

To collect and curate corpuses of unstructured data, some sort of collection process is
needed. The scale and complexity of this process will depend on the types of data you choose
to include in the knowledge base and where that data resides. One common collection
method is web scraping. Whether it’s a set of designated websites being monitored for
relevant information or the internet in general, web scraping is a common collection method
for RAG knowledge bases. Others include document stores you’d expect, like Amazon S3,
SharePoint, Confluence, internal wikis, or corporate file systems. Structured data from
SQL databases or data warehouses can also be used. To collect data from these data stores,
however, you need specialized connectors that can connect and retrieve the data.

355

Chapter 8 R A G RAG V c s V c D s s

If you are planning to implement a robust data collection process to support RAG,
the make versus buy decisions are critical here. Building connectors to data sources
carries several risks. It is not differentiating work, and each of the connectors would
likely need to be updated on an ongoing basis as the source data system evolves with
new versions and enhancements. If connectors are not available in the AWS ecosystem,
they are likely available as a product solution. General architectural approaches heavily
use AWS Lambda Functions for web scraping, API ingestion, and other small data
collection. Amazon EventBridge is the preferred choice for triggering schedule- or eventdriven workflows. Amazon AppFlow is specifically designed for data integration with
35+ third-party applications and services, including popular platforms like Salesforce,
SAP, Slack, ServiceNow, Google Analytics, Zendesk, and Marketo. AWS Glue can perform
small and large data ETL.

Because there are so many variations on this topic, it’s outside the scope of the
book. Instead, I’ll describe how to manage the data in AWS once it’s collected. Amazon
S3 is the obvious choice for storing unstructured data like documents, images, audio,
and video. Let’s take a look at how we might choose to organize our content in our RAG
collections store. For most use cases, you will need a minimum of three processing
stages: raw, extraction, and processed. Note that this assumes a landing zone exists as
a separate bucket. I use the collections prefix to distinguish it from other RAG steps, as
shown in Figure 8-6.

**_Figure 8-6._** _Organizing RAG Collections Store in Amazon S3_

356

Chapter 8 R A G RAG V c s V c D s s

The raw stage is for storing documents as they are extracted from the source. The
extraction stage is for the data extraction generated by Amazon AI services. This is
important data to capture, as it serves as the input to the final processing stage. You will
be able to audit the pipeline and, if needed, regenerate processed stage content without
needing to perform the initial extraction again, saving on unnecessary costs. Using the
extraction data, you can create a final document that will be used to generate vector
embeddings.

Within each collection stage prefix, I separate out documents, images, audio, and
video. The reason for this is because we’ll trigger different data processing pipelines from
each of these S3 prefixes.

rag /

I split documents into three main categories: complex document types like PDF,
scanned documents or those that arrived as images from the source, and text.

Despite these organizational strategies, data governance of unstructured data files
in S3 is still a challenge. We still need to track the relationships of files that are generated
from the source file somewhere. Practitioners were contemporaneously managing the
metadata for S3 objects in a separate data store like Amazon DynamoDB. This proved
overly tedious and unwieldy over time beyond a certain scale.

Luckily, Amazon S3 Metadata arrived to solve this nagging and persistent challenge!

**Amazon S3 Metadata**

A new feature launched in 2024 called Amazon S3 Metadata greatly simplifies metadata
management for unstructured data in S3, eliminating the need for external metadata
stores. A fully managed Apache Iceberg table is linked to a general-purpose S3 bucket.
As objects are added, updated, or removed in the general-purpose bucket, S3 Metadata
automatically captures these changes and makes them available to query in a read-only
table. This is shown in Figure 8-7.

357

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-7._** _S3 Metadata Sync and Querying Using Amazon Athena_

The S3 object metadata includes the immutable system metadata, mutable object
tags, and immutable user-defined metadata. First, I create an S3 Tables bucket called
rag-collections-metadata.

**Note** T Tables, which are fully managed Apache I
is covered in Chapter 3, “D L D Apache I Tables.”

With my tables bucket created, I can now link it to my general-purpose bucket where
I am storing my rag collections. Figure 8-8 shows where this lives in the console.

**_Figure 8-8._** _Connecting S3 Table Bucket to S3 General-Purpose Bucket_

358

Chapter 8 R A G RAG V c s V c D s s

With my table bucket connected to my RAG collections bucket, we are ready to
demonstrate these new features with an example. In Chapter 7, “Multimodal Data
Extraction and Enrichment with Amazon Bedrock and AWS ML Services,” I processed
a scanned form document with Amazon Textract. I’ll update the metadata on the final
JSON object representing the extracted form data. I’m including custom metadata fields
“s3_path_raw” and “s3_path_extraction,” which will link the source file and the Textract
output file. I also include other fields like page number, source, type, and cost_center to
highlight different metadata fields that might be valuable.

Since custom metadata is immutable, updating metadata is performed as an inplace copy. The code is below.

import boto3
bucket_name = "data-engineering-with-generative-ai"
object_key = "rag/collections_processed/documents/2025325926_claude.json"

new_metadata = {
"s3_path_raw": "s3://[...]/rag/collections_raw/documents/

image/2025325926.png",

}

# Get the current object metadata
response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
current_metadata = response.get('Metadata', {})

# Merge the current metadata with the new metadata
updated_metadata = {**current_metadata, **new_metadata}

# Copy the object to itself to update the metadata
s3_client.copy_object(

359

Chapter 8 R A G RAG V c s V c D s s

)

Updating the metadata triggered an event that generated a record in our metadata
table bucket. I can use Athena to query the metadata records of the S3 objects in the
linked general-purpose bucket. Before I’m able to query this metadata table from
Athena, I need to grant the proper permissions in Lake Formation. Figure 8-9 shows how
to locate the table in the Lake Formation console.

**_Figure 8-9._** _Locating the Metadata Table in Lake Formation_

On the table details screen, you select **Actions** dropdown in the upper right corner
and select **Grant** under the **Permissions** section. In the permissions screen, you’ll need
to grant select and describe permissions on the table, as shown in Figure 8-10.

360

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-10._** _Granting Permissions for Querying Metadata Table in_
_Amazon Athena_

Now we can navigate to the Amazon Athena query window and select the catalog
as “aws_s3_metadata.” The field containing our custom metadata in our metadata table
is called “user_metadata.” Since it’s a JSON field, I can use square brackets to reference
fields within the JSON. The query below is one common query I’ll need to run to find all
the files linked to the source file—from extraction and processed stages.

SELECT *
FROM "aws_s3_metadata"."s3metadata_data_engineering_with_generative_ai"
WHERE user_metadata['s3_path_raw'] = 's3://[...]/image/2025325926.png'

The query results are in Figure 8-11.

361

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-11._** _Athena Query Results from Metadata Table Bucket_

Records are returned that are linked to our source file in the raw stage. Customers
had the ability to add metadata to objects for many years, but they could not query
metadata like this until now.

Now that we have our processed document files, it’s time to create vector
embeddings.

**Collection Embeddings Process**

Generating vector embeddings for different modalities—like text, images, video, and
audio—and storing them in a shared vector space is needed to support multimodal
RAG. Data engineers may not have the luxury of consulting with data scientists and
instead will need to widen their competencies to gain deeper knowledge about this
topic. In this section, I’ll demonstrate how to create vector embeddings for text, images,
audio, and video. AWS has released two generations of embeddings models: their latest
Amazon Nova Multimodal Embeddings model and their last-generation Amazon Titan
text and multimodal embeddings models. I’ll focus primarily on the Nova Multimodal
Embeddings model. As you progress through these sections, think critically about how
you might scale these examples to process an entire corpus of data.

362

Chapter 8 R A G RAG V c s V c D s s

**Amazon Nova Multimodal Embeddings**

Amazon Nova Multimodal Embeddings represents AWS’s latest generation embedding
model designed to transform various content types—including text, images, video,
and audio—into unified vector representations within a shared semantic space. This
capability enables sophisticated cross-modal retrieval and search applications where
queries in one modality can retrieve relevant results from another. If you don’t fully
understand what I just said, you may miss the headline. A shared semantic space means
a shared vector space. The embeddings for each modality share the same vector space.
This is what enables cross-modal search, meaning that you can search for “car” and
retrieve not just documents with text that is related to cars, but also images, videos,
and audio related to cars. This is a high-value capability across many industries. If this
capability is important to your use case, understand that the choice of embeddings
model for any of the modalities is consequential—a model may outperform for a
particular modality, but it won’t utilize the same vector space, and thus the effectiveness
of a truly cross-modal search will be impacted. Therefore, to properly support crossmodal search, you’ll need to commit to one embeddings model for all modalities due to
the shared vector space requirement.

The Amazon Nova Multimodal Embeddings model provides both a synchronous
and asynchronous API. The synchronous API has an 8K token context length. The
asynchronous API supports built-in segmentation functionality that automatically
partitions long-form content into manageable chunks. This eliminates the need to
implement a chunking strategy on the client side. For example, you won’t need to write
additional code to split videos at keyframes or handle text tokenization boundaries.
When would you use one versus the other? You’d use the synchronous API to generate
embeddings for the user request to search for in real time. The context length is going to
be small and likely under the 8K token maximum, so there should not be a high volume
of requests. When generating embeddings for the document corpus to store in the
RAG vector database, there would be no user waiting for a response, and so this would
not require an immediate response. The job can run for as long as it needs to. Using
the asynchronous API means you can take advantage of the segmentation feature to
eliminate the need to implement custom chunking logic.

Nova Multimodal Embeddings was trained using Matryoshka Representation
Learning (MRL) and offers four dimension options (256, 384, 1024, 3072). With the
MRL approach, smaller dimension vectors are simply truncated versions of the
larger dimension vectors. This allows you to start with the highest dimension option

363

Chapter 8 R A G RAG V c s V c D s s

for indexing, then truncate to smaller dimension options (1024 or 384) for better
performance. This is becoming more relevant as the demand for lower latency RAG and
semantic search grows. But also, the fewer the dimensions, the less compute and storage
resources are needed to store and search.

In the next several sections, I’ll demonstrate how to generate embeddings for each of
the different modalities using the Nova Multimodal Embeddings model.

By far the most common and ubiquitous type of embeddings are text embeddings. While
it may not be obvious to those new to RAG engineering, text embeddings are languagedependent. The Nova Multimodal Embeddings model provides multilingual support
for over 200 languages, making it suitable for global applications. Evaluating which
model is the best is definitely an exercise I would not discourage anyone from. It would
only result in a much richer understanding of the different features and attributes of
embeddings models.

I’ll explain the steps required to properly create embeddings from a JSON artifact
like the one created from our document extraction process. Then I’ll go step by step with
code examples to demonstrate how to generate embeddings from our example JSON
document.

**Flatten JSON Object**

We’ll retrieve the file from S3 and read it into a Python variable as a JSON object. This
allows us to read through the key-value pairs and flatten the JSON. The JSON structure
falls away, producing a long string of words.

import boto3
import json

# Initialize AWS clients
s3_client = boto3.client('s3')
bedrock_client = boto3.client('bedrock-runtime')

# Load JSON object into data variable
response = s3_client.get_object(Bucket=input_bucket, Key=input_key)
data = json.loads(response['Body'].read().decode('utf-8'))

364

Chapter 8 R A G RAG V c s V c D s s

We can create a recursive helper function to flatten the JSON.

# flatten JSON return dict of key value pairs
def flatten_json(data, prefix=''):

I’ll then convert the dict of key-value pairs into a string separated by spaces.

# convert dict to string
flattened_data = flatten_json(data)
text = ' '.join(f"{k}: {v}" for k, v in flattened_data.items())
text = re.sub(r'\s+', ' ', text).strip()

If I use the synchronous API of the Nova Multimodal Embeddings model, I’ll need to
chunk the content if it exceeds the context length. First, I’ll split the long string into an
array of words so we can iterate through the list and create chunks of text that fit into the
fixed context size of the embeddings model. The Nova embeddings model can accept a
context window of up to 8K tokens. One token is approximately four characters of text.
75 words is approximately 100 tokens. It’s dataset-dependent so when you perform the
chunking, it’s important to leave a sufficient buffer. I’ll set the max number of words
at 5,000.

max_chunk_size = 5000
words = text.split()
chunks = []
current_chunk = []

365

Chapter 8 R A G RAG V c s V c D s s

# group the words into chunks
for word in words:

if current_chunk:

With these chunks prepared, we are ready to define the input parameters.

**Defining the Input Parameters**

We need to define the input parameters for the model invocation method. This is
ultimately packaged into a JSON object. To specify the synchronous API call using the
chunking objects we created in the previous section, we set the taskType parameter to
SINGLE_EMBEDDING.

# Define the request body for Nova
model_input = {

}

Embeddings need to be generated for each chunk. We’ll need to iterate through
the chunks we created in the previous section. I reference the generate_embedding()
method as the helper function to encapsulate the invoke logic.

366

Chapter 8 R A G RAG V c s V c D s s

This can potentially generate a lot of invoke calls to the model depending on
how large the document is. To mitigate this risk, you can add a delay to govern the
request rate.

If we instead use the asynchronous API and take advantage of its segmentation
feature, we’ll need to set the taskType parameter to SEGMENTED_EMBEDDING. We just
have to set the segment length. Here’s what it would look like.

model_input = {

367

Chapter 8 R A G RAG V c s V c D s s

You’ll notice that for the asynchronous request, the embedding job ingests the input
document from an S3 location.

Now that we have the input parameters defined, we can call the Bedrock invoke
method to perform inference on these inputs. We can specify the model ID directly or
use an inference profile. I’ll start with the synchronous API, which uses the invoke_
model() method.

# Invoke Nova Embeddings model synchronously
response = bedrock_client.invoke_model(

)

For the asynchronous API invocation, since we’re not getting the result back
immediately, we need to specify an output location specifying the S3 location where the
results will be written to. The async invocation uses the start_async_invoke() method.

# Invoke Nova Embeddings model asynchronously
response = bedrock_client.start_async_invoke(

)

368

Chapter 8 R A G RAG V c s V c D s s

**Parse and Save the Response**

If we use the synchronous request, we’ll receive the embedding result in the response.
We just have to parse the Bedrock response to extract the body and specifically the
embeddings.

# Parse the response for synchronous API call
response_body = json.loads(response['body'].read())
embedding = response_body['embeddings'][0]['embedding']

For the asynchronous request, we’ll instead receive a response object with the
request ID and invocation ARN.

# Parse the response for asynchronous API call.
request_id = response.get('ResponseMetadata').get('RequestId')
invocation_arn = response.get('invocationArn')
job_id = invocation_arn.split('/')[-1]

The results are written to the specified S3 output location, which has a predefined
folder structure.

s3://my-bucket/output/
└── {job-id}/
├── manifest.json
├── segmented-embedding-result.json
├── embedding-text.jsonl
├── embedding-video.jsonl
├── embedding-audio.jsonl
└── embedding-image.json

With the JobId, the S3 output location, and the text embeddings filename, we can
read the output.

# Your S3 output location
s3_output_location = 's3://my-bucket/embeddings-output/{job_id}/'
filename = 'embedding-text.jsonl'

# Parse the S3 URI to get bucket and prefix
uri_without_prefix = s3_output_location.replace('s3://', '')
parts = uri_without_prefix.split('/', 1)

369

Chapter 8 R A G RAG V c s V c D s s

#bucket
bucket = parts[0]

# prefix
prefix = parts[1] if len(parts) > 1 else ''
if prefix and not prefix.endswith('/'):

# Construct full S3 key
s3_key = f'{prefix}{filename}'

With our S3 key constructed, we can retrieve the object from S3.

# Download and read the file
response = s3_client.get_object(Bucket=bucket, Key=s3_key)
content = response['Body'].read().decode('utf-8')

Next, we need to parse the JSONL file to extract the embeddings.

# Parse JSONL
embeddings = []
for line in content.strip().split('\n'):

Finally, we will save the complete set of embeddings to an S3 Vectors bucket. It’s a
best practice to save the embeddings to a highly durable data store like S3 Vectors.

# Save embeddings to S3 Vectors bucket
s3vectors.put_vectors(

} ] )

370

Chapter 8 R A G RAG V c s V c D s s

To operationalize these embeddings for RAG, we’ll need to load them into a vector
store, which I address further in the chapter. Table 8-1 shows a comparison table for
generating text embeddings with Nova.

**_Table 8-1._** _Nova Multimodal Embeddings Comparison Table_
_for Text Embeddings Generation_

**Feature** **Synchronous** **Asynchronous**

API invoke_model start_async_invoke

taskType SINGLE EMBEDDING SEGMENTED EMBEDDING

I I S3 location

M 8K tokens 15M

M 1 (single embedding) 1900

R <1 second 1–10 minutes

O API S3: embedding-text.jsonl

O single JSON JSONL ON

In this section, I demonstrated how to generate text embeddings using Amazon’s
most recent embeddings model, Nova Multimodal Embeddings.

Next, I’ll describe how to generate image embeddings.

Image embeddings are more widely understood today due to the popularity of Google’s
reverse image search feature. Upload an image into the Google search bar, and Google
will find similar images. How does it do that? It’s nothing more than a similarity search of
embeddings, but for images! There are image embedding models that process an image’s
raw pixel data to capture visual characteristics like color, texture, shapes, patterns, and
spatial relationships. Transformer-based models can preserve the visual context and
composition of the image. Embeddings are also generated from the image uploaded as
part of the search query, and a similarity search is performed to identify similar images.
In this section, I’ll discuss what makes all this possible: image embeddings.

We can again use Nova Multimodal Embeddings, which supports all modalities,
including images. Since each image is itself a discrete “batch” of data, there’s no need for

371

Chapter 8 R A G RAG V c s V c D s s

chunking like for text embeddings. Since there’s no need for segmentation, you might
be wondering if there are any benefits to using the asynchronous API. The answer is
yes, several! If your images are already stored in S3, the job can ingest them from that
location directly. Synchronous requests require you to download the image, convert
it to base64, and pass it directly into the invocation method. The size limitation for
synchronous invocation is 25MB after base64 encoding (image size of ~18MB). If your
input images exceed this size, you’ll need to use the asynchronous API which has no size
limit. Let’s review how to convert the image to base64 for synchronous requests.

**Convert Image to Base64**

In order for us to use an image as input, we need to convert it into a format that can be
passed into the model. For binary data like images, this means base64 encoding. Python
makes it easy to perform this conversion.

import boto3
import base64
import json

# encode image as base64
s3_client = boto3.client('s3')
response = s3_client.get_object(Bucket=bucket_name, Key=image_key)
image_data = response['Body'].read()
image_bytes = base64.b64encode(image_data).decode('utf-8')

**Defining the Input Parameters**

Once we have our image converted to a base64 encoded string, the input parameters are
straightforward.

# Synchronous API with inline content
model_input =

372

Chapter 8 R A G RAG V c s V c D s s

For async requests, remember that images can’t be segmented, so we’re specifying
SINGLE_EMBEDDING as the taskType. We need to specify an S3 URI for the source
image location and an output S3 URI where the generated image embeddings will be
written to.

# Asynchronous API with S3 input and output locations
modelInput={

I provided examples for invoking the model both synchronously and asynchronously
previously. These generate methods are consistent across the different modalities. I
also provided examples for parsing the response objects and saving the embeddings
to S3 Vector tables, so I won’t be repeating that for each modality. Table 8-2 shows a
comparison table for generating image embeddings with Nova.

373

Chapter 8 R A G RAG V c s V c D s s

**_Table 8-2._** _Nova Multimodal Embeddings Comparison Table for Image_
_Embeddings Generation_

**Feature** **Synchronous** **Asynchronous**

API invoke_model start_async_invoke

taskType SINGLE EMBEDDING SINGLE EMBEDDING

I B S3 location

Supported formats jpeg, png, gif, webp jpeg, png, gif, webp

M ~18MB MB B N

M 1 (single embedding) 1 (single embedding)

R <1 second Seconds to minutes

O API S3: embedding-image.jsonl

O single JSON single JSON

Now let’s see how we can generate video embeddings.

Generating video embeddings is significantly more complicated without a managed
segmentation feature. I’ll describe briefly what’s involved—if for no other reason than to
impress upon you the value you’ll get from using the asynchronous API’s segmentation
feature. To do this manually, you’d need to extract video frames as images and generate
embeddings from these images. You can go even further to build out logic to group frames
into scenes or identify segments. This is outside the scope of this book, but if you are
interested in these capabilities, refer to the _Video Understanding with Generative AI on_
_AWS Workshop_ <sup>1</sup> on GitHub and the Amazon Rekognition Video Segment Detection API <sup>2</sup> .

1 “Media Analysis with Generative AI on AWS,” AWS Samples, GitHub repository, accessed January
[15, 2025, https://github.com/aws-samples/media-analysis-with-generative-ai-on-aws/.](https://github.com/aws-samples/media-analysis-with-generative-ai-on-aws/)

2 “Detecting video segments in stored video,” Amazon Web Services, accessed January 15, 2025,
[https://docs.aws.amazon.com/rekognition/latest/dg/segments.html.](https://docs.aws.amazon.com/rekognition/latest/dg/segments.html)

374

Chapter 8 R A G RAG V c s V c D s s

As we saw in the image embeddings section, the synchronous API for Nova
Multimodal Embeddings has a size limit of 18MB and 30 seconds. Due to the size of
most videos, there’s only a limited set of scenarios where you would be able to use the
synchronous API. Instead, I’ll focus on the asynchronous API. For my sample video, I’ll
use the “This is Coffee” video featured in the previous chapter.

A really neat feature of Nova’s video embedding capability is that you can generate
both combined (video and audio) and separated embeddings. The combined video
embedding is a single unified embedding and would work for searches to find similar
video (w/ audio) content. You can also generate separate embeddings for video (image)
and audio. You might find value in generating both kinds—you could search across
videos, images, and audio collections. For example, imagine that you want to search
through the entire video catalog to find which videos feature a particular song.

Let’s take a look at how to choose these options in our asynchronous request.

**Defining the Input Parameters**

We will be utilizing segmentation for each of these requests. Videos can vary in terms of
duration, and it’s quite convenient to allow our embedding model service to do all the
complicated work for us!

# Asynchronous API with combined embedding
model_input_combined = {

'embeddingMode': 'AUDIO_VIDEO_COMBINED',

embedding

375

Chapter 8 R A G RAG V c s V c D s s

If you chose to generate separate embeddings, they would appear in their
respective JSONL file under the JobId in the designated output folder. Table 8-3 shows a
comparison table for generating video embeddings with Nova.

**_Table 8-3._** _Nova Multimodal Embeddings Comparison Table for Video_
_Embeddings Generation_

**Feature** **Synchronous** **Asynchronous**

API invoke_model start_async_invoke

taskType SINGLE EMBEDDING SEGMENTED EMBEDDING

I B S3 location

Supported formats mp4, mov, mkv, webm, avi, flv mp4, mov, mkv, webm, avi, flv

M ~18 MB ~11.95 hours (43,020 seconds)

M 1 (single embedding) 1,434 segments

Segmentation type N A
seconds per segment)

Supported
embedding types

AUDIO VIDEO OMBINED
AUDIO VIDEO EPARATE

AUDIO VIDEO OMBINED AUDIO
VIDEO EPARATE

R <1 second M

O API S3: embedding-video.jsonl

O single JSON JSONL ON

The last modality left to discuss is audio.

Audio embeddings are vector representations of the technical features extracted from
audio. While the extracted features can include spoken language converted to text,
generating embeddings from transcribed text would be generated as text embeddings.
Audio embeddings for this purpose are something different. What’s being described by

376

Chapter 8 R A G RAG V c s V c D s s

the embedding is a representation of the actual sound. If you ever used the popular song
identification app Shazam!, you’ve experienced the capability of audio embeddings.
Like text, images, and video embeddings, audio embeddings can identify recordings that
contain similar audio features.

Audio is a unique kind of unstructured data. Digitized audio can be produced by
machines or created as a sample of an analog waveform. The sampling rate impacts
the quality of the embeddings. It’s important to understand a few basic concepts about
audio so that you can record and process it properly. There are different frequency
ranges for different kinds of audio. Increasing the sampling rate increases a wider range
of frequencies. Table 8-4 shows the recommended sampling rates for different audio
use cases.

**_Table 8-4._** _Recommended Sample Rates for Different Audio Sources_

**Use Case** **Recommended**
**Rate**

**Notes**

Speech/voice
(telephony)

Speech/voice
(podcast)

8kH H Captures speech frequencies transmitted over modern
telephony systems

16kH H Captures all speech frequencies

M 44.1kH M P

H
audio

48kH P

A higher sampling rate captures more harmonic detail. A sampling rate that is
higher than needed wastes storage and computation resources. In some cases, you may
need or want to adjust the sampling rate of the source audio. For any preprocessing
of audio, a Python library you will want to familiarize yourself with is TorchAudio.
TorchAudio is PyTorch’s audio processing library that provides tools and utilities for
loading, manipulating, and transforming audio data, including functions for tasks like
resampling, spectrograms, and audio transformations. For example, a common audio
transformation may be to adjust the amplitude because the audio is too soft and not
being heard clearly. Diving deeper into these scenarios is out of the scope of the book,
but readers are encouraged to experiment on their own.

377

Chapter 8 R A G RAG V c s V c D s s

**Defining the Input Parameters**

Let’s look at how we will define the input parameters for generating audio embeddings
for both the synchronous and asynchronous invocations. Audio has the same limitations
as video on the size and length of the input audio.

For the synchronous API, we’ll be passing in the audio inline as a base64 encoded
string. We’ll convert this the same way we did for images.

import base64

# Read audio file as binary
with open('audio.mp3', 'rb') as audio_file:

# Convert to base64
audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')

# Generate embedding
model_input = {

} } }

Similarly, for the other binary modalities, for asynchronous invocation, we specify
the S3 location of the audio file. Because we’re using segmentation, we’re able to specify
the duration in seconds of each segment.

model_input = {

378

Chapter 8 R A G RAG V c s V c D s s

Since I covered it previously, I’ll leave the model invocation and response parsing
as an activity for the reader. Table 8-5 shows a comparison table for generating audio
embeddings with Nova.

**_Table 8-5._** _Nova Multimodal Embeddings Comparison Table for Audio_
_Embeddings Generation_

**Feature** **Synchronous** **Asynchronous**

API invoke_model start_async_invoke

taskType SINGLE EMBEDDING SEGMENTED EMBEDDING

I B S3 location

Supported
formats

mp3, wav, ogg mp3, wav, ogg

M ~18MB
max

~11.95 hours (43,020 seconds)

M 1 (single embedding) 1,434 segments

Segmentation
type

N A
segment)

R <1 second M

O API S3: embedding-audio.jsonl

O single JSON JSONL ON

379

Chapter 8 R A G RAG V c s V c D s s

This completes our study of multimodal embeddings. I presented both the theory
and practical examples for generating embeddings for text, images, video, and audio.
Next, I’ll demonstrate how to set up vector-supported data stores in AWS, import the
embeddings that were generated into these databases, and perform semantic search.

**Vector Databases and Semantic Search**

I must acknowledge a simple truth: vector databases not only store vector embeddings,
they also implement the indexing of the vectors and provide the search engine and
resources (compute and memory) to execute semantic search. This makes it nearly
impossible to discuss vector databases as just a vector storage system. Several choices
are made at design time to build sophisticated vector indexes. At search time, algorithms
efficiently traverse these indexes to identify similarity matches to the query.

For this reason, I’ll cover some theory and practice of semantic search systems,
which includes vector formats and precision, distance metrics, semantic search
algorithms, search implementation libraries, and vector indexing. I attempt to relate all
these concepts in Figure 8-12.

**_Figure 8-12._** _Semantic Search Concepts and Architecture_

380

Chapter 8 R A G RAG V c s V c D s s

This demonstrates how the index (as expected) is central to semantic search
and how each of the terms you might casually encounter are related to building and
searching these indexes.

**Vector Format and Precision**

The next option to choose is between floating point 16, 32, and binary precision for
representing (and storing) vectors. To understand the tradeoffs of speed, cost, and
accuracy for each option, we must review computer engineering fundamentals for how
computers store numbers.

For floating-point numbers, the level of precision achievable is determined by how
many bits are used to store the number. Not surprisingly, FP16 uses 16 bits to store
the number, and FP32 uses 32 bits. The bit position and type are meaningful, as they
represent a part of the decimal number (either the sign, the exponent, or the fraction).
Figure 8-13 shows how the bits are allocated in FP16 and FP32 numbers and how it
determines precision.

**_Figure 8-13._** _FP16 vs. FP32 Precision_

381

Chapter 8 R A G RAG V c s V c D s s

FP16 achieves 3–4 digits of precision, while FP32 achieves an average of 7 digits
of precision. FP16 is likely to produce no noticeable difference because semantic
differences are larger than the precision loss. FP16 enables faster search times and
requires less storage. In rare instances where the content is dense and similar, a
similarity search could return ties or an incorrect ranking. Increasing the precision to
FP32 could resolve these issues.

Binary precision takes performance and storage optimization to the extreme by
sacrificing granularity. For each dimension, simply a 1 or 0 is stored, indicating that the
attribute is present or not. This yields a 32x optimization in speed and storage compared
to FP32. Binary similarity is calculated using bitwise operations like Hamming Distance.
Most models output embeddings in floating-point format, so additional preprocessing
is needed to convert to binary. Table 8-6 lists the different precision formats and the
tradeoffs between accuracy, speed, and storage consumed.

**_Table 8-6._** _Precision Format Comparison for 1024-Dimension Vector Embeddings_

**Format** **Accuracy** **Search Speed** **Vector Ops** **Storage**

B
(1 bit/dim)

FP
(16 bits/dim)

FP
(32 bits/dim)

L
(B

H
(~3.3 s.f. <sup>3</sup> )

H
(~7 s.f.)

Fastest
(4.2x vs FP

Fast
(1.6x vs FP

Slowest
(B

4x vs FP L
(128 bytes)

2x vs FP H
(2,048 bytes)

B H
(4,096 bytes)

In terms of use cases most appropriate for each, assume that very large-scale
deployments would benefit from binary format, and production RAG deployments
would likely only require FP16, with FP32 reserved for academic research or very
specialized use cases.

3 s.f. - Significant figures.

382

Chapter 8 Retrieval-Augmented Generation (RAG) with S3 Vectors and Vector Databases

**Distance Metrics**

There are two primary types of vector calculations for performing similarity search:
Euclidean distance and cosine similarity (via dot product). It’s important to understand
how these calculations impact the outcome and to know why the one that is favored
works better. I’ll review both in this section.

**Euclidean (L2) Distance**

Euclidean distance measures the straight line distance between two points in space.
To compare two multidimensional sets of vectors, you sum the square of the difference
between each vector for each dimension, then take the square root.

If we were to depict this visually, it would measure the distance of the line depicted
in Figure 8-14.

**_Figure 8-14._** _Illustration of Euclidean Distance_

383

Chapter 8 Retrieval-Augmented Generation (RAG) with S3 Vectors and Vector Databases

To calculate the similarity between vector A with dimensions [10, 1] and vector
B with dimensions [10,2], we’d calculate the distance between two points using the
equation for Euclidean distance. The equation reduces to sqrt(0 <sup>2</sup> + 1 <sup>2</sup> ) = 1. However,
if we augmented these dimension values slightly (e.g., [11,1] and [10,2]), we’d see a
disproportionate variation in the result. The equation would instead reduce to sqrt(1 <sup>2</sup> +
1 <sup>2</sup> ) = 1.41.
This demonstrates the magnitude sensitivity of Euclidean distance. A small change
in one large dimension could greatly impact the result. In real embedding spaces
with hundreds of dimensions, these effects can compound dramatically. This is why
Euclidean distance is not recommended for implementing semantic search.

**Cosine Similarity**

A more effective method for calculating similarity between vectors is _cosine similarity_,
which addresses the shortcomings of Euclidean distance because it normalizes for
magnitude. It is calculated by taking the cosine of the angle between two vectors to
determine if they are pointing in the same direction and are similar _directionally_ . Vectors
with a cosine distance closer to one are considered to have a similar direction. Vectors
with a cosine distance furthest from one are dissimilar in direction.

The cosine similarity can be calculated using a dot product as shown below.

This is visually depicted in Figure 8-15.

384

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-15._** _Cosine Similarity of Two Vectors_

Inner (dot) Product (IP) similarity is a vector similarity metric designed for use with
learned embeddings, including those generated from BERT, OpenAI, or Amazon Nova
and Titan embeddings models. _Learned embeddings_ are vectors that have valuable
information encoded in the magnitudes of the vectors, which can be extracted by
calculating the inner product. For example, the word “king” shows inner product
similarity with “queen” and “man,” but not “woman,” due to the magnitudes of the
vectors representing royalty and gender. Inner product similarity is sensitive to vector
magnitudes because vectors are not normalized as they are with cosine distance, but
they avoid the scaling risk from Euclidean distance by providing a weighted magnitude.

Next, let’s take a look at the sophisticated algorithms powering semantic search
engines.

**Semantic Search Algorithms**

The word “search” in semantic search should tip you off that this is a search problem. At
scale—comparing millions of vectors with high dimensionality—it is a computer science
problem. These types of search problems require optimized and efficient algorithms
for constructing and searching indexes and performant and scalable infrastructure

385

Chapter 8 R A G RAG V c s V c D s s

to deliver low latency performance. The best data engineers will build RAG solutions
optimized for their use case, using the AWS services that support the right combination
of algorithms and libraries. In this section, I’ll discuss three important algorithms—
Hierarchical Navigable Small World (HNSW), Locality-Sensitive Hashing (LSH), and
Product Quantization (PQ). I won’t include discussion of a less popular algorithm called
Annoy, which was developed by Spotify, but I’ll include it in comparisons.

**Hierarchical Navigable Small World (HNSW)**

As the name suggests, HNSW is implemented as a hierarchical multi-layer graph and
uses nodes (vectors), edges (connections), and layer assignments to organize the data.
The graph is sparse at the top and dense at the bottom. The algorithm starts from an
entry point at the highest layer and searches for its nearest neighbor and descends to the
next layer. A conceptual example is shown in Figure 8-16.

**_Figure 8-16._** _HNSW Multilayer Graph_

It traverses the graph using a greedy search in upper layers and beam search
refinement in lower layers. Greedy search follows one path and is practical up to a
certain number of vertices. Beam search scales by maintaining a list of top-N candidates
at each layer and exploring multiple paths in parallel.

Beam search of the base layer is governed by two parameters, _M_ and _ef_construction_ .
M defines the maximum connections per node. The “ef” in ef_construction stands for
expand factor and defines the beam width or search factor used during index building.
When choosing HNSW, you’ll want to choose these parameters based on the tradeoffs
shown in Table 8-7.

386

Chapter 8 R A G RAG V c s V c D s s

**_Table 8-7._** _Beam Parameter Performance Matrix_

**Low M** **High M**

**Low ef** Fast build
L
L

**High ef** M
M
H

M
M
M

Slow build
H
H

Typical values for M are 8 (sparse), 16 (balanced), and 32 (dense). For ef, typical
values range from 64 (fast build), 128 (balanced), and 512 (high quality).

**Locality-Sensitive Hashing (LSH)**

Locality-sensitive hashing (LSH) is a probabilistic technique for finding nearest
neighbors in high-dimensional spaces. Similar items are hashed into the same bucket
with high probability. There are several parameters that govern how the hashing is
implemented. The number of hash tables (L) is the most critical since it determines
memory usage and computational complexity. The number of hash functions (k)
balances precision and recall. The k value is typically between 10 and 100. The F1-score
can be used as a metric for optimization because it is the harmonic mean of precision
and recall. The bucket width (w) defines the size of the hash buckets, which will
determine the probability of similar items being hashed together.

Here are default or starting point values for each parameter:

     - L = 10 hash tables

     - k = log2(n), where n is the size of dataset

     - w = 0.5

Table 8-8 shows the LSH hash functions and when you would use each.

387

Chapter 8 R A G RAG V c s V c D s s

**_Table 8-8._** _LSH Hash Functions_

**Hash Function** **Similarity** **Best For**

M H Jaccard D
(sparse binary)

SimH Cosine Semantic search
(dense vectors)

p-stable L H L N
(metric spaces)

LSH will yield advantages when index construction speed and dynamic updates
are needed.

**Product Quantization (PQ)**

Product quantization (PQ) is a compression method for high-dimensional vectors. This
compression allows for faster similarity search in large datasets using less memory. It
uses fast approximate distance calculations through lookup tables instead of full vector
computations. The vectors are split into smaller chunks of sub-vectors and these subvectors are encoded based on the index of the nearest centroid. A centroid is simply
the average point (center) of a cluster of similar data points. With a group of similar
subvectors, the centroid represents the group. A concept called a “codebook” is an index
of these centroids. There are two hyperparameters, the number of sub-vectors (M) and
the number of centroids per sub-vector (k).

Default values for these hyperparameters are:

     - M = 16 sub-vectors

     - k = 256 centroids per sub-vector

So if you have a 256-dimension vector, you could split it into 16 sub-vectors, each
with 16 dimensions. This will yield 16 codebooks. If the original vector is represented
in FP32, the compression will be 256 dim x 32 bits = 8,192 bits (1,024 bytes). Since each
sub-vector is represented by an 8-bit integer (unit8), the total size of the vector after
PQ compression is 16 sub-vectors x 8 bits = 128 bits (16 bytes). For this example using a
256-dimension vector, PQ achieves a 64:1 compression ratio.

388

Chapter 8 R A G RAG V c s V c D s s

In this section, we reviewed HNSW, LSH, and PQ algorithms. Table 8-9 compares the
key metrics of these popular search algorithms.

**_Table 8-9._** _Comparison of Performance Metrics for Semantic Search Algorithms_

**Algorithm** **Query Time** **Memory** **Accuracy** **Build Time**

HN W Fastest M H M

L H M H L Fast

P Slow L M Slow

A M L M M

**Similarity Search Libraries**

Similarity search libraries are the implementation of the abstract theoretical algorithms
presented in the previous section. They include production-grade optimizations and
features like memory management, I/O handling, thread safety, and error handling. It’s
important to understand what the algorithms are doing so that you can choose the right
library that implements the most optimal algorithm for your use case. I’ll feature two
main libraries, NMSLib and FAISS.

**Nonmetric Space Library (NMSLib)**

The Non-Metric Space Library (NMSLib) is a similarity search library for approximating
nearest neighbor search in both metric and non-metric spaces. It is optimized for CPUbased workloads. In metric spaces, the distance between points follows mathematical
rules, including symmetry (distance A→B = distance B→A) or triangle inequality
(distance A→C ≤ distance A→B + distance B→C). In other words, a direct path cannot be
longer than any indirect path.

Non-metric spaces violate one of the mathematical rules. For example, the
geographic distance between cities is in metric space. The cultural distance between
countries is in non-metric space. For example, the US is more culturally similar to
Australia than Japan despite the US being 3,200 miles closer geographically. Another
example where nonmetric spaces are used is movie recommendations. Saving Private
Ryan is a war movie featuring Tom Hanks. Comparing it to Forrest Gump would show

389

Chapter 8 R A G RAG V c s V c D s s

similarity because it also features Tom Hanks and elements of war. The additional
element of the love story in Forrest Gump would show a similarity to The Notebook.
However, if you compared Saving Private Ryan directly to The Notebook, you’d produce
a much larger distance, breaking the triangle inequality rule.

NMSLib is not the standard library for storing vector embeddings for RAG, but it’s
important to know what it is and why it’s an option in OpenSearch Serverless.

**Facebook AI Similarity Search (FAISS)**

Facebook AI Similarity Search (FAISS) is a library for efficient similarity search and
clustering of dense vectors, particularly optimized for high-dimensional data with GPU
support. It is the default standard in RAG applications precisely for these reasons. Vector
embeddings have high dimensionality. The FAISS library provides detailed documentation
and has achieved mass adoption—it’s widely used in machine learning applications. It’s
actively maintained by Meta, which provides assurances of long-term support.

If we combine all the learnings from this section, we can start to identify some
general combinations of components for implementing common use cases, which I
explore in the next section.

**Common Semantic Search Architectures**

Why is this valuable for you to know? Because semantic search and RAG are evolving
as fast as other aspects of generative AI applications. There is no practical way to cover
every variation of semantic search architecture, but if you know the theory and the
building blocks of semantic search that don’t change as frequently, you can design
RAG solutions that are optimized for your use case. I discuss some general use cases for
choosing RAG-specific combinations of these features in Table 8-10.

**_Table 8-10._** _Semantic Search Stacks for Common Use Cases_

**Use Case** **Stack** **Feature**

H HN W MN L P CPU

L P AI P GPU

B IV P AI P GPU

390

Chapter 8 R A G RAG V c s V c D s s

In this section, I dove deep into vector format and precision, vector distance metrics,
and similarity search algorithms and libraries. Now I’ll demonstrate how to set up
databases for vector storage and search in AWS. I’ll also provide coding examples for
each, showing how to store and retrieve these vectors.

**Vector Databases on AWS**

It’s important to understand Amazon’s overall strategy with respect to vector stores.
Rather than build a standalone vector database to centralize all embeddings, they are
choosing instead to add vector storage and semantic search capabilities for many of
their data storage management services. Architecturally this means that vector database
features and capabilities are being bolted onto the database services you’re likely already
using! Figure 8-17 shows the various vector database options in AWS.

**_Figure 8-17._** _AWS Data Services Supporting Vector Storage and Semantic Search_

391

Chapter 8 R A G RAG V c s V c D s s

Not only is this architecturally efficient with respect to latency, but it provides other
significant benefits as well. For instance, if you are leveraging a vector store in an existing
managed database service like Aurora PostgreSQL, you automatically inherit all the
high availability (HA), multi-region, and disaster recovery (DR) features of the service.
Aurora PostgreSQL offers multi-AZ secondaries with automated failover as well as global
databases that support cross-region replication. This eliminates the need to plan and
manage HA and DR requirements for a separate vector store. Similarly, Amazon S3 offers
99.99% of availability and 11 nines of durability. By leveraging S3 Vectors, your vector
store achieves these availability and durability SLAs by default.

I don’t have the space to present every possible vector-enabled data store, so
I’ll focus on the three most popular in AWS: Amazon S3 Vectors, Amazon Aurora
PostgreSQL with the PgVector extension, and Amazon OpenSearch with the
Vector plugin.

**Amazon S3 Vectors**

Amazon S3 Vectors is a special bucket type (like metadata or table buckets) that is
designed specifically for storing, indexing, and querying vectors as part of semantic
search applications. Not only does it provide the elasticity and durability that I
mentioned previously, but it also provides a set of API operations to store, access, and
perform similarity queries with sub-second query performance. The primary use case
for Amazon S3 Vectors is cost optimization. Generating and storing embeddings with
high dimensionality in online data stores with provisioned compute, memory, and
storage can be cost prohibitive at scale. Amazon S3 Vectors provides a low-cost solution
for storing all the vectors while also natively integrating with more performant vector
search services like Amazon Bedrock Knowledge Bases and Amazon OpenSearch. Warm
or hot vectors frequently queried can reside in the higher-performance search services,
while colder, less frequently queried vectors can remain in S3 Vectors. Figure 8-18 shows
the overall architecture.

392

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-18._** _Amazon S3 Vectors Integration with AWS Vector Search Services_

In this section, I’ll demonstrate how to create and use S3 Vector buckets for semantic
search applications.

**S3 Vectors Buckets and Indexes**

In S3 Vector buckets, vector data is stored in vector indexes. We first create the S3 Vector
bucket, then create the vector index. One vector bucket can hold up to 10,000 vector
indexes—each index holding tens of millions of vectors. Figure 8-19 shows the creation
of the S3 Vector bucket and the vector index.

393

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-19._** _Creation of the S3 Vector Bucket and Vector Index_

When creating the vector index, the maximum number of dimensions is chosen. S3
Vector indexes support up to 4096 dimensions. You’ll also choose the distance metric
(cosine or Euclidean). This is as far as we can go via the console. To insert, list, or query
vectors from S3 Vector bucket indexes, only the AWS CLI, the AWS SDKs, or the S3 REST
APIs can be used.

394

Chapter 8 R A G RAG V c s V c D s s

**Loading and Querying Vectors in S3 Vectors**

In this section, I’ll describe how to load vectors into an S3 Vectors index and then how
to query that index using semantic or similarity search. I’ll be choosing to demonstrate
these operations using the AWS Python Boto3 SDK.

First, we need to create a client for the S3 Vectors service, like we would with any
other AWS service.

import boto3
s3vectors = boto3.client('s3vectors', region_name='us-east-1')

The put_vectors() method takes the vector bucket name and the vector index name or just
the vector index ARN. The last is the vector array, which can include metadata. In my example,
below, I’m only including one vector, but each request can bulk load multiple vectors, each
containing the maximum number of dimensions (as defined at bucket creation).

# Single vector with 3 dimensions
s3vectors.put_vectors(

)

Now to query this vector, we will use the query_vectors() method. Let’s assume I’ve
created embeddings for my query text and have it stored in query_embedding. Here’s my
query_vectors() request.

# Query the vector index
results = s3vectors.query_vectors(

)

395

Chapter 8 R A G RAG V c s V c D s s

There are several optional parameters that can return additional information about
our query.

     - **TopK (or MaxResults in some SDKs)** : Specify how many results
to return.

     - **returnMetadata** : Return the metadata stored with the vector (often
the source text).

     - **returnDistance** : Return the distance or similarity score.

     - **nextToken** : The pagination token

There is also filterable and nonfilterable metadata. Filterable metadata allows for
the results to be filtered using several operations. Metadata can typically include the
source text, but it can now include other valuable information. For example, if I’m
storing vectors representing product information, I can store the price for each product,
and then I can filter by the price using filtering operations (less than, greater than, equal
to, etc.).

# Create vector with metadata
vector = {

Using a helper function, I can take filters as a parameter.

# Query helper function
def search_products(query_text, filters=None, max_results=5):

396

Chapter 8 R A G RAG V c s V c D s s

Then I can use this function to search products.

results = search_products(

Table 8-11 provides a list of supported filter operations.

397

Chapter 8 R A G RAG V c s V c D s s

**_Table 8-11._** _Supported Filter Operations in S3 Vectors_

**Operator** **Description**

$eq E
element in the array.

$ne N

$gt G

$gte G

$lt L

$lte L

$in M

$nin M

$exists Check if the field exists.

$and L AND

$or L OR

Nonfilterable metadata keys must be explicitly configured during vector index
creation. It can be used to store larger context-related content, including the source
document itself.

Now that we’ve reviewed the basics of storing and querying vectors in S3 Vectors,
let’s see how we can extend these vector storage capabilities to high-performance vector
databases.

**Integrating S3 Vectors with Bedrock Knowledge Bases**

Amazon Bedrock Knowledge Bases supports the use of S3 Vectors as a managed vector
store to reduce the complexity and cost of vector storage for RAG applications. You can
elect to have Bedrock Knowledge Bases create a new S3 Vectors bucket and index for the
knowledge base to store its vectors (see Figure 8-20). This is recommended by AWS.

398

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-20._** _Creating a Bedrock Knowledge Base with S3 Vectors as the_
_Vector Store_

Alternatively, you can choose an existing bucket and index you’ve already created.
You’ll need to specify both the vector bucket name and the vector index.

Let’s now look at how S3 Vectors integrates with Amazon OpenSearch.

**Integrating S3 Vectors with Amazon OpenSearch**

We can store a large volume of vectors with high dimensionality in a cost-effective way
in Amazon S3. We can then import just the vectors needed to OpenSearch for real-time
vector search performance. AWS helps automate this process by providing a native
integration for importing vectors from S3 Vectors indexes. Similar to how OpenSearch
Serverless and OpenSearch collections are used to support Bedrock Knowledge Bases,
the same is provided as a target for S3 Vectors indexes. Figure 8-21 shows how to initiate
this integration via the console.

399

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-21._** _Amazon OpenSearch Zero-ETL Integration with S3 Vectors_

What is being selected here is a Zero-ETL import process that imports vectors from a
specific S3 Vector index. In the next screen, the ARN of the vector index is required (see
Figure 8-22).

400

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-22._** _Importing S3 Vectors to OpenSearch Vector Engine_

After the ARN is entered and the IAM service role creation options are selected, the
process is started.

The import process automates the following steps:

     - OpenSearch vector collection creation

     - IAM role creation for service access

     - OpenSearch Ingestion pipeline creation

When the import process is completed, I’ll have an OpenSearch Serverless collection
loaded with vectors from my S3 Vectors index.

This concludes my discussion on S3 Vectors as a cost-optimized vector store. Now
I’ll turn my attention to how we can use Aurora PostgreSQL for vector storage and
semantic search.

**Aurora PostgreSQL with Pgvector Extension**

Amazon Aurora PostgreSQL is AWS’s flagship managed PostgreSQL database service
that enhances the traditional PostgreSQL database with AWS-specific optimizations for
scalability, durability, and high availability. In the following sections, I’ll demonstrate the
steps needed to implement a vector store in Aurora PostgreSQL.

401

Chapter 8 Retrieval-Augmented Generation (RAG) with S3 Vectors and Vector Databases

**Install Vector Extension**

PostgreSQL supports the installation of extensions, or additional capabilities that are not
included in the core of the PostgreSQL database. Some examples include PostGIS for
handling spatial and geographic data and pgcrypto for data encryption. The pgvector
extension provides support for storing vectors and performing vector searches. To install
extensions, administrators use the CREATE EXTENSION command. To install the vector
extension, execute the following command.

CREATE EXTENSION IF NOT EXISTS vector;

To verify the extension was installed correctly, use the following psql command:

\dx vector

You should see a table printed showing the extension name, version, schema, and
description like in Figure 8-23.

**_Figure 8-23._** _Displaying a List of Installed Extensions_

We can see from the result that the vector extension was installed correctly.

**Create Vector Tables**

The vectors have to live somewhere, and in a relational database, that means a table.
The vector extension enables a new PostgreSQL data type called _vector(N)_, where N is
the number of dimensions. That one column in a table will hold the vectors, while any
number of other standard columns can be added to describe those vectors. I created
embeddings from document text, images, and audio. There’s one main distinction for
how we might store vectors for different modalities. With text embeddings, you’ll want to
store the source text in a column in the same table as the vector. This will eliminate any
additional retrieval time for the source content after a vector calculation to determine
similarity identifies relevant data. Most RAG applications support interactive user
experiences, and latency is a critical factor.

402

Chapter 8 R A G RAG V c s V c D s s

You can choose a design that’s best for your business requirements. You may
choose to create specialized content tables for each type. For this example, I’ll create
a common content table and then four embedding tables for text, images, audio, and
video that reference it. The theory supporting this separation is simple. The content
table contains data about the content. The embeddings tables contain data about the
embeddings generated from the content. There’s a 1-to-many relationship between the
source content and the embeddings because multiple embeddings can be generated for
the same source content. Some content needs to be chunked or segmented, requiring
multiple records for the same source content.

**Content Metadata Table**

Let’s take a look at what a prototypical metadata table schema might look like.

-- Core metadata table to store common attributes
CREATE TABLE rag.collections (

content_type VARCHAR(10) NOT NULL CHECK (content_type IN ('text',

'image', 'audio', 'video')),

);

This table features an original_source_url column, which will contain the S3
location of the file in collections_raw. There is also a content_hash that will hold a
hash of the raw content. This will indicate whether the referenced file is both correct and
hasn’t changed since it was catalogued. The metadata field is a binary JSON object that
can be used to store additional metadata specific to the content.

**Text Embeddings Table**

Let’s create a table to store our text embeddings.

403

Chapter 8 R A G RAG V c s V c D s s

-- Text embeddings table (Nova Multimodal Embeddings v1: 3072 dimensions)
CREATE TABLE rag.text_embeddings (

);

The text embeddings table includes (among others) the embeddings column and
three fields determining uniqueness: content_id, model_id, and chunk_index. This
makes sense because we can generate embeddings for the same document using
different models and store them in the same table. I’m defining the dimension limit
at 3,072 because this is the maximum number of dimensions the Nova Multimodal
Embeddings model supports. Other text embedding models may support more, so
you’ll need to determine what a good upper limit is to support your choice of models.
It’s important to understand the tradeoff in dimensions vs. disk usage, as this is going to
augment resource consumption for existing database clusters. Assuming 32-bit floating
point (4 bytes) for each dimension, we can calculate the storage required for vectors of
various dimensions (see Table 8-12).

**_Table 8-12._** _Storage Consumed for Different Vector Dimensions_

**Dimensions** **Bytes per Vector** **MB per 1M Vectors**

384 1,536 bytes 1,536MB GB

512 2,048 bytes 2,048MB GB

1024 4,096 bytes 4,096MB GB

1536 6,144 bytes 6,144MB GB

2048 8,192 bytes 8,192MB GB

3072 12,288 bytes 12,288MB GB

404

Chapter 8 R A G RAG V c s V c D s s

For example, you can see from the table that by doubling the dimensions from 512
to 1024, you double the storage size. I create similar tables for images, audio, and video.
Like chunks of documents, for audio and video embedding tables, I add columns to
manage segment start and end times.

-- Audio embeddings table
CREATE TABLE rag.audio_embeddings (

);

The video embedding table follows a similar pattern but is omitted for brevity.

**Create Embeddings Index**

Creating a proper vector index is critical for executing performant semantic search
queries. There are three different types of indexes PostgreSQL pgvector supports: HNSW,
inverted flat file, and exact vector match. For each of these algorithms, you can specify
distance metrics: cosine similarity, L2, and inner (dot) product.

The following are some sample create index statements paired with distance metrics.
These are provided only as an example of how algorithms and distance metrics are
specified when creating an embedding index in PostgreSQL.

--HNSW + cosine:
CREATE INDEX ON embeddings USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

--IVFFlat + L2
CREATE INDEX ON embeddings USING ivfflat (embedding vector_l2_ops)
WITH (lists = 100);

-- exact vector match + Inner Product
CREATE INDEX ON embeddings USING vector (embedding vector_ip_ops);

405

Chapter 8 R A G RAG V c s V c D s s

Common use cases for when to use each index type are shown in Table 8-13.

**_Table 8-13._** _Vector Indexing Feature Comparison by Index Type_

**Feature** **HNSW** **IVFFlat** **Exact**

Search speed Fastest Fast Slow

B Slow M Fast

M H M L

U D N Yes Yes

A ~95% 90% 100%

I L M Small

By understanding the tradeoffs in how these indexing strategies perform, you can
confidently make the right choice for your use case. You’ll also need to understand the
same for distance metric use cases, which are shown in Table 8-14.

**_Table 8-14._** _Feature Comparison by Distance Metric_

**Distance**
**Metric**

**Constraints** **Use Case**

E L A Vectors are not
normalized. Sensitive to vector magnitudes.

Cosine Vectors are normalized. D
more than magnitude.

E I
P

Small datasets (<100K rows). Vectors are not
normalized. Sensitive to vector magnitudes.

G

Semantic Search

D
and ML

Now, we have our tables and indexes constructed, we’re ready to insert embeddings.

I’ll use the embeddings I generated previously. First, we’ll insert a record into the rag.
collections table.

INSERT INTO rag.collections (

406

Chapter 8 R A G RAG V c s V c D s s

) VALUES (

);

Now we can insert the text embeddings into the rag.text_embeddings table.

INSERT INTO rag.text_embeddings (

) VALUES (

'[-0.009136928245425224, 0.08058325201272964 [...]

0.001537678181193769]'::vector,
'documentTitle: PLANNED PROJECT DATA SHEET [...] documentNumber:

202535936',

);

407

Chapter 8 R A G RAG V c s V c D s s

Now we have our generated embeddings stored in our Aurora PostgreSQL table
using the specialized vector data type.

In this section, I introduced Amazon Aurora for PostgreSQL with the pgvector
extension as a managed database capable of storing vector embeddings. I demonstrated
how to install the pgvector plugin and provided guidance on how to design and create
database tables with vector columns and provided an example for inserting embeddings
we generated previously into this table. Now let’s look at another popular option for
vector storage, Amazon OpenSearch.

**Amazon OpenSearch Serverless with Vector Engine**

Amazon OpenSearch Service is a fully managed service that makes it easy to deploy,
operate, and scale OpenSearch clusters in the AWS cloud. The k-nearest neighbors
(k-NN) plugin for OpenSearch allows users to store vector embeddings alongside
document data, making it possible to perform efficient similarity searches across
millions of vectors with configurable trade-offs between search speed and accuracy. The
k-NN plugin is what powers the Amazon OpenSearch Serverless Vector Engine feature.

**Create Vector Search Collection**

OpenSearch Serverless offers three collection types: Time-series (for log analysis),
Search (full text), and Vector Search. To create a vector store in OpenSearch Serverless,
you will choose the Vector Search collection option as shown in Figure 8-24.

**_Figure 8-24._** _Vector Search Collection in OpenSearch Serverless_

408

Chapter 8 R A G RAG V c s V c D s s

You’ll then choose which principals and what permissions they’ll have to manage
collections and indexes.

**Install OpenSearch Client Library**

A Python client for OpenSearch is provided in opensearch-py library, separate from
Boto3, and will need to be installed in your environment.

pip install opensearch-py

With the client library installed, we can connect to our OpenSearch Serverless
endpoint to perform operations on our vector search collection.

**Create Vector Embeddings Index**

Before we can store embeddings in OpenSearch, we’ll need to create an index. I’ll do
this visually via the console for demonstration purposes. Each index contains a vector
field and metadata fields. Figure 8-25 shows the console screen for adding a vector field
to a vector index. I’ll now discuss each of the parameter settings for semantic search
and RAG.

409

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-25._** _Creating Vector Indexes in OpenSearch Serverless_

Currently, OpenSearch serverless supports two similarity search libraries, NMSLIB
and FAISS. For this example I’ll choose FAISS, FP16, and dot product for cosine similarity
as our distance metric. Under additional settings, I chose the default values for M and
ef_construction.

With the indexes constructed, we can now perform semantic searches in our vector
databases. Specific knowledge of how the indexes were constructed is needed for querying
the index. For instance, if the index was constructed using cosine similarity as the distance
metric, then you would need to use cosine similarity when performing the search.

410

Chapter 8 R A G RAG V c s V c D s s

**Generate Embeddings from Query Text**

Remember that since we are comparing vectors, the submitted query needs to be
converted to vector embeddings before the search can be performed. You should use the
same embeddings model to create vector embeddings for the input query that was used
to create the vector embeddings of the corpus. I’ll break down a simple script to help
us do that. Like previous scripts, we will need to import common packages and create a
Bedrock client using Boto3.

import boto3
import json
import numpy as np

# Initialize Bedrock client
bedrock = boto3.client(

)

I’ll leave it for the reader to create a common function to standardize this task with
parameters. I’m simplifying the script to make it easier to understand.

# Input text
query_text = "This is a sample text for embedding creation."
# Alternative: query_text = ["First sentence.", "Second sentence.", "Third
sentence."]

# Convert single string to list if needed
if isinstance(query_text, str):

else:

I’ll again use the Amazon Nova Multimodal Embeddings model, which is the same
model I used to create vector embeddings for the corpus that I stored in my vector databases.
I construct the request body parameter for the synchronous invoke model API call.

embeddings_list = []
model_id = "amazon.nova-2-multimodal-embeddings-v1:0"

411

Chapter 8 R A G RAG V c s V c D s s

# Process each text and get embeddings
for text in texts:

})

# Invoke Nova Embeddings model synchronously
response = bedrock_client.invoke_model(

I parse the response and convert it to a NumPy array ready to be used for our
semantic search.

**Semantic Search in Aurora PostgreSQL**

PostgreSQL’s pgvector extension provides specialized operators for performing semantic
search in a PostgreSQL database. I’ll list these operators and provide search examples
using SELECT statements for each.

Distance metric operators:

     - <=> -- Cosine distance

     - <-> -- L2 (Euclidean) distance

     - <#> -- Inner product

412

Chapter 8 R A G RAG V c s V c D s s

Here are some example queries that use these specialized operators for each
distance metric.

-- Euclidean/L2: Better for absolute distances
SELECT * FROM rag.text_embeddings
ORDER BY embedding <-> query_embedding LIMIT N;

-- Cosine: Better for normalized vectors
SELECT * FROM rag.text_embeddings
ORDER BY embedding <=> query_embedding LIMIT N;

-- Inner Product: Good for learned embeddings
SELECT * FROM rag.text_embeddings
ORDER BY embedding <#> query_embedding LIMIT N;

If vector normalization is needed, you can create a common function.

-- 1.Normalize vectors if magnitude isn't important
CREATE OR REPLACE FUNCTION normalize_vector(v vector)
RETURNS vector AS $$
DECLARE

BEGIN

END;
$$ LANGUAGE plpgsql;

You can use psycopg2 to execute PostgreSQL statements from a Python script. Here’s
an example script (without any error handling or logging). It’s a best practice to store
database credentials in AWS Secrets Manager and reference them dynamically to avoid
hard coding secrets in code.

# Retrieve db credentials
secret_name = "your-secret-name"
region_name = "us-east-1"

413

Chapter 8 R A G RAG V c s V c D s s

Create the database connection using the parameters. Note that additional
configuration will be needed to enable network connectivity to the database. Refer to
AWS documentation.

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

We’ll then construct the SQL query and pass in the vector embeddings of the query
text and then execute the statement.

# SQL statement to execute
sql_statement = """

"""
parameters = (query_vector)

# Execute the SQL statement with parameters
cursor.execute(sql_statement, parameters)

We’ll fetch and iterate through the records from the cursor.

414

Chapter 8 R A G RAG V c s V c D s s

# Fetch records
records = cursor.fetchall()

# Print results
for row in records:

Finally, we’ll close the database cursor and connections.

# Close cursors and connections
cursor.close()
conn.close()

Let’s now look at semantic search in OpenSearch Serverless to finish out this section.

**Semantic Search in OpenSearch Serverless**

To perform a semantic search in an OpenSearch Serverless collection, we’ll need to
construct a search query JSON object, passing in the embeddings created for the search
query in the previous section, and then execute the search. Refer to AWS documentation
for OpenSearch Serverless collections to learn about authentication options.

**Construct Search Query**

I’ll construct the JSON config object to define our search. I’ll set the search size k
equal to 10.

415

Chapter 8 R A G RAG V c s V c D s s

With the search query object constructed, I can pass it into the search method.

The structure of the JSON response shown below is accessed from an array
referenced as response[‘hits’][‘hits’].

[

416

]

Chapter 8 R A G RAG V c s V c D s s

We can iterate through the results and extract the fields needed.

The OpenSearch project also includes a managed semantic search feature called
Neural Search. AWS announced support for this feature in early 2024. Let’s take a quick
look at this feature before we wrap up this section.

**OpenSearch Neural Search Plugin**

Neural Search is a feature in OpenSearch that fully manages embedding generation,
vector infrastructure, and semantic search. This feature uses the vector plugin as its
underlying engine but adds additional ML-powered capabilities and abstractions for
semantic search.

Creating an index using neural search can be achieved using the JSON editor in the
index creation screen, as shown in Figure 8-26.

417

Chapter 8 R A G RAG V c s V c D s s

**_Figure 8-26._** _Neural Search Index Creation in OpenSearch Serverless_

Combining neural search with keyword search is referred to as hybrid search and has
been shown to yield superior results compared to neural search alone. Here is a sample
JSON object to construct a hybrid search in OpenSearch Serverless.

search_query = {

"model_id": "amazon.neuralSearch.k-nn.cosine
similarity-­

418

Chapter 8 R A G RAG V c s V c D s s

}

With this JSON object constructed, we then pass it into the search method of our
OpenSearch client.

aoss_client = boto3.client('opensearchserverless')

collection_id = "vector-search-demo"
vector_index = "vector-search-index"
query_text = "your search query"

# Execute the search
response = aoss_client.search(

)

We can access the response data in the response object as shown previously.
While this provides another option for implementing semantic search in
OpenSearch, note that this neural search has the following limitations:

     - The text of the search query is limited to 512 tokens.

     - It only supports English text (currently).

     - It can’t use custom embedding models.

     - Raw embeddings can’t be accessed or exported.

OpenSearch Serverless provides several options for implementing semantic search
using its vector and neural plugins.

419

Chapter 8 R A G RAG V c s V c D s s

In this chapter, I explored retrieval-augmented generation (RAG), vector databases,
and how to implement them in AWS. I started the chapter with a high-level explanation
of RAG solution architecture and data flow. I showed how to create embeddings for
each modality using the Nova Multimodal Embeddings model. I then dove deep
into theoretical topics including vector formatting and precision, distance metrics,
semantic search algorithms, search implementation libraries, and vector indexing. I
then explained how semantic search algorithms like HNSW, LSH, and PQ worked and
when you might choose to use them. Throughout the chapter, I discussed the tradeoffs of
various RAG design choices, ensuring readers understand how to select and implement
the most appropriate solution for their specific needs. I presented various options for
implementing RAG in AWS, from highly abstracted managed solutions to those built
from a set of AWS services. I then showed how to store these embeddings in S3 Vectors
and AWS database services with vector support, including Aurora PostgreSQL and
Amazon OpenSearch.

By combining theoretical foundations with practical implementation guidance,
you should now be able to confidently design and develop scalable RAG solutions for
modern data engineering and AI applications.

In the next chapter, I address generative AI applications for streaming data.

420

**CHAPTER 9**

## **Streaming and Real-** **Time Data Processing** **with Generative AI** **Enrichment**

The value of some data has a steep time decay. In other words, the recency or freshness
of the data is the primary source of its value. The time it takes to ingest and process
this data and present insights to its consumers may determine its usefulness. If you’re
a retail investor pursuing a long-term buy-and-hold strategy, last week’s stock price
may be sufficient for your analysis. However, if you’re a day trader looking to exploit
inefficiencies in the market that can evaporate in an instant, every microsecond counts.
With the advent of social media, continuous communication, and evaporating attention
spans, the competition to attract and hold the attention of audiences is fierce. Today’s
online audience has high expectations for digital products—highly immersive and
dynamic experiences are now table stakes—but integrating generative AI into streaming
and real-time data processing presents unique challenges.

In this chapter, we’ll explore streaming and real-time data processing in AWS, how
it differs from batch data processing, and strategies for applying generative AI to enrich
data in a stream.

421
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_9](https://doi.org/10.1007/979-8-8688-2199-8_9#DOI)

Chapter 9 Streaming and R T D P c ss G AI E c

**What Is Streaming Data?**

Streaming data can be intimidating to the casual developer. While it is more complex
to implement and manage than batch data, conceptually, it should not be intimidating.
The mechanics of making this work in practice are complicated, but there’s software
and libraries and frameworks to abstract away that complexity. Streaming data is really
just a continuous series of discrete data records organized into topics. These topics
are append-only logs of immutable records. These records have a small payload and
represent an event with a timestamp—as time series data.

Streaming data pipelines are organized as a series of sources and sinks (see
Figure 9-1). Sinks are persistent data stores to which streaming data is transmitted from
sources.

**_Figure 9-1._** _Sources and Sinks in Streaming Data Systems_

There’s often a misunderstanding when first learning about streaming data. At first
glance it seems to be about the _stream_ when in reality it’s just records being sent from
sources and received by sinks. Real-time data sources include IoT sensors, application
logs, website click streams, financial market, and social media feeds. Sinks can include
data warehouses like Redshift, object stores like S3, messaging queues like Kafka, or
document stores like OpenSearch. In AWS, you can expect that managed services serving
as sinks are highly available and reliable.

Modern streaming architectures implement a publisher-subscriber (pub/sub)
pattern. This decouples the producers of data from its consumers and enables data
products to scale. This is shown in Figure 9-2.

422

Chapter 9 Streaming and R T D P c ss G AI E c

**_Figure 9-2._** _Decoupling Producers and Consumers_

Imagine if N number of consumers needed to integrate directly with M producers—
the number of connections would be N x M or O(NM) complexity. The pub/sub
pattern—assuming each published message needs to be delivered to each subscriber—
reduces this down to O(n) complexity. It also provides a standard interface, meaning
that there is no integration work needed to support additional producers or consumers.
Consumers can simply subscribe to a topic and receive the data without knowing
anything about the producers.

One of the topics I’ll discuss next is an important one: how to stream data into AWS.

Another way to ingest data into AWS is by streaming it. There are many options to choose
from for ingesting streams, and I don’t have the space to cover them all, unfortunately.
If readers want to dive deeper on topics like Amazon Managed Streaming for Apache
Kafka (Amazon MSK) or Amazon IoT Core, there are entire books dedicated to these
topics. The focus for this chapter is on how to integrate generative AI into streaming data
pipelines. The good news is that what I present here will translate to architectures that
use other streaming services.

423

Chapter 9 Streaming and R T D P c ss G AI E c

**Streaming Ingestion with Amazon Kinesis**

Let’s first review Amazon Kinesis, the streaming service I’ll be using for the use cases
I present in this chapter. Amazon Kinesis enables real-time processing and analysis
of streaming data at scale. It’s designed to handle large volumes of data from various
sources such as social media feeds, application logs, IoT devices, and financial
transactions. Kinesis allows you to continuously capture, store, and process these
data streams with low latency, making it ideal for scenarios that require real-time
analytics, monitoring, or event-driven applications. The service is highly scalable, able
to handle hundreds of terabytes of data per hour, and integrates seamlessly with other
AWS services, making it a powerful tool for building streaming data pipelines and
applications.

AWS provides two specialized and abstracted SDKs for producing and consuming
Kinesis streams, the Kinesis Producer Library (KPL) and the Kinesis Client Library
(KCL). It’s important to understand the performance optimizations these SDKs offer
and how they yield significant benefits over less abstracted methods provided by the
generalized AWS SDKs like the Boto3 library.

One limitation to be aware of is that both the KPL and KCL libraries are Java-based.
Support for other languages is possible, however. Both the KPL and KCL can be run as
a daemon, where language-specific wrappers can be used to leverage these methods.
Language support for Python and C++ is provided by AWS. Community wrappers are
available for other languages like Go and Node.js. For the following sections, I’ll be
using Python.

**Kinesis Producer Library (KPL)**

The Kinesis Producer Library (KPL) is a specialized SDK managed by AWS for efficiently
writing data to Amazon Kinesis Data Streams. It simplifies the process of building
producer applications by offering highly configurable methods to put records into a
Kinesis data stream. The KPL implements several key features to optimize performance
and reliability. Let’s take a look at these features:

**Scaling and Utilization Optimizations** : The KPL intelligently

groups records together, significantly boosting throughput while
simultaneously reducing costs. An asynchronous architecture that
includes sophisticated buffer management maximizes throughput
without adding shard capacity.

424

Chapter 9 Streaming and R T D P c ss G AI E c

**Reliability Features** : The KPL provides configurable retry queues

and policies for failure handling, which includes automatic
backoff strategies.

**Observability Features** : Built-in CloudWatch integration

that provides detailed logging and performance and health
monitoring.

**Kinesis Client Library (KCL)**

The complement to the KPL is the Kinesis Client Library (KCL), a specialized SDK that
provides a set of features to optimize the consumption of Kinesis Data Streams. These
features include:

**Shard Management and Load Balancing** : The KCL continuously

manages shard assignments and rebalancing, staying in sync with
your stream and adapting efficiently to resharding events.

**State Management and Recovery** : The KCL automatically

checkpoints stream positions, allowing your application to resume
from where it left off in case of interruptions. The KCL handles
worker failures by redistributing shards to healthy workers,
ensuring reliability.

**Operational Features** : The record processor interface minimizes

the risk of stream handling errors through standardized patterns.
CloudWatch integration provides real-­time visibility into key
metrics.

Now that we’ve reviewed the specialized SDKs for Kinesis, let’s step through setting
up a Kinesis stream, producing data into that stream, and then enriching this data with
generative AI.

**Enrich Streaming Data with Generative AI**

The example solution I’ll present simulates the ingestion of social media posts
to a Kinesis stream. Lambda functions have built-in tumbling window support
for Kinesis Data Streams. This feature can be set via the Lambda Function’s

425

Chapter 9 Streaming and R T D P c ss G AI E c

TumblingWindowInSeconds parameter either in the CloudFormation template, SAM, or
via the console. There’s also a MaximumBatchingWindowInSeconds parameter that will
specify a wait time up to N seconds to fill the batch. Once the batch is filled, the Lambda
Function will be triggered; it’ll package up the records into a payload and invoke the
Streaming Analysis Agent. For each post, the agent will determine the sentiment score
on a scale from 1 to 5, with 1 being the most negative and 5 being the most positive.
Figure 9-3 shows the high-level solution architecture.

**_Figure 9-3._** _Streaming Ingestion with Generative AI Enrichment_

This solution (available from the GitHub repository) includes a producer script that
simulates streaming social media posts to our Kinesis stream.

Here’s an example of a streaming record that we are simulating:

--------------------------------Successfully sent post to Kinesis: {"userId": "user789", "content":
"The CEO of ACME just announced they're raising minimum wage to
$25/hour. This is how you treat employees right!", "platform":

426

Chapter 9 Streaming and R T D P c ss G AI E c

"Facebook", "tags": ["wages", "employment", "fairness"], "timestamp":
"2025-06-08T04:10:24.417613"}
Sequence number: 49664001622261311821947202841736325985249353379205873666
Shard ID: shardId-000000000000
--------------------------------

The agent can send the bulk of the records all at once to a lower latency model like
Nova Micro or Anthropic Claude Haiku. The agent sends the scored posts to S3 and
CloudWatch to chart them in real time. Within this function we are constructing the
following prompt with context and invoking the Bedrock model:

Please analyze the sentiment of this social media post and rate
it on a scale from 1 to 5, where 1 is very negative and 5 is very
positive. Only respond with a single number (1, 2, 3, 4, or 5).
Post: {post}

The CloudWatch dashboard that was created as part of the solution shows the
average sentiment score, the volume of invocations, and a raw charting of each score.
Figure 9-4 shows the CloudWatch dashboard.

427

Chapter 9 Streaming and R T D P c ss G AI E c

**_Figure 9-4._** _Social Media Sentiment Visualized on a CloudWatch Dashboard_

Why not just use a Lambda Function to do all this? Well, a few reasons. We keep
the Lambda Function “dumb.” The agent works as an abstraction. We can adapt the
agent to handle all sorts of streaming data analysis and enrichment tasks. For even
more flexibility, we can use an orchestrator agent to analyze requests and route tasks to
specialized subagents.

This seems easy enough, but in reality adding generative AI models to streaming
pipelines carries risk. I’ll review and discuss each of the major risks and how to
mitigate them.

428

Chapter 9 Streaming and R T D P c ss G AI E c

The bigger the model, the larger the context window, or the more sophisticated its
reasoning capabilities, the longer it will take to get a response from an LLM. For this
reason, premium generative AI models are not well suited for streaming use cases
where the payload is small, the task being requested is simple, and response time is a
constraint. Instead, we are selecting models optimized for the lowest latency, which are
just capable enough to perform the task. In the Bedrock suite of text-to-text models, this
includes Amazon Nova Micro and Anthropic Claude Haiku.

When integrating generative AI capabilities into streaming solutions, the most critical
challenge is scaling inference. The physical realities of LLMs mean they are limited in
request concurrency and token processing throughput. Amazon Bedrock’s on-demand
capacity and thus throttling risk is determined by three metrics: requests per minute
(RPM), tokens per minute (TPM), and tokens per day (TPD). Throttling in Bedrock is
managed through AWS’s standard service quotas system, but unlike some third-party
AI services, Bedrock’s quotas can be increased through AWS support tickets. There are a
few other options that Bedrock provides for scaling inference, which I’ll describe next.

**Bedrock inference profiles** . This feature helps scale inference by allowing requests
to be routed to different regions through AWS’s private network infrastructure. The
service can then optimize routing for requests based on the available capacity of the
requested model.

Instead of using the foundation model ID directly, you instead pass the inference
profile ID for the desired model.

# Invoke using an inference profile ID in the modelId parameter
response = bedrock_runtime.invoke_model(
modelId='us.anthropic.claude-sonnet-4-20250514-v1:0', # inference

profile ID

)

429

Chapter 9 Streaming and R T D P c ss G AI E c

**Bedrock provisioned throughput** . Customers can provision a higher level of model
inference throughput at a fixed cost. Capacity is purchased in model units (MUs),
which specify the number of input and output tokens that can be processed (across all
requests) per minute. Be aware that this service incurs costs continuously while capacity
is provisioned. Ensure that you understand the pricing model and have a business case
to support the continuous cost. There are different commitment options (6 months and
1 year), including no commitment. This feature is not available for all models, so you’ll
need to refer to the pricing documentation to determine for which model and in which
regions this feature is available.

**Streaming Data into Transactional S3 Tables**

Data lakes are preferred for landing streaming data due to several factors—the raw
nature of the data quality and the volume and velocity of the data. However, traditional
write-once-ready-many data lake strategies fall short for several types of streaming data
use cases, like when streaming data needs to be updated or corrected after it was initially
transmitted. This is especially true with financial services use cases. For example, a
clearinghouse for stock trades may transmit the initial trade data but then later send
the same trade again with updated values either in-stream or as part of a reconciliation
process. This is the use case I’ll present in this section. The solution (available from
the GitHub repository) is shown in Figure 9-5 and depicts a streaming data pipeline
consisting of stock trades transmitted to a Kinesis Data Stream by the producer.

430

Chapter 9 Streaming and R T D P c ss G AI E c

**_Figure 9-5._** _Streaming Stock Trade and Reconciliation Solution with Trend_
_Analysis Agent_

Kinesis Firehose is used to land this streaming data into the S3 Tables service, which
provides a managed Apache Iceberg table. In parallel, we are analyzing the trades using
generative AI models in Amazon Bedrock to identify trends. Subscribers—i.e., traders on the
trade desk—receive notifications about any detected trends. What makes this Firehose-to-S3
Tables combination so powerful is that Firehose automatically handles both inserts and
updates to an S3 Tables bucket table. Because this is an Iceberg table, all versions of the table
are preserved, and we can “time travel” to any point in time (until snapshots are expired).
This is a powerful solution that solves a critical problem with traditional data lakes, but it
requires some advanced configuration, which I’ll present in the following sections.

**Create S3Tables Bucket and Managed Iceberg Table**

First, we’ll create the S3 Tables bucket. This is a container for our namespaces (databases)
and tables. I’ll use CLI commands here since we created similar tables via the console in a
previous chapter. For these operations, we use the “s3tables” command of the AWS CLI.

431

Chapter 9 Streaming and R T D P c ss G AI E c

aws s3tables create-table-bucket \

Using the ARN returned from the above command, we create the namespace.

aws s3tables create-namespace \
--table-bucket-arn "arn:aws:s3tables:us-east-1:ACCOUNT_ID:bucket/

stock-trading-­

Now with the namespace created, we can create the managed Iceberg table using a
JSON definition file that defines the schema of the table. We can pass this JSON file in as
a parameter to our table creation command.

aws s3tables create-table \
--table-bucket-arn "arn:aws:s3tables:us-east-1:ACCOUNT_ID:bucket/stock
trading-­

In our trades-table-schema.json file, we’ve defined the schema—the name, datatype,
and required flags—for each field.

cat > trades-table-schema.json << 'EOF'
{

}
EOF

432

Chapter 9 Streaming and R T D P c ss G AI E c

**Link S3Tables Namespace to Glue Catalog Using**
**a Resource Link**

Because S3Tables are a different kind of service from general-purpose S3 buckets, Glue’s
default catalog cannot natively read the S3 Tables namespace where our objects are
created. AWS provides a way to overcome this limitation by creating a resource link in
Glue’s default catalog that maps to the namespace in the table bucket.

aws glue create-database --region us-east-1 \
--cli-input-json \
'{

}'

Next, we need to create an IAM for Firehose so that Firehose can read and write to
the resources needed for its delivery.

**Create an IAM Role for Firehose**

For this solution, Firehose needs permission to read from Kinesis Data Streams and write
to S3 Tables in an Apache Iceberg format. It also requires permissions to AWS Glue to
list databases, tables and update tables, as well as CloudWatch for logging. Due to space
limitations, refer to the GitHub repo for the complete IAM role and policy.

# Create the IAM role
aws iam create-role \

433

Chapter 9 Streaming and R T D P c ss G AI E c

# Attach the permissions policy
aws iam put-role-policy \

**Set Lake Formation Permissions**

To properly configure the Lake Formation permissions for the S3 Tables streaming
solution, you need to grant the FirehoseS3TablesRole comprehensive access to the data
catalog and underlying storage locations. I’ll demonstrate these configurations using
lakeformation CLI commands.

aws lakeformation grant-permissions \
--principal DataLakePrincipalIdentifier=arn:aws:iam::[ACCOUNT_ID]:role/

FirehoseS3TablesRole \

Next, you need to grant table-level permissions for the “trades” table within the
“trading” database, again using the AWS LakeFormation grant-permissions command.
You should grant ALL permissions to allow the Firehose service to perform UPSERT
operations and manage table metadata.

aws lakeformation grant-permissions \
principal DataLakePrincipalIdentifier=arn:aws:iam::[ACCOUNT_ID]:role/
FirehoseS3TablesRole \

Finally, for S3 Tables integration, you must grant DATA_LOCATION_ACCESS
permissions to the S3 Tables bucket location using the DataLocation resource type.
You can do this by specifying the S3 Tables bucket ARN with a wildcard path (e.g.,
arn:aws:s3tables:us-east-1:ACCOUNT:bucket/*) as the --resource parameter.

434

Chapter 9 Streaming and R T D P c ss G AI E c

aws lakeformation grant-permissions \

--resource DataLocation='{ResourceArn=arn:aws:s3tables:us
east-­

**Create Firehose Delivery Stream**

With these settings configured, the last remaining task is to create the Firehose delivery
stream. I will show this via the console. We are choosing to ingest a Kinesis Data Stream
as the source and delivering it to an Apache Iceberg Table as the destination (shown in
Figure 9-6).

**_Figure 9-6._** _Choosing the Source and Destination for the Firehose Delivery Stream_

To enable the update or upsert operation in Firehose, we need to specify the S3
Tables configuration in the Unique key configuration as shown in Figure 9-7. We need
to choose the S3 Tables catalog “stock-trading-demo” and then specify the resource like
we created above as the namespace and then “trades” as the destination table in the
configuration script.

435

Chapter 9 Streaming and R T D P c ss G AI E c

**_Figure 9-7._** _Unique Key Configuration to Enable Updates and Upserts_

I can use Kiro CLI to generate sample trades and then query our table in Athena.
Figure 9-8 shows the results of the Athena query confirming that we can now stream data
into our managed Iceberg table.

436

Chapter 9 Streaming and Real-Time Data Processing with Generative AI Enrichment

**_Figure 9-8._** _Sample Trades_

Now I’ll simulate reconciliation by generating a modified trade with the same trade_
id as one that already exists. This is the update I’ll be sending through the pipeline.

Original TRADE-005:
Stock: TSLA
Price: $227.84
Quantity: 192
Type: BUY
Shard: shardId-000000000008

Reconciled TRADE-005:
Trade ID: TRADE-005
Stock: TSLA
Price: $235.75 (corrected from $227.84)
Quantity: 200 (corrected from 192)
Type: BUY

Waiting a bit for the data to flow through and get UPSERTED into our table,
Figure 9-9 shows the updated record in our result set.

437

Chapter 9 Streaming and R T D P c ss G AI E c

**_Figure 9-9._** _Trade Reconciled Successfully_

The last part of the solution incorporates generative AI analysis to detect trends and
alert based on those findings. This is a hypothetical demonstration, but it demonstrates
the power of just being able to dump a lot of information into a model and get
meaningful analysis that can be operationally actionable.

**Trend Analysis Agent**

The Trend Analysis Agent is invoked by a Lambda that is triggered by Kinesis as the
source (see Figure 9-10). The batch size is configurable. For the purposes of the demo, I
set it at 10.

438

Chapter 9 Streaming and R T D P c ss G AI E c

**_Figure 9-10._** _Lambda Trigger for Stock Trade Trend Analysis_

The Trend Analysis Agent simply reads the records (trades) from Kinesis when it
reaches our batch threshold. It concatenates the contents of the trades into a block of
text that we can insert into the prompt below:

Based on these trades, determine if there's a significant bullish

or bearish trend.

Respond with only "Yes" if there's a clear trend (bullish or

bearish), or "No" if no clear trend.

439

Chapter 9 Streaming and R T D P c ss G AI E c

This provides us with a simple way to scan and analyze streaming data with agentic
AI and then take action on it (i.e., send a notification to the trade desk). Keep in mind
that the context window of the chosen model or the batch size could alter how the
content and prompting is executed.

In this chapter, I explored the integration of streaming and real-time data processing
with generative AI enrichment in AWS architectures. I began by explaining the business
case for streaming data and then attemped to demystify it by presenting basic concepts
in a way that makes it easy to understand. I presented the publisher-subscriber (pub/
sub) pattern, which efficiently decouples data producers from consumers, reducing
system complexity. I introduced Amazon Kinesis as the managed AWS streaming
service, detailing its two specialized SDKs: the Kinesis Producer Library (KPL) for writing
data and the Kinesis Client Library (KCL) for consuming data. I discussed the challenges
for integrating generative AI into streaming pipelines—namely model latency and
inference capacity. I address this through encouraging the use of lower latency models
like Anthropic Claude Haiku or Amazon Nova Micro. I also present other strategies for
scaling inference, such as Bedrock inference profiles or (if the cost is warranted) Bedrock
provisioned throughput. I then grounded these concepts in practical implementations
(both available on GitHub), including a social media sentiment analysis use case and
a real-time stock trading reconciliation and trend analysis use case. These examples
demonstrate two valuable concepts in modern streaming architectures: analyzing data
streams with generative AI and streaming data into transactional Iceberg tables.

In the next chapter, I discuss how data warehousing and Amazon Redshift are
evolving with generative AI and dynamic text-to-SQL reporting capabilities.

440

**CHAPTER 10**

## **Data Warehousing** **with Generative AI and** **Text-to-SQL Reporting** **with Amazon Redshift**

Data warehousing is a data analytics strategy for collecting, storing, and managing
large volumes of structured data into a centralized repository where advanced analytics
processing and aggregation can be performed. Ad hoc and other complex reporting is
then served to business intelligence applications. Traditionally, data warehouses were
used like data lakes—to cleanse and transform the data—but data lakes and lakehouses
have largely assumed these responsibilities. For those use cases, data lakes excel
due to the flexibility of a schema-on-read paradigm and its ability to accommodate
all modalities—structured, semi-structured, and unstructured data—in one unified
repository. Review the sections “Separation of Data and Compute” and “Schema-onWrite vs. Schema-on-Read” in Chapter 3, “Data Lake Design with Apache Iceberg and
S3 Tables.” Data warehouses now adopt a more narrow scope, but one that is critical
for many enterprises. I would describe data lakes as a “bottom-up” strategy and data
warehousing as a “top-down” strategy. Due to the fact that object storage is so cheap
and getting cheaper, we can capture all the data in a data lake even if the value of that
data isn’t immediately apparent. Through exploration and discovery, we may uncover
value in the data that we then operationalize and distribute to the business. Because
of the schema-on-write nature of data warehouses, it’s expensive to build out and
maintain. That is why data warehouses should be thought of as a strategic, top-down
use case. For example, senior leaders need KPI reporting on the performance of the

441
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_10](https://doi.org/10.1007/979-8-8688-2199-8_10#DOI)

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

business to make high-value decisions. That’s one of the more common justifications
for a data warehouse. Another might be reporting features in a customer-facing product.
Today, report and query development is one of the largest costs associated with data
warehousing solutions. With generative and agentic AI, it’s possible for data warehouses
to deliver greater value at faster speeds and lower cost.

In this chapter, I discuss how generative AI is impacting data warehousing strategy at
enterprises. I’ll briefly review data warehousing theory and fundamentals, including star
schema and the benefits of columnar storage. I’ll dive deep into AWS’s managed data
warehousing service, Amazon Redshift, and explore many exciting features, including:

     - Replication with ZeroETL

     - Automated ingestion with S3 Copy

     - Multi-cluster data mesh architecture with Redshift data sharing

     - Generative BI features

     - Amazon Bedrock model inference for SQL data

     - As a structured data source for RAG via Bedrock knowledge bases

I’ll present an agentic AI architecture for implementing natural language Text-to-SQL
solutions for dynamic reporting. Finally, I’ll briefly discuss Redshift’s emerging role in
supporting AI model training use cases.

**Impact of Generative AI on Data Warehouses**

The ability to take a natural language request from a business user and use generative
AI to translate that into complex SQL to query the data needed by the business is a game
changer for enterprises. To help you understand and appreciate the value, I’ll describe
what many companies and product teams have gone through for decades. A high-priority
customer who purchased a data insights product asks to see their data in a new way
from what’s currently provided in the platform. The product team decides to build out a
report to satisfy the customer request. This requires a commitment of weeks of company
resources and attention: from the planning, the development work by data and reporting
engineers to testing and finally, deployment. The report is delivered, and the customer is
happy initially, but then their priorities change due to a leadership mandate. Now, they
need to see the data in a totally new way and request a new report, and the process starts

442

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

over. Now imagine you have dozens or even hundreds of customers all asking for different
permutations of their data! I refer to this phenomenon as the painful transition from an
insights company to a “report writing company.” With Text-to-SQL reporting, users are now
empowered to ask new questions in natural language and have generative AI dynamically
create the SQL query needed to deliver the results of that request.

First, I’ll start with a review of data warehousing fundamentals, then I’ll dive deep
into prompt engineering strategies for implementing Text-to-SQL.

**Data Warehousing Fundamentals**

It’s important to first understand the theoretical concepts and business drivers for why
data warehouses exist. I’ll focus on the following three:

1) Data scaling and the JOIN problem

2) The need to separate analytical and operational workloads

3) Optimizing data models for business reporting

One way to explain the architectural concepts and the need for data warehouses is
to distinguish them from operational data systems. Operational data systems support
transactional CRUD operations in a highly normalized data model. When a data model
is highly normalized, it produces many tables. Consequently, it implies that many table
JOINs need to be performed in SQL statements to produce any meaningful business
insights. These SQL queries with many JOINs are possible only when the data is small—
small compared to the big data volumes associated with data lakes and data warehouses.
Small data is typically defined as less than 1 million records, whereas big data exceeds
millions or billions of records (or petabytes) of data. The line of demarcation may be
better defined by the architectural demands that processing bigger data requires. Small
data can be processed on one machine, while big data requires distributed processing.

**Note** R 5, “Big Data
P Transformation with AWS Glue and A A

443

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**Data Scaling and the JOIN Problem**

I believe it’s critical to discuss the JOIN problem in depth because it truly is the limitation
that drives architectural design strategies for data warehousing. No matter what
architectural enhancements or performance optimizations are made, one thing remains
constant: for large unordered datasets, core algorithmic efficiency hasn’t substantially
improved since the hash join was introduced in the 1980s <sup>1</sup> .

I’ll introduce and briefly discuss several established JOIN strategies:

     - Nested Loop Join

     - Hash Join

     - Sort-Merge Join

     - Index Join

I won’t be reviewing the details of the specific algorithms for each of these strategies,
but you are encouraged to research and review them on your own. Instead, I’ll simply
describe how these different strategies scale with the size of the data sets. Consider a
simple example where we are joining just two tables with N and M number of rows.
Table 10-1 shows the scaling of join algorithms for tables of varying size.

**_Table 10-1._** _Number of Operations for Different JOIN Strategies and Table Sizes_

**JOIN Strategy** **Big O Notation** **Small Tables**
**(1M rows)**

**Big Tables**
**(50M rows)**

**Very Big Tables**
**(100M rows)**

Nested Loop Join O(n*m) 1T 2,500T 10,000T

H O(n+m) 2M 100M 200M

Sort-Merge Join O(n log n+m log m) 40M 4B 5.4B

Index Join O(n log m) 20M 2B 2.7B

Once the magnitude of the JOIN problem is appreciated, practitioners will better
understand that much of data warehousing architecture and design theory is based on
avoiding or mitigating the JOIN problem.

1 Kitsuregawa, Masaru, Hidehiko Tanaka, and Toshihide Moto-oka. “Hash Join Algorithms
in a Multiuser Environment.” IEEE Transactions on Knowledge and Data Engineering 2.1
(1986): 14-25.

444

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**Separating Analytical Workloads**

If the data volumes are not the constraint, there are still good reasons to separate
analytical workloads from operational workloads. Namely, you achieve separation of the
computing resources and can size each type of workload independently. Attempting to
serve reporting from operational systems either risks causing performance degradation
or results in overprovisioning to safely serve both workloads. As I mentioned previously,
merely housing analytical reporting in operational systems leads to more and more
artifacts (tables, scripts, ETL processes) being created to satisfy the ongoing and everchanging requirements of the business.

**Optimized Data Modeling and Organization**
**for Reporting**

Data warehouses provide both a primary data model and an organization strategy that is
optimized for reporting. A star or snowflake schema design attempts to address the JOIN
problem but also enables business intelligence tools to quickly aggregate quantifiable
data across any associated dimension. Data warehouses are primarily columnar rather
than row-based. We’ll review these two optimizations in this section.

**OLAP and Star Schema**

Online analytical processing (OLAP) systems describe a strategy where data is organized
into multiple dimensions (time, product, demographics) to facilitate data exploration
to discover trends and insights. This organization of data makes it easy to “slice and
dice” the data by specific dimensions. This in turn allows for aggregating (roll up)
or disaggregating (drill down) the data to provide summary or detail views. The star
schema data model is the primary implementation of an OLAP strategy. The star schema
features large “fact” tables with one or more quantifiable numeric fields and several
keys referencing dimension tables. The dimension tables are denormalized from any
subdimensions to ensure that each dimension table is only one join away. It’s important
to note that while there are multiple joins required to query this design, the dimension
tables are very small compared to the fact table, making these joins very efficient.
Figure 10-1 shows an example of star schema that features one fact table and fivedimension tables.

445

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**_Figure 10-1._** _Star Schema with Fact and Dimension Tables_

The diagram shows a series of dimensions with foreign keys (FK) referencing
primary keys (PK) in the dimension tables. A dimension is any attribute that describes
the numeric fact data. For instance, say we have a sales fact table that contains revenue
data. Each dimension will describe something about that revenue record. The most
common and valuable dimension is time, which answers the question—when was the
revenue generated? The time dimension can be broken down by day, month, year, or any
time dimension that is relevant. Another dimension may describe the location where
the sale took place, like a physical store or digital property, geographic region, zip code,
or designated marketing area (DMA). Other dimensions could indicate the customer
account, the sales representative, the sales territory, the district manager, or the area
leader. What makes these dimensions relevant is that they determine how the revenue data
can be aggregated for reporting, just by including or excluding dimensions in the query.
This is why capturing data accurately at the source at the lowest level of granularity is still
the most important factor for supporting robust, high-quality analytical reporting.

I discussed the benefits of columnar storage of data briefly in the context of serialization
formats and data lakes in Chapter 3, “Data Lake Design with Apache Iceberg and
S3 Tables.” In RDMS, data is stored in rows. This means that all the data for the row
is retrieved when it is in scope for the query. In columnar systems, data is stored by
columns across multiple rows (Figure 10-2) in blocks on disk.

446

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**_Figure 10-2._** _Columnar Storage of Data_

Columnar storage is a key strategy for data warehouses for several reasons.

Storing data by column allows the data set to be easily split and distributed across the
nodes of a cluster. Because the data from a column has the same attributes and data
type, it allows the nodes to process this data independently.

Queries that only include a subset of columns will exclude those columns entirely from
the data that is read and transmitted over the network and between nodes. For instance,
if my table has 100 columns, but I only want to return 5 of them, I’m saving 95% of the
data processing costs.

Because we are saving column data together, we can utilize a compression scheme
optimized for the column data type, further reducing disk space and I/O.

Now let’s take a look at the AWS flagship data warehousing solution, Amazon
Redshift.

Amazon Redshift is a fully managed petabyte-scale data warehouse that is used by
tens of thousands of customers to power their analytics workloads. Redshift features a
massively parallel processing (MPP) architecture and columnar storage, distributing

447

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

workloads across multiple nodes to deliver exceptional query performance. Features
like elastic resize and concurrency scaling allow Redshift to serve thousands of users
and scale up or down based on the demands of the workload. Redshift is integrated
with AWS services like Amazon S3 for automated ingestion with S3 Copy. Another S3
integration feature called Redshift Spectrum leverages cluster compute to power queries
on datasets in an S3 data lake. Redshift supports zero-ETL integration from 12 sources,
including continuous replication from Amazon Aurora databases. Through federated
query, Redshift can query data in operational data in external databases and join them
with other datasets. Robust security features protect data through encryption at rest and
in transit, IAM integration, and both column- and row-level security for fine-grained
access control. Redshift data sharing allows organizations to seamlessly and securely
share data across multiple Redshift clusters without the need for data copying. Data can
be shared across business units or between organizations without significantly affecting
the performance of the producer cluster. While we immediately think of structured data
primarily, Redshift supports querying of open data formats like Parquet, OCR, avro,
JSON, and CSV.

I don’t have the space to explore all these great features in depth, but there’s plenty
of guidance available in the product documentation and blogs. Instead, I’ll build a
sales datamart solution (available in the GitHub repo) that I’ll use to demonstrate
some of the Redshift design and optimization features while adding Text-to-SQL
reporting capabilities.

Let’s dive deeper into Redshift’s architecture. Any data engineer should have an intimate
understanding of the system architecture on which they’re running their workloads. In
a Redshift cluster there is a leader node and compute nodes. Leader nodes serve as the
SQL endpoint. It stores metadata and coordinates parallel SQL processing and other
ML optimizations. There is no charge for the leader node for clusters with two or more
nodes. Compute nodes are partitioned into “slices” of virtualized memory and disk
space that provide local columnar storage. They load, unload, back up, and restore from
Redshift-managed storage in Amazon S3. Redshift RA3 nodes utilize a custom analytics
processor developed by AWS that powers an Advanced Query Accelerator (AQUA).
AQUA is a distributed hardware-accelerated processing layer that executes queries in
parallel. Figure 10-3 shows the full Amazon Redshift architecture.

448

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**_Figure 10-3._** _Amazon Redshift Architecture_

I’ll highlight a few important features about this Redshift architecture. Redshift has
an autoscaling feature that spins up additional clusters to execute queries separate from
the primary cluster. There’s also a global cache provided as part of the cluster. From the
diagram you’ll notice that the Redshift data sharing service is delivered via a separate
compute cluster, which loads data directly from Redshift Managed Storage (RMS). The
RMS is a storage layer that separates data from compute in Redshift, allowing each
to scale independently. This allows the service to scale without causing performance
degradation on the primary cluster. When querying data from Amazon S3 with Redshift
Spectrum, AWS scales Spectrum compute nodes to 10x the number of Redshift cluster
nodes. You won’t be charged for this additional Spectrum compute. Instead, you’ll be
charged based on the volume of S3 data scanned.

449

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

Redshift offers two types of deployment: serverless and provisioned. Redshift Serverless
offers instant fine-grained scaling for compute and memory, pricing in Redshift
Processing Units (RPUs) rather than hourly pricing based on node size, and AI-powered
scaling and optimizations. With serverless, you can define a base capacity and max
capacity to control performance and costs. You’re only charged for the compute capacity
consumed when queries are running. You are charged for Redshift Managed Storage
for the duration that storage is consumed. This means that for workloads that are
highly spikey or irregular, Redshift Serverless could be very economical compared to
provisioned clusters while also requiring less operational overhead.

**Redshift Workload Management**

Redshift workload management (WLM) addresses how Redshift prioritizes and manages
concurrency when multiple queries compete for the same limited cluster resources.
WLM helps ensure that short, fast-running queries don’t get stuck in queues waiting for
long-running queries to complete. By default, Redshift provides an automated WLM that
dynamically determines whether to run queries on the primary cluster, on a concurrency
scaling cluster, or to send each to a queue, with shorter queries being prioritized. A
typical use case would be to create a separate queue for ad hoc queries by data analysts,
which may be long-running, to avoid blocking customer reporting queries.

**Redshift Table Design Considerations**

There are a few key differences in Redshift table design compared to RDBMS design that
practitioners should know when designing data warehouses. Some are Redshift-specific
implementations, and others are generally required due to its MPP architecture.

**No Enforceable Constraints**

The first important difference to note is that there are no enforceable constraints in a
Redshift data warehouse. This includes primary keys, foreign keys, unique constraints,
check constraints, or exclusion constraints.

450

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**Note** Unique, primary key, and foreign key constraints are permitted but
are informational only and NOT H
_are_ considered by the query planner. It is recommended to add informational
constraints to enhance maintainability and query performance.

The reason is obvious when you remember that Redshift, like other data warehouses,
is based on an MPP architecture and utilizes columnar storage. In an operational data
system with a highly normalized relational data model, constraints are needed to enforce
data integrity. It’s important to understand that these constraints are enforced with some
piece of internal code that has to validate whatever the constraint is asserting. Each
piece of code requires compute and memory consumed over a discrete period of time.
Imagine running this piece of enforcement code on a one-billion-row table with just
three constraints! For MPP data warehouses, tradeoffs are made in favor of performance,
relegating data integrity enforcement as a responsibility of the developer to validate prior
to loading. Since analytical systems are intended to be mostly read-heavy systems, this
tradeoff makes sense.

An important design consideration in Redshift table design is the use of sort keys. They
allow the designer to choose one or more columns by which to sort the data set. Recall
the join problem discussion earlier in the chapter: the Sort-Merge join had an order of
magnitude of O(n log n + m log m), but this was for an _unordered_ data set. If the table
maintains a sorted order, join complexity drops to O(n + m). Sort keys are not required
by default, as they add overhead to insert operations. Staging tables and other writeheavy tables that require faster data loading shouldn’t get a sort key. Most other tables
that are queried and have predictable query patterns will benefit from sort keys. Here’s a
brief overview of the options.

**Note** Sort keys are immutable after table creation. To change a sort key, the
existing table needs to be migrated to a new table with the updated sort key.

451

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**Single Sort Key**

The table is sorted by a single column. Access patterns that consistently choose a specific
dimension in all queries may have just one sort key. For example, time series data tables
that feature a timestamp or date column could choose it as the sort key. Another use case
may be ID lookup tables.

**Compound Sort Key**

A compound sort key includes multiple columns where the sort order is enforced. This
type of sort key is optimal for queries that filter the data in the order defined in the sort
key. Compound sort keys cannot include boolean columns and are limited to tables with
400 columns or less.

**Interleaved Sort Key**

An interleaved sort key includes multiple columns where each column is given equal
weight. This is preferred for tables with less predictable query patterns and requires
additional maintenance. Tables with interleaved sort keys are limited to a maximum
of eight columns and require VACUUM REINDEX to be run after large table updates.
For example, when the number of unordered records exceeds 20% or after large table
operations like bulk inserts or mass updates and deletes.

If you’re unsure as to how to choose a sort key strategy, you can use the SORTKEY
AUTO clause in the table definition to use the Redshift ML feature to analyze a table’s
query patterns and recommend a sort key strategy. System tables and views can be
queried to retrieve the suggestions. Consult the documentation for more details.

Another important design configuration is the distribution style of the table. Since
we know Redshift is an MPP data warehouse with cluster architecture, how the data
is distributed across the compute nodes will ultimately determine how queries will
perform. The more data that needs to be copied across the network to execute a
query plan, the more latency will be incurred. Redshift allows designers to choose a
distribution style for their tables. Like sort keys, distribution styles are immutable, and
tables must be recreated if you wish to change them. Table 10-2 shows a brief overview of
each distribution style and when they might be used.

452

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**_Table 10-2._** _Redshift Distribution Styles and Their Recommended Use Cases_

**Distribution**
**Style**

**Best For** **Use Case** **Notes**

A T Unknown
patterns

New tables R
distribution style and adapts as data volume and
query patterns change.

E E No clear key Standalone
tables

Distributes rows round-robin across all slices.
Minimizes data skew and enhances parallel
processing.

KE Join
operations

Fact tables Distributes keys based on column values, with
matching values going to the same compute node.

A Small tables Dimension
tables

R
E

**Change Data Capture (CDC) with ZeroETL**

One of the most common business requests for data warehouses is that they reflect the
real-time changes of the operational system. The fresher the data, the more valuable
it is to the business. Sometimes the need for freshness causes compromises in the
basic principles discussed earlier in the chapter—namely, to separate analytical from
operational workloads. In the rush to get the business the most current data, leaders
may hastily agree to enable reporting from operational systems. To avoid this conflict, an
enterprise data practice needs to anticipate this need and put in place a robust change
data capture (CDC) strategy. AWS now offers a managed solution for its Amazon Aurora
database service called ZeroETL (see Figure 10-4), which is a managed CDC feature that
replicates data in real time from Aurora databases to Redshift.

**_Figure 10-4._** _Amazon Aurora ZeroETL to Amazon Redshift_

453

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

There are no ETL jobs to write, run, monitor, or manage. There is no additional cost
beyond what additional resources are consumed in Aurora or Redshift to facilitate this
replication.

**Automated Batch Loading with Auto-Copy**

For batch workloads, Redshift provides an auto-copy feature to execute the COPY
command on files delivered to a designated S3 bucket and prefix location. You can
designate multiple table-loading operations distinguished by an S3 prefix. Multiple
operations can load into the same table or different tables. Figure 10-5 shows the
architecture of the auto-copy feature and the prefix mapping.

**_Figure 10-5._** _Redshift Auto-Copy Feature from Amazon S3_

The auto-copy feature provides an AWS-managed, event-driven bulk ingestion
process into Redshift, eliminating logic customers had to build and manage themselves.

Next, I’ll demonstrate data warehousing design principles in Redshift through a
sample data warehouse for sales data.

**Sales Datamart Demo**

Building out a sample data warehouse to use for hands-on exploration and testing is the
best way to learn Amazon Redshift. As a reader of this book, you’re provided a GitHub
repo that contains a fully designed datamart complete with generated sample data for a

454

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

prototypical sales operation. I’ll provide some highlights from the data model and some
design considerations for Redshift.

For this sales data warehouse, I’ve created one fact table and nine dimension tables.
Due to space constraints, I won’t present the full data model here, but you’re encouraged
to reference it in the GitHub project. Here is the full table definition for the fact table;

CREATE TABLE sales.fact_sales (

455

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

FOREIGN KEY (territory_key) REFERENCES dim_sales_

territory(territory_key),

) DISTSTYLE KEY
SORTKEY

Column compression is an important optimization feature at scale. The column
clause “ENCODE az64” indicates that the column is compressed using the Automatic
Zero-Padding (AZ64) encoding algorithm, which is recommended for numeric columns.
In Table 10-3, I list and describe all the tables in our star schema model.

**_Table 10-3._** _Sales Datamart Demo Tables_

**Table Name** **Description**

fact_sales A T
order_id and order_date_key.

dim_time A
attributes that enables time-based reporting across date hierarchies.

dim_account A
customer.

dim_district Sales district table.

dim_dma Designated Marketing A A
of households.

dim_product P

dim_region R

dim_sales_rep Sales representatives with associated contact information, territory, and
manager.

dim_sales_territory Sales territory table.

dim_zipcode Location table with zip code with lat and lon, city, state, country, and
timezone.

456

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

The solution available in the GitHub repo deploys this data model and simulated
data. The hope is to provide a real-world data warehouse to experiment with Text-to-SQL
and dynamic reporting.

Next, let’s take a quick look at the generative AI features integrated into Redshift
query editor v2.

**Redshift Query Editor v2**

Amazon Redshift Query Editor v2 is accessible via the AWS console (see Figure 10-6) and
includes several generative AI features that enhance the SQL development experience.

**_Figure 10-6._** _Redshift Query Editor v2 in the AWS Console_

At its core, the editor offers SQL query generation capabilities, allowing users to
translate natural language descriptions into SQL queries and receive contextaware query suggestions. For query optimization, the editor leverages AI to provide
performance recommendations and automated troubleshooting suggestions. The code
completion system is AI-enhanced, offering intelligent auto-completion for SQL syntax
and smart suggestions based on schema context, including intelligent recommendations
for table joins. Additionally, the editor provides natural language explanations of
complex SQL queries and execution plans, making it easier for users to understand and
optimize their database operations.

The editor itself has all of the premium features you’d want or expect from an
enterprise SQL client and editor, like the ability to share notebooks and scripts with
team members, query execution plan visualization, multiple tabs for parallel query
development, and query history and search. There are two things that are needed to
enable Redshift query editor v2 and its generative AI features. First, you need to specify
an S3 bucket where the query editor can write results. You’ll also need to configure
additional permissions for the role, including:

457

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

     - redshift:GenerateQuery

     - redshift:ExplainQuery

     - redshift:OptimizeQuery

Consult the documentation for detailed guidance. You can access Amazon Q
generative SQL by clicking on the Q icon on the lefthand menu (see Figure 10-7).

**_Figure 10-7._** _Amazon Q Generative SQL_

Clicking on this icon opens up a chat window where you can ask it to generate
SQL queries using natural language. I used one of the sample reports, “Compare sales
performance by region for the last 3 months,” suggested in the Redshift sales demo. The
generated SQL did provide a date filter that I didn’t ask for. However, the more I thought
about it, the more I realized that from a cost perspective, this serves as an important cost
governor. The filter reduces the likelihood that an analyst blindly scans an entire data set.
Instead, the user is forced to review and modify the date filter.

458

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

Here is the generated query produced by Redshift query editor v2:

_SELECT_
_dr.region_name,_
_SUM(fs.sales_amount) AS total_sales,_
_SUM(fs.profit_amount) AS total_profit_
_FROM_
_sales.fact_sales fs_
_JOIN sales.dim_time dt ON fs.order_date_key = dt.time_key_
_JOIN sales.dim_region dr ON fs.region_key = dr.region_key_
_WHERE_
_dt.date_actual BETWEEN DATE '2025-04-21'_
_AND DATE '2025-07-20'_
_GROUP BY_
_dr.region_name_
_ORDER BY_
_total_sales DESC;_

Figure 10-8 shows the query editor and the generative SQL chat window where you
can engage in an interactive session defining and refining the data request.

459

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**_Figure 10-8._** _Amazon Q Generative SQL in Redshift Query Editor v2_

The feature can also recommend reports and queries to run based on your schema.
The Redshift query editor v2 feature is best suited for the research analyst, who
iteratively develops ad hoc reports (with eyes on glass) from Redshift in the console. For
production applications, you’ll need a programmatic interface.

In the next section, I’ll present guidance for implementing Text-to-SQL
solutions on AWS.

**Prompt Engineering for Text-to-SQL**

Whether using an LLM directly or a specialized agent, we can dynamically generate valid
SQL from natural language to query data warehouses for reporting. This is a generalized
strategy and not one that is specific to any platform or service. Anthropic Claude 4 has
been shown to produce the most robust coding results and will be used in the following
examples.

460

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**Caution** E
LLMs creates a threat vector for SQL injection-style attacks. Use guardrails and
evaluation agents to screen for risks as part of any solution.

Text-to-SQL prompts require several elements. First, the prompt needs to include
explicit instructions for the task the model is being asked to perform. For Text-to-SQL,
the task will be to generate a SQL statement for a specific SQL data system (Redshift)
with a natural language description of the desired report. The next element needed
for the context is the description of the data model. Foundation models utilizing deep
reasoning agentic architectures are able to infer quite a bit with even vague requests. You
can then provide guidelines to constrain or enhance how the SQL query is generated.
Finally, we define the output desired. We can specify how we want the results. Do we
want just the SQL query? Do we want comments added? Do we want an explanation or
assumptions made about the data model? Let’s look at how to structure the data model
in the context.

**Structured Input Formatting**

We can use a loosely structured input format when defining the data model. LLMs can
understand quite a bit of nuance. Describing the schema doesn’t require a strict ANSIcompliant block of code. Instead, you can simply list a table and its columns and include
all the extra artifacts like keys and informational constraints. In the interest of both
optimization for token consumption (cost) and security, we can limit what fields we tell
the model exist in the data warehouse. By excluding fields in the definition, they will not
be used to generate the SQL query. You can even use generative AI to generate a schema
description for your prompt template:

_DATABASE SCHEMA_
_**Schema**: sales (Star Schema Architecture)_
_FACT TABLE_
_**sales.fact_sales** (Main Transaction Table)_

_- sales_key (BIGINT)_

_- order_id (VARCHAR)_

_- order_date_key (INT)_ → _dim_time.time_key_

_- ship_date_key (INT)_ → _dim_time.time_key_

461

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

_- account_key (INT)_ → _dim_account.account_key_

_- product_key (INT)_ → _dim_product.product_key_

_- sales_rep_key (INT)_ → _dim_sales_rep.sales_rep_key_

_- territory_key (INT)_ → _dim_sales_territory.territory_key_
_…_

This structured formatting identifies the type of table, the name of the table, and its
columns. You can also include primary key, foreign key, or other constraints. With this
information, the model can construct an SQL query depending on the request. If the
data set was semi-structured, unstructured, or complex, we could use nested JSON with
descriptive tags to format the schema for the prompt. You can add other sections to the
prompt template, including guidance on join relationships, common query patterns,
geographic and time hierarchies, key metrics and calculations, and example queries.

_## COMMON JOIN PATTERNS_
_Basic Fact-Dimension Joins:_
_-- Time-based analysis_
_fact_sales f JOIN dim_time t ON f.order_date_key = t.time_key_
_-- Product analysis_
_fact_sales f JOIN dim_product p ON f.product_key = p.product_key_
_-- Customer analysis_
_fact_sales f JOIN dim_account a ON f.account_key = a.account_key_
_-- Sales rep analysis_
_fact_sales f JOIN dim_sales_rep sr ON f.sales_rep_key = sr.sales_rep_key_

_### Geographic Hierarchy Joins:_
_-- Full geographic hierarchy_
_fact_sales f_
_JOIN dim_sales_territory st ON f.territory_key = st.territory_key_
_JOIN dim_district d ON f.district_key = d.district_key_
_JOIN dim_region r ON f.region_key = r.region_key_

_## KEY METRICS & CALCULATIONS_
_### Standard Measures:_

_- `SUM(sales_amount)`_

_- `SUM(profit_amount)`_

_- `SUM(quantity)`_

462

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

_- `COUNT(DISTINCT order_id)`_

_- `COUNT(*)`_

Only an excerpt is shown due to space constraints. Consult the prompt template for
the full scope. Now let’s look at what an architecture might look like on AWS.

**Text-to-SQL Solution Architecture**

Operationalizing this capability into a product or application requires a full solution
architecture beyond sending prompts in the LLM. We can envision these tasks being
performed by agents. There may even be a Text-to-SQL agent that specializes in this task.
If not, you can certainly train and deploy one. Figure 10-9 shows what a basic Text-toSQL architecture would look like on AWS.

463

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**_Figure 10-9._** _Text-to-SQL Solution Architecture_

The diagram features user request handling by Amazon API Gateway. The Lambda
Function passes the request to a Text-to-SQL agent. This agent pulls the prompt template
from DynamoDB, combines it with the user request, and prompts an LLM in Bedrock to
generate the SQL. The agent then sends the generated SQL query to the SQL Evaluation
Agent to validate the syntax and analyze it for any security risks. The agent then queries
Redshift via MCP. Let’s take a closer look at each of the agents.

464

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

I use the template below as instructions for the TextToSQLAgent in Bedrock Agents.

_You are a specialized text-to-SQL agent for a Redshift data warehouse with_
_a sales schema. Your job is to convert natural language requests into SQL_
_queries._
_You will be provided with a schema and a user request. Generate a valid SQL_
_query that answers the user's request based on the schema provided._

_[USER REQUEST]_

_[SCHEMA]_

_Guidelines:_

_Include appropriate JOINs between fact and_

_dimension tables_

_Use descriptive column aliases for calculated fields_

_Format the query with proper indentation and comments_

_Consider performance optimization for Redshift_

_(distribution keys, sort keys)_

_Include appropriate filters, grouping, and sorting based_

_on requirements_

_Pay attention to _key vs _id naming conventions_

_(use _key for dimension keys)_

_For time-based analysis, leverage the dim_time table_

_hierarchy_

_Output:_

_Provide the complete SQL query_

_Include brief comments explaining key parts of the query_

The placeholders in brackets are intended as guidance for a constructed prompt that
is sent into an LLM.

465

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**SQL Evaluation Agent**

No matter how great the initial SQL generation is, there’s no way for us to know. So in
order to evaluate the generated queries, I use an SQL Evaluation Agent to analyze the
generated SQL query for errors, inefficiencies, or security risks. Here are the instructions
I provided to the agent:

_You are a specialized SQL evaluation agent._
_Your job is to validate SQL queries for correctness and safety._
_When given a SQL query, analyze it for:_
_1. Syntax errors_
_2. Potential performance issues_
_3. Security concerns like SQL injection_

_If the query is valid, respond with "VALID" followed by the_
_validated query._
_If the query has issues, explain the problems and suggest corrections._

Why utilize a different agent for SQL evaluation? You definitely could attempt to
perform the same tasks from one agent; however, the separation of concerns allows for
each to be developed independently and without contamination.

The demo solution provided as part of this book includes a fully functional web interface
that processes requests through API Gateway. Figure 10-10 will help you envision the
capabilities.

466

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**_Figure 10-10._** _Web Interface for Redshift Text-to-SQL Demo_

The demo solution processes the request and returns both the SQL statement that
was generated and the result set (see Figure 10-11) from executing the query on the
Redshift cluster.

467

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**_Figure 10-11._** _The Generated SQL and Resultset from the Demo Solution_

This demo provides a great testbench for exploring Redshift data warehousing and
Text-to-SQL reporting that you can customize specifically to your use case.

**Generating Report Suggestions**

Generative AI can even suggest reports and queries based on the data model. Providing
options to users might be a good way to get them to start exploring. For example,
asking Kiro CLI in the project folder, “ _What are some reports I can run against this data_
_warehouse?”_ yielded the following list:

1. Monthly Sales and Profit Analysis

       - Track sales and profit trends over time by region

       - Identify seasonal patterns and year-over-year growth

468

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

2. Product Performance Analysis

     - Identify top-selling products by revenue, quantity, or
profit margin

     - Analyze product category performance across different regions

3. Sales Representative Performance

     - Compare sales rep performance metrics (sales amount, new
accounts, profit)

     - Track performance against targets and historical benchmarks

4. Customer Segmentation Analysis

     - Analyze sales by customer segment and industry

     - Identify high-value customer accounts and growth opportunities

5. Geographic Sales Distribution

     - Visualize sales distribution across territories, districts,
and regions

     - Identify underperforming or high-potential geographic areas

6. Sales Channel Comparison

     - Compare online vs. in-store sales performance

     - Analyze channel effectiveness by product category or
customer segment

7. Return Rate Analysis

     - Track product returns by category, region, or sales rep

     - Identify quality issues or customer satisfaction problems

8. Day of Week/Time Analysis

     - Analyze sales patterns by day of week, time of day, or season

     - Optimize staffing and inventory based on peak sales periods

469

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

9. Customer Lifetime Value Analysis

       - Calculate and track customer lifetime value metrics

       - Identify factors that correlate with high-value customers

10. Market Penetration Analysis

       - Analyze sales by Designated Market Area (DMA)

       - Identify market share and growth opportunities

These are highly relevant business-focused report suggestions generated from the
data model.

**Redshift Integration with Amazon Bedrock**

Redshift now integrates directly with Amazon Bedrock to apply Bedrock model
inference to data in Redshift. This integration allows you to invoke LLM models from
SQL statements in Redshift. The benefit of this capability is that it allows you to bring
generative AI inference for sentiment analysis, text classification, or data enrichment at
scale without moving data out of Redshift. With the broad selection of Bedrock models,
you can optimize the best model choice for the task based on capability, cost, and
latency. Let’s take a look at how to set this up.

**IAM Policy to Authorize Bedrock Access**

First, we need to add this IAM policy to the Redshift IAM role to authorize Redshift to
invoke models in Bedrock.

{

470

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

}

In the resource section, you can add multiple models and just those models you
want to allow invocation from Redshift. This provides an important control mechanism,
as you can specify models priced to meet the budget at scale.

**Create External Model**

Redshift implements Bedrock integration through the CREATE EXTERNAL MODEL
command.

CREATE EXTERNAL MODEL public.customer_sentiment
FUNCTION fn_analyze_sentiment
IAM_ROLE default
MODEL_TYPE BEDROCK
SETTINGS
( MODEL_ID 'amazon.nova-micro-v1:0',
PROMPT 'Analyze the customer feedback for sentiment and score it from 1
least positive to 5 most positive');

**Generate Sentiment Scores with Bedrock Model**

Let’s see how we can invoke the Bedrock model on a tabular data set of structured data.

SELECT fn_analyze_sentiment(customer_feedback) as sentiment_score
FROM support_tickets
Where ticket_date = [date]

This provides a powerful option for enriching our Redshift data. You can also
integrate your own custom or SageMaker Jumpstart models hosted on SageMaker
endpoints. We’ll take a look at how to do that next.

471

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**Redshift Integration with Amazon SageMaker**

Redshift also supports invoking LLMs hosted on Amazon SageMaker from SQL
statements for various data enrichment use cases. This Redshift ML feature allows
models you’ve customized or fine-tuned that you’ve hosted on SageMaker to apply AI
augmentation on sets of data. Let’s take a quick look at what we need to do to set this up.

**IAM Role and Policy to Authorize SageMaker Access**

We will be required to specify an IAM role and attach it to the Redshift cluster as well
as reference it in the CREATE MODEL statement. The Redshift cluster validates that a
referenced IAM role was attached to the cluster by a systems administrator, allowing its
use. I’ll call it RedshiftMLRole:

{

}

Now we need to create a policy that gives Redshift permission to DescribeEndpoint
and InvokeEndpoint for the specific SageMaker endpoint we want to use. We can list all
the endpoints we want to provide access to.

{

472

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

}

We’ll need to attach the role to the Redshift cluster, which will validate that the
reference role ARN in the SQL statement is a valid, attached IAM role.

**Create External Model**

Once we have the IAM policies defined and attached to the Redshift cluster, we use the
CREATE MODEL SQL statement. We specify both the SageMaker endpoint and the IAM
role ARN.

CREATE EXTERNAL MODEL public.sentiment_classifier
FUNCTION fn_classify_sentiment(super)
RETURNS super
SAGEMAKER 'custom-bert-sentiment-endpoint'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftSageMakerRole';

**Generate Sentiment Scores with Custom Model**

Now we simply reference the custom model like we did with the Bedrock model.

SELECT fn_classify_sentiment(customer_feedback) as sentiment_score
FROM support_tickets
Where ticket_date = [date]

Great, now we can use both Bedrock-hosted models and custom SageMaker-hosted
models to enrich our Redshift data.

Let’s look at another way Redshift can support AI use cases.

**Redshift for Retrieval-Augmented Generation (RAG)**

Redshift data warehouses can also be used as a data source for knowledge bases for
Retrieval-Augmented Generation. From the Bedrock console, choose **Knowledge Bases** .
To source your knowledge base from Redshift, you’ll need to choose **Structured data**

473

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**store** from the **Create** button. Figure 10-12 shows Redshift as the only option for our
Bedrock knowledge base.

**_Figure 10-12._** _Redshift as a Structured Data Source for Bedrock Knowledge Bases_

We specify the Redshift cluster and database and let Bedrock Knowledge Bases do
the rest. Once the service has ingested and vectorized the metadata, we can perform a
semantic search on this structured data to enhance the context of our model prompt.

474

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

**Redshift ML for Predictive Model Training**

We can train predictive models right in Redshift using an SQL interface (no Python, no
notebooks, no SageMaker console) with the data in Redshift! Behind the scenes, Redshift
is calling SageMaker ML operations. You may wonder why anyone would want to train
ML models from Redshift. Well, you may be surprised to learn that RedshiftML-trained
models are hosted inside Redshift itself and not on SageMaker endpoints! They run
locally on your Redshift compute nodes. There are two primary benefits. First, Redshift
model inference runs faster because these models are hosted locally, avoiding the
latency of additional network hops to invoke a different service endpoint. The second
benefit is cost. Redshift model inference is served using the cluster compute. You avoid
the additional cost of running separate inference endpoints in SageMaker. You will be
billed for any SageMaker services that are consumed during the training, compilation,
and validation phases of the Redshift ML model creation process. These costs are
typically minimal.

Before we jump into the examples, take note of the following data requirements to
ensure a well-trained model:

     - At least 500 rows (preferably 10,000+)

     - Clean data (handle NULLs)

     - Balance classes for classification (if possible)

     - Representative of production data

**Create an S3 Bucket for Training Data Export**

As part of the model training process, Redshift will export the training set specified in the
CREATE MODEL statement to S3. We’ll need to create an S3 bucket first so that we can
specify access permissions in the IAM role.

# Create dedicated bucket
aws s3 mb s3://redshift-ml-123456789012 --region us-east-1

Now we can define our IAM role and permissions.

475

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

**IAM Role and Policy for SageMaker Model Training**

There are a few blocks of permissions needed to enable SageMaker model training from
Redshift. I’ll break it down by section and point out any important notes.

#SageMaker permissions
{

These are the core SageMaker permissions for the entire ML training lifecycle. The
reason for the wildcards in the resource list is because SageMaker resources are created
dynamically with generated names. Redshift doesn’t know the names in advance, so it

476

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

needs wildcard access. Following the principle of least privilege, you could restrict to
specific patterns as I show above.

Then we’ll need to authorize Redshift to pass the RedshiftMLRole permissions to the
SageMaker service.

{

We’ll need to add permissions so Redshift can find the S3 bucket and export the
training data.

{

{

477

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

Because the SageMaker operations create dynamically named training jobs, we need
to enable Redshift to create log groups and write logs for these training jobs to Amazon
CloudWatch.

{

}

SageMaker runs training jobs in Docker containers with pre-built images stored in
Amazon Elastic Container Registry (ECR). AWS provides pre-built images for the most
common ML algorithms, including XGBoost, Linear Learner, MLP, and K-Means. Also,
there’s a prebuilt image for AutoML as a strategy.

During the training jobs, SageMaker publishes various metrics to CloudWatch. We
need to add an additional permission to allow these metrics to be published.

{

478

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

Training job metrics that get published to CloudWatch include:

     - Training loss

     - Validation accuracy

     - CPU/GPU utilization

     - Memory usage

     - Training progress percentage

With our IAM role and permissions defined, we’ll attach this to the Redshift cluster.

**Grant User Access to Model Creation and Schema**

One final step before we start training models. We need to grant the user permissions to
create a model and access the schema we’re using to organize the model.

-- Grant CREATE MODEL permission
GRANT CREATE MODEL TO my_user;

-- Grant schema permissions
GRANT CREATE, USAGE ON SCHEMA analytics TO my_user;

Now that we have all the permission set, we’re ready to train a model.

There are two types of model training supported by RedshiftML: AUTO ON and AUTO
OFF. I would recommend AUTO ON to train models using the SageMaker AutoML job
exclusively. With AutoML training jobs, Redshift (SageMaker) automatically handles
everything: feature engineering, algorithm selection, and hyperparameter tuning. Due
to space constraints, I’ll only demonstrate the AutoML training job option. The model
I’ll build for our example is a customer churn prediction model. For supervised ML

479

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

algorithms, a target column indicating the verified outcome is required. In this case,
whether the customer churned or was retained. In our analytics.customer_data table,
the target column we specify is “churned” and contains a boolean “Y” or “N”.

**Note** Machine learning fundamentals are out of the scope of this book, but
readers are encouraged to consult additional references if needed.

To kick off the training process, we’ll execute this statement in Redshift.

CREATE MODEL analytics.churn_predictor
FROM analytics.customer_data
TARGET churned
FUNCTION fn_predict_churn
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftSageMakerRole'
SETTINGS (

)
AUTO ON;

Training time will vary depending on the size of the dataset. Here is general guidance
for training job duration given the following data sizes:

     - Small datasets (<10K rows): 15-30 minutes

     - Medium datasets (10K-100K rows): 30-90 minutes

     - Large datasets (>100K rows): 1-3 hours

The maximum model size that can be imported into Redshift is 100MB (compiled);
however, most models are between 1MB and 50MB.

The CREATE MODEL statement kicks off a process that includes the following steps:

1. Redshift exports training data to S3 (your specified bucket)

2. SageMaker AutoML jobs launch (if AUTO ON):

a. Profiles the data

b. Performs feature engineering on the data

480

Chapter 10 DATA AREH TH E ERAT EA A TE T-T REP RT TH
A A RE H T

c. Tests multiple algorithms (XGBoost, Linear Learner, MLP)

d. Performs hyperparameter tuning

e. Selects the best model based on validation metrics

3. The trained model is compiled using SageMaker Neo

4. The compiled model is imported back into Redshift

We can test the model performance using the EXPLAIN_MODEL function.

-- Get model explanation (if AUTO ON was used)
SELECT EXPLAIN_MODEL('analytics.churn_predictor');

The EXPLAIN_MODEL() function returns a JSON result that includes model
performance metrics and SHAP values showing which features (customer attributes)
have the most impact on predictions.

In order to perform batch inference with our trained model, we simply need to call our
model function and include the same attributes used to train the model, excluding the
target column, “churned.”

-- Score all active customers
SELECT

481

Chapter 10 DATA AREH TH E ERAT E A A TE T-T REP RT TH
A A RE H T

FROM analytics.customer_data
WHERE churned IS NULL;

We made it to the end of our data warehousing deep dive with Amazon Redshift!
Let’s summarize what we covered and move on to the next topic.

In this chapter, I explored theoretical concepts of data warehousing and its practical
implementation on AWS with Amazon Redshift. I examined how generative AI is
transforming traditional data warehouse development and reporting. I described the
fundamental challenges of the JOIN problem at scale and how it has influenced modern
architectural strategies. I dived deep into Amazon Redshift’s architecture, describing
its key features and components like leader and compute nodes in Redshift clusters,
separated autoscaling and data sharing clusters, global caches, its ASICpowered Advanced Query Accelerator (AQUA), Redshift Spectrum for powering queries
on data in S3, and Redshift Managed Storage (RMS). I highlighted best practices for
data warehouse design generally, including the implementation of the star schema.
I demonstrated how to design data warehouses in Redshift, including sort key and
distribution style selection strategies to enable efficient query processing at scale. I
demonstrated theoretical concepts by providing concrete examples of table design and
optimization strategies through a deployable sales data mart. The chapter then shifted
to AI integration, examining both assistive and autonomous capabilities. An agentic
Text-to-SQL architecture demonstrated how to query structured data with natural
language, while the query editor v2’s AI coding features showed practical productivity
gains. RedshiftML opened even broader possibilities: native integrations enable model
inference from models hosted in Bedrock and SageMaker directly within the warehouse.
You can train predictive ML models on your data warehouse and use them locally for
batch inference—all without moving data outside Redshift.

In the next chapter, I continue the discussion of generative business intelligence with
Amazon Quick Suite and dynamic reporting with Amazon QuickSight Q.

482

**CHAPTER 11**

## **Generative Business** **Intelligence with Amazon** **Quick Suite**

Generative and agentic AI promises to transform business intelligence more now than
at any time since it rose to prominence in the 1980s. Up until recently, BI tools and
platforms offered variations on a theme: a report designer for power users to design
reports and dashboards with (pivot) tables, charts, and graphs and publish them to
business stakeholders. These reporting platforms included features to easily exploit the
Star Schema data model—like providing a “drag and drop” experience for authors to
select numeric columns (referred to as “measures”) and any combination of dimensions
for aggregation. For example, think of a sales fact table containing the most granular
level of sales—individual orders. This table includes the date and time of the sale, the
location of the sale, and the product and quantity sold. We may want to see sales per day,
week, month, or quarter. We may want to see sales aggregated by DMA, territory, or zip
code. With a modern BI platform, we can “slice and dice” sales revenue this way for any
combination of dimensions.

Now with the emergence of generative and agentic AI, there are opportunities
to significantly extend and augment capabilities well beyond what traditional
business intelligence can deliver. One of the first and most compelling use cases is
transforming how organizations conduct research and analysis—moving from static
dashboards and manual data exploration to AI-powered agents that can autonomously
investigate complex questions, synthesize insights from multiple sources, and generate
comprehensive reports that would traditionally require days of an analyst’s time.

In this chapter, I explore the origins and evolution of business intelligence leading
up to the modern-day capabilities of using generative and agentic AI for unifying

483
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_11](https://doi.org/10.1007/979-8-8688-2199-8_11#DOI)

Chapter 11 Generative Business I g c A c S

intelligence across an enterprise. I present Amazon Quick Suite and its AI-powered
features for supercharging enterprise productivity, including deep research, workflow
automation, and document search. I dive deep into the generative BI (GenBI) features of
QuickSight, demonstrating how to design a semantic layer to support natural language
querying and dynamic insight generation. Another QuickSight feature uses generative AI
to create insight narratives for data, called data stories.

**The Origins of Business Intelligence**

The term “Business Intelligence” dates all the way back to 1865, when Richard Miller
Devens first described the concept in his “Cyclopædia of Commercial and Business
Anecdotes.” In it, Devens told the story of Sir Henry Furnese, a banker, who profited
by gathering and analyzing information and taking action before the competition.
Throughout the latter half of the 20th century, with the proliferation of digital computing,
business intelligence evolved to exist exclusively within the context of technology
and data analytics systems. In 1989, Howard Dresner of the Gartner Group further
popularized it—defining it as concepts and methods to improve business decisionmaking by using fact-based support systems. The arrival of data warehousing and OLAP
systems enabled the proliferation of business intelligence solutions.

**Amazon Quick Suite for unified intelligence**

Amazon Quick Suite is an enterprise AI platform that transforms how organizations work
with their data by combining generative AI-powered search, deep research capabilities,
and intelligent automation into a unified solution. The platform extends beyond
traditional business intelligence to deliver comprehensive workplace productivity
through features like Quick Research for professional long-form reports, customizable
AI agents with tailored instructions and knowledge bases, Quick Flows for automating
repetitive multi-step workflows, and Spaces for organizing company data, including files,
dashboards, and datasets. By integrating all existing QuickSight analytics capabilities—
including visualizations, dashboards, and the SPICE engine—with advanced generative
AI features, Quick Suite enables teams to quickly surface insights from both internal
company data and external sources, automate complex processes, and make data-driven
decisions faster while maintaining enterprise-grade security and access controls.

484

Chapter 11 Generative Business I g c A c S

**Note** AWS A S A S
accessible as a feature within A S
to QuickS S AWS
IAM A S
require the purchase of Quick S

I’ll first highlight each of Quick Suite’s core features, and then I’ll dive deep into Amazon
QuickSight. In the menu of QuickSuite (see Figure 11-1), we can see the core features listed.

**_Figure 11-1._** _Quick Suite Menu of Core Features_

I’ll start with chat agents.

**Chat Agents in Quick Suite**

Quick Suite empowers users to create custom chat agents with specialized instructions
and knowledge bases tailored to specific business needs, which can be shared across
teams for consistent AI assistance. Let’s say I want to create a training agent that can help
all new employees onboard to the company. Figure 11-2 shows how easy this is.

485

Chapter 11 Generative Business I g c A c S

**_Figure 11-2._** _Creation of a Chat Agent to Assist with Training New Employees_

Within minutes, I can create a specialized agent, customize it with suggested
prompts (see Figure 11-3), upload source documents or connect it to knowledge
bases, empower it to perform actions in connected applications, and then share it
enterprise-wide!

486

Chapter 11 Generative Business I g c A c S

**_Figure 11-3._** _Customizing the Quick Suite Chat Agent_

This capability can be extended to general users who can create specialized agents
they deem valuable.

**Quick Spaces in Quick Suite**

Spaces are collections of documents, knowledge bases, actions, QuickSight dashboards,
and topics that support unified intelligence for an organization. In the previous section
we created specialized chat agents. As part of the configuration, we connect knowledge
bases and actions to our agent. The Spaces feature allows us to define these knowledge
bases and actions. Figure 11-4 shows the integrations to data sources that Spaces natively
supports for knowledge bases, which includes Amazon S3, Atlassian Confluence,
Microsoft OneDrive and SharePoint, and internet web crawlers.

487

Chapter 11 Generative Business I g c A c S

**_Figure 11-4._** _Data Source Integrations for Quick Suite Knowledge Bases_

Actions can be anything from MCP to updating the status of a task in Asana, adding a
user story to Jira, or executing GitHub actions. Figure 11-5 shows a sample of the dozens
of app integrations for performing actions in Quick Suite Spaces.

488

Chapter 11 Generative Business I g c A c S

**_Figure 11-5._** _Sample of App Integrations for Actions in Quick Suite Spaces_

These spaces can be shared within and across teams.

**Quick Flows in Quick Suite**

Quick Flows are defined workflows that automate repetitive and routine tasks using
simple, everyday language prompts. We can apply these automations to various systems
we can integrate with through Quick Suite. Let’s consider an example for Jira. Say we
want to update all the ticket types for our Jira tickets. This field isn’t completed when
it’s submitted, and it would take a lot of time for a human to go through and manually
perform the task. We could just leave it blank, but we want to generate insights from our
tickets to help inform the business of important trends. We can instead create a Quick
Flow (see Figure 11-6) that connects to our Atlassian Jira, reviews and classifies the
tickets, then updates the ticket with the correct type.

489

Chapter 11 Generative Business I g c A c S

**_Figure 11-6._** _Creating Quick Flow to Update the Ticket Type in Jira_

This provides a powerful tool for automating repetitive tasks, freeing up staff to focus
on higher-value work.

**Quick Research in Quick Suite**

Quick Research is an agentic service designed for deep, comprehensive research that
produces professional, exportable long-form reports. It works by first creating a research
plan and confirming it with you before conducting a thorough investigation across your
selected data sources—including web content, internal Spaces, uploaded files, and
QuickSight dashboards. Third-party data from sources like FactSet, IDC, PubMed, the
US Patent and Trademark Office, and S&P Global Market Intelligence data can also be
included. Figure 11-7 shows how to structure the research request and direct it to use
specific sources as part of its investigation.

490

Chapter 11 Generative Business I g c A c S

**_Figure 11-7._** _Initiating a Deep Research Request with Quick Research_

The research agent reviews topics in depth, connects scattered evidence across
multiple sources, and draws well-supported conclusions to deliver structured, detailed
reports with inline citations and a comprehensive list of linked sources at the end. The
report is generated asynchronously since it takes several minutes to complete. The
requester receives an email when the report is ready for viewing. The Quick Research

491

Chapter 11 Generative Business I g c A c S

feature is ideal for complex research tasks requiring extensive analysis, like strategic
planning, market research, or competitive analysis, but it can also be called upon to
support more mundane day-to-day inquiries.

**Quick Automate in Quick Suite**

Quick Automate is a browser-based orchestration platform for agentic cross-system
workflow automation. Rather than scripting linear task sequences, it deploys
coordinated agent teams that can traverse web applications, interpret UI state, make
runtime decisions based on contextual data, invoke APIs, and generate code on demand
to handle edge cases that emerge during execution.

In this example, I’ll demonstrate how we can automate a common data task—
visiting a website and downloading a data file. But we can take it one step further. We
can read the file, loop through the rows, complete a web form, and submit the form, all
via our automation project. We can think of Quick Flows as a managed Robotic Process
Automation (RPA) service that’s enhanced with generative AI. Figure 11-8 shows the
visual designer for our RPA workflow.

492

Chapter 11 Generative Business I g c A c S

**_Figure 11-8._** _Visual Designer of Our Automation Workflow_

Quick Automate defines everything as actions. We can specify agents and process
flows. Then we have specialized actions that are specific to the solution. For instance,
there are web browser actions like “Start browser session,” “Go to webpage,” “Click,” and
“Enter keystroke,” etc. There are Microsoft Excel actions to “Open existing workbook,”
“Read cell,” “Write cell,” etc. Additionally, there are data table actions, orchestration
actions, and exception handling actions. Quick Automate provides an AI-powered
capability for automating complex tasks in an enterprise.

493

Chapter 11 Generative Business I g c A c S

Now that we’ve explored these new(er) features of Quick Suite, let’s look at AWS’s
generative BI platform, Amazon QuickSight.

**Generative BI with Amazon QuickSight**

When data and other workloads moved to the cloud, business intelligence moved with it.
In 2015, AWS released its cloud-native business intelligence service, Amazon QuickSight,
with basic visualization and reporting capabilities. Today, Amazon QuickSight stands out
with a comprehensive suite of ML- and generative AI-infused features for modern data
analytics. Built with enterprise-grade security, QuickSight features row-level security,
single sign-on, and encryption at rest and in transit. Its AI features include smart
anomaly detection, automated forecasting, and narrative insights that automatically
generate data stories. QuickSight Q enables natural language querying for intuitive data
exploration. You can build QuickSight elements into external products with embedded
analytics that scale to thousands of users and offer pay-per-session pricing. A mobilefirst design ensures consistent performance across devices. What used to define BI—
interactive dashboards with drill-down capabilities and dynamic filtering—are now table
stakes and could soon be obsolete. The next generation of BI is GenBI.

**Dynamic Reporting with QuickSight Q**

As I pointed out in Chapter 10, “Data Warehousing with Generative AI and Text-toSQL Reporting with Amazon Redshift,” the traditional BI approach of designing reports
with a static design where each field needs to be specified as included or excluded
does not scale with the business. Companies and product teams end up becoming
“report-writing” companies, building out more and more reports to satisfy leadership or
customer requests. Now with AI, we can simply describe the report we want to see, and it
can dynamically generate it, complete with visuals—charts and graphs—or full narrative
stories packed with insights about the data. Previously, because we didn’t have AI to
assist us, consumers of the insight reports still needed to view the reports and attempt
to understand them to ascertain the insights. Now we can simply feed these artifacts to
AI and task them with developing intelligent insights from the data. This is true insight
generation.

494

Chapter 11 Generative Business I g c A c S

In the next several sections, I will build generative BI reporting in QuickSight on
top of the Redshift data warehouse I presented in _Chapter_ _10: Data Warehousing with_
_Generative AI and Text-to-SQL Reporting with Amazon Redshift_ . I provide all the code for
this working demo in the GitHub repository provided with the book.

**Note** QuickS
into R R
relevant data source for QuickS I
For other data sources, consult the QuickS

Before getting started, note that QuickSight Enterprise Edition is required and the QuickSight
Q feature needs to be enabled in the console. Choosing IAM authentication to connect
QuickSight to Redshift is the most secure. To implement IAM authentication, you’ll need to
create an IAM role with a trust policy that allows the QuickSight services to assume the role.

{

}

You’ll then need to create and attach a policy to that role that grants that role access
to Redshift.

{

495

Chapter 11 Generative Business I g c A c S

"arn:aws:redshift:region:account-id:dbuser:cluster-name/

quicksight_user"

}

QuickSight also needs access to system tables in Redshift: information_schema
tables, pg_stats, pg_class, pg_namespace tables, and the sales schema tables.

-- Grant schema usage
GRANT USAGE ON SCHEMA sales TO "IAM:QuickSightRedshiftRole";

-- Grant select permissions on all existing tables
GRANT SELECT ON ALL TABLES IN SCHEMA sales TO "IAM:QuickSightRedshiftRole";

ALTER DEFAULT PRIVILEGES IN SCHEMA sales

GRANT SELECT ON pg_stats
GRANT SELECT ON pg_class
GRANT SELECT ON pg_namespace TO "IAM:QuickSightRedshiftRole";

With our configurations, roles, and policies set, we can now create the data set.

496

Chapter 11 Generative Business I g c A c S

The data set in QuickSight specifies the data source and the connection details. From
the left-hand menu on the QuickSight console screen, choose **Datasets** and then choose
**NEW DATASET** in the upper right side of the datasets page. For our example, we’ll
choose Redshift as the source and provide all the connection details (see Figure 11-9).

**_Figure 11-9._** _Configure a Redshift Data Source in QuickSight_

Once we connect to the Redshift data warehouse, you’ll be able to view the tables
and views you can choose to populate the dataset. For simplicity, you can create a
view in Redshift that joins the fact table with its associated dimension tables to fully
denormalize the dataset. This may not be practical for every data warehouse design,
but I provide this view as part of my Redshift data warehousing solution. By clicking
Create data source, we advance to the next screen, which asks us to select a table or view.
I’ll choose the vw_sales view (see Figure 11-10).

497

Chapter 11 Generative Business I g c A c S

**_Figure 11-10._** _Schema and Table Selection for the Dataset_

To complete data set creation, we need to choose how to deliver the data. You can
ingest the data into SPICE or query the data directly from the source. SPICE stands for
“Super-fast, Parallel, In-memory Calculation Engine” and is Amazon’s proprietary inmemory engine to reduce latency of report serving. SPICE is more than a hot cache—it’s
doing a lot under the hood to produce low-latency query performance. SPICE replicates
data across nodes, applies compression to reduce the size of the data, and optimizes
queries for faster execution. Use of SPICE is also intended to reduce the load on the
source systems, but it does have limitations.

As of July 2025, SPICE limits on data set size for the Enterprise edition increased
from 25GB to 2TB in size and from 1 billion to 2 billion rows. Data can be refreshed at
a minimum interval of 15 minutes, but there’s a limit of 24 refreshes a day per dataset.
Refreshes can be full or incremental.

If needed, you can modify these datasets to apply column- and row-level security.
With our dataset created, we’ll now create our semantic layer. If we look at what’s going
on conceptually, we can envision a semantic layer on top of the query execution engine,
in this case, SPICE. QuickSight performs entity resolution using the semantic layer that’s
created using topics, synonyms, and named entities. Figure 11-11 shows what this looks
like conceptually.

498

Chapter 11 Generative Business I g c A c S

**_Figure 11-11._** _Q&A Processing and Query Execution in QuickSight_

The question is submitted in natural language. QuickSight analyzes the text and
attempts to map words and phrases to defined entities within a topic (fields, synonyms,
measures, dimensions). Remember that a topic represents a dataset and there could be
multiple topics and datasets a question could resolve against. Keep in mind, however,
QuickSight will not natively combine multiple topics to answer a question. To achieve
this, you can instead combine the datasets in the data warehouse using a view.

**Build a Visual with Q**

Using Q’s generative features, I can also build visuals using natural language. I need to
prepare the data to support my prompts, but assuming I’ve done that, stunning visuals
can be created in seconds using the build a visual with Q feature.

By clicking on the Q icon in the ribbon bar (see Figure 11-12), I can open up a side
panel that accepts a prompt describing the visual I want to build.

499

Chapter 11 Generative Business I g c A c S

**_Figure 11-12._** _Accessing the “Build a Visual” Feature in the QuickSight Toolbar_

In the side panel that opens, I can prompt Q to create a visual for me. I’ll choose a
relatively difficult one to do manually. I’ll choose to create a geographic bubble map of
sales by Designated Marketing Area (DMA). Figure 11-13 shows the result.

**_Figure 11-13._** _Geographic Bubble Map Created with the “Build a Visual” Feature_

500

Chapter 11 Generative Business I g c A c S

Certainly the most impressive and promising generative BI feature in QuickSight is its
data stories feature. What are we really attempting to achieve by building out reports
with charts and graphs to begin with? We’re looking to tell a story. What if generative and
agentic AI can simply inspect our data and write that story for us, without the middle
layer of analysts and data engineers? That reality is becoming more and more true as this
feature evolves.

Today, we can get a lot of mileage out of the story feature with some curated data and
have it draft full stories about our data. We maintain full control over what sections are
included.

That concludes our look at the generative BI features of QuickSight. It’s worth a
mention that QuickSight also supports the traditional report-building experience;
however, that’s thoroughly covered in the documentation and other books.

Topics are used to create a semantic layer in QuickSight, which facilitates natural
language querying. You need to first create a dataset, which we did in the previous
section. Now topics can be created from the dataset. What do topics represent? Well, if
the goal is to have conversations with our data, then topics are the _topic of conversation_ .
It may sound like I’m trolling when I say that, but it really is that simple. Topics are
associated with a dataset, so consider that a topic could contain all the conversations
that are related to that dataset. Within topics, we define entities, which represent
the questions a business wants to know about a topic (and can be answered with a
combination of fields in the dataset). I’ll step through topic creation and provide several
more examples to help illustrate the point.

With the dataset created, we can go back to the QuickSight menu and choose **Topics**,
next to the Q icon. Select **New topic** and you’ll start by naming and describing the topic.
You’ll also see a check box confirming that you want to utilize generative AI features (see
Figure 11-14).

501

Chapter 11 Generative Business I g c A c S

**_Figure 11-14._** _Create New Topic with Generative Q&A Experience_

In the next screen, I select the dataset created using the vw_sales view. Upon
creation, QuickSight performs an analysis on the dataset and uses generative AI to make
a number of decisions about the dataset. This automation eliminates a lot of the inertia
you’d need to overcome in order to create a semantic layer (manually all by yourself).
These decisions are viewable and editable, so you’re always in control. You’ll notice that
in the data tab, QuickSight has already chosen the fields it suspects should be included
for that specific topic. Many of the fields will display AI-generated synonyms based on
the column names of the dataset.

**Caution** R AI
decisions, field synonyms, and reporting results to verify they are correct. T
current state of AI
replacement for sound data engineering knowledge and experience.

From the data tab of the sales topic, I can simply choose **OPEN Q&A** and enter a
question like “sales performance by category,” and QuickSight will dynamically generate
numerous charts and graphs and a table with raw data powering those reporting
elements (see Figure 11-15).

502

Chapter 11 Generative Business I g c A c S

**_Figure 11-15._** _Dynamically Generated Report in QuickSight Q_

I didn’t have to spend time working in a report designer interface specifying that
I wanted a table, a horizontal bar chart, or a multi-series line graph. I didn’t need to
specify the metrics for the X and Y axes. The report also generated a Monthly Business
Review (MBR)-style narrative (highlighted in red) that reported standard business
insights like month-over-month (MoM), year-to-date (YTD), and year-over-year (YoY)
growth. If you’ve avoided MBRs up until now, you’d be well served to familiarize yourself
with these growth metrics and why they’re important to a business. I also didn’t ask for
or define these metrics specifically; QuickSight just generated them. You can view how

503

Chapter 11 Generative Business I g c A c S

the report was made and adjust it if needed. Once it has been reviewed, you can mark
it as verified. There’s another feature I want to highlight. By clicking the lightbulb icon
above an element (see Figure 11-16), you can view additional insights about the data.

**_Figure 11-16._** _Insight and Forecasting Features in QuickSight_

Not only do I see a time series of performance across several quarters, but the
additional insights also identify the highest and lowest quarter, quarter-over-quarter
growth, and a 4-quarter compounded growth rate. But the cherry on top is the forecast
at the bottom. This ML-powered insight predicts total sales out into Q1 of the following
year. These are high-value insights I didn’t ask for. For time series charts, check to see
if the **Forecast** flag is active and choose to enable it. You’ll see an orange forecast band
(see Figure 11-17) extending beyond the actual data. It’s partially obstructed by the
insight pane.

504

Chapter 11 Generative Business I g c A c S

**_Figure 11-17._** _Enabling Forecast Bands and Inline Charts_

Similarly, the insights feature also includes smart anomaly detection. The adaptive
anomaly detection feature creates a dynamic band that shifts with the data. It detects
an anomaly if it falls outside of that band. Figure 11-18 shows these anomaly detection
insights.

505

Chapter 11 Generative Business I g c A c S

**_Figure 11-18._** _ML-Powered Anomaly Detection in QuickSight_

These anomaly reports generated off of daily sales are an important tool to help
alert you to the questions that need to be asked. For example, the higher-than-expected
revenue on May 20, 2024, described in Figure 11-9 should lead a business analyst to
ask, “Why?”.

To add more structure to our reporting capability, we can use named entities.

**Named Entity Feature**

The challenge with generative AI capabilities is that it is probabilistic. The business is
seeking reporting solutions that deliver insights that are credible with high confidence,
verifiable, deterministic, and repeatable. Much of the generative AI features in
QuickSight include a significant number of tools to help define and constrain these
generative capabilities to operate more deterministically.

The **NAMED ENTITY** feature, accessible from the data tab, is one such feature. It
removes the highest level of abstraction—users need to explicitly define the fields to
include. Without named entities with defined fields and rankings, QuickSight will infer

506

Chapter 11 Generative Business I g c A c S

and decide on those decisions from the full list of included fields and the question being
asked. Requiring more time and attention to define a named entity is the tradeoff for
building a more constrained reporting mechanism.

I created a named entity called “sales by territory” that includes eight fields. There
are three measures (sales amount, profit amount, gross profit) and five dimensions
(order date, order year, order quarter, order month, territory name). Figure 11-19 shows
the expanded named entity view.

**_Figure 11-19._** _Named Entity View_

I can choose **OPEN Q&A** from this screen to test this named entity. I’ll time-bound
the sales by territory query by choosing a quarter. Figure 11-20 shows the dynamically
generated report (table not shown).

507

Chapter 11 Generative Business I g c A c S

**_Figure 11-20._** _Sales by Territory for Q2 of 2024_

What’s cool about this report is the bubble chart on the right side showing sales
vs. profit. The bubbles represent territories. The further up in the quadrant a bubble
appears, the more revenue and profit generated by the territory.

**Administering Amazon Quick Suite**

Amazon Quick Suite comes in two editions: Standard and Enterprise. Both include the
full set of features, while the Enterprise addition offers encryption at rest and Microsoft
Active Directory integration. Due to space constraints and the various options for
configuring a Quick Suite enterprise edition deployment, I’ll recommend that you
consult the latest documentation. Instead, I’ll provide an overview of the steps needed to
deploy and administer Quick Suite for the enterprise.

**Create an Amazon Quick Suite Account and Sign Up**

Begin the Quick Suite configuration by establishing the service account with appropriate
federation settings. Navigate to the Amazon QuickSight service in the AWS Management
Console and select the appropriate AWS Region, ensuring that Quick Suite capabilities
are available in your chosen region.

508

Chapter 11 Generative Business I g c A c S

**Configure Authentication Method and Identity Integration**

Select the authentication method for your Quick Suite account, recognizing that identity
methods cannot be changed after account creation. Choose between IAM Identity
Center integration, IAM users and roles, or Active Directory integration based on your
organizational identity architecture and the IdP configuration completed in the previous
section.

Configure the default AWS Region for the QuickSight account and set initial SPICE
capacity allocation. The service starts with 1GB of SPICE capacity that can be expanded
based on organizational requirements. Enable autodiscovery for AWS data sources if
your organization uses multiple AWS services for data storage and processing, allowing
Quick Suite to automatically identify available data sources.

**Establish SAML Federation Connection**

Configure Quick Suite to accept SAML assertions from your identity provider by
establishing the federation connection through the AWS console settings. Navigate to
“Manage QuickSight” and select “Security & permissions” to access the identity and
access management configuration options.

**Configure User Provisioning and Role Assignment**

You can establish automated user provisioning settings to streamline user management
and reduce administrative overhead. After setting up SAML and IAM policies, users do
not require manual invitation and are provisioned automatically using the highest-level
permissions in the policy when they first access Amazon QuickSight.

Quick Suite supports three primary user types: Readers who can view dashboards
and reports, authors who can create and modify analyses and dashboards, and admins
who have full administrative access to the QuickSight account and resources.

Set up group-based access control mechanisms to leverage organizational
hierarchies and role structures from your identity provider. You can implement rolebased access control through SAML attribute mapping and IAM role assignments that
reflect organizational structure and access requirements.

509

Chapter 11 Generative Business I g c A c S

**Implement VPC Integration for Enterprise Security**

For Enterprise Edition deployments requiring secure access to private data sources,
configure VPC integration to enable Quick Suite connectivity to resources within your
organization’s VPC. Quick Suite Enterprise edition is fully integrated with the Amazon VPC
service, enabling secure access to databases and data sources that are not publicly accessible.

**Configure Data Source Connections and Security**

Establish connections to your organization’s data sources, implementing appropriate
security controls and access restrictions. Quick Suite supports connections to popular SaaS
applications, including Salesforce, ServiceNow, GitHub, and Jira, as well as third-party
databases such as Teradata, MySQL, PostgreSQL, and SQL Server with native connectors.

Connecting AWS-based data sources from Amazon Redshift, Amazon Athena, Amazon S3,
Amazon RDS, and Amazon Aurora will yield optimal performance due to their proximity. Rowlevel and column-level security can be applied to restrict what data is accessible by users.

**Implement Hierarchical Permission Structure**

Quick Suite implements a three-tier permission hierarchy that provides granular control over
user access and capabilities. This hierarchical structure consists of account-level permissions
that establish baseline security policies applied organization-wide, role-level permissions
assigned to admin, author, and reader roles, and user-level permissions that provide
individual user overrides with the highest precedence in the system.

You can set up automated user provisioning workflows by configuring LDAP
integration to synchronize user groups and hierarchies. You can then apply role-based
access controls (RBAC) to these groups to manage permissions at scale.

**Configure Data Access Controls and Security Boundaries**

Quick Suite provides sophisticated security capabilities, including row-level security,
column-level security, and dataset-level access controls that enable granular data
protection. Administrators can configure column masking and filtering rules that protect
personally identifiable information, financial data, and other sensitive information
based on user roles and access requirements. Column-level security can be applied
dynamically based on user context and data sensitivity classifications. These types of
controls are typically required for an enterprise-wide data platform.

510

Chapter 11 Generative Business I g c A c S

**User Lifecycle Management and Request Approval**

Since this is an enterprise-wide platform, some thought should be given toward user
lifecycle management. To manage this at scale, you’ll need to implement automated
onboarding workflows that provision new users with appropriate access based on their
organizational role and department assignment. Automated workflows can adjust user
permissions based on organizational changes such as promotions, department transfers,
or project assignments.

In addition, you’ll need to implement approval processes for access changes and
maintain audit trails that document all permission modifications and their justifications.

In this chapter, I provided a short history lesson on business intelligence and its rise to
prominence in the 1980s. I defined what generative business intelligence (GenBI) is and
how dynamic reporting capabilities are transforming business intelligence. I introduced
Amazon Quick Suite and its AI-powered features for supercharging enterprise
productivity, including deep research, workflow automation, and document search. I
then dove deep into Quick Suite’s GenBI platform, Amazon QuickSight, and provided
in-depth guidance on how to implement generative BI reporting. I demonstrated how
to define a semantic layer on top of datasets through topics. I highlighted the many
AI features that performed a lot of the tedious heavy lifting, like suggesting which
fields to exclude, synonyms for data fields, and suggested queries. I discussed key
features including SPICE (Super-fast, Parallel, In-memory Calculation Engine) for data
delivery, natural language querying capabilities, ML-powered forecasting, and anomaly
detection. I emphasized how named entities can be used to create more structured,
deterministic reporting mechanisms while still leveraging the benefits of generative AI,
moving beyond traditional static report design to dynamic insight generation that can
automatically create visualizations and narrative analyses from natural language queries.
In the latter part of the chapter, I provided an overview of the steps needed to create and
administer a Quick Suite deployment enterprise-wide.

In the next and last chapter, we learn how to implement autonomous multi-agent
systems for data engineering with Amazon Bedrock AgentCore, Strands Agents SDK, and
Model Context Protocol (MCP).

511

**CHAPTER 12**

## **Building AI Agents** **with Bedrock AgentCore,** **Strands Agents,** **and Model Context** **Protocol (MCP)**

Throughout the book, I focused on the theory of data engineering, its practical
implementation on AWS, and where to apply generative and agentic AI to add significant
value. I focused on the theory and fundamentals of building AI agents for data
engineering. I saved the mechanics of building agentic systems for the last chapter of the
book for exactly the following reason. The pace of innovation is so severe that just during
the time it took me to write this book—admittedly longer than anticipated—models
were augmented with agentic systems capable of tool use and sophisticated deep
reasoning. Model context protocol (MCP) was open sourced by Anthropic. AWS released
the Strands Agents SDK and its groundbreaking toolkit of agentic primitives, Bedrock
AgentCore. While this volatility will continue, we can see the formation of a long-term
agentic AI technology strategy driven by the industry and wider developer community.

The more I talk to customers and practitioners, a consistent theme emerges.
Experimentation with agentic AI is easy; moving AI agents to production is hard. The
feedback we’ve received from customers made the “ask” clear: make it easier to develop
and deploy agentic AI solutions to production. That’s exactly what AWS did with the
release of Bedrock AgentCore and their open-source Strands Agents SDK.

513
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8_12](https://doi.org/10.1007/979-8-8688-2199-8_12#DOI)

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

In this chapter, I dive deep into the mechanics of implementing agentic AI for data
engineering on AWS. I demonstrate how to enhance existing APIs and data sources
with MCP to enable agentic AI integration. I’ll build agents trained for data engineering
tasks using the Strands Agents SDK. I’ll show you how easy it is to deploy AI agents to
production with Bedrock AgentCore. Let me introduce the major pieces for this agentic
AI stack.

**Strands Agents SDK**

Strands Agents is an open-source SDK that allows you to “build production-ready,
multiagent AI systems in a few lines of code.” Developed by AWS and released as
open source, it’s designed to simplify agent development by leveraging the reasoning
capabilities of large language models rather than requiring developers to define complex
workflows. Strands is model agnostic; it supports Amazon Bedrock, Anthropic, Gemini,
LiteLLM, Llama, Ollama, OpenAI, Writer, and custom providers. It provides native
support for MCP and AgentCore, which makes it optimal for the solution I’ll build.
Within the first 4 months of its launch in July of 2025, it received 1 million downloads
and 3,000 GitHub stars.

**Model Context Protocol (MCP)**

Within months, Anthropic’s Model Context Protocol (MCP) achieved widespread
industry adoption, including Amazon, Google, Microsoft, and OpenAI, as well as
exponential community growth. However, its rollout drew significant scrutiny over
security concerns, with researchers finding that nearly half of MCP servers contain
command injection vulnerabilities, lack proper authentication controls, and are
susceptible to prompt injection attacks that could allow malicious actors to execute
harmful commands or steal sensitive data. Specification changes in June 2025
introduced security improvements, which addressed much of the initial criticism. As late
as August 2025, security researchers discovered a security flaw in Anthropic’s reference
MCP server for PostgreSQL, which allowed read-only restrictions to be bypassed and
arbitrary SQL statements to be executed. Other limitations and gaps will continue to
be identified and addressed as development progresses. However, let’s recognize that
the problem it is solving is a critical one for agentic AI—agents need a standard way to

514

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

integrate with tools, data, and systems. Attempting to directly integrate with each service
or data source would be an M x N complexity problem. MCP is a unified, universal
natural language API that allows agents to leverage tools and data sources without
needing to know the particulars of how those requests are made.

If we look out into any enterprise and consider the current state of its data strategy,
we’re forced to confront some inconvenient truths. Without a clear and compelling
business case, company data and the systems that hold it can languish for years (if not
decades), suffering from irrelevance, obsolescence, politics, a lack of governance, or fear
of change. Maybe there’s a data lake. Maybe there’s a data warehouse serving executive
dashboards. There may be countless SaaS platforms and vendors that handle HRM, ERP,
CRM, SCM, CPQ, payroll, accounting, customer support, marketing automation, expense
management, document management—the list goes on and on. When introducing a new
and innovative technology to “transform the enterprise,” what becomes immediately
apparent is that there won’t be a grand multiyear strategy to right all the sins of the past.
There won’t be investments made to clean up _all_ the data, to implement _comprehensive_
governance, or to pay down technical debt and consolidate tool stacks. Instead, the
approach needs to _meet the enterprise where it is_ and produce quick wins with surgical
precision that demonstrate a high return. Only through that process will additional
investments be made where the return is well understood and risk-adjusted. That’s why
agentic AI via MCP is so powerful. We can meet the enterprise where it is and build out
an agentic integration layer via MCP to enable agentic AI workflows strategically based on
business needs and priorities to yield immediate value for minimal risk.

If we want to take a more optimistic view, consider that many businesses have
already migrated to the cloud and are cloud native. These businesses have positioned
themselves extraordinarily well to rapidly leverage the benefits of agentic AI—putting
non-cloud-adopted laggards at a competitive disadvantage. Not only are all AWS
services controlled with APIs, but many of the data services themselves now have API
access _into_ the data, which eliminates the need to connect via drivers and SQL. For
relational databases, there’s the RDS Data API to query RDS databases. Similarly, an
Amazon Redshift Data API enables querying of Redshift data warehouses. Having an
API into the data makes the implementation of MCP and agentic AI a much lighter lift.
But if that didn’t go far enough, AWS published (and maintains) MCP servers for many
of their services, including their data services. The project is available on GitHub under
[the Apache 2.0 licensing. Visit [https://github.com/awslabs/mcp] to view the full list of](https://github.com/awslabs/mcp)
MCP servers for AWS services.

515

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Beyond AWS services, many SaaS providers have native APIs to perform actions
and query data. The possibilities for agentic AI are limited only by the systems and
data that agents can integrate and use to inform decisions or take action. Imagine the
modern data strategy for enterprises as API-enabled backend services unified with MCP
servers. As agentic AI spreads and becomes a dominant strategy, scaling would require
that multiple business units own, develop, and serve MCP servers and train specialized
agents that can cooperate with other agents shared in the enterprise. Figure 12-1 shows
how two business units might implement and share MCP and their specialized agents.

**_Figure 12-1._** _Agentic AI Scaling Strategy for the Enterprise_

Later in this chapter, I will dive deep into MCP and MCP security. I will step you
through the process of selecting an MCP deployment strategy, and then I will show you
how to deploy MCP servers on Bedrock AgentCore Runtime. Before I get to that, let’s take
a closer look at Bedrock AgentCore and discuss its key features.

516

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Amazon Bedrock AgentCore**

Bedrock AgentCore is a set of primitives, or low-level building blocks, that provides a
fundamental abstraction for the most difficult agentic AI challenges. It provides answers
to critical questions like: Where will I run my agent, which may require several hours
or more of uninterrupted runtime? How will I isolate sessions when serving requests
from multiple users? How will I run my agents securely by authenticating identities
and provisioning access to tools and resources? How will I manage short- and long-term
memory of user interactions involving several turn-by-turn conversations? For any
software code that agents generate, how will I test that it’s valid? How will I observe this
multiagent system over time to ensure it is not degrading in accuracy or efficiency? How
do I enable agents to search for information or take action on the internet on my behalf?
All these questions and more can be answered with Bedrock AgentCore. Since Bedrock
AgentCore was released in July 2025, it has enjoyed growing acceptance. However, for
early adopters of agentic AI development, one thing is clear: the problems AgentCore
is solving are _durable_ . Without it, after developing agentic AI solutions over time, you
would be encouraged to essentially replicate it—perhaps even mirroring the separation
of concerns AWS has chosen. You could adopt AgentCore to solve these problems today,
and even if something gets released that replicates this functionality, it would have to
exceed “marginally better” to justify migrating to it. If you are fully AWS-adopted today,
I have a difficult time seeing a third-party solution achieve this high standard. What is
more likely is that higher-level abstractions, tools, and platforms are developed using
these primitives. However, with abstraction comes loss of control and customization. If
you are committed to building an agentic AI practice, you should be investing at the level
of abstraction AgentCore provides and be reassured by the stated commitments by AWS
to integrate these primitives with third-party open-source frameworks (like A2A) that
achieve widespread industry adoption.

I’ll provide a quick overview of each of the Bedrock AgentCore primitives, then we’ll
dive into implementing our own agents. Table 12-1 provides a list of each primitive and a
description of its scope and value proposition.

517

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Table 12-1._** _Bedrock AgentCore Primitives Description, Scope, and Value_
_Proposition_

**Primitive** **Description and Scope** **Value Proposition**

A
R

A
Identity

A
Memory

A
Gateway

A
Observability

518

Serverless runtime for deploying and
scaling A
(LangGraph, CrewA ­
agnostic, extended runtime (8 hours),
session isolation, multimodal support.

Secure identity and access management
for agents. Integrates with existing
providers (Okta, E AWS/
third-party access (GitH
Slack), just-enough permissions, token
vault.

Managed memory infrastructure for
context-aware agents. Short-term
(conversations) and long-term memory
(cross-agent/session), developer control,
industry-leading accuracy.

Converts AP ­
compatible tools. AP
(OpenAP
third-party services (Salesforce, Slack,
Jira), comprehensive authentication.

Monitoring and debugging platform with
operational dashboards. OpenTelemetry
compatibility, step-by-step visualization,
metadata tagging, trajectory inspection,
troubleshooting filters.

Zero infrastructure management for
lower operational overhead. A
features like session management for
accelerated time-to-market.

Security risk mitigation of agentic
A A
no user migration required. Secure
permission delegation. R
fatigue.

A
complexity. E
agents and cross-agent memory sharing
for better CX. E
learning and training.

A
existing AP P, eliminating
weeks of development time. 1-click
tool integration and no infrastructure
provisioning lower operational overhead.

Unified dashboards with real-time agent
visibility for operational risk management
and enhanced debugging for reduced
downtime.

( _continued_ )

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Table 12-1._** ( _continued_ )

**Primitive** **Description and Scope** **Value Proposition**

A
Code
Interpreter

A
Browser

A
E

A
Policy

Secure code execution in isolated
sandboxes. A
framework integration, complex
workflow, and data analysis support.

Cloud-based browser runtime for web
interactions. Website navigation, form
completion, task automation, sub-­
second latency, session isolation.

Continuous quality monitoring and
real-time alerts that catch issues before
they become problems. Insights to help
continuously improve agents based on
how they perform in the wild.

R
define exactly what agents can and
cannot do.

Secure code execution and enterprise
security compliance. E
accuracy. Complex problem-solving and
analysis capabilities.

H
infrastructure overhead. E
observability (Live View, Session R

R
implementing monitoring for agents in
production.

Simplify policy creation and management
with natural language. Manage A
controlling agent behavior.

I’ll be demonstrating different AgentCore primitives as part of a design and build
of an agentic AI solution for data engineering. Be sure to familiarize yourself with the
service quotas and limits for Bedrock AgentCore services <sup>1</sup> .

Now I’ll return to the topic of MCP and MCP security. This is critical content for
anyone looking to introduce MCP into an enterprise. Skipping this section is not advised,
unless you have a deep understanding of MCP and MCP security.

**MCP Server Fundamentals**

I’ve talked a lot about the value of MCP agentic AI solutions. But what actually is an MCP
server? If you’re planning to adopt MCP in your organization, understanding the finer
technical details should be a top priority. You can read the full protocol specification

[1 Bedrock AgentCore Developer Guide - Service Quotas (https://docs.aws.amazon.com/](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html)
[bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html)

519

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

and the updates, but that’s not why you bought this book! I’ll help you identify the
most critical components and features to accelerate your journey. I’ll discuss language
support and SDKs, transport options (local and remote), the MCP messaging protocol
and structure, MCP methods, and MCP security, including authentication.

**MCP SDKs, Frameworks, and Language Support**

The Model Context Protocol is designed as a language-agnostic standard. It was
launched with SDKs for Python, TypeScript, C#, and Java. At the time of this writing,
MCP SDKs for Go, Kotlin, Swift, Ruby, Rust, and PHP have since been released. Keep
in mind that these SDKs implement the core functionality at a lower level, and the
number of examples and documentation may vary. Today, most MCP server and client
development is being implemented using a framework called FastMCP (inspired by
the FastAPI framework). FastMCP provides a high-level abstraction from the official
MCP SDK implementation. Things like server creation, protocol handling, and resource
management can now be handled with just a few lines of code. At the time of this writing,
FastMCP was available for Python and TypeScript. TypeScript may be more popular due
to its dominance in web-based integrations and API servers. However, between the two,
Python wins out in data engineering and AI/ML domains. Also, AWS-published MCP
servers are written in Python using FastMCP. The implementation uses decorators to
route MCP requests to functions and handles parameters and arguments in a pythonic
way. For these reasons, I choose Python and FastMCP for my MCP implementation and
will feature these in my examples later in this chapter.

**Local and Remote MCP Transport Mechanisms**

MCP supports both STDIO and HTTP transport protocols primarily. Note that HTTPS
(HTTP over TLS/SSL) is _required_ for all MCP servers that are not hosted locally. HTTP is
permitted for local hosts only (i.e., http://localhost:3000/mcp). This was formalized in
the MCP protocol specification as part of the OAuth 2.1 adoption. I’ll use “STDIObased MCP server” and “HTTP-based MCP server” to distinguish the two. For STDIObased MCP servers, the server is spawned as a subprocess of an MCP client. An STDIO-­
based MCP server reads messages from standard input (stdin) and sends messages to
its standard output (stdout). Command line interface (CLI) tools like GitHub CLI or Kiro
CLI utilize this transport option.

520

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

When using Python, STDIO-based MCP servers are spawned using uvx, which is a
tool that allows Python packages to be run temporarily without installation. It removes
the tool automatically after use but uses caching to speed up future use of the same tool.
Spawned local MCP servers automatically terminate when the host process terminates,
so there are no orphaned processes or zombie connections.

STDIO-based MCP Servers:

     - **Runtime:** uvx (Python)

     - **Transport Protocol:** STDIO

     - **Method:** stdin/stdout in JSON-RPC 2.0 format

Applications like desktop clients, including Kiro, Claude Code, Cursor, or Visual Studio
Code, act as an MCP host. Similarly, CLIs like GitHub CLI or Kiro CLI can also act as MCP
hosts. These hosts can create several MCP clients that either spawn a STDIO-based
MCP server or connect to a remote MCP server over HTTP. The relationship between the
MCP host, client, and local and remote servers is depicted in Figure 12-2.

**_Figure 12-2._** _MCP Host, Client, and Server with Local and Remote_
_Transport Options_

Remote MCP servers are standalone network services over HTTP. This will be the
option that enterprises will adopt as part of a larger agentic data strategy. By default, a
remote MCP server endpoint will use “/mcp” as its standard endpoint path. All messages
must be sent as HTTP POST requests using the JSON-RPC 2.0 format.

521

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Remote MCP Servers:

     - **Endpoint:** hostname.com:443/mcp (standard path)

     - **Runtime:** Docker/containerized

     - **Protocol:** HTTPS required (OAuth 2.1)

     - **Method:** POST for JSON-RPC 2.0 requests

     - **Content-Type:** application/json

Now that we’ve reviewed the two primary transport options for MCP, I’ll explain how
MCP messaging works.

**MCP Message Protocol**

MCP messages must comply with the JSON-RPC 2.0 message protocol. JSON-RPC is a
language-neutral protocol that supports many programming languages. All messages
must be UTF-8 encoded and use a standard message in JSON regardless of transport
method. This ensures the same parsing logic for all implementations. This enables
consistent error handling and seamless switching between transport options.

The specification defines the three fundamental types of messages:

     - Requests

     - Responses

     - Notifications

In the next section, I’ll break each one of these down and provide the required fields
with example JSON objects.

**MCP Message Structure**

In this section, I’ll present the structure for MCP requests, responses, and notifications
along with examples of each.

522

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

MCP requests are structured JSON-RPC 2.0 objects that request an action from an MCP
server. Request methods span four general categories: initialize (connection), tools,
resources, and prompts. Here is a list of common MCP methods:

     - **initialize** : Initialize connection

     - **tools/list** : List available tools

     - **tools/call** : Execute a tool

     - **resources/list** : List available resources

     - **resources/read** : Read resource content

     - **prompts/list** : List available prompts

     - **prompts/get** : Get prompt content

MCP servers are _required_ to support the **initialize** and **ping** request methods and
**notifications/initialized** notifications. Support for any other method is optional. The
methods listed above are just a sampling of some of the common methods supported
by MCP servers. For example, most MCP servers support the **tools/list** and **tools/call**
methods, but not all MCP servers support prompt-related methods. MCP servers will
indicate this in their configuration. In terms of the specific structure of the MCP request,
the following fields are required:

     - **jsonrpc** : Always “2.0”

     - **id** : Unique identifier (string or number)

     - **method** : Method name being called

     - **params** : Optional parameters

Here is the example of MCP request message structure:

{

}

523

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

In MCP request messages, method names are case-sensitive and use forward slashes
as separators. Following this convention and utilizing the general categories of tools,
resources, and prompts to offer additional methods will make it easier for users utilizing
the MCP server. For example, one common method for the tools category is **tools/**
**search**, which seeks to identify the right tool in the catalog given a supplied description
of a task.

When the MCP server responds to a request, the response indicates either “success” _or_
“error” and never both. The unique id in the MCP response message is the exact same id
as the corresponding MCP request message that it is responding to.

Here is the example of an MCP response (with a successful result) message structure:

{

}

The result field can include a content array that lists one or more items of various
types. The following example shows a multipart content response message with text and
image content types. Note that the binary data field is base64 encoded (truncated for
readability).

{

524

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

"text": "The chart above shows the performance trends over

the last 30 days."

}

A successful MCP response message may include an error from a tool or resource.
This is different from the reported status of the MCP response message itself. An MCP
request may be handled successfully, but a resource may be unavailable and thus return
an error on execution. The error information for tools and resources will be returned as
part of the content section of the result object.

"tool_execution_error": {

"text": "Error: Failed to retrieve weather data\n\

nDetails:\n- API endpoint returned HTTP 429 (Too Many
Requests)\n- Rate limit exceeded: 100 requests per hour\n"

I’ll now describe the last type of MCP messages, notifications.

525

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

MCP notifications are one-way messages without an expected response. Notifications
are used for a variety of informational use cases, including:

     - Status updates (progress, health, errors)

     - Modifications (changes to tools, resources, prompts)

     - Events (alerts, data updates)

     - Logging (diagnostics and debugging)

Let’s take a look at the structure of MCP notifications and some examples. Note
that **id** is not a required field. This is an important distinction between requests and
notifications. Notifications are one-way communication messages that do not have an
**id** field.

Required fields for an MCP notification:

     - **jsonrpc** : “Always 2.0”

     - **method** : Method name

     - **params** : Optional parameters

Now for some examples. Let’s say tools are added to the tools list dynamically; the
MCP server can send a notification to the client (agent) to inform them of this, so the
**tools/list** method can be called to get an updated list of tools.

// Server adds new tools at runtime
{

}

Similarly, a resource that the MCP server is monitoring could be modified, and it
could send a notification to the client prompting it to retrieve the updated resource with
a **resources/read** request.

// Server notifies when a watched file changes
{

526

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

}

For longer-running asynchronous tasks, MCP servers can send progress
notifications, indicating how much of a task was achieved.

{

}

These are just a few examples of how notifications can be sent by an MCP server.

The primary inhibitor for enterprise-wide adoption of MCP, and by extension, agentic
AI, is and will continue to be security. Today, most MCP implementations use local MCP
servers over STDIO transport, which do not use OAuth but instead use environment
credentials. This is why coding assistants and IDEs with plugins acting as MCP hosts
that build out local MCP servers have gained faster adoption. Eventually, standalone
remote MCP servers over HTTP will be the transport option that enterprises will need
to adopt to fully realize the transformational value of autonomous multiagent systems.

527

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

An attempt was made to close this gap in June 2025 by requiring that MCP servers
implement OAuth 2.1 and other security measures for private and public clients. For a
deep dive into MCP security with OAuth and SigV4, see Chapter 2, “Data Security and
Governance.”

These are the best options available right now, but gaps still remain. There is a
spirited debate as to what is needed to implement an autonomous agent mesh securely.
Some of these topics include

     - **Cross-agent Authorization Delegation** : Allow agents to delegate
tasks to other agents with its permissions.

     - **Headless Consent Mechanisms** : Allow an agent to grant permissions
on behalf of a user.

     - **Trust Framework for** **Multiagent Systems** : Provide agent identity
and trust chains to track the authorization of an agent and its sub-­
agents performing a task.

Stay tuned as MCP maintainers and industry players address these challenges.

**MCP Server Deployment on AWS**

There are several factors to consider when designing and building out an MCP strategy
for data solutions. The first is the MCP server itself. Is there a publicly available MCP
server produced and managed by a reliable source? When I say “server” in this context, I
mean the definition of the server—the code—not a server hosted on infrastructure ready
to service requests. Next, we’ll need to choose an infrastructure option to deploy the
MCP server. Currently there are a few deployment options for MCP servers on AWS: AWS
Lambda, AWS Fargate, and AgentCore Runtime. Table 12-2 describes the differences
between these deployment options and when you might choose one or the other.

528

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Table 12-2._** _MCP Server Deployment on AWS: AWS Lambda, AWS Fargate,_
_AgentCore Runtime_

**Consideration** **AWS Fargate** **AgentCore**
**Gateway w/**
**Lambda**

**AgentCore Runtime**

Usage Pattern P
microservices

E Container-based task
execution

Infrequent usage Sustained interactive
sessions

E Long-running

State management
and session isolation

Stateless between task
execution. Only task-level
isolation.

Stateless between
requests

R No limit Standard: 15
minutes
Durable: 1 year

Scaling A
scaling based on CP
memory metrics.
Cannot scale to zero.

Cost model Pay for vCP
allocated (per second
billing)

Connection handling Persistent connections
within the container
lifecycle

A
on concurrency
limit

Pay per invocation
+ duration

New connection
every invocation

Fully managed/
serverless

Stateful across requests
with MicroVM-level session
isolation.

8 hours

E
by a new MicroVM with 2
vCP
Most agentic workloads will
be I/O bound. Can scale to
zero.

Billed for active processing,
not for I/O wait periods (i.e.,
waiting for LLM)

Connection pooling and
caching

Managed runtime
environment

( _continued_ )

529

Infrastructure
management

Managed container
orchestration

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Table 12-2._** ( _continued_ )

**Consideration** **AWS Fargate** **AgentCore**
**Gateway w/**
**Lambda**

**AgentCore Runtime**

A None - A

                                  - Checkpoint and recovery

                                         - Built-in identity and
observability

Use Cases Microservices
architecture
Batch processing jobs
Data processing pipelines

AP
handling
Database
transactions
(CRUD)
File operations
(R

Complex agent reasoning
with state management
Persistent connection for
real-time data
Document search and
indexing
E
integration

Choosing an MCP server strategy is a multistep process for each data system or
tool. Is there an MCP server definition released as open source by providers? If one
doesn’t exist, is the functionality already implemented via an API defined with Smithy or
OpenAPI specification? How about AWS Lambda? Can the logic be implemented quickly
using a Lambda? If so, you can quickly generate an MCP interface using AgentCore
Gateway.

**AgentCore Gateway for MCP**

AgentCore Gateway provides many capabilities to help developers rapidly “MCPify”
their existing APIs (Smithy and OpenAPI) and Lambda Functions, referred to as “targets.”
AgentCore Gateway provides a secure gateway endpoint and agentic tool registry that
includes ingress and egress authentication in a fully managed service. It offers a search
option that agents can use to semantically search for tools using natural language rather
than executing a list tools action. The list tools action returns the list of all the tools in
the registry, which greatly increases model token consumption. You can choose the

530

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

semantic search option at gateway creation. The service manages the generation and
management of text embeddings to optimize tool search. AgentCore Gateway also acts
as a resource credentials provider for outbound authentication to the resource targets.
Figure 12-3 shows the conceptual diagram of AgentCore Gateway.

**_Figure 12-3._** _MCP Requests Handled by AgentCore Gateway_

Let’s take a look at how we can use AgentCore Gateway to turn Lambda Functions
into MCP servers. I believe this is one of the highest value features of the AgentCore
primitives, so it’s important to spend a little bit of time understanding how it works.

**Lambda Function Target for AgentCore Gateway**

We can configure an AWS Lambda Function to act as an MCP server that responds to
protocol requests from the AgentCore Gateway (the MCP client). This greatly simplifies
MCP server construction and deployment—Lambdas already have a scalable runtime
environment that AWS customers know and understand.

The Lambda target configuration follows a request-response pattern where:

1. AgentCore Gateway invokes the Lambda and sends an MCP

request.

531

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

2. Lambda receives the MCP request in the event param via lambda_

handler() entrypoint.

3. Lambda routes the request to the appropriate MCP request helper

function.

4. Lambda returns an MCP-compliant response.

The Lambda also needs to utilize the MCP error response codes at the MCP
messaging layer:

# Standard error codes
-32700
-32600
-32601
-32602
-32603

At the request handling layer, the Lambda function is expected to return one of the
following three response codes:

     - 200: Success

     - 400: Bad request (client error)

     - 500: Internal server error

We can consider these MCP-related requirements like an API contract. Let’s first take
a look at how to implement our Lambda MCP server for each of the request-response
steps. Once the Lambda is defined, I’ll provide the AgentCore Gateway configuration to
wire this all up!

**Lambda MCP Request Entrypoint**

For a Lambda function to act as a target for AgentCore Gateway, the standard lambda_
handler() entry point will receive and parse the event to extract the MCP request
parameters.

def lambda_handler(event, context):

532

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

...

As an example, let’s say the Lambda function receives this request from AgentCore
Gateway:

{

← Tool name is HERE
← Arguments are HERE

The extracted text indicates the MCP method “tools/call” and specifies the tool get_
company_metrics(). We’ll also add support for MCP methods “initialize” and “list/tools.”

**MCP Request Routing**

With the extracted MCP method, we can use conditional logic to test for and route the
request to the correct handler function.

# Route based on MCP method
if method == "initialize":

elif method == "tools/list":

elif method == "tools/call":

else:

533

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Process the MCP Request**

The minimal request handling for the MCP initialize method is to acknowledge that
you have tools. The descriptions of the tools themselves will be defined in a JSON
configuration object that is provided when the AgentCore Gateway is created.

**​** def handle_initialize(request):

The function returns a properly constructed MCP response in JSON RPC 2.0 format.

**List Tools Request**

For the list tools request handling, we’re simply referencing the JSON object. We can
define this in the Lambda code or retrieve a JSON file from S3.

def handle_list_tools(request):

534

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

In our list of tools, we include a tool that retrieves the KPIs for a company.

TOOLS = [

"description": "List of metrics to retrieve (e.g., ARR,

NRR, CAC)"

]

Let’s see how it changes when we actually want to invoke the tool.

**Call Tools Request**

The “call/tools” request is routed to the handle_call_tool() function. We parse the name
of the tool and any arguments and route it to the specific tool’s execution function to

535

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

fulfill the request. If we don’t recognize the tool, the function will return an error, and the
main function will assign an MCP error code.

def handle_call_tool(request: Dict[str, Any]) -> Dict[str, Any]:

Our hypothetical example includes database access. The tool execution function
creates a DynamoDB client and retrieves the metrics for a company using the company_
id provided in the request.

def execute_get_company_metrics(arguments: Dict[str, Any]) ->
Dict[str, Any]:

536

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

return {

}

OK, we’ve built our MCP Lambda. Let’s put it all together to create a functional MCP
server with AgentCore Gateway.

**AgentCore Gateway Configuration**

Now that we have our Lambda, we need to create an AgentCore Gateway, configuring
it to target our Lambda. Inbound authentication is also needed. We have two options
for inbound authentication—OAuth or IAM. I demonstrate OAuth for inbound
authentication later in this chapter. For IAM authentication with SigV4 signing,
refer to Chapter 2, “Data Security and Governance.” Instead, I want to focus on the
configurations that are specific to designating Lambda as a target for MCP.

There are three steps for configuring our AgentCore Gateway with Lambda as
a target:

1. Retrieve the tools JSON schema.

2. Retrieve the Lambda function ARN.

3. Create the AgentCore Gateway with Lambda ARN and tools

schema inputs.

We can host the tools schema in S3 or provide it inline.

# Read tool schemas from S3
s3 = boto3.client('s3', region_name=REGION)
response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
schemas = json.loads(response['Body'].read().decode('utf-8'))

Using Boto3, we create a bedrock-agent client and then call the create agentcore
gateway method.

LAMBDA_ARN = 'arn:aws:lambda:us-east-1:123456789012:function:my-mcp-server'

537

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

# Create AgentCore Gateway
bedrock_agent = boto3.client('bedrock-agent', region_name=REGION)
gateway_response = bedrock_agent.create_agentcore_gateway(

)

Great, now we can use Lambdas as MCP servers with AgentCore Gateway. Within the
AWS environment, this is a recommended and preferred way to get MCP implemented
quickly.

Now that we’ve seen an introduction of the most critical aspects of the agentic
solution architecture. I will now demonstrate how to build and deploy an agentic AI
solution.

**Build and Deploy Agentic AI Solutions on AWS**

For the rest of the chapter, I’ll be demonstrating the design and implementation of an
agentic AI solution. Like any data project, we want to work backwards from the business
need. We’ll say that at a particular enterprise, its business users want a user-friendly
interface to be able to interrogate the company’s sales data using natural language. We’re
going to keep the solution simple to demonstrate the steps. Building upon our previous
solutions, namely, the Redshift sales data warehouse, I’ll develop and deploy an MCP
server for this data warehouse. I’ll build a sales reporting agent using the Strands Agents
SDK. I’ll then deploy the agent in AgentCore Runtime. I’ll test both my sales reporting
agent and my Redshift MCP server with some basic questions to verify everything was

538

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

built correctly. This pattern can be adapted to support the more than 60+ awslabs-­
published MCP servers available on GitHub <sup>2</sup> .

Before getting started, note the following prerequisites:

     - Python 3.10 or higher

     - AWS account with sufficient permissions

     - AWS credentials configured locally

     - Install MCP and bedrock-agentcore-starter-toolkit

For the last requirement, note that there is a starter toolkit to assist with deploying
Bedrock AgentCore solutions. This may change in the future, but for the time being,
install the CLI on your machine or in a Python env.

For this buildout, I’ll demonstrate how to

     - Build and deploy a remote streamable HTTP MCP server on
AgentCore Runtime

     - Build and deploy an AI agent on AgentCore Runtime

     - Invoke the Redshift MCP tool using the AI Agent

AWS CloudWatch is integrated with AgentCore and will capture the logs. AWS
Secrets Manager will be used to store authentication secrets. Figure 12-4 shows the high-­
level solution architecture.

[2 Amazon Web Services Labs. “AWS MCP Servers.” GitHub, 2025, (https://github.com/awslabs/](https://github.com/awslabs/mcp/tree/main/src)
[mcp/tree/main/src)](https://github.com/awslabs/mcp/tree/main/src)

539

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-4._** _Solution Architecture of Sales Reporting Agent with Redshift MCP_
_Integration_

I’ll build and deploy the MCP server first.

**Build and Deploy an HTTP MCP Server**

Generally speaking, the process for building and deploying an MCP server starts with
development and testing locally before deploying on AWS.

Here’s an overview of the steps I will follow:

1. Adapt the reference Redshift MCP server script into an HTTP MCP

server script.

2. Deploy the Redshift MCP server to localhost and test locally.

3. Deploy Redshift MCP server to AWS

a. Set up Amazon Cognito for authentication.

b. Create an IAM execution role with necessary permissions.

540

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

c. Configure Redshift MCP server for AgentCore Runtime.

d. Deploy Redshift MCP server on AgentCore Runtime.

4. Write remote Redshift MCP client test script.

5. Test remote Redshift MCP server.

Let’s start with the server script.

**Create Redshift HTTP MCP Server Script**

The goal for adapting the server script is to write as little custom code as possible. The
more code that’s customized, the more risk we potentially introduce, not to mention it’s
more code that needs to be maintained. I’m essentially creating a wrapper script that
imports the Redshift MCP server code from AWS Labs augmented for HTTP transport
and maps the MCP handlers to the imported functions and models. To make this work,
you’ll need to copy the awslabs.redshift_mcp_server folder into the project folder. This
will allow the script to find and load the package. The code below shows how I import
the models, functions, and constants from the reference MCP server.

# Import the existing Redshift functionality
from awslabs.redshift_mcp_server.models import (

)
from awslabs.redshift_mcp_server.redshift import (

)

541

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

from awslabs.redshift_mcp_server.consts import (

)

I then use FastMCP to set the host and transport.

mcp = FastMCP(host="0.0.0.0", stateless_http=True)

I use the @mcp.tool() decorator to indicate that the Python functions in my
script will be registered as MCP tools. Since we’re making requests to a Redshift data
warehouse, I define the MCP tools/functions as asynchronous. This is done by using the
async and await keywords so that the function waits for the response before returning.

async def list_clusters() -> list[RedshiftCluster]:
"""List all available Amazon Redshift clusters and serverless

workgroups."""

There are several tools like this one. I can’t show each one, but the full script is
available on the GitHub repo accompanying this book. I’ll instead show the definition of
the execute query tool.

@mcp.tool()
async def execute_redshift_query(
cluster_identifier: str = Field(..., description="The cluster identifier

to execute the query on"),
database_name: str = Field(..., description="The database name to execute

the query against"),
sql: str = Field(..., description="The SQL statement to execute")
) -> QueryResult:
"""Execute a SQL query against a Redshift cluster or serverless

workgroup."""

542

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Finally, the next block of code starts the MCP server with the streamable HTTP
transport option when it is run directly.

if __name__ == "__main__":

We also need a requirements.txt to ensure the dependencies are loaded.

mcp[cli]>=1.11.0
boto3>=1.38.39
botocore>=1.38.39
pydantic>=2.10.6
loguru>=0.7.0
regex>=2024.11.6
bedrock-agentcore
bedrock-agentcore-starter-toolkit

With our script written along with the requirements.txt file, I will first deploy it to a
local HTTP server and test it.

**Deploy and Test Redshift HTTP MCP Server Locally**

To start the server, I simply execute it as a Python application from the terminal.

python redshift_mcp_http_server.py

This will start the HTTP server running locally at http://localhost:8000/mcp. To test
the server locally, we can use a test script. It’s a good practice to test the functionality
of the MCP server before moving to security or remote deployment. Note that the
permissions used to make requests to resources in this local testing scenario are the AWS
IAM credentials configured in the local environment. You’ll notice that we’re utilizing
the Python SDK for MCP to provide the streamable HTTP client.

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():

543

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

terminate_on_close=False) as (

asyncio.run(main())

The client session object handles the connection between the MCP server and
client and the requests for tools and resources. You’ll see from the call_tool() method
that we are requesting to use the execute_redshift_query tool to execute the SQL query
and return the results. Again, the reason why this works is because the requests are
being made with your configured AWS credentials. This is not sufficient for remote
deployment. Let’s see what else we need to do to deploy it remotely.

**Deploy the Redshift MCP Server to AWS**

To take a local HTTP MCP server and deploy it on AWS to run remotely, I need to
perform several steps. The first is to implement security. To support user authentication
and authorization—remember this would be required by an enterprise—I will create a
user pool for authentication in Amazon Cognito. At the time of this writing, Cognito only

544

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

supports OAuth 2.0 grants, including USER_PASSWORD_AUTH flow. If MCP requires
OAuth 2.1, how can this be? As it turns out, Amazon Cognito does not yet support
OAuth 2.1. However, these gaps are mitigated by the way AWS architected its runtime
environment. For example, security features like session isolation neutralize several
threat vectors.

Amazon Cognito doesn’t support Dynamic Client Registration (DCR), but it can be
implemented with a custom/register endpoint that integrates with Cognito. However, for
enterprise use, pre-registration would likely be required anyway.

**Configuring Amazon Cognito for MCP Authentication**

We can use Amazon Cognito to authenticate requests to the Redshift MCP server. We
can use it to define user pools, users, and client applications, which act as the pre-­
registration mechanism for MCP and provide the unique client identifier (client_id).
AWS provides a standard bash script named setup_cognito.sh that helps automate the
creation of the artifacts needed to support authentication of the MCP server.

The script performs the following tasks:

     - Creates a Cognito User Pool and captures the Pool ID

     - Creates an App Client and captures the Client ID

     - Creates a User with a temporary password

     - Sets a permanent password for the User

     - Authenticate User and capture Access Token (JWT)

As a bash script, it allows for all CLI commands to be executed and return values for
assignment to environment variables.

Here’s an excerpt:

# Create User Pool and capture Pool ID directly
export POOL_ID=$(aws cognito-idp create-user-pool \

| jq -r '.UserPool.Id')

545

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

You can find a link to the full setup_cognito.sh script in the GitHub repo that
accompanies this book or from the AWS documentation page <sup>3</sup> . You will use the source
command to execute the commands and set the environment variables.

source setup_cognito.sh

With the User Pool, Client App, User, and Bearer token created, I now have what
I need to authenticate and authorize requests to the resource via the MCP server.
However, I also need outbound auth to authenticate to the Redshift data warehouse. For
that I will create and assign permissions to an IAM execution role that will be attached to
the AgentCore Runtime environment.

**Create IAM Execution Role for Redshift HTTP MCP Server**

Using an IAM execution role attached to the AgentCore Runtime environment means
that the Redshift MCP server will use IAM to authenticate to the Redshift cluster. This is
more secure than authenticating with user credentials. The files and code mentioned
here are available in the GitHub repo for this chapter.

First, I’ll create the trust policy (trust-policy.json) to allow the AgentCore service to
assume the role and act on its behalf.

{

}

3 Amazon Web Services. “Deploy MCP servers in AgentCore Runtime.” _Amazon Bedrock_
_AgentCore Developer Guide_ [, Amazon Web Services, docs.aws.amazon.com/bedrock-agentcore/](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html#runtime-mcp-appendix)
[latest/devguide/runtime-mcp.html#runtime-mcp-appendix](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html#runtime-mcp-appendix)

546

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

We’ll need three IAM policies to make this Redshift MCP server work. The Redshift
permissions are needed to support the MCP operations offered in the tool list. AgentCore
deployment includes container builds with the resulting images getting stored in ECR
before getting pulled and launched into the runtime environment. There’s also a token
exchange where the JWT is exchanged for a “workload access token,” which essentially is
a mapping of external identity to internal IAM permissions (execution role).

Here is my RedshiftMCPPolicy (redshiftmcp-policy.json):

{

}

547

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Here’s the AgentCoreRuntimeECRPolicy (ecr-policy.json):

{

}

And then finally, here’s the AgentCoreRuntimeJWTPolicy (jwt-policy.json):

{

}

We can now create the execution role and attach the policy:

# Create role and policy
aws iam create-role --role-name RedshiftMCPExecutionRole --assume-role-­
policy-document file://trust-policy.json

aws iam put-role-policy --role-name RedshiftMCPExecutionRole --policy-name
RedshiftMCPPolicy --policy-document file://redshiftmcp-policy.json

548

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

aws iam put-role-policy --role-name RedshiftMCPExecutionRole --policy-name
AgentCoreRuntimeECRPolicy --policy-document file://ecr-policy.json

aws iam put-role-policy --role-name RedshiftMCPExecutionRole --policy-name
AgentCoreRuntimeECRPolicy --policy-document file://jwt-policy.json

I split these policies into three to maximize reusability.

**Configuring IAM Authentication for Amazon Redshift**

We’ll be attaching the IAM execution role to the AgentCore Runtime and using it for IAM
authentication with the Redshift server. To enable IAM authentication, an admin needs
to grant access to certain resources.

-- Create the IAM user
CREATE USER "IAMR:RedshiftMCPExecutionRole" PASSWORD DISABLE;

-- Grant schema usage
GRANT USAGE ON SCHEMA sales TO "IAMR:RedshiftMCPExecutionRole";

-- Grant access to tables
GRANT SELECT ON ALL TABLES IN SCHEMA sales TO "IAMR:RedshiftMCPExecut
ionRole";

With the IAM role configured and IAM authentication enabled in the database, we’re
ready to deploy the Redshift HTTP MCP server to AgentCore Runtime.

**Deploying MCP on AgentCore Runtime**

With the MCP server script written and tested locally and the identity and access
management details generated, we can look to configure and deploy the MCP server
using the Bedrock AgentCore CLI. This is a two-step process. I will first call _agentcore_
_configure_, which will prompt me for all the parameter values it needs to define the
configuration of the environment. After the configuration is defined, the command
_agentcore launch_ kicks off a number of tasks, which I’ll describe later.

549

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Configure AgentCore Runtime**

By default, the AgentCore Runtime configuration process is interactive. It will prompt for
any missing required and optional configurations, including OAuth settings.

agentcore configure -e redshift_mcp_http_server.py --protocol MCP

_Configuring Bedrock AgentCore..._
_Entrypoint parsed: file=/[path]/redshift_mcp_http_server.py, bedrock__
_agentcore_name=redshift_mcp_http_server_
_Agent name: redshift_mcp_http_server_

_Execution Role_
_Press Enter to auto-create execution role, or provide execution role ARN/_
_name to use existing_

arn:aws:iam::[ACCOUNT_ID]:role/RedshiftMCPExecutionRole

_Using existing execution role: arn:aws:iam::[ACCOUNT_ID]:role/_
_RedshiftMCPExecutionRole_

_ECR Repository_
_Press Enter to auto-create ECR repository, or provide ECR Repository URI to_
_use existing_

[ENTER]

_No dependency file found (requirements.txt or pyproject.toml)_
_Enter path to requirements file (use Tab for autocomplete), or press Enter_
_to skip:_

/[path]//requirements.txt

_Using requirements file: /[path]//requirements.txt_

_Authorization Configuration_
_By default, Bedrock AgentCore uses IAM authorization._
_Configure OAuth authorizer instead? (yes/no) [yes]:_ yes

_OAuth Configuration_
_Enter OAuth discovery URL:_

550

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

­https://cognito-idp.us-east-1.amazonaws.com/us-east-1_nXXXXXX/.well-known/
openid-configuration

_Enter allowed OAuth client IDs (comma-separated):_ 1p1kf98XXXXXXXXXcuj457

That completes the parameter capture for the configuration. The service announces
that it has created a Docker file and instructs us to execute the launch command to
deploy the server.

**Launch AgentCore Runtime**

Executing the AgentCore launch command triggers a series of tasks that builds the
image, stores it in ECR, and deploys the image on the AgentCore runtime. It sets up and
configures the runtime.

A high-level solution architecture of the AgentCore CLI is shown in Figure 12-5.

**_Figure 12-5._** _MCP Server Build and Deploy with AgentCore CLI_

551

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Here’s a list of tasks that AgentCore Runtime completes as part of the launch process:

**Container Build** : Uses AWS CodeBuild to build ARM64 containers

**Image Push** : Pushes built container to ECR repository

**Runtime Deployment** : Deploys to Bedrock AgentCore runtime

**Environment Setup** : Configures environment variables

**Role Assignment** : Attaches execution role with required

permissions

**Network Configuration** : Sets up public network mode

**Protocol Configuration** : Configures MCP server protocol

**Observability Setup** : Enables monitoring and logging

**Authorization Setup** : Configures JWT authorizer with Cognito (if

configured)

**Session Initialization** : Creates agent session for invocations

I now execute the agentcore launch command. The output, with some of the
deployment milestones highlighted, is shown in Figure 12-6.

552

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-6._** _AgentCore CLI Launch Execution and Output_

With our MCP server deployed, we now need to test it.

553

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Testing the Remote HTTP MCP Server**

We can create a test script to test the MCP server for us. I’ll need the access token, which
I can request from Cognito using the USER_PASSWORD_AUTH flow and providing the
Client ID and user credentials. If this were the agent, we would use the AWS Secrets
Manager. However, for demonstration purposes, I hard code the dummy username and
password directly to make it easier to follow. For the buildout of the AI agent in the next
section, I show how to use AWS Secrets Manager to store and retrieve secrets for MCP
token requests.

# Get token
client = boto3.client('cognito-idp', region_name='us-east-1')
response = client.initiate_auth(

)
token = response['AuthenticationResult']['AccessToken']

The request URL is constructed from the runtime endpoint URL (which includes the
encoded agent ARN), the headers, and the MCP request.

I break the URL down into its logical parts to make this easier to understand. We need to
prepare the encoded agent ARN, as this is embedded into the URL.

agent_arn = [AGENT_ARN]
encoded_arn = quote(agent_arn, safe='') #from urllib.parse import quote

Now we can add the encoded agent ARN into the URL path.

url_domain = "bedrock-agentcore.us-east-1.amazonaws.com"
url_path = "/runtimes/{encoded_arn}/invocations"
url_querystring = "?qualifier=DEFAULT"

554

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Putting it all together, we have the full URL that we’ll use to send the HTTP POST
request.

url = f"https://{url_domain}{url_path}{url_querystring}"

There are three headers needed. For the Accept header, note that you’ll need to include
the “text/event-stream” option (bolded for emphasis) because the MCP server uses
streamable HTTP transport.

headers = {

**text/event-stream** "
}

**Construct the MCP Request**

For the MCP request, we construct it following the JSON-RPC 2.0 format that I presented
earlier in the chapter. You can request something simple like list_tools to test that the
MCP is working. However, I’ll provide an example SQL query.

# Test execute_redshift_query with sample query
query_request = {

555

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

JOIN sales.dim_time dt ON fs.order_date_key = dt.time_key
JOIN sales.dim_region dr ON fs.region_key = dr.region_key

}

I use httpx to help make the HTTP POST request to the MCP server.

async with httpx.AsyncClient(timeout=30.0) as client:

It works! Figure 12-7 shows us that the query executed successfully, with a pretty
print of the results.

556

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-7._** _Pretty Print of the Redshift MCP execute_redshift_query Tool_
_Call Results_

With the Redshift MCP server built, deployed, and tested, we now need to build our
sales reporting AI agent that will utilize this MCP resource.

**Build and Deploy Sales Reporting AI Agent**

Let’s pretend I’m a data engineer at a product company. Senior leaders continuously
ask me all kinds of random questions about our product sales. We have a well-designed
data warehouse in Amazon Redshift, but these leaders are not technical nor would they
be interested in writing and executing the SQL queries needed to get the answers they
need to make critical decisions for the business. Instead of spending all my time writing
these ad hoc reports, I instead build out an agent to do it for me, allowing me to focus on
more strategic and impactful initiatives. Similar to the MCP server build, I’ll develop and
test my agent locally, including the MCP integration, and then deploy it to AgentCore
Runtime. A common pattern is to utilize an orchestrator agent to centralize all requests
and route them to the specialized agent. There are examples provided in the GitHub
repo accompanying this book. Due to space constraints, it is excluded for this build.

Here’s an overview of the steps I will follow:

1. Develop the sales reporting agent script, incorporating Redshift

MCP tool use and memory hooks.

2. Test the sales reporting agent locally.

3. Set up Amazon Cognito for agent authentication.

557

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

4. Create an IAM execution role with necessary permissions.

5. Configure the sales agent for AgentCore Runtime.

6. Deploy the sales agent to AgentCore Runtime.

7. Write a client script to invoke the sales agent.

8. Test the client script with sample questions.

9. Set up observability and monitoring

With the power of Strands Agents SDK and Bedrock AgentCore, I’m able to take you
from concept to POC to a scalable production solution in just a few pages. Let’s start with
the agent script.

**Create Sales Agent Script**

We need an agent to field my sales reporting requests, convert my natural language
question into a SQL query, and utilize the Redshift MCP server to execute that query,
analyze the results, and return the data and insights to the client. For the agent build-out,
I’ll use the Strands Agents SDK. With Strands, I’m able to take advantage of abstracted
methods and decorators that simplify my code and define the entry point. For my sales
reporting agent, I’m exposing only one tool: generate_insights(). When invoked, this
agent tool takes as an input a natural language question about the company’s sales.
The agent that I’m building with Strands is a specialized piece of software. The control
operates as an agentic loop. The agent takes the prompt as input and loops through
model and tool invocations until it has determined to have processed the request per its
instructions. Figure 12-8 shows the agentic loop.

558

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-8._** _Agentic Loop with Model Reasoning and Tool Use_

Creating an agent with the Strands Agents SDK allows up to four inputs:

     - **Model** : The large language model (LLM) that will power the agent’s
reasoning capabilities.

     - **Hooks** : Callback functions that allow you to intercept and customize
the agent’s behavior at key points in its execution flow.

     - **Tools** : The collection of functions available to the agent, enabling it to
interact with external systems, retrieve data, perform calculations, or
execute tasks.

     - **System Prompt** : The foundational instructions that define the
agent’s role, objectives, and behavioral guidelines, serving as the core
directive that shapes how the agent performs tasks and generates
responses.

Let’s take a look at the agent script code.

First, I’ll start with importing modules, classes, and functions specific to Strands:

from strands import Agent, tool
from strands.models import BedrockModel

559

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Import statements for Bedrock AgentCore include the BedrockAgentCoreApp class.
This allows us to apply the app.entrypoint decorator and invoke the agent. The memory
client enables the agent to save and retrieve context from the AgentCore memory
service.

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from bedrock_agentcore.memory import MemoryClient
from bedrock_agentcore.memory.constants import StrategyType

Since we’re utilizing an MCP server, we’ll need some MCP import statements.

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

There’s several more import statements needed. The full script is available on the
GitHub repo that accompanies this book.

We’ll be utilizing all four of the input parameters—model, hooks, tools, prompt—so
before I define my Strands Agent, I’ll define the tools and memory capabilities that I’ll
need to pass into it.

**Tool and Function Definition**

I’ll start with the tool’s definition. With the decorator capability, I simply add the @tool
decorator above the functions I want to designate as a referenceable tool for my agent.

@tool
async def generate_insights(query_description: str) -> str:
"""Generate sales insights by discovering schema and executing

appropriate queries"""

The function is asynchronous because we rely on external resources (the Redshift
MCP server). We’ll await completion, yielding control to allow the event loop to handle
other tasks while the external resources process asynchronously. I provide another
­function called call_mcp_tool() that can invoke any MCP tool. For that function, I don’t
use the @tool decorator because I don’t want to expose it through the agent and allow

560

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

clients to invoke it directly. Instead, the agent uses it as an internal function to help meet
its objective:

async def call_mcp_tool(tool_name: str, arguments: dict = None, session =
None) -> str:
"""Call any MCP tool dynamically with given arguments and optional

session"""

Let’s move on to memory.

**Create Memory Hooks for Saving and Injecting User Context**

Adding hooks for memory helps us implement short- and long-term memory
transparent to the agent logic. The hooks are triggered from certain events—for example,
messages received or sent. Memory hooks will capture and store all the user prompts
and agent responses automatically. In long-term memory, it’ll vectorize the stored
context and provide semantic search capabilities. We can define hooks to automatically
inject the saved context from memory into the prompt so the LLM is provided all of the
requests that the user made previously. This allows the LLM to customize and adapt its
response to each request, knowing what topics the user discussed. This is very powerful
stuff for building robust, agentic AI solutions without a lot of code.

To implement this, I import the following classes and create a separate file that
includes a memory hooks class for my sales agent:

from strands.hooks import HookProvider, \

from bedrock_agentcore.memory import MemoryClient

class SalesAgentMemoryHooks(HookProvider):

I’ll start at the end because I think it’ll make more sense. After the hooks are defined
(shown next), we need to register them. By starting at the last step, we get to see how the
callbacks are added and which events they are triggered by:

561

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

def register_hooks(self, registry: HookRegistry) -> None:

registry.add_callback(MessageAddedEvent, self.retrieve_sales_

context)
registry.add_callback(AfterInvocationEvent, self.save_sales_

interaction)

The MessageAddedEvent is a hook event from the Strands framework that triggers
when a new message is added to the agent’s conversation.

It fires before the message is processed by the Bedrock model, allowing the memory
hook to:

1. Intercept the incoming user message

2. Retrieve relevant context from memory based on the

message content

3. Modify the message by prepending the retrieved context

4. Let the enhanced message continue to the model for processing

This enables the agent to have contextual awareness of previous interactions
when generating responses. Here’s a code snippet for how this is implemented in my
hook class.

def retrieve_sales_context(self, event: MessageAddedEvent):

messages[-1]["content"][0]["text"] = f"Sales Context:\n{context_text}\

n\n{original_text}"

The AfterInvocationEvent is a hook event that triggers after the agent completes
processing and generates a response.

It allows the memory hook to:

1. Capture the completed conversation turn (user query + agent

response)

562

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

2. Save this interaction to memory for future retrieval

3. Store it with the user’s ID and session ID for personalized context

This creates a feedback loop where each interaction gets stored and can be retrieved
in future conversations to provide relevant context. There’s a snippet of how this is
implemented.

def save_sales_interaction(self, event: AfterInvocationEvent):

With memory capabilities defined, we can build the agent.

563

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Sales Agent Definition**

Like I mentioned previously, I’ll be defining parameters for my agent: a model, tools,
memory, and a system prompt. The model identifier and region can be dynamic or
parameterized; however, for this demo, they’ll be hardcoded.

MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"
REGION = "us-east-1"

def create_sales_agent(headers=None):

user_id,

The system prompt includes the instructions that the AI will follow.

564

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

System_prompt = _"""You are a sales reporting agent with access to Redshift_
_data via MCP tools._
_You have access to the generate_insights tool for automated insights_
_generation._
_The generate_insights tool automatically:_
_1. Discovers available MCP tools_
_2. Explores database structure_
_3. Generates appropriate SQL queries_
_4. Executes queries on sales-demo-cluster/salesdb_
_5. Presents formatted results_
_Use generate_insights("your query description") to get sales insights._
_When presenting business reports, use clear ASCII tables with proper_
_spacing:_
_Example format:_
_```_
_Rank_
_----_
_1_
_2   SecureIT ERP Draw_
_3_
_```_
_Always provide clear, formatted results with business insights."""_

Now we need to write this up to provide the “invoke” capability of the agent. To do
this, we create an instance of the BedrockAgentCoreApp class.

# Initialize the AgentCore Runtime App
app = BedrockAgentCoreApp()

Then we use the @app.entrypoint decorator to define the invoke function to handle
invocation requests.

@app.entrypoint
def invoke(payload):

565

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Authenticate to the Redshift MCP Server**

The agent will first request the list of tools offered after authenticating to the Redshift
MCP server. I store secrets like the MCP agent ARN and the username and password in
AWS Secrets Manager.

# Create new session
ssm_client = boto3.client('ssm', region_name=REGION)
agent_arn = ssm_client.get_parameter(Name='/mcp/redshift/agent_arn')

['Parameter']['Value']
credentials_secret = "/mcp/redshift/credentials"

secrets_client = boto3.client('secretsmanager', region_name=REGION)
response = secrets_client.get_secret_value(SecretId=credentials_secret)
creds = json.loads(response['SecretString'])

I use these secrets to authenticate to Cognito and receive the Bearer token I need to
make the resource request.

cognito_client = boto3.client('cognito-idp', region_name=REGION)

566

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**Construct the Request to the Redshift MCP Server**

As I showed in the testing script for MCP, we can construct the request from these parts.

encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')
mcp_url = f"https://bedrock-agentcore.{REGION}.amazonaws.com/

runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"

Now, we have the agent script written, it’s time to test this locally.

**Test the Sales Agent Script Locally**

I can run the sales_reporting_agent.py script as a simple Python application. I’ve gone
through several iterations to debug and enhance the script. There is a default query
that’s provided, which is used for testing. The question being asked of the sales reporting
agent is, “What are the top five products by sales in Q4 2023?”

I use my Python environment to execute my script locally:

python -c "from sales_reporting_agent import invoke; result =
invoke({'prompt': 'What were the top 5 products by sales in Q4 2023?'});
print('Result:', result)"

The results show me that both the model and MCP server integration work. Not
only do I get the raw dataset related to the query, but I also get additional insights about
the dataset. Insights like “Average order values ranged from $68K to $106K, indicating
strong enterprise sales performance,” are just one example where the model is able to
anticipate certain business questions based on its training. Figure 12-9 shows the full
response to my question.

567

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-9._** _Local Test Results from My Sales Reporting Agent_

This is a lot of progress for just a few short pages, but we’re not done yet. We need to
deploy this agent to production, and we’ll do that using AgentCore.

**Deploy Sales Reporting Agent to AgentCore Runtime**

Deployment using AgentCore is a two-step process, as shown before. First, I’ll call
_agentcore configure_ to set the configurations for launch. Then I’ll _agentcore launch_ to
deploy the solution to AgentCore Runtime with those configurations.

This time I won’t create an execution role; I’ll just have AgentCore create one as part
of the configuration process.

agentcore configure

I’m provided updates and asked a series of questions:

Agent name: sales_reporting_agent
Press Enter to auto-create execution role, or provide execution role ARN/
name to use
existing Execution role ARN/name (or press Enter to auto-create): [Enter]
Will auto-create execution role

568

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

Press Enter to auto-create ECR repository, or provide ECR Repository URI to
use existing ECR Repository URI (or press Enter to auto-create): [Enter]
Press Enter to use this file, or type a different path (use Tab for
autocomplete):
Detected dependency file: requirements.txt
Path or Press Enter to use detected dependency file: [Enter]
By default, Bedrock AgentCore uses IAM authorization.
Configure OAuth authorizer instead? (yes/no) [no]: [Enter]

For my agent deployment, I’m choosing IAM authorization. This is similar to any
application authorization method I may deploy as an AWS solution. I’m able to assign
IAM permissions to client applications for this specific agent. Figure 12-10 shows a
summary of the AgentCore configuration process.

**_Figure 12-10._** _AgentCore Configuration Results for Sales Reporting Agent_
_Deployment_

Now, to complete the deployment, we just call the launch command.

agentcore launch

The launch process reports its steps (some intermediate steps not shown).

_Launching Bedrock AgentCore (codebuild mode_

_• Build ARM64 containers in the cloud with CodeBuild_

_• No local Docker required (DEFAULT behavior)_

569

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

_• Production-ready deployment_
_Starting CodeBuild ARM64 deployment for agent 'sales_reporting_agent' to_
_account [ACCOUNT_ID] (us-east-1)_
_Setting up AWS resources (ECR repository, execution roles)..._
_Getting or creating ECR repository for agent: sales_reporting_agent_
_Getting or creating execution role for agent: sales_reporting_agent_
_Starting execution role creation process for agent: sales_reporting_agent_
_Preparing CodeBuild project and uploading source..._
_Getting or creating CodeBuild execution role for agent: sales__
_reporting_agent_
_Waiting for IAM role propagation..._
_CodeBuild execution role creation complete:_
_Uploaded source to S3: sales_reporting_agent/source.zip_
_Created CodeBuild project: bedrock-agentcore-sales_reporting_agent-builder_
_Starting CodeBuild build (this may take several minutes)..._
_CodeBuild completed successfully_
_Deploying to Bedrock AgentCore..._
_Observability is enabled, configuring Transaction Search..._
_CloudWatch Logs resource policy already configured_
_Agent endpoint: arn:aws:bedrock-agentcore:us-east-1:[ACCOUNT_ID]:runtime/_
_sales_reporting_agent-XXXXXXX/runtime-endpoint/DEFAULT_
_Deployment completed successfully_ _­_
_east-­_

The process creates a number of artifacts needed to support the build process,
including the Dockerfile, which is not required by the user. AgentCore will create the
Dockerfile and use it to build the container image. The primary deliverables of the
overall process are the agent endpoint (how to invoke the agent) and the agent ARN (the
resource for authorizing access).

Figure 12-11 shows the summary of the AgentCore launch process.

570

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-11._** _Summary of the AgentCore Runtime Launch Process_

Now that I have the agent deployed, let’s test it.

**Testing the Sales Reporting Agent on AgentCore Runtime**

There are several options available to invoke the hosted agent for testing. I provide a few
options.

A client script can use a Boto3 AgentCore client to invoke the agent. The invoke_
agent_runtime() method takes the ARN of the agent and the payload.

import boto3
import json

571

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

client = boto3.client('bedrock-agentcore', region_name='us-east-1')
try:

agentRuntimeArn='arn:aws:bedrock-agentcore:us-east-1:[ACCOUNT_ID]:runtime/
sales_reporting_agent-XXXXXXX',

except Exception as e:

Similarly, we can invoke the agent from the command line.

aws bedrock-agentcore invoke-agent-runtime --agent-runtime-arn
"arn:aws:bedrock-agentcore:us-east-1:[ACCOUNT_ID]:runtime/sales_reporting_
agent-­XXXXXXX" --payload '{"prompt": "What were the top 5 products by sales
in Q4 2023?"}' --region us-east-1 /tmp/agent_response.json

My hosted sales reporting agent is ready for use! But we’re not done yet. We need to
implement observability, evaluations, and policies for our agent.

**Observability and Monitoring for AI Agents**

AWS provides features for observing and monitoring our agents in production. Bedrock
AgentCore Observability Dashboard is a native feature accessible from Amazon
CloudWatch. This dashboard provides an extensive set of metrics for agents, memory,
gateways, and identity. It supports agents deployed using AgentCore as well as externally
deployed agents. Figure 12-12 shows the real-time performance in a detailed view that
includes error rates, throttling, and sessions, as well as vCPU and memory consumption.

572

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-12._** _AgentCore Observability Dashboard—Detail View_

To enable the reporting for this dashboard, we need to add delivery of the logs to
CloudWatch. From the Bedrock AgentCore console, choose the primitive (Runtime,
Memory, Gateway) from the **Build** menu. Then choose the instance of the primitive.
For example, I would choose my sales_reporting_agent that appears under **Runtime** .
Scroll down to the **Log deliveries and tracing** section and choose **Add** and select
APPLICATOIN_LOGS. Figure 12-13 shows this.

573

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-13._** _Add AgentCore Logs Delivery to CloudWatch Logs_

We can also use Bedrock Evaluations to monitor our agent over time. At the time
of publication, Bedrock Evaluations offered 13 prebuilt evaluators spanning response
quality, task completion, use of tools, and safety. Figure 12-14 shows a sample of prebuilt
evaluators.

574

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

**_Figure 12-14._** _Bedrock Evaluations Prebuilt Evaluators_

Bedrock Evaluations also supports custom evaluators.
Let’s review what we covered.

Throughout this book, I describe where and how AI agents can be used across the data
engineering life cycle. In this final chapter, I present a comprehensive exploration of
building and deploying agentic AI solutions for data engineering using Amazon Bedrock
AgentCore, Strands Agents SDK, and the Model Context Protocol (MCP). While agentic
AI will transform data strategy, the pace will be slower than in software engineering
due to data’s unique requirements for accuracy, governance, and specialized domain
knowledge. Using the concept of “durable needs”—consumer needs that persist over
time—as a framework for evaluating technology investments, I argue that despite rapid
evolution and remaining challenges, the fundamental problems these technologies
address will endure, justifying strategic investment today.

575

Chapter 12 BUILDING A A E T TH E R A E T RE TRA A E T A E TE T
PR T P

I start with a discussion on how data—as a critical input to AI—possesses unique
requirements for accuracy, governance, and specialized domain knowledge, making the
practice of data engineering more valuable than ever. I explain how MCP solves the MxN
integration challenge by providing a unified natural language interface that allows agents
to access tools and resources without knowing specific implementation knowledge. I
dive deep into the MCP protocol itself, describing how MCP servers use local (STDIO) or
remote (HTTP) transport mechanisms, the different message and request types and the
JSON-RPC 2.0 format.

I introduced Bedrock AgentCore, which provides several primitives, including
serverless runtime environments, identity management, memory management, gateway
services, observability tools, code interpretation capabilities, and browser automation.
I also showcased Strands Agents SDK, which is an open-source framework released by
AWS that simplifies and accelerates the development of agentic AI solutions.

Through a detailed practical example, the second half of the chapter demonstrates
step-by-step how to build a sales reporting agent that converts natural language
sales questions into SQL queries to run on a Redshift data warehouse accessed via
an MCP server. The implementation demonstrates advanced AgentCore features like
implementing memory hooks for context awareness across sessions and automating
deployment from a local script to a managed, scalable solution on AWS. Once deployed,
I showed how to observe and monitor the agent using AWS features like the Bedrock
AgentCore Observability Dashboard and Bedrock Evaluations.

Congratulations on making it all the way through my book! Now you possess the
knowledge to transform your data engineering practice with generative and agentic
AI on AWS!

576

### **Index**

**A**

Accelerating Time to Value (TTV), 14
Access token request, 86, 87
Account governance

data publisher accounts, 169
DataZone domain account, 169
multi-account strategy, 168
subscriber accounts, 170
Advanced Query Accelerator (AQUA), 482
Advanced serialization formats

advantages, 105–106
Apache Avro, 105
Apache Parquet, 105–107
features, 105–106
ORC, 104
Snappy, 107
trade-offs, 105–106
Zstandard (ZSTD), 107
AgentCore Gateway, 530, 531, 537, 538
Agentic AI, xxxi, 218, 219

agentic loop, 19
agents, 24, 77
architecture, 19, 20
conceptual diagram, 18
data engineering, 20
data governance, 46
data strategy, 575
data transformation and orchestrate

logic, 18
defined, 18

development with Kiro, 26
emergence of, 483
for enterprise, 1
and generative ( _see_ Generative AI)
LLM, 19
log aggregation and analysis, 287
modern data strategy, 26–27
RPA, 19
scaling strategy, 516
_vs._ traditional, 3, 4
Agentic AI solutions

demonstration, 539
prerequisites, 539
Redshift HTTP MCP server script ( _see_

Redshift HTTP MCP server script)
sales reporting agent, 539, 540
Agents, 18, 20
AI, _see_ Artificial intelligence (AI)
AI-assisted ETL development

data engineering with Kiro, 231–232
generative and agentic AI, 231
Kiro and Kiro CLI, 231
Kiro-generated Jupyter notebook, 236
software and data engineering, 231
AI-augmented enterprise, 15
AI Development Lifecycle (AI-DLC), 5
AI-generated content, 502
Amazon AppFlow, 356
Amazon Augmented AI (Amazon

A2I), 311

577
© Justin J. Leto 2026
J. J. Leto, _Data Engineering with Generative and Agentic AI on AWS_,
[https://doi.org/10.1007/979-8-8688-2199-8](https://doi.org/10.1007/979-8-8688-2199-8#DOI)

INDEX

Amazon Aurora PostgreSQL, 401

embeddings index, 405, 406
insert embeddings, 406–408
metadata table, 403
semantic search

coding secrets, 413
cursor and connections, 415
database connection, 414
distance metric operators, 412
psycopg2, 413
records, 414
SQL query, 414
vector normalization, 413
text embeddings table, 403–405
vector extension installation, 402
vector tables creation, 402, 403
Amazon Bedrock, 16, 52, 70–73, 97

batch inference

service limits, 252
steps, 253–255
knowledge bases, 353

Amazon S3 Vectors, 398, 399
chunking strategy, 354, 355
data sources, 354
embedding model, 354
Amazon DataZone, 64, 111, 160
Amazon DynamoDB, 54
Amazon EC2, 102
Amazon EMR Jobs, 284–286
Amazon EventBridge, 356
Amazon Kinesis, 424, 440

KCL, 424, 425
KPL, 424, 425
service, 424
Amazon Managed Workflows for

Apache Airflow (Amazon MWAA),
_see_ Amazon MWAA
Amazon MWAA

578

Apache Airflow, 265, 266
architecture, 266–268
DAG, 266
environment, 268–270
extensibility, 266
orchestrating workflows

DAG processing logs, 272
DAG Tasks, 273
DAG validation, 271–273
Landing Zone phase, 270
log stream, DAG, 273
Published Zone phase, 270
Amazon Nova Multimodal Embeddings,

362, 363
_vs_ . audio embeddings, 379
cross-modal search, 363
_vs_ . image embeddings, 373, 374
MRL, 363
RAG vector database, 363
semantic space, 363
synchronous/asynchronous API, 363
_vs_ . text embeddings, 371
_vs_ . video embeddings, 376
Amazon OpenSearch, 399, 408

client library, 409
import process, 401
imports vectors, 400
integration, 399, 400
neural Search, 417–419
semantic search

execution, 416, 417
search query, 415, 416
vector embeddings index, 409, 410
vector search collection, 408
Amazon Q for Business, 352, 353
Amazon QuickSight

analytics capabilities, 484
anomaly detection, 505, 506

automation, 502
data sources, 495
data stories, 501
datasets

analyzing, 499
console screen, 497
creation, 498
modification, 498
Q&A processing and query

execution, 498, 499
Redshift data source, 497
schema and table selection, 497, 498
SPICE limits, 498
forecast band and inline charts,

504, 505
GenBI, 494
insight and forecasting, 504
NAMED ENTITY feature, 506–508
prerequisites, 495, 496
reports, 502, 503, 506
topics, 501, 502
Amazon Quick Suite, 484

approval processes, 511
authentication method, 509
chat agents, 485–487
connections and security, 510
create account, 508
data access controls, 510
editions, 508
hierarchical permission structure, 510
identity integration, 509
menu, 485
Quick Automate, 492, 493
Quick Flows, 484, 489, 490
Quick Research, 490, 491
Quick Spaces, 487–489
role assignment, 509
SAML, 509

INDEX

security boundaries, 510
teams, 484
unified intelligence, 484
user lifecycle management, 511
user provisioning, 509
VPC integration, 510
Amazon Redshift, 54, 447

architecture, 448, 449, 482
auto-copy feature, 454
CDC, 453
constraints, 450
deployment, 450
distribution styles, 452, 453, 482
Query Editor v2, 457

Amazon Q generative SQL, 458–460
features, 457
generated query, 459
permissions, 457
query optimization, 457
sample reports, 458
SQL query generation

capabilities, 457
RAG, 473, 474
sort keys, 451, 452, 482
table design considerations, 450
workload management (WLM), 450
Amazon Resource Name (ARN), 301
Amazon S3, 51, 91, 102, 114

server logging, 91, 92
Amazon SageMaker Catalog, 160, 161
Amazon SageMaker Unified Studio

AI, 231
Glue interactive sessions, 228–230
JupyterLab application, 228
ML, 231
notebook-based development, 228–230
SageMaker Catalog, 231
SageMaker Domain setup, 227

579

INDEX

Amazon’s customer-centric model, 27
Amazon S3 Metadata

Athena, 360
code, 359, 360
connections, 358
locating table, Lake Formation, 360
permissions, 360
query, 361
query results, 361, 362
records, 362
S3 Tables, 358
sync and querying, 357, 358
updation, 359, 360
user_metadata, 361
Amazon’s Tranium, 2
Amazon S3 Vectors, 392

architecture, 392, 393
buckets and indexes, 393, 394
cost optimization, 392
loading and querying

Bedrock Knowledge Bases,

398, 399
create client, 395
filter operations, 397, 398
helper function, 396, 397
metadata, 396, 398
OpenSearch, 399–401
parameters, 396
put_vectors() method, 395
query_vectors() method, 395
Amazon Textract, 304
Analytical workloads, 445
Anaphora resolution, 21
Apache Airflow, 258, 265, 266
Apache Avro, 105
Apache Iceberg, 129

operations in Spark, 146–149
reference architecture, 126

580

and S3 Tables, 129, 130 ( _see also_

S3 Tables)
versions supported by AWS Glue, 130
Apache Parquet, 105–107
API service

AWS Lambda functions, 204, 205, 207
Application Specific Integrated Circuits

(ASICs), 2
Artificial General Intelligence (AGI), 1, 3
Artificial intelligence (AI), xxx

investment, 2
revolution, 4
Asset filter, 186, 187
Asymmetric risk, 3
Attention scoring, 21
Audio analysis

algorithms, 338
Amazon Transcribe, 337
ASR model architectures, 338
audio into text, 337
businesses, 337
hallucinations, 338
inaccuracies, 339
Parakeet, 337
redacted transcription result, 339
self-attention mechanism, 341
solution architecture, 340
SRP, 340
traditional _vs_ . transformer-based ASR

models, 338
transcription, 340
transcription output, 339
Whisper, 337, 338, 341
Automatic Zero-Padding (AZ64), 456
Auto scaling, Glue ETL jobs

AWS Glue 3.0, 250
–enable-auto-scaling parameter, 250
Glue code updates, 251

job details, 250
schema change detection, 251, 252
Availability-partition tolerance (AP),

37, 38
AWS

Audit Manager, 92, 93
Backup, 94
Clean Rooms, 63
cloud, business agility, 13–15
CloudHSM, 58, 59
CloudTrail, 91
Config, 90, 91
credentials, 90
data mesh architecture, 158, 159
DR, 93–96
Entity Resolution, 63
HA, 96
Security Hub, 92
services, 13, 266, 347, 515, 516
shared responsibility model, 47–48
SSO, 50
AWS Certificate Manager (ACM), 61
AWS Database Migration Service (AWS

DMS), 200
CDC, 198
create database migration task, 202
create source endpoint, 199
databases and synchronizing data, 197
premigration assessment, database

migration task, 203
replication instance, 198
S3 target endpoint, 201
steps, 198–203
AWS DevOps Agent, 16

agent access to AWS resources, 290, 291
agent service, 289
DevOps agent space, 289, 290
incident response investigation, 294

INDEX

operator access, 292–294
Web app access, 291, 292
AWS DMS, _see_ AWS Database Migration

Service (AWS DMS)
AWS Glue

and Apache Spark, 145
Data Catalog

crawlers, 119–121
create a database, 118–119
databases, 117
features, 117
logical abstraction, 117
navigation menu, 118
DataBrew, 214, 223, 224
DataBrew Profiling Job, 215, 218
Jobs, 283, 284
logs, 276, 277
metrics, 278, 279
Spark Configuration, 146
Studio, 224–226
traces, 282
workflows, 260
AWS IAM, _see_ AWS Identity and Access

Management (AWS IAM)
AWS Identity and Access Management

(AWS IAM)
access request, 51
Amazon S3, 51
authentication for data services, 54–56
authentication of principal, 50
configuration and validation of an

access request, 49
configuration of IAM roles, policies,

and permissions, 49
IAM policies, 51
policy definition, 50
PoLP, 52–54
principals, 48

581

INDEX

AWS Key Management Service (KMS)

AWS-owned keys, 57, 58
custom key store, 58, 59
customer-managed keys, 57, 58
encryption across regions, 60
XKS, 59, 60
AWS KMS External Key Store (XKS), 59, 60
AWS KMS multiregion keys, 60
AWS Lake Formation, 64

benefits, 121
column-level access, 122, 123
data filters, 122
fine-grained access control, 121, 122
granting data filter to principal, 124
row-level access controls, 123
scalability, 121
AWS-owned keys, 57, 58
AWS Security Agent, 16, 44

creation process from console, 73, 74
design, 73
managed security requirements, 75, 76
services, 74, 75
vulnerabilities, 73
AWS Signature Version 4 (SigV4), 89, 90
AWS Step Functions

Airflow, 261
orchestrating workflows

AWS IAM roles and policies, 262, 263
Kiro CLI, 264, 265
visual workflow diagram, 264, 265
standard workflows _vs_ . express

workflows, 261, 262

**B**

Bedrock AgentCore, 517

abstraction, 517
features, 576

582

primitives, 517–519, 576
uses, 517
Bedrock Data Automation (BDA), 298

blueprints

ARN, 301
bank statement, 299, 300
clients, 300
configuration, 301
CSV file, 300
definition, 299
documentation, 301
JSON file, 300
sample blueprints, 299
data-centric workflows, 298
extraction capabilities, 298
projects, 302

abstraction, 304
ARN, 303
completion status, 303
creation, 302
document splitting, 302
employee onboarding process, 302
override configuration, 302
S3 bucket, 303
Bedrock invoke method, 368
BDA, _see_ Bedrock Data Automation (BDA)
BI, _see_ Business intelligence (BI)
Big data processing in cloud

efficiency, 192, 193
scalability, 193, 194
BigTable, 103
boto3 library, 124
Business agility, 13–15
Business alignment, 31–33
Business intelligence (BI)

GenBI, 494, 511
origins, 484
tools and platforms, 483

Business-level SLA, 259
Business logic, 100
Business of data

and aligning data, 27
business alignment, 31–33
dark data, 30–31
data-driven decision-making, 28–29
data-driven revenue, 29–30
leadership roles, 31
strategic asset, 28

**C**

Callback functions, 559
CAP theorem, 35–36
Catalog management

Amazon DataZone, 161
Amazon SageMaker Catalog, 160
CDC, _see_ Change data capture (CDC)
Center of excellence (CoE), 166
Change data capture (CDC)

AWS DMS, 197–203
Debezium, 197
ChatGPT3, 1, 15, 16
Chief Financial Officer (CFO), 32
Chief Information Officer (CIO), 32
Chief Marketing Officer (CMO), 32
Chief Operating Officer (COO), 32
Chief Product Officer (CPO), 32
Client credentials, 87–88
Cloud computing, 37
CloudWatch, 277, 279–281, 294
CNNs, _see_ Convolutional neural

networks (CNNs)
Command line interface (CLI)

tools, 520
Concurrency control, 128
Confused deputy, 68

INDEX

Consent fatigue, 87
Consistency-partition tolerance (CP), 37
Convolutional neural networks (CNNs),

320, 338
Crescendo attack, 69
Cross-agent authorization

delegation, 528
Cross-Site Request Forgery (CSRF), 85
Custom key store, 58, 59
Custom logs, 277
Custom metrics, 279
Customer master keys (CMK), 57
Customer-managed keys, 57, 58
Cyberattacks, 3

**D**

DAGs, 268
Dark data, 30–31
Data assets, 178
Data breaches, 43
Data catalog

AWS Glue, 117–121
Data discoverability, 164
Data domain owners, 165
Data domains, 5
Data-driven decision-making, 28–29
Data-driven revenue, 29–30
Data engineering

ACID properties, 33
agentic AI ( _see_ Agentic AI)
AP, 37, 38
availability, 36
AWS cloud, 13–15
business of data, 27–33
CAP theorem, 35–36
consistency, 36
database normalization, 33

583

INDEX

Data engineering ( _cont_ .)

distributed computing, 33–34
encryption for data protection,

56–62
generative AI ( _see_ Generative AI)
knowledge work, 12–13
MCP, 24–25
partition tolerance, 36–38
people, 9–11
PPT framework, 8, 9
practitioners, 33
processes, 11–12
RAG, 24
RAID, 33
scalability, 38–41
SQL Joins, 33
tasks, structure, people, and

technology, 8
technology, 12
transformer architecture, 21–24
Data engineers, 349, 362, 386
Data extraction, 297
Data filters, 122, 124
Data governance

Amazon Bedrock, 71–73
Amazon S3 Server Logging, 91, 92
AWS, 62, 63
AWS Audit Manager, 92, 93
AWS CloudTrail, 91
AWS Config, 90, 91
AWS Entity Resolution, 63
AWS IAM, 48–56
AWS Security Agent, 73–76
AWS Security Hub, 92
AWS shared responsibility

model, 47–48
challenge, 46
components, 45

584

data engineers, 64
data owners, 64
data stewards, 64
executive sponsors, 64
fine-grained access control for

data, 64
generative and agentic AI, 46
generative and agentic AI

security, 65–71
goals, 45
government regulations for data

and AI, 46
MCP security, 77–90
methodology, tools, processes, and

policies, 62
operating model, 44, 45
unstructured data, 46
Data governance, DataZone

Amazon SageMaker Catalog, 160
catalog management, Amazon

DataZone, 161
catalog search and subscribe, 164
core components, 160
data discoverability, 164
data lineage, 162, 163
out-of-console web-based

experience, 160
publish and subscription

management, 162
Data Iceberg, 30
Data integrity analysis, 213
Data lake ingestion

API service

AWS Lambda functions, 204,

205, 207
CDC

AWS DMS, 197–203
Debezium, 197

ELT policy, 196
SFTP server, AWS transfer

family, 207–212
Data lakes, 173, 430, 431, 441

and Apache Iceberg ( _see_ Apache

Iceberg)
on AWS, 112–113
_vs_ . data mesh

engagement model, 167
organizational structure, 166
and data warehouses, 101, 103
AWS Lake Formation, 121–124
components, 108, 109
data catalog, 117–121
data ingestion layer, 111
data lifecycle layer, 111
data processing layer, 111
databases, 108
EDW, 101, 102
5 “Vs” of big data, 101
HDFS, 102
layers, 109, 110
medallion architecture, 113–117
metadata management layer, 111
OTF, 125–129
schema-on-write _vs._ schema-on-read,

103, 104
security and governance layer, 110
separation of data and

compute, 102–103
serialization, 104–108
serving layer, 112
storage layer, 110
Data lineage, 162, 163
Data mesh strategy, 158

CoE role

matrixed organizational structure,

166, 167

INDEX

data domain owners, 165
data ownership role and

responsibility, 165
two-pizza team principle, 164
Data Mesh with Amazon DataZone

account governance

data publisher accounts, 169
DataZone domain account, 169
DataZone environment, 173
glue manage access role,

DataZone, 174
multi-account strategy, 168, 169
subscriber accounts, 170
associate accounts, 172

connect DataZone to other data

publisher accounts, 172
publisher accounts, 171
requests sent from domain

account, 173
configure user management, 171
consume data

create asset filter, 186, 187
data product subscription, 184
data utilization, 187, 188
discover data products, 183
review subscription

request, 184–186
create, 170
data governance ( _see_ Data governance,

DataZone)
data mesh strategy, 158
lake formation hybrid access

mode, 174–176
publishing data

create data product, 180–182
create data source, 176
data source definition, 177
discover data assets, 177, 178

585

INDEX

Data Mesh with Amazon DataZone ( _cont_ .)

generate metadata, data

asset, 178–180
publishing data product, 182, 183
step-by-step guide, 168
steps, set up, 167, 168
Data pipeline orchestration

Amazon MWAA _vs_ . AWS Step

Functions, 261
AWS Glue Workflows, 260
best practices

control flow management, 259
encapsulation, 258
interoperability, 259
schema evolution, 259
separation of concerns, 258
time to answer, 259, 260
Data pipelines observability

logging, 274

AWS Glue logs, 276, 277
custom logs, 277
MWAA, 275
metrics, 274

AWS Glue, 278, 279
custom metrics, 279
embedding metric format, 279–281
MWAA, 278
quantitative measurements, 278
monitoring, 274
traces, 274

AWS Glue, 282
end-to-end view, single

transaction, 281
trace variables distribution,

282–286
transaction, 281
trace variables distribution

Amazon EMR Jobs, 284–286

586

AWS Glue Jobs, 283, 284
DAG file, 282
workloads, production, 274
Data practice, 11
Data practitioners, 5
Data profiling and analysis

agent, 215
AI agents, 213–215, 218, 219
AWS Glue DataBrew profiling job,

215, 218
data integrity analysis, 213
data quality, 213
data structure, 212
descriptive statistics, 213
Glue DataBrew, 213–215
profiling job, 215
Q&A with Amazon Q, business, 219–221
relationships between variables, 213
Data project, 538
Data publisher accounts, 169
Data quality, 113, 213

big data, 240
data lake, 240
data validation reports, 240
Deequ

analyzers, 243
constraint suggestions, 244–249
data validation, 241
notebooks, 242
profiler, 244
PyDeequ project, 242
PySpark Glue jobs, 242
Scala, 242
Spark-based data quality

framework, 240
Data quality agent, 240
Data’s lifecycle, 100
Data scaling, 444

Data solution development lifecycle, 195

phases, 195
use case, 196
Data source, 177
Data strategy, 26–27
Data structure, 212
Data warehouses, 103

column compression, 456
data lakes, 441
data model and organization

strategy, 445
columnar storage, 446, 447
OLAP, 445
star schema, 445, 446
fact table, 455
generative AI, 442
use case, 441
Data warehousing

definition, 441
fundamentals, 443
DataZone domain account, 169
DCR, _see_ Dynamic client registration (DCR)
Debezium, 197
Deep learning models, 347
Deequ

Constraint Writer Agent, 246, 247
data quality

constraint suggestions, 244–249
data Validation, 241
Deequ analyzers, 243
Deequ Profiler, 244
PySpark Glue jobs, 242
Deequ Profiler, 244
Spark-based data quality framework, 240
De-risking strategy, 14
Descriptive statistics, 213
Designated marketing area (DMA), 446
Developer agent (Kiro), 16

INDEX

DevOps agent space, 289
Digital enterprise, 4
Digital images, 297
Digital technology, 13
Directed acyclic graph (DAG) workflow

management, 266
Direct prompt injection, 69
Disaster recovery (DR), 60

architectural decisions and costs, 94
architecture strategies, 95, 96
backup and restore, 94
define, 93
multiregion active-active, 95
pilot light, 95
RPO, 94
RTO, 94
strategies, 94
strategy matrix, 95
warm standby, 95
Distance metrics

cosine similarity, 384, 385
Euclidean (L2) distance, 383, 384
inner (dot) product (IP), 385
types, 383
Distributed computing, 33–34
Domain experts, 9
DR, _see_ Disaster recovery (DR)
Dynamic client registration (DCR),

83, 84, 545
DynamoDB, 38

**E**

Earnings before interest and taxes

(EBITA), 28
Efficiency, 192, 193
Elastic Container Registry (ECR), 478
Electromechanical devices, 36, 37

587

INDEX

ELT (Extract, Load, Transform)

strategy, 115
Embedded metric format, 279, 280
Embeddings

Amazon Nova Multimodal

Embeddings, 362–364
audio embeddings, 376

audio transformation, 377
digitized audio, 377
input parameters, 378, 379
_vs_ . Nova Multimodal

Embeddings, 379
sampling rates, 377
TorchAudio, 377
creation, 411, 412, 420
image embeddings

asynchronous API, 372
Google’s reverse image search, 371
image to base64, 372
input parameters, 372, 373
process, 371
models, 362
text embeddings, 364

chunks, 365, 366
input parameters, 366, 367
invoke_model() method, 368
JSON object, 364, 365
_vs_ . Nova Multimodal

Embeddings, 371
response, 369, 370
vector embeddings, 351, 362, 382
video embeddings, 374

combined video embedding, 375
input parameters, 375, 376
_vs_ . Nova Multimodal

Embeddings, 376
size limit, 375
video catalog, 375

588

video frames, 374
Encapsulation, 258
Encrypting data-at-rest, 60, 61
Encrypting data-in-transit, 61–62
Encryption for data protection

cloud platforms and cloud data

services, 56
encrypting data-at-rest, 60, 61
encrypting data-in-transit, 61–62
KMS, 57–60
on-premises data center, 56
stakes, 56
Enterprise data warehouses (EDW),

101, 102
Enterprise-ready services, 14
Entity resolution, 22–24
ETL (Extract, Transform, Load)

strategy, 115
ETL design and development

Python, 221
Spark, 221
visual ETL design tools

AWS Glue DataBrew, 223, 224
AWS Glue Studio, 224–226
business logic, visual artifacts, 222
business users, 222
humans, 222
SCM, 223
trade-offs, 222
Express Workflows, 262
Extract, load, transform (ELT) policy, 196

**F**

Facebook AI Similarity Search (FAISS),

389, 390
FastMCP framework, 520
Foundation models (FMs), 21, 23

**G**

General purpose buckets, 130
General purpose transformer (GPT)

model, 15
Generative AI, xxxi

and agentic ( _see_ Agentic AI)
Amazon Bedrock, 16
AWS, 16
ChatGPT3, 15
cloud platforms, 15
data engineering, 20
data governance, 46
data warehouses, 442
digital content, 17
emergence of, 483
FMs, 21
GPT model, 15
_vs_ . machine learning models, 17
models, 309, 347, 431
Nova and Titan, 16
observability, 286–289
open domain models, 17
task-oriented models, 17
Text-to-SQL, 17
timeline, 15, 16
use cases, 17
Generative AI risks

confused deputy, 68
Guardrails, 70–71
hallucination, 69
Model poisoning, 66
NightShade, 67
prompt injection attack, 69–70
sensitive data leakage, 67
supply chain attack, 66–67
training and inference, 65
Waterhole poisoning, 67

Generative BI (GenBI), 494, 511
Glue Crawlers, 251
Glue DataBrew, 213, 214
Glue Job Update Writer Agent, 252
Glue Manage Access role, 173
Glue PySpark, 229
_GlueServiceRole_, 131
Glue session, 132
Google File System (GFS), 34
Google’s IO Protobuf, 104
Google’s TPUs (Tensor Processing

Units), 2
Guardrails, 70–71

**H**

Hadoop Distributed File System

(HDFS), 34
Hallucination, 69
Hands-on learning, xxxii
Hardware security module (HSM), 58
Headless consent mechanisms, 528
Hidden Markov models (HMMs), 338
Hierarchical Navigable Small World

(HNSW), 386, 387, 389, 420
High availability (HA), 96

**I**

IAM authentication

to Amazon RDS, 55
data services, 54–56
with SigV4, 89, 90
IAM Database Authentication, 54
IAM policies, 52

Anthropic Claude 3 Sonnet, 53
conditions, 51
with generative AI, 54

INDEX

589

INDEX

IAM policies ( _cont_ .)

in JSON, 52
statements, 51
version, 51
Iceberg API, 149
Iceberg table maintenance agent

analysis and planning tools,

152, 153
conceptual elements, 150
discovery and inventory tools, 150
experimental phase, 150
maintenance actions, 153
metrics collection tools, 150, 151
rules-based operations, 149
S3 buckets, 149
IDP, _see_ Intelligent document

processing (IDP)
Image analysis

attention scoring, 321, 322
CNNs, 320
facial recognition, 334

attributes, 336
Claude Response, 336, 337
DEFAULT parameter value, 335
detect_faces method, 334
helper function, 335, 336
purpose-built services, 337
rekognition, 334
sample image, 334
IDP ( _see_ Intelligent document

processing (IDP))
image properties

Amazon Rekognition console, 328
Anthropic Claude, 330, 331
Bedrock, 330
helper function, 328, 329
rekognition and Claude Sonnet 3.5,

332, 333

590

response, 330
transformer-based model, 332
object detection

Anthropic Claude, 325
Bedrock response, 327
Boto3 clients, 323
helper functions, 324, 325
JSON response, 326
label detection demo, 323
libraries, 323
printer-friendly display code, 326
rekognition, 325–327
training set, 327
OCR, 320
self-attention mechanism, 321
transformer architecture, 321
transformer models _vs_ . CNNs and OCR

models, 322
vectors, 321, 322
Indirect prompt injection attack, 69
Integrated development environment

(IDE), 26, 228
Intelligent document processing (IDP), 304

AWS ML services, 304
classification

Amazon Comprehend, 305
cutting-edge smartwatch, 309
document text, 308
documents, 305–307
JSON, 306
mislabeled category, 307, 308
patient intake form, 305, 306
Sports model, 309
enrichment, 316

business/location names, 320
Claude’s response, 319, 320
customization, 318
determination of PII, 320

entities detection, 317
JSON response object, 317
Python script, 318
redacted script, 318, 319
sample document, 317
extraction

Amazon A2I, 311
AWS ML services, 309
boto3 Python script, 311, 312
Claude’s response, 314, 315
data extraction results, 316
document analysis, 312, 313
document review, 310
document types, 309
documents and forms, 309
indicate ‘yes’ or ‘no’ as appropriate

section, 312, 313
JSON response, 315
justification category, 312
response, 312–314
sample document, 310
Textract, 310–313, 316
workflow, 304, 305

**J**

JOIN problem, 444, 482
JOIN strategies, 444
JupyterLab

application, 228
notebook, 232
space, 229

**K**

Kinesis Client Library (KCL), 424, 425, 440
Kinesis Producer Library (KPL), 424,

425, 440

INDEX

Kiro, 26, 233
Kiro CLI, 264, 294
KMS, _see_ AWS Key Management

Service (KMS)
k-nearest neighbors (k-NN), 408
Knowledge work, 12–13

**L**

Lambda Function

AgentCore Gateway, 537, 538
MCP error response codes, 532
MCP request entrypoint, 532, 533
MCP request process

call/tools request, 535–537
initialization, 534
list tools request, 534, 535
MCP request routing, 533
request handling layer, 532
target configuration, 531
Lambda functions, 204, 425, 426
Large language model (LLM), 19, 559
Leadership, 10, 11
Leadership Principles (LPs), 11
Locality-sensitive hashing (LSH), 387,

389, 420
Logs, 274
Long-range dependency, 22
Lower latency models, 440

**M**

Machine learning, 17, 312
Managed workflows, 208
Massively parallel processing

(MPP), 447
Matryoshka Representation Learning

(MRL), 363

591

INDEX

MCP, _see_ Model context protocol (MCP)
MCP client-server request and

authorization flows
authorization code and client

credentials, 81
client-server initialization and

handshake, 81, 82
DCR, 83, 84
metadata, 82–83
in OAuth 2.1, 81
MCP servers, 514

agents, 516
applications, 521
data services, 515
deployment, 528–530
endpoint, 521
framework, 520
language support, 520
methods/notifications, 523
monitoring, 526
Python, 521
remote servers, 521, 522, 527
SDKs, 520
security flaw, 514
selection, 530
STDIO-based servers, 521
termination, 521
transport mechanisms, 576
Medallion architecture

Amazon S3, 114
audit, 115
conform, 116
debugging, 114
description, 113
Landing Zone, 115
optimized, 116
published, 117
raw, 115, 116

592

stages, 114, 117
unified analytics, 116
Mel-frequency Cepstral coefficients

(MFCCs), 338
Model context protocol (MCP), 2, 24–25,

27, 513, 515, 516
access token request, 86, 87
AgentCore Gateway, 530, 531
agentic AI, 515
authorization code request, 84–86
client-server request and authorization

flows, 81–84
_vs._ direct integration, 77, 78
enterprise, 77, 515
headless consent mechanisms, 78
host/client/servers, 521
IAM authentication with SigV4,

89, 90
implementations, 527
inbound outbound authentication, 79
industry adoption, 514
message protocol, 522
message structure

MCP notifications, 526, 527
MCP requests, 523, 524
MCP responses, 524, 525
OAuth, 80
OAuth resource servers, 80
optimistic view, 515
PostgreSQL, 77
security, 528
security improvements, 77
servers ( _see_ MCP servers)
technical details, 519
transport mechanisms, 520, 521
Model poisoning, 66, 67
Multiagent systems, 528
Multiregion active-active, 95

**N**

Neural network models, 297
NightShade, 67
NLP, 22
Non-linear revenue, 3
Non-Metric Space Library (NMSLib),

389, 390
Notebook-based development, 228, 229

**O**

OAuth, 80
OAuth resource servers, 80
Online analytical processing (OLAP), 445
Open domain models, 17
Open Table Formats (OTF)

Apache Iceberg, 129
concurrency control, 128
features, 129
metadata and manifest files, 125
object stores, 125
partition evolution, 127, 128
schema evolution, 127
selection, 129
table management, 125
time travel, 126
Operational database, 100
Operational workloads, 445
Optical Character Recognition (OCR), 320
Optimistic concurrency control (OCC), 128
OPTIMIZE Iceberg Tables, 144
Optimized Row Columnar (ORC), 104
OTF, _see_ Open Table Formats (OTF)

**P**

Partition evolution, 127, 128
Partition tolerance, 36–38

INDEX

Patching vulnerabilities, 47
Personally identifiable information (PII),

46, 67, 72
Pilot light, 95
Pre-registration, 87, 88
Pretrained audio neural networks

(PANNs), 338
Pre-trained foundation model, 24
Principle of least privilege (PoLP), 52–54
Private MCP clients, 87–88
Product quantization (PQ), 388, 389, 420
Projected representations, 21
Prompt engineering, 460–463
Prompt injection attack, 69–70
Proof Key for Code Exchange (PKCE),

80, 83, 84
Public-private partnerships, 2
Publishing data, DataZone

create data product, 180–182
create data source, 176
data source definition, 177
discover data assets, 177, 178
generate metadata, data asset, 178–180
publishing data product, 182, 183
PyDeequ packages, 247
PyIceberg library, 150
Python, 221

**Q**

QuickSight Q

create visuals, 499, 500
dynamic reporting, 494

**R**

RAG, _see_ Retrieval-augmented

generation (RAG)

593

INDEX

Ransomware, 43
RDBMS (relational database management

systems), 101
Read-Eval-Print-Loop (REPL), 228
Real-time data processing, 421, 424, 440
Real-time data sources, 422
Recipes, 223, 224
Recovery Point Objective (RPO), 94
Recovery Time Objective (RTO), 94
Recurrent Neural Networks (RNNs), 338
Redshift HTTP MCP server

AgentCore Runtime

configuration process, 550
launch process, 551–553
AWS, 544

Amazon Cognito, 545, 546
IAM authentication, 549
IAM execution role, 546–548
deploy and test, 543, 544
deployment steps, 540
script, 541, 543
testing

headers, 555
MCP request, 555, 556
token requests, 554
URL, 554
Redshift integration

Amazon Bedrock

CREATE EXTERNAL MODEL, 471
IAM policy, 470, 471
sentiment scores, 471
Amazon SageMaker, 472

Create External Model, 473
IAM role, 472, 473
sentiment scores, 473
benefit, 470
Redshift Managed Storage (RMS), 482
Redshift ML, predictive model training

594

batch inference, 481
benefits, 475
data requirements, 475
grant user access, 479
IAM role and policy

authorization, 477
log groups/write logs, 478
permissions, 476
pre-built images, 478
SageMaker, 478
S3 bucket/training data, 477, 478
training job metrics, 479
training jobs, 478
model performance, 481
S3 bucket, 475
training process, 480
types, 479
Redundant Array of Independent Disks

(RAID), 33
Relational databases, 515
Retrieval-augmented generation (RAG),

20, 24, 349, 473, 474
conceptual process flow, 350
corpus collection and storage

Amazon AppFlow, 356
Amazon EventBridge, 356
Amazon S3 Metadata ( _see_ Amazon

S3 Metadata)
connectors, 356
documents, 357
organizing, 356
processing stages, 356, 357
robust data collection, 356
S3, 357
scale and complexity, 355
web scraping, 355
embeddings process ( _see_ Embeddings)
managed RAG, 351

advantage, 352
Amazon Bedrock Knowledge

Bases, 353–355
Amazon Q for Business, 352, 353
computing similarity, 352
data collection process, 351
disadvantage, 352
vector embeddings, 351
objective, 350
request, 351
semantic search ( _see_ Semantic search)
use cases, 390
vector format and precision, 381, 382
Risk-adjusted analysis, 2
Robotic Process Automation (RPA), 19, 492
Robust generative AI models, 349
Role-based access controls (RBAC), 510

**S**

SageMaker Catalog, 231
Sales and relationship management, 9
Sales datamart demo tables, 456
Sales reporting AI Agent

AgentCore Runtime

agent deployment, 569
configuration process, 568
configuration results, 569
Dockerfile, 570
launch command, 569
launch process, 569–571
questions, 568
testing, 571, 572
create agent script

agentic loop, 558
function definition, 560
import statements, 559, 560
inputs, 559

INDEX

memory hooks, 561–563
Redshift MCP server, 566
request, construct, 567
sales agent definition, 564, 565
Strands Agents SDK, 558
tool’s definition, 560
observing and monitoring

AgentCore logs delivery to

CloudWatch logs, 573, 574
Bedrock Evaluations, 574, 575
dashboard, 572, 573
pattern, 557
script testing, 567, 568
Scalability, 38–41, 193, 194
Schema evolution, 127, 259
Schema-on-write _vs._ schema-on-read,

103, 104
Self-attention mechanisms, 21, 23
Semantic search

algorithms, 386, 420
algorithms comparison, 389
architecture, 380, 390
Aurora PostgreSQL, 412–415
concepts, 380
definition, 351
HNSW, 386, 387
indexes, 410
LSH, 387
OpenSearch, 415–417
PQ, 388
search problem, 385
stacks, 390
Sensitive data leakage, 67
Separate analytical workloads

from operational data systems, 100
lock-In, 100
scalability, 101
vendor-agnostic data, 101

595

INDEX

Serialization formats

advanced serialization

formats, 104–107
performance, scalability, and

compatibility, 104
text-based serialization, 104
Server-side encryption using Amazon S3

managed keys (SSE-S3), 61
Similarity search libraries, 389

FAISS, 389, 390
NMSLib, 389, 390
Single Responsibility Principle (SRP), 340
Single Sign-On (SSO), 170
Skilled data engineers, 5
S3 Metadata, 111
S3 Object Lock, 115
Source control management (SCM), 223
Spark, 221

configuration, 133
Iceberg table

creation, 147
snapshots, 149
update, 148
vacuuming, 149
write data, 147
perform time travel queries, 148
ScanFiles, 147
session, 132–134
Spec-driven development, 5
S3 Tables, 129, 130

configure IAM policy, 131
Iceberg Queries

inspect snapshots, 137, 138
inspecting data files, 136, 137
s3-tables-catalog-for-iceberg.jar., 132
selection, 135
Spark session, 132–134
table buckets, 130, 131

596

unmanaged apache iceberg, 138–145
updating, 136
write data, 134–135
s3tablesbucket, 133
s3-tables-catalog-for-iceberg.jar., 132
Stakeholders, 9
Standard Workflows, 262
Star Schema data model, 483
Strands Agents SDK, 514, 538, 576
Streaming data, 422

Generative AI

Bedrock model, 427
CloudWatch dashboard, 427, 428
lambda function, 428
latency, 429
lower latency models, 427
scaling inference, 429, 430
streaming record, 426
producers and consumers, 422, 423
reconciliation solution, 430, 431
sources and sinks, 422
stock trades, 430, 431
stream, 422
transactional S3 tables ( _see_

Transactional S3 tables)
use cases, 430
Streaming ingestion, 423

Amazon Kinesis, 424

KCL, 424, 425
KPL, 424, 425
lambda functions, 425, 426
service, 424
Generative AI, 426
Subscriber accounts, 170
Super-fast, Parallel, In-memory

Calculation Engine (SPICE), 511
Superintelligence, 3
Supply chain attack, 66–67

**T**

Table buckets, 130, 131
Target bucket, 92
Task-oriented models, 17
TensorFlow, 222
Text-based serialization, 104
Text embeddings model, 24
Text-to-SQL

prompt engineering, 460, 461
solution architecture, 463, 464, 482

report suggestions, 468–470
SQL Evaluation Agent, 466
TextToSQLAgent, 465
web interface, 466, 468
structural input formatting, 461–463
The National Security Agency (NSA), 43
The USB-C port for AI, 25
Threat intelligence, 3
Time to answer, 259, 260
Time travel, 126
Traces, 281
Transactional S3 tables

create namespace, 432
creation, 431
Firehose, 431
Firehose delivery stream

creation, 435
hypothetical demonstration, 438
reconciliation, 437
sample trades, 436, 437
source and destination, 435
unique key configuration, 435, 436
update/upsert operation, 435
updated records, 437, 438
IAM role, 433
Lake Formation permissions, 434
managed Iceberg table, 432

INDEX

namespace to glue catalog, 433
trades-table-schema.json file, 432
trend analysis agent, 438–440
Transfer learning, 312
Transformer encoder (decoder)

model, 22, 23
Transformer model architecture

anaphora resolution, 21
attention scoring, 21
conceptual diagram, 22
entity resolution, 22–24
FMs, 23
long-range dependency, 22
multihead attention, 23
NLP, 22
projected representations, 21
self-attention mechanisms, 21, 23
Transformer models, 320, 339
Two pizza teams principle, 164

**U**

UI/UX strategy, 5
Unmanaged Apache Iceberg

AWS Glue, 145–146
in S3

creation, 138, 139
metadata, 141–143
OPTIMIZE Iceberg Tables, 144
perform maintenance, 138
time travel feature, 140, 141
updation, 139, 140
VACUUM Iceberg Tables, 144, 145

**V**

VACUUM Iceberg Tables, 144, 145
Vector databases, 380, 391, 392

597

INDEX

Vendor-agnostic data, 101
Video analysis

Amazon Transcribe, 346
AWS ML services, 346
creation, 344
detected labels, 343
LLM pricing, 344
modification, 344
narrator, 343
Rekognition, 346
Rekognition Video, 342
scene-by-scene analysis, 345
solution architecture, 346
time-stamped labels, 342, 343
transcriptions, 343, 344

598

uses, 341
video extraction, 342

**W, X, Y**

Warm standby, 95
Waterhole poisoning, 67
Web app, 291
Web Server, 267
Write-Once, Read-Many (WORM)

protection, 94

**Z**

Zstandard (ZSTD), 107
