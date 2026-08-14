---
title: Build Your Own Agentic AI Framework Design Flexible Multi-agent Systems in
  Python with MCP and A2A integration Gigi Sayfanz-lib
source: sources/ai/pdf/Build Your Own Agentic AI Framework Design Flexible Multi-agent
  Systems in Python with MCP and A2A integration Gigi Sayfan z-librarysk 1libsk z-lib.pdf
source_type: paper
source_hash: 5347e44091e9f0dfb48b30004cad6f63355575b2f359588a1a5b5d8333b9b3f0
tags:
- ai
- paper
extracted: '2026-08-14'
---

EXPERT INSIGHT 

L 

Design Multi-Agent Al Systems Using MCP and A2A 

Engineer your own Python-based agentic Al framework with tool use, memory, and multi-agent workflows 

iy 

oe) 

Gigi Sayfan 

<packt> 

#### **Design Multi-Agent AI Systems Using MCP and A2A** 

Engineer your own Python-based agentic AI framework with tool use, memory, and multi-agent workflows 

###### **Gigi Sayfan** 

###### **Design Multi-Agent AI Systems Using MCP and A2A** 

Copyright © 2026 Packt Publishing 

_All rights reserved_ . No part of this book may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, without the prior written permission of the publisher, except in the case of brief quotations embedded in critical articles or reviews. 

Every effort has been made in the preparation of this book to ensure the accuracy of the information presented. However, the information contained in this book is sold without warranty, either express or implied. Neither the author, nor Packt Publishing or its dealers and distributors, will be held liable for any damages caused or alleged to have been caused directly or indirectly by this book. Packt Publishing has endeavored to provide trademark information about all of the companies and products mentioned in this book by the appropriate use of capitals. However, Packt Publishing cannot guarantee the accuracy of this information. 

This book was written by Gigi Sayfan. Generative AI tools were used only to assist with ideation, phrasing, and diagram drafts, and all technical content and code were created, verified, and tested by the author and Packt’s editorial team. Packt does not accept AI-generated content that replaces expert authorship. 

**Portfolio Director:** Gebin George **Relationship Lead:** Gebin George/Sonia Chauhan **Project Manager:** Prajakta Naik **Content Engineer:** Aditi Chatterjee **Technical Editor:** Rahul Limbachiya **Copy Editor:** Safis Editing **Indexer:** Hemangini Bari **Proofreader:** Aditi Chatterjee **Production Designer:** Shantanu Zagade **Growth Lead:** Nimisha Dua 

First published: February 2026 Production reference: 1100226 

Published by Packt Publishing Ltd. Grosvenor House 11 St Paul's Square Birmingham B3 1RB, UK. 

ISBN 978-1-80611-647-8 `www.packtpub.com` 

#### **Contributors** 

###### **About the author** 

**Gigi Sayfan** is a member of the AI agents infra team at Perplexity, where he is focused on building large-scale environments and harnesses for AI agents. 

He has been developing software professionally for more than 30 years in domains as diverse as instant messaging, morphing, chip fabrication process control, embedded multimedia applications for game consoles, brain-inspired machine learning, custom browser development, web services for 3D distributed game platforms, IoT sensors, and virtual reality. He has written production code in Go, Python, Java, C#, C++, and Typescript/JavaScript. 

His technical expertise includes AI agents, generative AI, cloud-native technologies, DevOps, databases, low-level networking, distributed systems, unorthodox user interfaces, and the full software development life cycle. 

Gigi has authored several books on Kubernetes and microservices and written hundreds of technical articles on a wide range of topics. 

###### **About the reviewers** 

**Shruti Dhumak** is a senior technology executive and the head of customer engineering at Google, where she leads large-scale enterprise transformation through data, the cloud, and AI. She is recognized for building and scaling high-performing teams and aligning complex technology strategy with executive priorities. Shruti partners closely with C-suite leaders to enable sustainable growth and measurable business outcomes, bringing a strong focus on operational excellence and customer impact. As a deep technical expert in advanced cloud architectures and autonomous agentic systems, she serves as a trusted advisor and mentor passionate about results-driven leadership and advancing the next generation of technology leaders. 

**Nicolas Bievre** is a senior machine learning engineer at Meta, specializing in AI, recommender systems, and generative AI for advertising and healthcare. He has held critical leadership roles at Meta and PayPal, architecting systems that personalize content for hundreds of millions of users and ensuring compliance for major revenue-driving models. A Stanford alumnus, his peer-reviewed research in leading AI and bioinformatics journals is now utilized in hospitals for cancer research. Internationally recognized, he has received the AdKDD Best Paper Award, the Core Ads Growth Privacy Award, and the Outre-Mer Outstanding Talent Award. He also serves as an AI consultant to the French government and a reviewer for top AI organizations. 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns— _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and GenAI systems. Subscribe now and receive a free eBook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OA<br>ae<br><!-- End of picture text -->

#### **Table of Contents** 

|**Preface**|**xxi**|
|---|---|
|**Free benefits with your book**<br>**........................................................................**|**..**<br>**xxviii**|
|**Part 1: Foundations of Agentic AI**|**1**|
|**Chapter 1: Introduction to Generative AI and AI Agents**|**3**|
|Free benefits with your book • 4||
|**The evolution of generative AI**<br>**.....................................................................**|**.........**<br>**4**|
|The early days of symbolic AI • 5||
|The expert systems era • 6||
|The rise of machine learning and statistical methods • 7||
|Deep learning and the neural network renaissance • 7||
|The emergence of generative models, transformers, and language models • 8||
|The rise of AI agents • 9||
|**Introducing AI agents**<br>**..................................................................................**|**.......**<br>**10**|
|AI agent characteristics • 10||
|Key differences: chatbots versus agents • 12||
|Use cases for agentic AI • 13||
|**Introducing the components of agentic AI systems**<br>**.......................................**|**........**<br>**15**|
|Common components of agentic AI systems • 16||
|Types of agentic AI architectures • 17||
|_Single-agent loop_•_17_||
|Planner and executors • 19||
|_Multi-agent system_•_20_||
|_Graph-based architecture_•_21_||
|**Summary**<br>**....................................................................................................**|**.......**<br>**22**|

|_Table of Contents_<br>viii|
|---|
|**Chapter 2: Understanding How AI Agents Work**<br>**25**|
|**Understanding the agent loop: sense, think, act**<br>**..................................................**<br>**26**<br>l|
|The session workflow • 26|
|The agent loop phases • 27|
|Workings of an agent loop in AutoGen • 30<br>_The core implementation of AutoGen_•_30_|
|**Managing long conversations with memory, goals, and state**<br>**...............................**<br>**35**|
|The context window • 37<br>_Why do LLMs have no memory?_•_38_|
|Memory in AutoGen • 40|
|**Planning and reasoning mechanisms**<br>**...................................................................**<br>**41**|
|Working with reasoning models • 41|
|Single-agent planning and reasoning • 42|
|Multi-agent planning and reasoning • 42|
|**Tool use and environment interactions**<br>**...............................................................**<br>**43**|
|How are user-defined tools implemented? • 44|
|How are tools declared? • 45|
|_How does the LLM decide which tool to use?_•_46_|
|Tool use in AutoGen • 48|
|**Agent evaluation and feedback loops**<br>**..................................................................**<br>**50**|
|Human feedback • 51|
|Automated evaluation • 52|
|Industry benchmarks • 55|
|**Summary**<br>**...........................................................................................................**<br>**56**|
|**Chapter 3: A Hands-On Walk-Through of a Simple AI Agent**<br>**59**|
|**Technical requirements**<br>**......................................................................................**<br>**60**|
|**Introducing the k8s-ai agent**<br>**..............................................................................**<br>**60**|
|Setting up a local kind cluster • 61|
|Running the k8s-ai agent • 64|
|Checking the cluster with k8s-ai • 65|

_Table of Contents_ 

ix 

|**Understanding the k8s-ai agentic system**<br>**.............................................**|**...............**<br>**70**|
|---|---|
|Code walk-through of the k8s-ai agent • 71||
|Defining and registering tools with OpenAI • 73||
|Implementing the tool-calling execution loop • 76||
|Running and interacting with the Kubernetes chat agent • 80||
|**Summary**<br>**............................................................................................**|**...............**<br>**81**|
|**Part 2: Building Your Own Agentic AI Framework**|**83**|
|**Chapter 4: Building a Tool-Based Agentic AI Framework**|**85**|
|**Technical requirements**<br>**.......................................................................**|**...............**<br>**86**|
|**AI-6 framework backend architecture and components**<br>**........................**|**...............**<br>**86**|
|Core engine • 87||
|_Initialization_•_87_<br>_Running the engine_•_91_||
|_Executing the agentic loop_•_92_||
|The LLM provider abstraction • 97||
|_The LLMProvider interface_•_97_||
|_The supported providers_•_99_||
|**Tool system architecture**<br>**......................................................................**|**..............**<br>**105**|
|Custom tool support • 106||
|_What about built-in tools?_•_107_||
|Tool security and permissions • 108||
|**Memory management**<br>**.........................................................................**|**...............**<br>**111**|
|What is a session? • 111||
|Short-term memory in the agentic loop • 115||
|Sessions and conversations • 115||
|Long-term memory and session loading • 115||
|Handling long contexts • 118||
|**Summary**<br>**............................................................................................**|**..............**<br>**122**|
|**Chapter 5: Implementing Custom Tools**|**125**|

_Table of Contents_ 

x 

|**Technical requirements**<br>**.....................................................................................**<br>**126**|
|---|
|**Defining provider-agnostic tools**<br>**........................................................................**<br>**126**<br>i|
|OpenAI Python tool specification • 126<br>i|
|Ollama Python tool specification • 133<br>i    i|
|Defining the AI-6 tool specification schema • 135<br>**i**|
|**Defining AI-6 custom tools**<br>**................................................................................**<br>**136**|
|General command-line tools • 136|
|Filesystem tools • 138|
|Implementing the echo tool • 140|
|Test runner tool • 142|
|Bootstrap tool • 144|
|Memory tools • 145|
|Listing sessions • 146|
|Loading sessions • 148|
|Getting the current session ID • 149|
|Deleting sessions • 151|
|**Implementing a new tool from scratch with AI-6**<br>**...............................................**<br>**152**|
|How to interact with AI-6 • 153|
|Building a new GitHub tool with AI-6 • 153|
|**Implementing a new tool manually**<br>**....................................................................**<br>**161**|
|**Summary**<br>**..........................................................................................................**<br>**164**|
|**Chapter 6: Creating Chat Interfaces Using Slack and Chainlit**<br>**167**|
|**Technical requirements**<br>**....................................................................................**<br>**168**|
|**Why the UI matters in agentic AI workflows**<br>**.....................................................**<br>**168**|
|Agent feedback loops and visibility • 168|
|Interruptibility and human-in-the-loop design • 169|
|Diagnosing and debugging agent behaviors • 170|
|Balancing autonomy and user control • 171|
|UI as a trust-building mechanism • 173|
|**Building a Slack bot interface**<br>**.............................................................................**<br>**174**|
|Taking the AI-6 Slack bot for a spin • 175|

_Table of Contents_ 

xi 

Authentication and configuration setup • 179 **/.env.*Slack Bot initialization • 183 Message handling and event processing • 185 Channel management and multi-user support • 188 Integration with the AI-6 engine • 191 **Developing a web UI with Chainlit..................................................................... 192** Chainlit framework overview • 193 Taking AI-6 Chainlit for a spin • 193 Configuration and engine integration • 200 Application life cycle and event handlers • 201 _The on_chat_start event handler_ • _202 The on_message event handler_ • _204 The on_settings event handler_ • _206_ **Best practices for interactive agent interfaces.................................................... 208** Clarify the agent’s role and capabilities • 208 Safeguards – confirmations, dry-runs, and safety nets • 208 Design for turn-based transparency • 209 Prioritize tool invocation and feedback loops • 209 Embrace configurability and runtime control • 209 Logs, metrics, and distributed tracing for agentic systems • 210 **Summary ......................................................................................................... 210** **<mark>Chapter 7: Integrating with the Model Context Protocol Ecosystem 213</mark> Technical requirements ..................................................................................... 214 What is MCP? .................................................................................................... 214** The motivation behind MCP • 214 **MCP architecture core and core components ...................................................... 215** MCP servers • 216 MCP clients • 217 MCP hosts • 217 Local versus remote MCP servers • 217 Benefits of using MCP • 218 

_Table of Contents_ 

xii 

|The MCP ecosystem • 219||
|---|---|
|**Building MCP servers**<br>**.......................................................................................**|**.**<br>**219**|
|Filesystem MCP server • 220||
|GitHub MCP server • 224||
|**Building MCP clients**<br>**........................................................................................**|**229**|
|The MCPClient class • 229||
|Connecting to an MCP server • 230||
|Invoking an MCP tool • 232||
|**Integrating MCP into the AI-6 framework**<br>**.........................................................**|**234**|
|The universal MCPTool class • 235||
|MCP tool discovery • 239||
|The tool manager • 240||
|How the engine uses the tool manager • 245||
|**Putting it all together**<br>**.......................................................................................**|**248**|
|**Summary**<br>**.........................................................................................................**|**250**|
|**Part 3: Constructing Multi-Agent Systems**|**253**|
|**Chapter 8: Designing Multi-Agent Systems**|**255**|
|**Technical requirements**<br>**....................................................................................**|**256**|
|**What is multi-agent orchestration and why does it matter?**<br>**...............................**|**256**|
|What is an AI agent? • 256||
|Adding explicit agents to AI-6 • 256||
|_Renaming Engine to Agent_•_257_||
|_Adding a system prompt to the Agent configuration_•_257_||
|_Adding enabled_tools and disabled_tools fields to the Agent configuration_•_258_<br>_Adding a new AgentTool that wraps an AI-6 Agent instance_•_258_||
|Why do we need multi-agent systems? • 260||

_Context window limitations_ • _260 Specialization challenges_ • _261 Model selection constraints_ • _261 Cognitive load distribution_ • _261_ 

_Table of Contents_ 

xiii 

_Fault tolerance and resilience_ • _261 Testability and debugging_ • _262_ How to orchestrate multiple agents • 262 _Sequential orchestration_ • _262 Parallel orchestration_ • _263 Hierarchical orchestration_ • _265 Event-driven orchestration_ • _266 Collaborative orchestration_ • _268 Hybrid orchestration_ • _269_ Design considerations • 270 **Introduction to the A2A protocol........................................................................ 271** Core components of the A2A protocol • 272 

_A2A communication mechanisms_ • _274 Adding A2A support to AI-6_ • _274 Integrating A2A client capabilities into AI-6_ • _274 The A2ATool class_ • _277 Configuration and setup_ • _279_ **Designing collaborative agent workflows........................................................... 281** Agent decomposition strategies • 281 _Decomposition by domain expertise_ • _281 Decomposition by workflow stage_ • _282 Decomposition by capability pattern_ • _282 Decomposition decision framework_ • _283_ System prompt design patterns • 284 _The specialist agent template_ • _285 The coordinator agent template_ • _286 The validator agent template_ • _288 Domain-specific prompt examples_ • _290_ 

Tool assignment decision framework • 292 Context engineering for multi-agent systems • 294 

_Types of context in multi-agent systems_ • _295_ 

_Context management strategies_ • _296_ 

_Table of Contents_ 

xiv 

|_Context window management_•_298_<br>_Inter-agent context sharing_•_300_<br>Taking AI-6 and A2A for a ride • 302<br>_Multi-agent patterns in action_•_304_<br>**l**||
|---|---|
|**Conflict resolution and role assignment in multi-agent systems**<br>**............**<br>Best practices for conflict prevention • 308<br>_Design-time conflict analysis_•_308_<br>_Runtime conflict detection_•_308_<br>_Clear escalation paths_•_309_|**............**<br>**306**|
|**Summary**<br>**.............................................................................................**|**............**<br>**309**|
|**Chapter 9: Implementing Multi-Agent Systems with A2A**|**311**|
|**Technical requirements**<br>**........................................................................**|**.............**<br>**312**|
|**Building an AI-driven DevOps team**<br>**......................................................**|**.............**<br>**312**|
|What makes DevOps suitable for multi-agent AI? • 312||
|MAKDO – a multi-agent Kubernetes DevOps system • 313<br>_System architecture_•_313_<br>_The coordinator agent – orchestrating operations_•_314_||
|Agent interaction patterns • 316||
|_LLM-driven agent coordination_•_316_||
|_Extending AI-6 with new tools_•_318_||
|_Tool discovery and assignment_•_319_||
|_Context sharing and state management_•_320_||
|**Defining roles and responsibilities for specialized agents**<br>**.......................**|**.............**<br>**321**|
|From DevOps workflows to agent architecture • 321<br>_Why four agents instead of one?_•_322_||
|_Why separate the analyzer and fixer?_•_323_<br>_Why separate Slack_Bot?_•_323_||
|_Tool access boundaries_•_324_||
|Extending the architecture • 324<br>_Key design patterns_•_325_||

**Implementing the agents.................................................................................. 326** 

_Table of Contents_ 

xv 

Configuration-driven agent implementation • 326 _Tool discovery and assignment_ • _330 Session isolation_ • _331 Configuration over code_ • _332 Key takeaways_ • _332_ **Orchestrating the team with a manager agent.................................................... 333** Dynamic workflow execution • 333 _Decision points and branching_ • _334_ Handling complex multi-step operations • 335 _Multi-cluster coordination_ • _335 Conditional remediation_ • _336 Retry and verification loops_ • _336_ Error handling and recovery • 337 _Agent communication failures_ • _337 Partial failures_ • _337 Cascading failures_ • _338_ State management and coordination • 338 _Memory tools for long-term state_ • _338 Avoiding duplicate operations_ • _339_ Proactive versus reactive orchestration • 340 _Reactive mode – user-initiated operations_ • _340 Proactive mode – autonomous monitoring_ • _340 Hybrid approach – event-driven coordination_ • _340_ **Integrating human feedback and control channels ............................................. 341** The human-AI interface challenge • 341 The Slack_Bot agent architecture • 341 Building a custom MCP server with FastMCP • 342 _The FastMCP Slack server_ • _343_ Communication patterns • 346 _Notification hierarchy_ • _346 Message formatting_ • _347 Contextual messaging_ • _348_ 

_Table of Contents_ 

xvi 

|Escalation pattern for restricted operations • 348|
|---|
|Alternative communication channels • 350|
|Security and access control • 350|
|Observability and audit trail • 351|
|**MAKDO in action – a complete demo walk-through**<br>**...........................................**<br>**352**|
|Demo setup • 352|
|Creating cluster problems • 352<br>_i_|
|_Step 1 – demo start notification_•_354_|
|_Step 2 – analysis phase_•_355_|
|_Step 3 – remediation phase_•_360_|
|_Step 4 – demo complete_•_364_|
|Key observations • 365|
|**Summary**<br>**.........................................................................................................**<br>**366**|
|**Chapter 10: Testing, Debugging, and Troubleshooting Multi-Agent**<br>**369**|
|**Systems**|
|**Common failure modes in agentic systems**<br>**........................................................**<br>**370**|
|Agent hallucination • 370|
|Wrong tool use and tool misuse • 372|
|Poor instruction following • 373<br>i|
|Infinite loops and runaway agents • 375|
|Communication and coordination breakdowns • 376|
|Timeout and latency issues • 377|
|State management and consistency errors • 378|
|Security and permission failures • 379|
|**Instrumentation and observability for AI agents**<br>**...............................................**<br>**379**|
|Core observability primitives • 380|
|_LLM call tracing_•_380_|
|_Tool execution logs_•_380_|
|_Agent state snapshots_•_381_|
|_Span and trace hierarchies_•_381_|
|_Metadata enrichment_•_381_|

_Table of Contents_ 

xvii 

|_Structured logging and trace formats_•_381_|
|---|
|LLM-specific observability tools • 382|
|Metrics and KPIs for agent performance • 383|
|Real-time monitoring and alerting • 384|
|Debugging with observability data • 385|
|Privacy and security considerations • 386|
|**Debugging tool use and function call chains**<br>**......................................................**<br>**387**|
|Understanding the tool call life cycle • 387|
|Tracing function call chains • 388|
|_Common tool use anti-patterns_•_389_|
|_Debugging strategies for tool use_•_390_|
|_Building tool use guardrails_•_391_|
|**Diagnosing coordination failures in multi-agent workflows**<br>**..............................**<br>**392**|
|Understanding coordination failure patterns • 392|
|_Agent interaction patterns and their failure modes_•_395_<br>_l_|
|_Tracing dependencies and data flow_•_397_|
|Managing shared state and detecting deadlocks • 399|
|_State synchronization challenges_•_400_|
|_Detecting and resolving deadlocks_•_401_|
|Building coordination guardrails • 403|
|**Designing for resilience and recoverability**<br>**........................................................**<br>**404**|
|Redundancy and failover mechanisms • 404|
|Graceful degradation strategies • 405|
|Retry logic and circuit breakers • 407|
|Checkpointing and state recovery • 409|
|Human escalation patterns • 410|
|**Summary**<br>**..........................................................................................................**<br>**411**|
|**Chapter 11: Deploying Multi-Agent Systems**<br>**413**|
|**Technical requirements**<br>**.....................................................................................**<br>**414**|
|**Setting up dual KinD clusters for multi-agent deployment**<br>**.................................**<br>**414**|
|Installing KinD and prerequisites • 414|

_Table of Contents_ 

xviii 

Creating the control cluster configuration • 415 Creating the worker cluster configuration • 417 Setting up cluster networking and port forwarding • 419 Verifying cross-cluster connectivity • 420 Deploying a test workload to the worker cluster • 421 **Deploying MAKDO to the control cluster........................................................... 424** Preparing the MAKDO configuration • 424 Creating Kubernetes secrets for API keys • 428 Creating the kubeconfig ConfigMap • 430 Deploying MAKDO as a Kubernetes deployment • 431 Building and loading the MAKDO image • 432 Configuring MAKDO to connect to the worker cluster • 434 Verifying MAKDO deployment and logs • 435 **Deploying k8s-ai to the worker cluster ............................................................. 436** Building the k8s-ai Docker image • 437 Creating k8s-ai deployment manifests • 439 Deploying k8s-ai to the worker cluster • 439 Exposing the k8s-ai service for cross-cluster access • 442 Verifying k8s-ai deployment • 443 _Check pod status_ • _443 Verify pod health_ • _444 Check server logs_ • _444 Test the A2A endpoint_ • _445 Verify service configuration_ • _446_ Testing the k8s-ai Admin API and session management • 446 _Exposing the Admin API port_ • _447 Creating a session_ • _447 Listing active sessions_ • _448 Deleting a session_ • _449 Using sessions with the A2A protocol_ • _450_ 

**Enabling secure communication between clusters ............................................ 450** Service discovery and networking • 450 

_Table of Contents_ 

xix 

_How MAKDO discovers k8s-ai_ • _451 Tracing a request path_ • _451_ Service discovery patterns • 452 _Cross-cluster networking approaches_ • _453 Testing end-to-end connectivity_ • _455_ Understanding the security architecture • 456 API key authentication • 457 _k8s-ai authentication_ • _457 MAKDO configuration_ • _458_ Session-based security • 458 RBAC and least privilege • 460 _Inspecting RBAC configuration_ • _460 Testing permission boundaries_ • _461_ Network segmentation in KinD • 461 _Port mapping security_ • _461 Testing network isolation_ • _462_ Production security enhancements • 463 **Summary ......................................................................................................... 466** **<mark>Chapter 12: Advanced Topics and Future Directions 469</mark> Superhuman reasoning and strategic foresight.................................................. 470** What is superhuman reasoning? • 470 Why is strategic foresight so important? • 471 Challenges and limitations of superhuman reasoning • 472 Implications for society and ethics • 473 **Massive context windows and their implications .............................................. 474** The evolution of context windows • 474 What can you do with million-token context windows? • 475 Challenges and trade-offs of large context windows • 476 Context windows and multi-agent systems • 476 The future – infinite context and continuous learning • 476 Architectures for long-horizon planning • 477 

_Table of Contents_ 

xx 

_The challenge of planning over time_ • _477 Hierarchical planning and abstraction_ • _477 Model-based planning and world models_ • _477_ **Beyond text – multi-modal models and world simulation .................................. 478** Transformers for everything: vision, audio, video, and beyond • 478 _Biological models: proteins, DNA, and molecular design_ • _478 From language models to world models and simulations_ • _479 Multi-modal multi-agent systems_ • _479_ Designing for generative user experience • 479 The robots are coming • 480 _The convergence of AI and robotics_ • _480 Embodied AI agents_ • _480 Humanoid robots and general-purpose physical intelligence_ • _480 Multi-agent and multi-robot coordination in physical spaces_ • _481 Challenges in real-world deployment_ • _481_ The AI economy • 481 _Cryptocurrencies and AI agents as economic actors_ • _481 Payment protocols for autonomous agents: AP2 and beyond_ • _482 Robots accelerate the AI self-improvement loop_ • _482 Conquering space – the final frontier_ • _483_ **Summary ......................................................................................................... 484** 

|**Chapter 13: Unlock Your Exclusive Benefits**|**487**|
|---|---|
|**Unlock this Book’s Free Benefits in 3 Easy Steps**<br>**........................**|**.........................**<br>**488**|
|**Other Books You May Enjoy**|**492**|
|**Index**|**495**|

#### **Preface** 

The rapid evolution of large language models has shifted artificial intelligence from static, prompt-driven systems to dynamic, agentic architectures capable of reasoning, planning, and acting in the real world. Today’s most powerful AI applications are no longer single-model pipelines; they are systems of collaborating agents that use tools, manage context, and coordinate with one another to solve complex problems. Building such systems requires going far beyond surface-level framework usage. It demands a deep understanding of how agentic AI actually works. 

Rather than treating agent frameworks as black boxes, this book takes a ground-up, hands-on approach. You will explore what happens behind the curtain of modern agentic systems by building a flexible and extensible multi-agent framework in Python from first principles. Core concepts such as tool use, secure execution, context management through the **Model Context Protocol** ( **MCP** ), and agent collaboration via **Agent-to-Agent** ( **A2A** ) messaging are broken down into concrete implementations and reusable design patterns. This foundational understanding will enable you not only to build your own frameworks but also to reason about, customize, and troubleshoot agentic systems built with existing tools. 

The journey through the book is intentionally practical and progressive. You will begin by constructing a simple tool-using agent, then incrementally enhance its capabilities—adding secure tool execution, persistent and structured context handling, collaborative planning, and memory. As the book progresses, these individual components come together into fully autonomous, multi-agent systems capable of coordinating actions and solving complex tasks through structured communication and shared context. 

Complete with step-by-step walk-throughs, annotated Python code, and deep dives into realworld agent workflows, this book bridges theory and practice. By the end, you will be able to design and implement your own agentic AI systems, build custom tools for intelligent agents, integrate protocols such as MCP and A2A, and deploy collaborative AI workflows that reason, plan, and act effectively in real-world environments. Armed with these skills, you will be well prepared to build the next generation of intelligent, adaptive AI applications. 

_Preface_ 

xxii 

The book is structured into three parts: 

- _Part 1_ , _Foundations of Agentic AI_ , lays the foundation for agentic AI. It traces the evolution of generative AI, defines what an AI agent is, and distinguishes agents from chatbots. You’ll learn about core agent architecture and components, including the agent loop (sense–think–act), memory and context management, planning and reasoning, tool use, and evaluation. The part concludes with a hands-on walk-through of a simple Kubernetes-focused agent, showing how tool calling works end-to-end and how a minimal code base can deliver real autonomy. 

- _Part 2_ , _Building Your Own Agentic AI Framework_ , walks you through building a real agentic AI framework (AI-6) from the ground up. You’ll explore the core engine that runs the agent loop, manages memory, sessions, tools, and multiple LLM providers, then dive into designing robust, provider-agnostic tools with schemas, validation, and execution flow. The part then shifts to user-facing interfaces, showing how to build Slack and web UIs that support visibility, control, and human-in-the-loop workflows. It closes by integrating the framework with the **Model Context Protocol** ( **MCP** ), enabling standardized tool discovery and interoperability across the broader ecosystem. 

- _Part 3_ , _Constructing Multi-Agent Systems_ , takes you into multi-agent systems at full scale: designing agent teams, orchestration patterns, role prompts, tool scoping, and context strategies, then implementing real multi-agent workflows with the **Agent-toAgent** ( **A2A** ) protocol. You’ll build a practical multi-agent DevOps system (MAKDO), learn how to test and debug agent coordination failures, and apply resilience patterns such as redundancy, graceful degradation, and human escalation. The part then moves into production deployment, walking through a realistic multi-cluster setup with secure communication and service discovery. It concludes with advanced topics and future directions, including massive context windows, long-horizon planning, multimodal systems, and the broader implications of increasingly capable agents. 

###### **Who this book is for** 

The target audience for this book encompasses AI engineers, machine learning practitioners, and software architects interested in building sophisticated, real-world agentic AI systems. It’s especially valuable for those working with LLMs in production, developing tool-using agents, or exploring multi-agent orchestration. DevOps engineers, AI product managers, and researchers experimenting with advanced LLM frameworks will also benefit from this book. 

_Preface_ 

xxiii 

###### **What this book covers** 

_Chapter 1_ , _Introduction to Generative AI and AI Agents_ , sets the stage for the rest of the book by introducing the foundational concepts behind generative AI and agentic systems. It covers the current landscape of generative models, including **large language models** ( **LLMs** ), and explains why AI agents represent a compelling next step in leveraging these models for realworld applications. You will come away with a clear understanding of the distinction between simple LLM use and full-fledged agentic behavior, along with historical context and emerging patterns. 

_Chapter 2_ , _Understanding How AI Agents Work_ , dives into the core mechanics of AI agents: how they perceive, plan, and act. It introduces the fundamental loop that governs agent behavior (from perception to reasoning to action) and explains the infrastructure behind it. You will understand the internal architecture of AI agents and what makes them effective in solving complex problems. 

_Chapter 3_ , _A Hands-On Walk-Through of a Simple AI Agent_ , guides you through building a basic tool-using AI agent that interacts with a live Kubernetes cluster. The agent leverages OpenAI's tool calling capabilities to accept natural language input, interpret intent, execute corresponding kubectl commands, and return results. This real-world walk-through demystifies tool integration and message handling within an agentic AI framework. 

_Chapter 4_ , _Building a Tool-Based Agentic AI Framework_ , introduces the foundational concepts and implementation strategy for building an AI agent framework that supports dynamic tool use. You will learn how to construct a robust architecture where an agent can decide when and how to invoke external tools (e.g., APIs, shell commands, command-line tools) to enhance its capabilities. The focus is on building a minimal yet functional core framework that can be extended with more complex behavior later. 

_Chapter 5_ , _Implementing Custom Tools_ , explores the design and implementation of custom tools, enabling agents to take real actions, retrieve structured data, and interact with external systems. You will learn how to define tool interfaces, handle argument schemas, return structured results, and ensure safe and reliable execution. The chapter emphasizes the role of tools in extending an agent’s capabilities beyond simple text generation. 

_Chapter 6_ , _Creating Chat Interfaces Using Slack and Chainlit_ , demonstrates how to create engaging chat interfaces for interacting with your AI agents. You'll learn how to build integrations with Slack to bring your agents into the workplace and how to use Chainlit to create web-based UIs. These interfaces are key to making your AI agents accessible, interactive, and useful in real-world scenarios. 

_Preface_ 

xxiv 

_Chapter 7_ , _Integrating with the Model Context Protocol Ecosystem_ , introduces the **Model Context Protocol** ( **MCP** ) and its role in enhancing context awareness, interoperability, and modularity in agentic AI systems. You will learn the principles behind MCP, how to build MCP servers and clients, and how to leverage MCP-compatible components to extend agent capabilities across different execution environments. The chapter also shows how to use MCP as the backbone of the tool-calling agentic loop. 

_Chapter 8_ , _Designing Multi-Agent Systems_ , explores how multiple AI agents can work together toward a shared goal using **Agent-to-Agent** ( **A2A** ) communication. You will learn about the patterns and architectures for multi-agent orchestration, including broadcasting, delegation, and consensus. The chapter will cover real-world use cases, challenges in coordination and conflict resolution, and provide best practices for designing scalable, resilient collaborative agentic systems. 

_Chapter 9_ , _Implementing Multi-Agent Systems with A2A_ , presents the implementation of a fullfledged multi-agent system that brings together all the core ideas from earlier chapters. We’ll build an AI-powered DevOps team composed of specialized agents that communicate via the A2A protocol and utilize MCP for powerful tool-using capabilities. The team includes a Kubernetes expert agent, a CI/CD expert agent, a security specialist agent, and a DevOps manager agent who oversees coordination and interacts with human engineers. This project showcases how multiple agents collaborate to solve real-world problems in a complex, distributed environment. 

_Chapter 10_ , _Testing, Debugging, and Troubleshooting Multi-Agent Systems_ , equips you with practical debugging strategies for identifying issues in tool execution, message routing, context sharing, and multi-agent coordination. It covers logging, tracing, observability hooks, and diagnostics tailored for autonomous agents operating in dynamic environments. 

_Chapter 11_ , _Deploying Multi-Agent Systems_ , focuses on deploying our multi-agent DevOps system across two separate **Kubernetes-in-Docker** ( **KinD** ) clusters to simulate a distributed, production-like environment. We’ll run the manager agent on one cluster and deploy the rest of the specialized agents – Kubernetes, CI/CD, and Security – on the other. This setup models a realistic architecture where the control plane (manager) is decoupled from the worker agents for scalability, isolation, and operational resilience. We’ll cover configuration, service exposure, inter-cluster communication, and common pitfalls when deploying agent-based systems in Kubernetes environments. 

_Preface_ 

xxv 

_Chapter 12_ , _Advanced Topics and Future Directions_ , surveys the frontier of agentic AI capabilities, from superhuman reasoning and large-context comprehension to long-horizon planning and emergent autonomous behaviors. You will gain perspective on how breakthroughs such as 1M+ token context windows and generative memory architectures unlock new patterns of interaction, enable strategic foresight, and hint at agents that reason beyond human capabilities. We also introduce the concept of **Generative User Experience** ( **GenUX** ) as the next evolution in human-agent interface design. 

###### **To get the most out of this book** 

You should have a basic understanding of Python programming, familiarity with machine learning concepts, and a basic understanding of large language models. 

|**Software/hardware covered in the book**|**Operating system requirements**|
|---|---|
|Python 3.x|Windows, macOS, or Linux|
|OpenAI API key|Windows, macOS, or Linux|

You will need access to a Python development environment. An OpenAI API key is required for many of the examples. A machine with at least 8 GB of RAM is recommended for running the more complex examples. 

If you are using the digital version of this book, we advise you to type the code yourself or access the code from the book’s GitHub repository (a link is available in the next section). Doing so will help you avoid any potential errors related to the copying and pasting of code. 

###### **Download the example code files** 

The code bundle for the book is hosted on GitHub at `https://github.com/PacktPublishing/ Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A` . We also have other code bundles from our rich catalog of books and videos available at `https://github.com/PacktPublishing` . Check them out! 

###### **Disclaimer on images** 

Some images in this title are presented for contextual purposes, and the readability of the graphic is not crucial to the discussion. Please refer to our free graphic bundle to download the images. 

_Preface_ 

xxvi 

###### **Download the color images** 

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. You can download it here `https://packt.link/gbp/9781806116478` . 

###### **Conventions used** 

There are a number of text conventions used throughout this book. 

`CodeInText` : Indicates code words in text, database table names, folder names, filenames, file extensions, pathnames, dummy URLs, user input, and Twitter handles. Here is an example: “ `tool_config` and `provider_config` are mappings that allow you to specify additional configuration for each tool and provider." 

A block of code is set as follows: 

```
    response = client.chat.completions.create(
        model=model_name, messages=messages,
        tools=tools, tool_choice="auto")
```

**Bold** : Indicates a new term, an important word, or words that you see on the screen. For instance, words in menus or dialog boxes appear in bold. For example: "We have two deployments: **some-app** and **nginx** . The **some-app** deployment has three pending Pods, and the **nginx** deployment has one Pod in an error state due to an invalid image name.” 

**Note** 

Warnings or important notes appear like this. 

**Tip** 

Tips and tricks appear like this. 

_Preface_ 

xxvii 

###### **Get in touch** 

Feedback from our readers is always welcome! 

**General feedback** : Email `feedback@packtpub.com` and mention the book's title in the subject of your message. If you have questions about any aspect of this book, please email us at `questions@packtpub.com` . 

**Errata** : Although we have taken every care to ensure the accuracy of our content, mistakes do happen. If you have found a mistake in this book, we would be grateful if you reported this to us. Please visit `http://www.packtpub.com/submit-errata` , click **Submit Errata** , and fill in the form. 

**Piracy** : If you come across any illegal copies of our works in any form on the internet, we would be grateful if you would provide us with the location address or website name. Please contact us at `copyright@packtpub.com` with a link to the material. 

**If you are interested in becoming an author** : If there is a topic that you have expertise in and you are interested in either writing or contributing to a book, please visit `http:// authors.packtpub.com/` . 

_Preface_ 

xxviii 

###### **Free benefits with your book** 

This book comes with free benefits to support your learning. Activate them now for instant access (see the _How to unlock_ section for instructions). 

Here’s a quick overview of what you can instantly unlock with your purchase: 

<!-- Start of picture text -->
.<br>~ eo =<br>ce)<br><!-- End of picture text -->

_Preface_ 

xxix 

###### **How to Unlock** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
Okt aC]<br>*<br>4<br>|<br>e<br>ae<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require one._ 

_Preface_ 

xxx 

###### **Share your thoughts** 

Once you have read _Design Multi-Agent AI Systems Using MCP and A2A_ , we would love to hear your thoughts! Scan the QR code below to go straight to the Amazon review page for this book and share your feedback. 

<!-- Start of picture text -->
Oba AO<br>capac<br>[al fer<br><!-- End of picture text -->

Your review is important to the tech community and us, and it will help us make sure we’re delivering excellent quality content. 

###### **Join our Discord and Reddit Space** 

You’re not the only one navigating fragmented tools, constant updates, and unclear best practices. Join a growing community of professionals exchanging insights that don’t make it into documentation. 

Join our Discord at `https://packt.link/ z8ivB` or scan the QR code below: 

<!-- Start of picture text -->
OF ao<br><!-- End of picture text -->

Follow us on Reddit at `https:// packt.link/0rExL` or scan the QR code below: 

<!-- Start of picture text -->
Oka<br><!-- End of picture text -->

## Part 1 

### Foundations of Agentic AI 

_Part 1_ lays the foundation for agentic AI. It traces the evolution of generative AI, defines what an AI agent is, and distinguishes agents from chatbots. You’ll learn core agent architecture and components, including the agent loop (sense–think–act), memory and context management, planning and reasoning, tool use, and evaluation. The part concludes with a hands-on walkthrough of a simple Kubernetes-focused agent, showing how tool calling works end-toend and how a minimal codebase can deliver real autonomy. 

This part contains the following chapters: 

- _Chapter 1, Introduction to Generative AI and AI Agents_ 

- 

- _Chapter 2, Understanding How AI Agents Work_ 

- 

- _Chapter 3, A Hands-On Walk-Through of a Simple AI Agent_ 

- 

# 1 Introduction to Generative AI and AI Agents 

AI agents representidx_e496bf2c a significant evolution in how we build and interact with intelligent systems. Unlike static models or chatbots, agents can reason, use tools, remember past interactions, and act autonomously within defined boundaries. AI agents are built on top ofidx_3870b29f the **generative AI** ( **GenAI** ) technology and allow building systems that are adaptive, purposeful, and effective in dynamic environments. 

This book is a comprehensive exploration of the evolution, architecture, and practical implementation idx_32b384feof agentic AI systems. What makes this book unique is that you will build a full-fledged agentic AI framework from idx_f1496e2cscratch. The AI-6 framework supports idx_03d3f7b2the development of sophisticated autonomous agents capableidx_7809c93d of complex reasoning, tool use, and multi-step task execution. Spanning 12 chapters, the book covers everything from foundational concepts and single-agent architectures to advanced multi-agent systems, testing methodologies, deployment strategies, and integration with emerging technologies such as idx_bca4b4f6the **Model Context Protocol** ( **MCP** ) and idx_014aae18the **Agent2Agent (A2A) Protocol** . The book provides both theoretical understanding and hands-on implementation guidance, making it valuable for developers, researchers, and practitioners looking to build real-world AI agent systems. 

This chapter establishes that AI agents differ fundamentally from chatbots through five key characteristics: autonomy, perception, reasoning and planning, action capability, and learning and adaptation – transforming AI from reactive responders to proactive problem-solvers. The chapter traces AI's evolution from symbolic reasoning (1950s) through expert systems (1980s), machine learning (1990s), and deep learning (2006+), to today's transformer-based agents, showing idx_6ba33107how each era's limitations drove the next breakthrough. 

_Chapter 1_ 

4 

Four architectural patterns emerge for agentic systems – single-agent loops, planner-executor models, multi-agent collaboration, and graph-based workflows – each supported by three critical components: memory, tools, and orchestration. 

In this chapter, we will explore the foundational concepts of GenAI and AI agents. We will define what an AI agent is, how it differs from traditional chatbots, and discuss various use cases for agentic AI. We will also delve into the architecture of agentic systems. 

In this chapter, we will cover the following main topics: 

- The evolution of generative AI 

- 

- Introducing AI agents 

- 

- Understanding the architecture of AI agents 

- 

###### **Free benefits with your book** 

Your purchase includes a free PDF copy of this book along with other exclusive benefits. Check the _Free Benefits with Your Book_ section in the Preface to unlock them instantly and maximize your learning experience. 

###### **The evolution of generative AI** 

**Artificial intelligence** ( **AI** ) has been aidx_bfa3cc14 dream of computer scientists and futurists for decades. As early as the 1940s, when digital computers were first developed, researchers idx_a5e30300began to explore the potential of machines to simulate human thought and behavior. Over the years, AI has evolved through various stages and cycles of hope and despair. Along the way, there was always an interesting tension between brain-inspired approaches and logic-based approaches. For idx_59ffd225 example, the perceptron, an early neural network model, was i **d** x_4391bc3a eveloped in the 1950s by Frank Rosenblatt and is the ancestor of modern neural networks. Initially, there were high hopes for perceptron-based systems, as it could solve problems where a single linear decision boundary separates classes. This includes basic tasks such as distinguishing the following: 

- Vertical versus horizontal lines 

- 

- Light versus dark patterns 

- 

- Some handwritten characters under controlled conditions 

- 

These seemed impressive in the 1950s and 1960s, when the idea of a machine learning from data at all was novel. However, the model was very limited, the industry became disillusioned with this approach, and neural network research remained dormant for several decades. 

_Introduction to Generative AI and AI Agents_ 

5 

###### **The early days of symbolic AI** 

The idx_a4d5ea **c** d omputer idx_53df0db8science pioneers of the 1950s and 60s laid the groundwork for AI with symbolic reasoning ( `https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence` ) and early neural networks. Some examples of symbolic AI include Alan Turing’s work on the Turing Test ( `https://en.wikipedia.org/wiki/Turing_test` ) and John McCarthy’s development of LISP ( `https://en.wikipedia.org/wiki/Lisp_(programming_language)` ) as a programming language for AI. 

**Symbolic reasoning** refersidx_867655e4 to the broad set of techniques in AI that rely on high-level, humanreadable representations of problems, logic, and search. It employs tools such as logic programming, production rules, semantic networks, and frames to model and solve problems through structured symbolic manipulation. 

During this period, several ambitious and interesting systems were idx_49782294built, such as **SHRDLU** , a natural language understanding program that lets users interact with a virtual world of blocks. Take a look at this human and SHRDLU natural language conversation: 

```
Person: Pick up a big red block.
Computer: OK.
Person: Grasp the pyramid.
Computer: I DON'T UNDERSTAND WHICH PYRAMID YOU MEAN.
Person (changing their mind): Find a block which is taller than the one you are
holding and put it into the box.
Computer: BY "IT", I ASSUME YOU MEAN THE BLOCK WHICH IS TALLER THAN THE ONE I AM
HOLDING.
Computer: OK.
Person: What does the box contain?
Computer: THE BLUE PYRAMID AND THE BLUE BLOCK.
Person: What is the pyramid supported by?
Computer: THE BOX.
```

This is very impressive for a system built in the 1970s, but it was limited to a specific domain and required extensive hand-crafted knowledge. 

**Perceptrons** also idx_01206821gained traction during this period. To compare the idx_2eb4b14etwo, symbolic AI relies on explicit, human-readable rules and logical reasoning to solve problems, making it highly interpretable but often rigid and manually intensive. Another major drawback is that the combinatorial explosion of rules in real-world scenarios quickly becomes unmanageable. 

_Chapter 1_ 

6 

On the other hand, early neural network models such as the perceptron learned from data by adjusting numeric weights, enabling them to generalize from examples but offering little transparency into their decision-making. In general, symbolic AI excels at structured, rulebased tasks, and perceptrons are better suited for pattern recognition in noisy or ambiguous environments. 

But this wave did not last long. This period ended with the first **AI winter** when funding and interest in AI waned due to the failure to deliver on the ambitious promises of the early systems. There were several reasons for these early failures. The most prominent ones were that the techniques weren’t sophisticated enough to deal with the complexity of real-world problems, the available compute resources were insufficient, and the lack of training data. 

Then came the expert systems era. 

###### **The expert systems era** 

In idx_4df732ddthe 1980s, expert systems came to the fore. Theidx_4467979a idea was to encode human expertise into rules that could be executed by a software program. Expert systems such as MYCIN ( `https:// en.wikipedia.org/wiki/Mycin` ) for medical diagnosis and DENDRAL ( `https:// en.wikipedia.org/wiki/Dendral` ) for chemical analysis were developed, but they were limited by the need for extensive domain knowledge and the difficulty of capturing the complexity of human reasoning in rules. Here is an example rule from MYCIN: 

```
IF
theinfectionisprimary-bacteremia
ANDthesiteofcultureisoneofthesterilesites
ANDthesuspectedportalofentryisthegastrointestinaltract
THEN
thereissuggestiveevidence(0.7)thattheorganismisBacteroides.
```

This rule-based approach allowed for some level of automation in decision-making and had some success. Unfortunately, overall, expert systems were brittle and difficult to maintain, leading to another AI winter in the late 1980s. This brittleness stemmed from several core limitations: the number of rules required to handle real-world complexity quickly became unmanageable, and as domains evolved, rules had to be constantly updated, leading to maintenance challenges. Moreover, it was often impossible to define explicit rules for every possible scenario, particularly when dealing with ambiguous or uncertain situations. These factors made expert systems inflexible and ultimately unsustainable at scale. 

The next significant milestone was the machine learning era. 

_Introduction to Generative AI and AI Agents_ 

7 

###### **The rise of machine learning and statistical methods** 

The idx_195bea6amodern era of AI began in the 1990s with theidx_6328319d rise of **machine learning (ML)** and statistical methods. Methods such idx_c814 **a** 072 s **Support Vector Machines** ( **SVM** ), decision trees, random forests, and logistic regression allowed processing of large datasets and learning. There wasn’t a lot of hype around this time, but the groundwork was laid for the next wave of AI advancements. The focus shifted from hand-crafted rules to data-driven approaches, enabling systems to learn patterns and make predictions based on examples rather than explicit programming. Instead of tellingidx_1dde501a the computer how to think, we just threw a bunch of data at it and let it figure it all out. The phrase _data is the new oil_ was coined at this time. But, while these methods were effective for many tasks, they required a lot of patient work around feature engineering and still struggled with complex reasoning and understanding. Following this was the popularity of deep learning networks. 

###### **Deep learning and the neural network renaissance** 

Researchidx_76e6d234 breakthroughs in layered neural networks, GPU acceleration, andidx_dff69f66 even larger datasets unlocked new capabilities in vision, speech, and text. The term **deep learning** was idx_beff0651coined in 2006 to describe this new approach. I was part of this wave, working on brain-inspired machine learning at Numenta ( `https://www.numenta.com/` ) in the mid-2000s. 

The rise of social media with the likes of YouTube, Facebook, and Twitter, and the cost of storage and compute dropping dramatically, led to an explosion of data. Researchers finally had access to the scale of data and hardware needed to train deep nets effectively. 

Innovations idx_5af9ae28such as AlexNet ( `https://en.wikipedia.org/wiki/AlexNet` ) in 2012, Word2Vec ( `https://en.wikipedia.org/wiki/Word2vec` ) in 2013, and DeepSpeech ( `https://arxiv.org/ abs/1412.5567` ) in 2014 redefinedidx_946142fa the capabilities of AI in fields such as imageidx_19c49f21 recognition, natural language processing, and speech recognition. The Turing test wasn’t definitively conquered yet, but we were getting close. 

The explosion of internet usage and digital storage in the late 1990s and early 2000s created unprecedented opportunities to collect and process massive datasets that would fuel the next generation of AI breakthroughs. The creation of ImageNet in 2009, containing over 14 million hand-labeled images across 20,000+ categories, exemplified how large-scale, meticulously curated datasets became essential infrastructure for training robust models. ImageNet's annual competition catalyzed breakthrough architectures such as AlexNet in 2012, proving that deep neural networks could achieve unprecedented accuracy when given sufficient highquality training data. This dataset-centric approach established a new paradigm where model performance scaled predictably with data volume and quality, leading organizations to prioritize data collection and curation as core competitive advantages. 

_Chapter 1_ 

8 

Funnily enough, one of the most notable AI successes of the time was IBM’s Deep Blue beating Gary Kasparov in chess, utilizing raw compute power while using old-fashioned symbolic AI and hand-crafted code techniques. The Netflix recommendation system, which used collaborative filtering to suggest movies based on users’ preferences, was representative of this era. 

Then we moved into the times we are living in now. 

###### **The emergence of generative models, transformers, and language models** 

In 2014, **Generative Adversarial Networks** ( **GANs** ) ( `https://en.wikipedia.org/wiki/ Generative_adversarial_network` ) were introduced and idx_e15b2733allowed the idx_80db5214generation of images, videos, and music from scratch. But the biggest breakthrough came in 2017, with the introduction of the Transformer architecture in the seminal paper “Attention is All You Need”: `https://arxiv.org/pdf/1706.03762` . Transformers revolutionized idx_6566b2bethe field by using selfattention mechanisms coupled with feed-forward only networks. That allowed parallel training, which was orders of magnitude more efficient than the previous state of the art idx_51753321with **recurrent neural networks** ( **RNNs** ). The Transformer architecture became the foundation for many subsequent models, including Google’s BERT, OpenAI’s GPT-2, and later GPT-3. The success can also be attributed to theidx_54380459 emergence of massive datasets such as Common Crawl ( `https://commoncrawl.org/` ) and idx_ca049aa6the Pile ( `https://arxiv.org/abs/2101.00027` ), enabling the training of increasingly capable language models. 

But it wasn’t until the end of 2022 that the real magic happened with the release of OpenAI’s ChatGPT, based on GPT-3.5. Suddenly, AI jumped to the mainstream, and the world was captivated by the capabilities of these large language models. The discovery that **Reinforcement Learning from Human Feedback** ( **RLHF** ) couldidx_9ce04d39 be used to fine-tune these models for better alignment with humans was a game-changer. Other companies quickly followed suit, releasing their own models, such as Google’s Bard and Meta’s Llama. On the image generation side, models such as DALL-E, Stable Diffusion, and Midjourney showed that the transformer architecture could also be used for generating high-quality images from text prompts. 

_Introduction to Generative AI and AI Agents_ 

9 

###### **Note** 

- OpenAI researchers described RLHF back in 2017: `https://openai.com/ index/learning-from-human-preferences/` 

- You can also read about RLHF here: `https://en.wikipedia.org/wiki/ Reinforcement_learning_from_human_feedback` 

Suddenly, AI wasn’t just talking but painting too. The world was buzzing with excitement, and the possibilities seemed endless. It also shattered the worldview of many people when it became evident that AI could compete in the area of creative expression, which was often considered the exclusive domain of humans. 

###### **The rise of AI agents** 

At idx_210bb8c5the beginning of March 2023, OpenAI released GPT-4, a more capable and steerable successor to GPT-3.5. GPT-4 handled longer contexts, hadidx_2277c2ea improved reasoning, and showed early signs of multi-modal fluency as it was capable of idx_9cb337baunderstanding idx_6d7788b9 text, images, and idx_f1d0f915speech. OpenAI, Anthropic, Google, Meta, Mistral, and Chinese companies such asidx_46855b89 DeepSeek idx_4057eb3cand AliBaba kept idx_e143c08areleasing idx_0f29ad **b** 5 etter and better models. Benchmark after benchmark fell to the unstoppable march of innovation. 

Models such as Anthropic’s Claude pushed the envelope of LLMs in the realm of coding, and recent models introduced a long reasoning mode, where a model can spend more time and resources to complete complicated tasks. 

At the same time, the frontier shifted toward agentic AI: models that don’t just respond, but plan, reason, use tools, and act. The OpenAI API function-calling capability, replicated by other LLM providers such as Google with its Gemini models and Anthropic with its Claude models, explored how LLMs could become the backbone of multi-step workflows, coding assistants, web agents, and real-world automation. 

Multiple idx_e3 **a** 7dc27 genticidx_fcd0ab53 AI frameworks emerged, such idx_1ec902e1as LangChain, AutoGPT, AutoGen, andidx_b2af09d4 BabyAGI. These frameworks allow developers to build complex LLM-based systems. These systems bring us full circle: not just chatbots, but autonomous collaborators that can reason about tasks, use external APIs, and adapt on the fly. But what is an AI agent? 

_Chapter 1_ 

10 

###### **Introducing AI agents** 

Thisidx_189021a4 question _What is an AI agent?_ is at the heart of this book. In this section, we will explore the common definition of an AI agent, its characteristics, and the different types of AI agents. In the next chapter, _Understanding How AI Agents Work_ , we will go much deeper and explore in detail how AI agents are structured and their various components and capabilities. 

If you ask ChatGPT what an AI agent is, it will tell you something along these lines: 

_An AI agent is a system that can perceive its environment, reason about its goals, and take actions to achieve those goals, often autonomously or interactively._ 

This is a pretty intuitive definition that aligns well with the common understanding of what an intelligent agent is. Let’s consider the characteristics of such an AI agent. 

###### **AI agent characteristics** 

In order idx_d95eb1a7 to function according to the preceding definition, an AI agent must have the following characteristics: 

- **Autonomy** : The agent must be able to operate on its own and perform multiple steps to achieve its goal without human intervention in each and every step. Note that it doesn’t mean that the agent is completely autonomous. It can still be supervised by a human, especially when it comes to taking potentially risky actions. We will see some examples later. The agent can operate independently, making decisions and taking actions without human intervention. 

###### **Note** 

If the agent performs well enough or if the consequences of its actions are not critical, it may operate completely autonomously without any human supervision. 

_Introduction to Generative AI and AI Agents_ 

11 

- **Perception** : An AI agent must be able to perceive its environment, either physical, digital, or both. This perception can come in the form of structured inputs such as API responses or unstructured data such as natural language, audio, or visual signals. The agent uses this information to assess its current state, context, and relevant changes. It informs the agent’s subsequent actions and decisions and provides feedback on previous actions. Assembling the inputs into a usable internal representation is an enormous technical challenge. Consider just raw web data, which comes in countless formats, resolutions, and quality levels, requiring sophisticated pipelines to parse, validate, and standardize these diverse inputs into consistent internal representations suitable for reasoning. 

- **Reasoning and planning** : Once an agent perceives the environment, it must reason about the new information and make decisions about its next action. This involves identifying goals, evaluating possible actions, and formulating or updating a plan. Modern AI agents may use symbolic planning, reinforcement learning, or neural network-based methods to carry out this process. Planning enables agents to look ahead and choose sequences of actions rather than just reacting to immediate stimuli. 

- **Action** : The core function of an AI agent is to take actions in the environment. These actions could include invoking a tool or API, generating a response, triggering a workflow, or even controlling a device. The agent must be capable of executing these actions in a way that aligns with its goals and adapts to the feedback it receives from the environment. In order to be effective, the agent must have the proper access and permission to perform the actions that are required to achieve its goals. 

- **Learning and adaptation** : An advanced AI agent should be able to learn from experience. This might include updating internal memory, adjusting strategies, or refining its behavior over time. Some agents learn offline (through training data), while others learn online (from real-time interactions). Adaptive behavior is critical for agents operating in dynamic, unpredictable environments. 

AI agents combine idx_73602c23autonomy, perception, reasoning, action, and learning to operate effectively in dynamic environments. They can make informed decisions and adapt over time. These capabilities have started to drive real-world applications across industries, enhancing efficiency and enabling more intelligent systems. 

But how are they different from chat interfaces such as ChatGPT, Claude Desktop, and Gemini that we have started to use daily? Let’s find out. 

_Chapter 1_ 

12 

###### **Key differences: chatbots versus agents** 

**Chatbots** and AI agents idx_052 **a** c38e re often used interchangeably, but they have i **d** x_3860cf28 istinct characteristics. **LLM-based chatbots** allow users to interact with LLM through naturalidx_22942480 language. The interaction is typically limited to a single query that may include an image or through a voice interface. 

Here is the typical chatbot interaction workflow: 

<!-- Start of picture text -->
—_><br>=| chatbot<br>&<br>User<br><!-- End of picture text -->

_Figure 1.1: LLM-based chatbot and user interaction_ 

The LLM will i **d** x_a29982e4 igest the user’s input query and generate a response. The user can’tidx_c64ddde5 control directly what the model does except through prompt engineering. In particular, the user can’t provide the model access to external data sources and APIs (although uploading files is possible). 

But an AI agent interaction workflow is more complex. Based on the user input and reasoning and planning mechanisms, an AI agent can autonomously execute tasks and even run complete workflows. 

Here is an illustration idx_044dfb49of an AI agent workflow. 

<!-- Start of picture text -->
(a ,<br>Th At<br>i A abot —_ LLM<br>Ty<br>i i PLANNING<br>SS<br><!-- End of picture text -->

_Figure 1.2: AI agent workflow_ 

_Introduction to Generative AI and AI Agents_ 

13 

Let’s summarize the key differences in a idx_cb71c833table: 

|**Feature**|**Chatbots**|**AI Agents**|
|---|---|---|
|Purpose|Primarily for conversation<br>and information|Autonomous task execution<br>and decision-making|
|Interaction|Primarily text-based, often<br>limited to FAQs|Multi-modal, can use tools<br>and APIs|
|Autonomy|Limited, often requires<br>human input|High autonomy, can operate<br>independently|
|Context Awareness|Limited context retention|Can maintain and utilize<br>long-term context|
|Learning|Static, based on pre-trained<br>parameters|Dynamic, can learn and<br>adapt over time|

_Table 1.1: Key differences between chatbots and AI agents_ 

Agentic AI systems find several use cases in the GenAI era. You may have encountered some of the agents, too! Let’s look at some examples of AI agents in action. 

###### **Use cases for agentic AI** 

AI agents can be idx_f3188fc9applied in a wide range of domains and use cases. What is fascinating is that some of the most successful applications are in domains that were previously thought to be too complex or nuanced for AI. But, as we progress towards more capable AI agents, we are seeing breakthroughs in areas such as software development, customer support, research, and even empathic user interaction. 

- Here are some examples of how AI agents are being used effectively today: 

   - **Autonomous coding assistants** : Software engineering is a complex task that requires a deep understanding of both the problem domain and the technical implementation. AI agents have already reached a level where they can explore large code bases, be assigned GitHub or Jira issues, and autonomously fix problems, perform massive refactorings, write and run tests, and ensure the changes are valid. The current generation of AI coding agents still can’t totally replace a high-level human engineer, but they can significantly augment the productivity of software teams. I consider the current crop of coding AI agents as a savant intern. 

_Chapter 1_ 

14 

They can perform some tasks on their own but may get lost in a large code base and require some steering and hand-holding. Some examples of AI coding agents are Devin.ai ( `https://devin.ai/` ), Claude Code ( `https://www.anthropic.com/claudecode` ), OpenAI’s codex CLI ( `https://github.com/openai/codex` ), Google’s Jules ( `https://jules.google/` ), and the open source OpenHands ( `https://github.com/ All-Hands-AI/OpenHands/` ). 

• **Automated customer support** : Customer support was always considered a prime target for automation. Customer support bots have been around for more than 20 years. But they were always very limited in their capabilities, and users largely opted to escalate to a human. AI agents are now transforming customer service by replacing static chatbots with dynamic assistants capable of multi-turn dialogue, tool use, and real-time problem resolution. Unlike traditional bots, these agents can authenticate users, pull data from CRMs, and even escalate or resolve tickets. Intercom’s Fin ( `https://fin.ai/` ) is a good example – it’s a support agent that can answer complex queries based on your company’s documentation. Similarly, Ada ( `https:// www.ada.cx/` ) and Forethought ( `https://forethought.ai/` ) use AI agents to handle tier-1 and tier-2 support tasks across messaging channels, reducing load on human agents. These systems integrate with helpdesk platforms such as Zendesk and Salesforce, providing end-to-end ticket resolution without needing custom scripts. 

• **Research agents** : Research is another domain where AI agents are making a significant impact. The rate of knowledge accumulation is growing significantly. Unfortunately, not all of it is high-quality. AI agents can help researchers sift through vast amounts of research papers, correlate and find connections between them, and even generate new hypotheses. All the major LLM providers now offer research modes for the top-level models where the foundation model itself autonomously performs complex research projects that involve generating searchidx_5ae871ae queries, performing web searches, analyzing the results, and synthesizing the findings into a coherent report. The report is also grounded with source reference links. Here are some of the current (May 2025) leading thinking models: OpenAI o3, o4-mini, Anthropic Claude 4 Opus, Google Gemini 2.5 Pro, and xAI Grok 3 Think. But research agents can do more than just access reasoning models. They can also use tools and provide access to private data stores that are unavailable to foundation models. There are also several scientific research initiatives that utilize AI agents, such as Elicit ( `https://elicit.org/` ), Google’s Co-Scientist ( `https://research.google/blog/accelerating-scientific-breakthroughs-withan-ai-co-scientist/` ), and Microsoft’s Discovery platform ( `https://` 

_Introduction to Generative AI and AI Agents_ 

15 

`azure.microsoft.com/en-us/blog/transforming-rd-with-agentic-aiintroducing-microsoft-discovery/` ). 

• **Personal productivity agents** : Personal productivity is an exciting domain for AI agents. They can help users manage their schedules, prioritize tasks, and draft emails or documents. I believe that in the near future, most people will have a personal AI assistant that will help them manage their digital life and will become better and better as it learns more about the user. This will be especially powerful when using local models that eliminate the resistance to sharing personal data with third-party providers. Some examples include Motion AI strategists ( `https://motionapp.com/aicreative-strategists` ), Reclaim AI ( `https://reclaim.ai/` ), and Superhuman AI ( `https://superhuman.com/ai` ). 

- **AI companions** : AI companions are designed to provide emotional support, conversational interaction, and sometimes even entertainment. They are not just chatbots. They can actually evoke meaningful emotions in the humans they interact with by simulating human-like behavior with fine-tuned personality traits, memory, and multimodal capabilities. 

These agents can play roles ranging from empathetic listeners to motivational coaches or playful friends. They often learn from the user over time and adapt their tone, memory, and behavior accordingly. Some examples of AI companions include Replika ( `https://replika.ai/` ), Pi ( `https://pi.ai/` ), Character.AI ( `https:// character.ai/` ), and Anima ( `https://anima.ai/` ). 

It is now time to understand how AI agents are utilized and organized in practice. 

###### **Introducing the components of agentic AI systems** 

The architecture of agentic AI systems includes several components that work together to enable idx_d060c563 the agents to perceive, reason, and act within their environment. The spectrum of agentic AI systems ranges from highly constrained agents that operate within a specific domain and under tight constraints to fully autonomous agents that can function in the real world with minimal human intervention. 

In general, agentic AI systems are very similar to traditional software systems. They have compute and storage resources, and they can communicate over the network with other systems. The key difference is that in traditional software systems, the logic, decision-making, and responses to events are explicitly programmed by software engineers. In contrast, agentic AI systems delegate some of these high-level cognitive tasks to AI agents. 

_Chapter 1_ 

16 

###### **Common components of agentic AI systems** 

Regardless of the idx_42e6 **c** 11d hosen architecture, any non-trivial agentic AI system will have the following components: 

<!-- Start of picture text -->
Al<br>as a<br><!-- End of picture text -->

_Figure 1.3: Common components of an agentic AI system_ 

1. **Memory** is a idx_f6d238bfcritical component of agentic AI systems. It allows agents to store and retrieve information about their environment, past actions, and learned knowledge. Memory idx_bd88175bcan be short-term (the context for the current session or task) or long-term (for storing knowledge, preferences, and learned behaviors). We will explore different types of memory in _Chapter 2_ , but just to give you a taste, here are the most common types of memory used in agentic AI: 

   - **Working memory** maintainsidx_72590d5d the current context window. This is the immediate, short-term memory used by the system to process and perform its tasks. It includes all the input and output tokens in the current session. 

   - **Episodic memory** tracks idx_51ba76d8recent conversations/events (i.e., the record of prior interactions or significant events), stored across sessions. This allows the system to recall specific exchanges or user behaviors, enabling continuity and personalization over time. 

   - **Semantic memory** is idx_c290d52dthe facts/concepts learned over time. It is a long-term store of structured knowledge such as general world facts, domain-specific information, or conceptual relationships. 

2. **Tools** are external idx_fa4c9081resources or APIs that agents can use to perform actions in the environment. If the LLM is the brain, then tools are the eyes, ears, and limbs of the AI system that allow it to sense and operate on its environment. Without tools, an AI system will only be able to provide advice based on user input and will not have any actual agency in the world. 

3. **Orchestration** is theidx_518b9e77 process of coordinating the various components of an agentic AI system and making them collaborate to accomplish its goals. 

_Introduction to Generative AI and AI Agents_ 

17 

This includes managing the flow of information between agents, tools, and memory, as well as handling interactions with external systems and humans. Orchestration can be done through a central controller or by using decentralized approaches where agents communicate directly with each other. The level of humans in the loop can vary. 

Let’s now take a look at various agentic AI architectures. 

###### **Types of agentic AI architectures** 

There are different architectures that are useful for different scenarios and situations. The choice of architecture depends on the specific use case, the level of autonomy required, and the complexity of the tasks to be performed. Here are some common architectures: 

###### **Single-agent loop** 

A **single-agent loop architecture** consists idx_c3750939of aidx_6c6a211e single AI agent that perceives its environment, reasons about its goals, and takes actions to achieve those goals. This loop typically includes a cycle of observation, planning, and execution, allowing the agent to interact with its environment in a purposeful and adaptive manner. 

<!-- Start of picture text -->
Single-agent Loop<br>i Observe<br>Think \<br><!-- End of picture text -->

_Figure 1.4: A single-agent loop architecture_ 

Reasoning about goals in this context refers to how the agent, typically powered by a **large language model** ( **LLM** ), interpretsidx_94c554f1 its instructions and chooses a course of action. The LLM infers intent from prompts, historical context, and any explicitly stated objectives, then decomposes complex tasks into subtasks or steps that align with the desired outcome. While LLMs don’t _reason_ in a human-like way, they use patterns learned from training data to simulate reasoning, often by predicting what a helpful or goal-directed response would look like in a given context. This allows the agent to appear deliberative and coherent in pursuit of its assigned goals. 

This architecture is suitable for simple tasks where a single agent can handle all the complexity, and the context window (the total amount of tokens available to the LLM in every request) is large enough to accommodate the entire task. The agent can use tools and memory to enhance its capabilities, but it operates independently without the need for coordination with other agents. 

_Chapter 1_ 

18 

###### **Note** 

LLM thinking is best understood as a simulation of human-like reasoning through language. It predicts the next word in a sequence by analyzing patterns in vast text data. It uses probabilities, context, and training to simulate reasoning. It mimics cognitive patterns by leveraging patterns in its training data, but lacks understanding, intentionality, and consciousness. 

Some typical use cases **i** dx_dfe71bf2 nclude the following: 

- **Tool-augmented question answering** : When paired with external tools (e.g., web search, calculators, databases), a single agent can fetch facts, compute results, or retrieve real-time information to respond to user queries more accurately 

- **Monitoring devices** : An agent can monitor devices such as air quality sensors, analyze them over time, and raise an alert if it detects anomalies 

- **Automated code review** : An agent can dynamically watch out for changes in a code repository and provide review comments for changes 

###### **Note** 

Search is not integrated into LLMs in general, but some LLM providers now offer reasoning models that may run an internal agentic loop that can use tools such as web search and file search over external data being uploaded (not training data). 

When the idx_bd5344dfagent observes a change in the environment, such as a thermostat reading, based on its training data, in similar situations, the correct action is to check the current temperature against the set temperature. If this information is not already in the context, this will trigger an action to read the set (desired) temperature. Once the agent has both the current temperature and the set temperature, it will send a message to the model, which, based on its training data, will generate the next action: increase the temperature (if the current temperature is too low), decrease the temperature (if the current temperature is too high), or do nothing (if the current temperature is equal to the set temperature). 

_Introduction to Generative AI and AI Agents_ 

19 

###### **Planner and executors** 

In the **planner and executors architecture** , a **planner AI agent** is idx_86f11b54responsible for reasoning about idx_9878e727the idx_7702742dgoals and formulating a plan that decomposes goals into sub-tasks. These sub-tasks are then delegated to other agentsidx_8f79fe00 called **executor agents** . The planning process involves the steps of the plan being generated by the planner AI agent based on its training data and the prompt. The results of the execution may be sent back idx_c98c73f2to theidx_57f35aa5 planner, which may adjust the plan and launch more executor agents. 

<!-- Start of picture text -->
Planner<br>(LLM + Planning<br>Logic)<br>Task List<br>Results Results<br>Executor 1 Executor 2<br>(LLM + Tools) (LLM + Tools)<br>Planner<br>(Updates state,<br>replans if needed)<br><!-- End of picture text -->

_Figure 1.5: Planner and executor architecture_ 

These executor agents are specialized for their tasks and interact with the LLM independently from the planner and other executor agents. Thisidx_ae3a0043 means that they manage their own context and have their own set of tools. Coordinating the execution of the plan and handling dependencies between tasks can be the responsibility of the planner agent or a dedicated coordinator agent when the planner launches. 

_Chapter 1_ 

20 

This architecture is suitable for complex tasks that exceed the capabilities of a single agent. The executor agents utilize the same agentic AI techniques and don’t require any idx_b8506e42custom programming in general cases. All the custom programming that is necessary for accessing resources, data stores, and APIs is implemented by the tools. 

Typical use cases include the following: 

- Automated research and report generation 

- 

- Complex multi-step data processing pipelines 

- 

- Software refactoring and testing plans 

- 

- Coordinated use of multiple APIs or tools for integration tasks 

- 

###### **Multi-agent system** 

The idx_0ea19542planner and executors architecture is a cohesiveidx_00aa879f multi-agent architecture where the planner controls (directly or via a coordinator agent) and orchestrates the workflow. This can be extended to a more complex **multi-agent architecture** where multiple agents with specific roles (CEO, engineer reviewer) can operate independently and collaborate with each other, very much like a human team. 

<!-- Start of picture text -->
User<br>; Y<br>AgentA: |<br>Architect |<br>(um) |<br>Communication<br>¥<br>\<br>: Shared* memory or message bus* .<br>AgentB Agente<br>Builder Tester<br>Multi-Agent Architecture<br><!-- End of picture text -->

_Figure 1.6: Mult-agent architecture_ 

In idx_7b233159this architecture, agentsidx_9034dbfa can communicate with each other, share memory, and iterate together towards the system’s goals. This is a more sophisticated flow than the top-down structure of a planner and executors, allowing for more dynamic interactions and parallel processing of tasks. 

_Introduction to Generative AI and AI Agents_ 

21 

For example, when the coder agent completes implementing a module, it can notify the tester agent, which will proceed to test the new module. When all the modules the architect envisions are implemented by the coder agent and tested successfully by the tester agent, the architect can start working on the next version of the target system. Multiple coder agents and tester agents can work in parallel on multiple modules. 

###### **Graph-based architecture** 

**Graph-based architectures** represent idx_ec6d14bf the relationships between agents, tasks, tool invocations, and idx_b6139493memory updates as a graph. Each task or agent may spawn multiple subagents dynamically. The overall structure of the graph emerges organically based on the results of earlier tasks. 

<!-- Start of picture text -->
Graph-based architectures represent<br>the relationships between agents,<br>tasks, tool invocations, and memory<br>updates as a graph.<br>Sub- Sub- Panay<br>agent agent C) agentB<br>Tool<br>Task call<br><!-- End of picture text -->

_Figure 1.7: Graph-based architecture of agentic systems_ 

For simplicity, consider an example where the task may be to count all the words in all the files in a directory. Sub-agent C may be a sub-agent that counts words in a file, so multiple subagent Cs can be launched, one for each file. Later on, agent 1 will aggregate the results from all sub-agent Cs. 

_Chapter 1_ 

22 

Each node in the graph idx_d68252a9represents an agent, task, tool, or memory update, and the edges represent the flow of information and dependencies between them. One idx_72b71f99of the most prominent frameworks that uses this architecture is LangGraph ( `https:// www.langchain.com/langgraph` ). 

The main advantage of the agent graph architecture is that the problem can be broken down naturally into a deep hierarchical structure, such as software development planning, where a top-level goal such as “build a web application” decomposes into subsystems such as frontend, backend, and database, each with their own tasks, such as UI design, API development, schema modeling, and testing. Each subtask can be handled by specialized agents, passingidx_2576581d outputs and context down the graph, enabling coordinated and modular execution across layers of abstraction. 

But the agent graph architecture has several disadvantages too. It introduces significant coordination complexity, as managing dependencies, message passing, and error propagation between agents can become difficult to scale and debug. Additionally, it may incur overhead from excessive decomposition or agent churn, leading to latency, resource inefficiency, or brittle behavior when tasks don’t align cleanly with a hierarchical structure. 

###### **Summary** 

In this chapter, we followed the remarkable journey of generative AI from the pioneering work of symbolic reasoning and expert systems to the meteoric rise of deep learning and transformer-based models. We explored how the field evolved from rule-based automation to data-driven intelligence, leading to our current sophisticated generative models, capable of not only understanding but also creating content. 

We examined the emergence of AI agents and intelligent, autonomous systems that perceive, plan, act, and adapt to their environment. Unlike traditional chatbots, AI agents are equipped with memory, tool use, and multi-step reasoning abilities, enabling them to perform complex, dynamic tasks across diverse domains. We studied multiple architectures, saw how they differ from chatbots, and surveyed some real-world use cases, from autonomous coding assistants to AI companions. 

At this point, you should have all the necessary background to understand the principle of AI agents and what they are all about, their place in the overall AI revolution, and their current abilities. This should serve as solid groundwork to continue our journey. With this solid foundation, we are now ready to dive deeper into the inner workings of AI agents in the next chapter and unpack in detail how they are constructed, how their components interconnect, and how they achieve autonomy and intelligence in practice. 

_Introduction to Generative AI and AI Agents_ 

23 

###### **Get This Book’s PDF Version and Exclusive Extras** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
i<br>4<br>|<br>e<br>aeé<br>[=] :<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require an invoice._ 

# 2 

##### Understanding How AI Agents Work 

In _Chapter 1_ , we explored foundational concepts in **GenAI** and agentic systems, including various architectures used in their design. In this chapter, we’ll take a closer look at how AI agents actually function. We’ll examine the key components and subsystems of agentic AI, such as the core agent loop, memory, goal formulation, state management, planning/ reasoning, tool use, and feedback mechanisms. 

To ease your understanding, the chapter will introduce various concepts or components in an agentic system and discuss their roles. We will then discuss how these components are implemented in an open-source agentic AI framework, AutoGen. 

It's important to note again that we will focus on agentic AI systems where all the decisionmaking, planning, and reasoning is doneidx_2cc8fefb by a **large language model** ( **LLM** ). Other agentic AI systems are possible, where such logic is implemented in a different way, such as using a rule engine or traditional programming, or **retrieval-augmented generation** ( **RAG** ). External RAGidx_4a7176c1 is also a common idx_04f6fb08pattern where the AI system interprets the model's response and fetches relevant data from an external source, such as a database or knowledge base, to provide more accurate and contextually relevant answers or feed it back to the LLM. However, we will see later that even RAG can be as simple as a tool call controlled by the LLM itself. 

In this chapter, we will cover the following main topics: 

- Understanding the agent loop: sense, think, act 

- Workings of an agent loop in AutoGen 

- 

- Managing long conversations with memory, goals, and state 

- 

- Planning and reasoning mechanisms 

_Chapter 2_ 

26 

- Tool use and environment interactions 

- 

- Agent evaluation and feedback loops 

- 

###### **Understanding the agent loop: sense, think, act** 

The **agent loop** is theidx_f32e2bc3 core cycle that defines how AI agents operate. It is similar to many other control loops in other fields, such as robotics or control systems. Some famous examples of control loops are idx_90557a8cthe **OODA** ( **Observe, Orient, Decide, Act** ) loop ( `https://` 

`en.wikipedia.org/wiki/OODA_loop` ) and the Kubernetes reconciliation loop ( `https:// pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/reconcile` ). 

An agent loop idx_15 **c** 41d67 onsists of a session workflow and three phases called sensing, thinking, and acting. Let’s see how they operate. 

###### **The session workflow** 

The idx_9d6310e1agent loop revolves around the LLM. In each step of the loop, the agent interacts with the LLM to either send messages that contain new information (user input, sensor data, etc.) or to receive messages. 

<!-- Start of picture text -->
SEND<br>MESSAGE<br>(user input,<br>sensor data,<br>etc.)<br>NO<br>YES,<br>RESPONSE<br>SEND<br>RESULT<br>DO THE<br>THING<br><!-- End of picture text -->

_Figure 2.1: Session workflow of an agent_ 

If the idx_99fecef2received message is a final response, then the agent is done processing, the loop is terminated, and the response is returned to the caller (a user, another system, or a higher-level agent). However, if the received message is an instruction from the LLM to perform some 

_Understanding How AI Agents Work_ 

27 

action (typically a tool call), then the agent will perform the requested action and then continue the loop by sending the result of the action back to the LLM. 

###### **Note** 

The LLM API that the agent is working with is usually responsible for indicating if the response is final. 

Next, we’ll talk about the phases of an agent loop. 

###### **The agent loop phases** 

The agent loopidx_13711ec5 can be divided into three main phases: sensing, thinking, and acting. We will now describe how they function in the context of exchanging messages with an LLM. 

- **Sensing** : AI agents idx_a044b873perceive their environment through various sensing mechanisms. They collect data, observe the state and changes in the environment, and can use APIs, physical sensors, or access a datastore. However, the trigger for the sensing phase is always a tool call message from the LLM. 

<!-- Start of picture text -->
CALL<br>SYSTEM TOOL<br>PROMPT<br>aed | SU<br>| een<br>as<br>DATASTORE<br><!-- End of picture text -->

_Figure 2.2: The sensing phase of the agent loop_ 

Users, AI frameworks, or other agents may invoke an agent with a system prompt, an initial user message (the user doesn't have to be a human), and a set of tools. However, this initial information is always sent to the LLM, which may decide to trigger sensing by sending a tool call message. The agent will then execute the tool call, which could be reading some data from an API or physical sensor, or even utilizing RAG, and send the collected data back to the LLM. 

_Chapter 2_ 

28 

- **Thinking** : Here is the idx_074a2b33surprising part – the thinking phase is not a separate phase in the agent loop. The LLM does all the thinking, whether it is planning, reasoning, analyzing results of earlier tool calls, deciding which tools to invoke, or, of course, formulating a final response. The agent loop is simply a conduit to exchange messages with the LLM. The thinking phase happens every time the agent loop sends a message to the LLM. 

<!-- Start of picture text -->
AGENT<br>LLM<br>THINKING<br>LOOP<br><!-- End of picture text -->

_Figure 2.3: LLM thinking is invoked every time the agent sends a message_ 

Remember that idx_ae623e84this pure thinking at the LLM level is not an axiom. 

There may be agentic AI systems that operate in hybrid mode that intercept intermediate actions, such as the results of tool calls, and then process them and decide what to do next without delegating all the thinking to the LLM. However, such systems perform their thinking above the level of the agentic AI framework. 

<!-- Start of picture text -->
Al SYSTEM<br>TOOL<br>RESPONSE<br>AGENT<br>LOOP<br>=e<br><!-- End of picture text -->

_Figure 2.4: Hybrid mode of agentic AI systems_ 

The AI agent frameworkidx_a0b47794 itself that runs the agent loop is still a conduit for exchanging messages, but it may provide a hook where each tool call result is sent to the AI system above that uses the AI framework. Then, dedicated code with domain knowledge may control or hint further interaction with the LLM by processing the tool's response to the LLM, directly modifying the context, or simply terminating the agent loop even if the LLM didn't provide a final response yet. 

_Understanding How AI Agents Work_ 

29 

###### **Note** 

The agent never does any thinking. The thinking is either done by the LLM (below the agentic loop) or by the AI system (above the agentic loop). The agentic framework and the agents never perform any thinking on their own. 

• **Acting** : Acting is idx_7494fe03very similar to sensing. They are actually indistinguishable from each other from the perspective of the agent loop. The agent loop sends a message to the LLM, which responds with a tool call message. The agentic AI framework then executes the tool call and sends the result back to the LLM. Acting is simply a tool call that has some impact on the outside world. It could be a call to an API, a database, or even a physical action in the real world (such as moving a robot arm). 

###### **Note** 

The difference between sensing and acting is in its impact on the outside world. Sensing is just observing the state of the world. Acting changes the state of the world. 

<!-- Start of picture text -->
SEND MESSAGE<br>ae TOOL CALL<br>Yo\<br>A,<br>AGENT<br>ACT<br>RESULT<br><!-- End of picture text -->

_Figure 2.5: Acting phase of the agent loop_ 

The key pointidx_df33bfd1 is that the agent loop facilitates this interaction by sending the tool call and receiving the result. The agent loop is oblivious to the nature of the tool call, whether it is sensing or acting. The result of an action tool call will typically be a success or error message, which is sent back to the LLM. If the action is a long-term action, the response may be some action ID that the LLM may query later for progress and status updates. As always, the LLM will decide how to continue given a particular response to an action tool call. 

_Chapter 2_ 

30 

If the response was a success status, then the LLM may just respond with a final response message and terminate the agent loop. However, in case of failure, it may retry or take some recovery actions. 

In multi-agent systems, oneidx_3582bc8f of the most significant actions is launching another agent with its own agent loop. We will cover this aspect in depth later in the book ( _Chapter 8_ ). Another form of multi-agent collaboration is communicating with another already running agent that wasn't launched by the current agent. This interaction may be considered either sensing or acting, depending on what the other agent does. If it just returns some information, then it is sensing, but if it performs some action in the world, then it is acting. If it seems confusing at this point, don't worry. We will unpack all the details and nuances of multi-agent systems in _Part 3_ of the book. 

Let's see how the agent loop concept is implemented in aidx_fb81c295 popular agent framework by Microsoft: AutoGen ( `https://github.com/microsoft/autogen` ). 

**Note** 

AutoGen is widely known for its modular and clean design, with abstractions for agents, conversations, and strong tool integration, making it an ideal pick for the demonstration of the concepts. 

###### **Workings of an agent loop in AutoGen** 

AutoGen implements theidx_8e33a78d agent loop phases (sensing, thinking, acting) through its `AssistantAgent` class and supporting infrastructure, which closely followsidx_7c31a215 the described pattern where the LLM drives the loop through tool calls. In this section, we will walk you through the core implementation of AutoGen to illustrate how sensing, thinking, and acting work in practice. 

###### **The core implementation of AutoGen** 

The idx_5c34de07agent loop is primarily implemented in the `tool_agent/_caller_loop.py` module ( `https://github.com/microsoft/autogen/blob/main/python/packages/autogen-core/ src/autogen_core/tool_agent/_caller_loop.py#L16` ), which handles the continuous cycle of LLM interaction and tool execution. It is part of the core layer of AutoGen ( `https:// deepwiki.com/microsoft/AutoGen/1.1-core-architecture` ). 

Take a look at _Figure 2.6_ , which illustrates how the AutoGen agent loop functions: 

_Understanding How AI Agents Work_ 

31 

_Figure 2.6: An overview of an AutoGen agent loop_ 

Here is how this idx_fb4c1ee0loop works: 

1. First, a caller loop is started for a tool agent, `tool_agent_caller_loop()` . This function sends messages to the tool agent and the model client in an alternating fashion until the model client stops generating tool calls. The arguments are as follows: 

   - `tool_agent_id (AgentId)` : The agent ID of the tool agent 

   - 

- `input_messages (List[LLMMessage])` : The list of input messages 

- 

- `model_client (ChatCompletionClient)` : The model client to use for the model API 

- `tool_schema (List[Tool | ToolSchema])` : The list of tools that the model can use 

It returns `List[LLMMessage]` – the list of output messages created in the caller loop. 

_Chapter 2_ 

32 

Here is how the `tool_agent_caller_loop` function is implemented: 

```
from ..tools import Tool, ToolSchema
from ._tool_agent import ToolException
asyncdeftool_agent_caller_loop(
    caller: BaseAgent | AgentRuntime,
tool_agent_id: AgentId,
model_client: ChatCompletionClient,
input_messages: List[LLMMessage],
tool_schema: List[ToolSchema] | List[Tool],
cancellation_token: CancellationToken | None = None,
caller_source: str = "assistant",
) -> List[LLMMessage]:
```

2. **The sensing phase in AutoGen** : AutoGen implements sensing through tool calls triggered by idx_6c6afbab the LLM. When the LLM decides to gather information, it generates `FunctionCall` objects that the agent executes. The agent then executes these tool calls and sends results back to the LLM. The following code illustrates this part: 

```
    generated_messages: List[LLMMessage] = []
# Get a response from the model.
    response = await model_client.create(input_messages,
        tools=tool_schema, cancellation_token=cancellation_token,)
# Add the response to the generated messages.
    generated_messages.append(
        AssistantMessage(
            content=response.content,
            source=caller_source
        )
    )
# Keep iterating until the model stops generating tool calls.
while (
isinstance(response.content, list)
andall(
isinstance(item, FunctionCall)
```

_Understanding How AI Agents Work_ 

33 

```
for item in response.content
)
    ):
# Execute functions called by the model by sending messages to the tool
agent.
        results: List[FunctionExecutionResult | BaseException] = await
asyncio.gather(
            *[
                caller.send_message(
                    message=call, recipient=tool_agent_id,
                    cancellation_token=cancellation_token,
                )
for call in response.content
            ],
            return_exceptions=True
        )
# Combine the results into a single response and handle exceptions.
        function_results: List[FunctionExecutionResult] = []
for result in results:
ifisinstance(result, FunctionExecutionResult):
                function_results.append(result)
elifisinstance(result, ToolException):
                function_results.append(
                    FunctionExecutionResult(
                        content=f"Error: {result}",
                        call_id=result.call_id,
                    )
                )
elifisinstance(result, BaseException):
raise result  # Unexpected exception.
        generated_messages.append(
            FunctionExecutionResultMessage(content=function_results)
        )
```

_Chapter 2_ 

34 

3. **The thinking phase in AutoGen** : AutoGen confirms that thinking happens entirely within the idx_6bb60e38 LLM, and not as a separate phase on the AI framework side. The agent loop acts as a conduit by continuously calling the model client. The loop continues while the LLM returns tool calls, with all reasoning, planning, and decision-making delegated to the LLM itself. Here is how: 

```
# Query the model again with the new response.
    response = await model_client.create(
        input_messages + generated_messages, tools=tool_schema,
        cancellation_token=cancellation_token)
    generated_messages.append(AssistantMessage(
        content=response.content, source=caller_source))
return generated_messages
```

4. **The acting phase in AutoGen** : Acting is implemented identically to sensing – throughidx_79f6ebc9 tool execution. The agent is "oblivious to the nature of the tool call," as described. Whether a tool reads data (sensing) or performs an action (acting), the implementation is the same. For more complex tool interactions, AutoGen provides a dedicated `tool_agent_caller_loop` function ( `https://github.com/microsoft/ autogen/blob/main/python/packages/autogen-core/src/autogen_core/` 

- `tool_agent/_caller_loop.py` ), which implements the complete sensing-thinkingacting cycle. 

This function demonstrates the core loop: send message to LLM → receive tool calls → execute tools → send results back → repeat until no more tool calls. 

###### **Note** 

AutoGen supports the described multi-agent collaboration through handoffs, where one agent can launch or communicate with another agent. This is implemented through `HandoffMessage` ( `https://github.com/microsoft/autogen/blob/main/ python/packages/autogen-agentchat/src/autogen_agentchat/messages.py` ) and the Swarm pattern, allowing agents to delegate tasks to specialized agents with their own agent loops. 

- **HandOffMessage** is aidx_b012567c message intended to transfer the conversation to another agent. 

- **Swarm pattern** is a idx_49ee03d9coordination strategy where multiple agents contribute to solving a task. 

_Understanding How AI Agents Work_ 

35 

For an agentic system to retain context, it needs to have access to information that may enable its course of action. That’s where memory, goals, and state come into play. Let’s talk about them next. 

###### **Managing long conversations with memory, goals, and state** 

Agentic AI systems performidx_f0182412 complex multi-step tasks over a potentially long period of time, interacting with humans, other systems, and other AI agents in a synchronous or asynchronous manner. As you are very aware at this point, all the thinking is done by the LLM, but the LLM has no memory (although chatbots such as ChatGPT have a long-term memory on top of the LLM; see `https://help.openai.com/en/articles/8590148-memory-faq` ). This means that in every call to the LLM, we need to provide it with all the relevant information, which typically includes the entire history of the session so far, in addition to the latest user message or tool call response. Some LLM providers provide stateful long-term memory, which is injected into the LLM’s context dynamically. 

We will focus here on a single invocation of an agent that contains exactly one system message, one user message (AKA prompt), zero or more tool messages, and a single final response message from the LLM. 

The general instructions for the agent are specified in the system message, which is typically a long text that describes the agent's capabilities, its role, some initial knowledge, output specifications, and examples. For example, the system message for a Python coding agent may look like this: 

```
You are a Python programming expert and assistant. You write clean, idiomatic,
well-documented Python code and
explain your choices clearly and concisely when asked.
You can analyze requirements, debug code, refactor existing implementations, and
suggest improvements in architecture and style.
Always assume the user is technically competent but may not know the full details
of Python’s standard library or idioms.
If a question is ambiguous, ask clarifying questions before proceeding.
When writing code, prefer clarity over cleverness, and add brief comments where
appropriate.
Output Python code inside triple backticks unless instructed otherwise.
You may use third-party libraries only if explicitly allowed or commonly accepted
(like requests, pandas, or numpy).
```

_Chapter 2_ 

36 

```
Follow best practices like writing unit tests and documenting your code following
PEP-257 conventions.
```

A long conversation with this agent may be broken down into several invocations of the agent loop, each with its own final response message. The thread of the conversation will be kept by the AI system, which will feed all the messages from the previous session into the next session. 

For example, the user may request _Build me a calculator in Python_ and the agent will respond with a clarifying question as a final response message: _Do you prefer a CLI program or a GUI application?_ . The controlling AI system will present the question to the user, who may choose a CLI program. Now, a new invocation of the agent starts with all the history of the first session, as well idx_d **a** f3540b s the user's choice of CLI program as the initial user message to the agent. Then, the new agent, having the information that the user prefers a CLI program, can start iterating with tool calls to generate and write code and tests until it is satisfied and return a final response such as _Done. The CLI program is called calc.py and the unit tests are in calc_test.py_ . 

<!-- Start of picture text -->
Session<br>Agent: Bo you prefer a Cut<br>program or a Gut<br>‘polation?<br>Seaton?a<br>toc: Generate CLE<br>callThalcode ig<br>+ call tot: Generate unit<br>+ all tot Vatéate and<br>+ Repeat as needed<br>End Lop<br>‘gent Hoa expense<br>The Lt program is called<br>cale.testoy<br><!-- End of picture text -->

_Figure 2.7: Multi-session conversation_ 

Let's see how this is all represented in terms of the LLM context window. 

_Understanding How AI Agents Work_ 

37 

###### **The context window** 

The **context window** inidx_28f5049c a language model refers to the total amount of information the idx_396f333emodel can process and reason over during a single invocation. This includes not just text, but also other input modalities such as images, audio, structured data, or embeddings—depending on the model’s capabilities. The context window really serves as the model’s working memory, determining what information it can _see_ and use to generate a response. 

###### **Note** 

RAG embeddings may be injected directly into the context window regardless of the encoding that all modalities go through. 

Now, all the high-level concepts we have discussed so far, such as the agent memory, goals, and state, must eventually be represented as tokens and fit into the context window of each and every API request to the LLM. 

When the LLM forms its response, it relies on its knowledge from training, which is encoded in the model weights. But all the information in the context window is immediately forgotten once the response from the model is generated. Note that the operators of the LLM may store this information for auditing, future training, or other purposes, but the model itself doesn't learn or retain any information from the context window. The only way to retain information across multiple invocations of the agent loop is to store it at the AI framework or AI system level and then feed it back into the context window of the next invocation. 

**Note** The LLM (models such as GPT 4o) doesn't manage user profiles. The LLM provider (e.g., OpenAI) may store user-specific information and inject it into the context window automatically in an interactive chat session, such as with ChatGPT. In this case, ChatGPT fulfills the role of the AI system that manages the memory. 

In agentic AI systems using AI frameworks, the interaction with the LLM is usually through dedicated API keys, and there is no user-level profile. 

A larger context window enables more sophisticated behavior: longer conversations, richer inputs, more complete reasoning over prior steps, or detailed references to complex artifacts. A smaller window constrains the model’s ability to maintain continuity, integrate context, or handle deeply nested tasks. 

_Chapter 2_ 

38 

But, even with a large context window, you may run out of space for long conversations or complex tasks with large inputs and outputs. Each model has its own context window size, and it’s important to take it into account when choosing which model to use. In such situations, you may need to truncate the conversation history, summarize it, or compress it in some form to fit into the context window. In multi-agent systems, you may also apply a divide-andconquer idx_8743d0dd approach where each agent is responsible for a specific sub-task and can dedicate the entire context window of the model for just its own sub-tasks, and only the results, which are typically smaller, are aggregated by a higher-level agent. We will cover this scenario in _Chapter 9_ . 

###### **Why do LLMs have no memory?** 

But why can't the LLM just remember everything? Why does it need to be fed with all the context every time? The answer is complex and nuanced. First of all, there is no benefit in having a memory component in the LLM itself. What we're actually talking about is the LLM provider maintaining the state of each user's conversations (the history of all the messages) so the user can just send the latest message in each request. 

The LLM provider can then add the latest message to the user's saved session and feed it to the LLM as a transient context window. So, the question is, why can't the LLM providers offer this service to users? In theory, it could save a lot of bandwidth because there is no need to send the entire history of a session in each request, only the delta of new messages. 

However, at scale, you want multiple copies of each LLM running in parallel and able to handle a massive number of requests. If each LLM instance had its own memory, then you would need to keep session affinity between user requests and the LLM instance. In addition, there may be a delay between subsequent messages from the user. When the LLM provider manages the session's memory, it must maintain the state even when no messages are sent. That can add up quickly, especially for long-term sessions. 

Let’s look at an example: 10,000 users send, within 5 minutes, a total of 10 TB of data to the LLM provider. The LLM provider needs to store all this data in order to service additional messages from users. Deciding where to store this data is complicated (in memory, in a database, in a distributed cache). Whenever a user sends another message, the LLM provider needs to fetch the context for this user’s conversation and inject it into the LLM. That is complicated and can introduce multiple failure modes and performance issues. 

Finally, there is the issue of session termination. The LLM provider has two options: either keep the session state forever so users can continue the conversation at any point, or decide based on some heuristics when to erase the session's memory. In general, LLM providers prefer to keep the LLM stateless and let the AI frameworks or AI systems manage the session's state to improve scalability, reduce latency, and minimize costs. 

_Understanding How AI Agents Work_ 

39 

Chatbots such as ChatGPT, Perplexity, and Claude.ai appear to have a long-term memory and can continue previous conversations. Here is an example where Claude.ai shows a list of previous conversations. 

<!-- Start of picture text -->
oO < > SC GB B claudeaiy A @&Search DuckDuckGo<br>Q © Claude<br>+<br>© Newenat<br>Recents<br>| Writing Content for Google Docs<br>Se tetas * What’s new, Gigi?<br>e How Language Models Predict Nex.<br>CreatingSVG Vector Graphics<br><!-- End of picture text -->

_Figure 2.8: Sample conversation storage of the Claude.ai service_ 

This is actually a feature of the AI system that manages the chatbot, not the LLM itself. Claude.ai is a web service that provides interactive chat services with Anthropic models. It stores all conversations in persistent storage, and it shows the list of previous conversations to the user. When the user selects a conversation, the Claude.ai service retrieves the stored conversation and feeds it as the initial message to the selected LLM (e.g., Claude Sonnet 4). The LLM itself always just has an ephemeral context window that is scoped to the current invocation. Some LLM providers, such as OpenAI, started experimenting with global long-term memory across all conversations with ChatGPT memory ( `https://openai.com/index/ memory-and-new-controls-for-chatgpt/` ). A summary of all past conversations (users can opt in and out of long-term memory) is fed to every invocation, so it appears that the model remembers all your past interactions. 

For a real-life implementation, let's see how memory is implemented in the AutoGen framework ( `https://github.com/microsoft/autogen` ). 

_Chapter 2_ 

40 

###### **Memory in AutoGen** 

Surprisingly, AutoGen doesn't idx_67b6cd79provide memory facilities at the core level ofidx_cd39a9af its architecture. Memory is supported at the higher abstraction level of chat agents. There are three types of memory: 

1. **Simple sequential list memory** : AutoGenidx_ebba79d3 defines an abstract memory protocol for simple sequential list memory with operations such as `add()` , `query()` , `update_context()` , `clear()` , and `close()` . For example, an agent that returns the current weather may use the memory to store the user's temperature unit preferences ("imperial versus "metric") and respond accordingly to user queries. In the context of interaction with the LLM, the content of the memory is added to the context window. 

2. **Vector-based RAG memory** : AutoGen idx_f2088bd8supports more complex memory stores that implement the memory protocol too. AutoGen provides, out of the box, an extension that implements vector-based RAG memory in the `ChromaDBVectorMemory` class ( `https://github.com/microsoft/autogen/blob/main/python/packages/autogenext/src/autogen_ext/memory/chromadb/_chromadb.py` ). 

3. **Task-centric fast memory (experimental)** : The idx_74213049experimental task-centric fast memory is implemented in `MemoryController` . It doesn't use the memory protocol and is still an active research project within AutoGen. Its goals are as follows: 

   - Accomplish general tasks more effectively by learning quickly and continually beyond context-window limitations 

   - Remember guidance, corrections, plans, and demonstrations provided by users 

   - Learn through the agent's own experience and adapt quickly to changing circumstances 

   - Avoid repeating mistakes on tasks that are similar to those previously encountered 

They are all used in the `AssistantAgent` class, which is the main class for implementing chat agents in AutoGen. 

We will now move our focus to the planning and reasoning mechanisms of LLMs. 

_Understanding How AI Agents Work_ 

41 

###### **Planning and reasoning mechanisms** 

As you might recall, all planning and reasoning in agentic AI systems is done by the LLM. However, the AI framework can still structure the interaction with the LLM to facilitate orchestrated planning and reasoning. In this section, we will look at different methods for planning and reasoning in agentic AI systems, including single-agent and multi-agent planning, as well as working with reasoning models. 

###### **Working with reasoning models** 

LLM providers idx_316be378now offer reasoning models that are specifically designed for complex multistep reasoning tasks (see the following figure): 

<!-- Start of picture text -->
A<br>«For maith:<br>REASONING ‘tins+ Manageancepti ande cost -<br>Al<br>FRAMWORK<br><!-- End of picture text -->

_Figure 2.9: Working with reasoning models_ 

This means that in idx_f9e6cf73a single request, these models may perform multiple steps of reasoning and use internal tools such as web search and code execution that don't require interacting with the AI framework or the user. For example, OpenAI's o-series models (o3, o4-mini) take more time (and tokens), and in effect run their own internal agent loop. These models may still invoke external tools when necessary, but the thinking phase on the LLM side is more involved. From the AI framework’s perspective, there isn't much of a difference between using a reasoning model and a regular LLM. But it's important to manage user expectations regarding performance, latency, and cost. 

_Chapter 2_ 

42 

###### **Single-agent planning and reasoning** 

Single-agent planning and reasoning **i** dx_6f15e4da s the simplest form in agentic AI systems. The following diagram illustrates this: 

<!-- Start of picture text -->
SYSTEM * Agent invoked<br>MESSAGE with messages<br>ou— + andNo interactiontools<br><— (wos LLM with other agents<br>* Return plan or<br>foo FINAL onanalysiscomplete based history<br>RESPONSE<br><!-- End of picture text -->

_Figure 2.10: Single-agent reasoning_ 

The idx_8 **a** a2b5ee gent loop is invoked with a system message, a user message, and a set of tools. The agent never communicates with other agents or launches sub-agents. In each request to the LLM, the complete history of the session is sent to the LLM, which then decides how to continue. The resulting plan or analysis is sent back to the user as a final response message. The agent may invoke tools to gather information that will be useful in formulating a plan or reasoning about the input data. 

###### **Multi-agent planning and reasoning** 

In multi-agent systems, planningidx_01d03551 and reasoning are more complex. The top-level agent may invoke additional sub-agents or communicate with already running agents. Note that the decision to invoke a sub-agent or communicate with another agent is itself the result of planning by the LLM invoked by the top-level agent, which results in a tool call, where the tool execution results in launching a sub-agent or sending a message to another agent. 

The interactions between agents in multi-agent systems introduce several layers of interaction that don't exist in single-agent scenarios. When a parent agent delegates work to a sub-agent, it must carefully craft the sub-agent's context, including the system prompt, initial goals, available tools, and any relevant background information from the parent's session. 

_Understanding How AI Agents Work_ 

43 

<!-- Start of picture text -->
TOP-LEVEL AGENT<br>qn J<br>+ Invoke sub-agents<br>‘SUB-AGENT with‘or communicateother agents<br>‘SUB-AGENT g AGENT<br><!-- End of picture text -->

_Figure 2.11: Multi-agent reasoning_ 

The parent idx_8 **a** 4a1df7 gent also needs to decide whether to wait synchronously for the sub-agent's completion or to continue processing other tasks asynchronously while monitoring the subagent's progress. Communication protocols become crucial when agents need to exchange information during execution – agents may need to negotiate, coordinate shared resources, resolve conflicts, or aggregate results from multiple parallel sub-agents. Additionally, error handling and recovery strategies become more sophisticated, as failures in one agent can cascade through the system, requiring parent agents to detect failures, retry with different parameters, or dynamically reassign tasks to alternative agents. The context window limitations of individual agents also create challenges for information sharing, as agents must decide which information to pass between each other, potentially requiring summarization or selective filtering of large conversation histories. 

###### **Tool use and environment interactions** 

Managing tools is theidx_1301be2d primary responsibility of the AI framework. The LLM drives everything by doing the actual planning and reasoning, but for many tasks, the agent needs to interact with the environment, which is done through the available tools. The list of tools that the agent makes available to the LLM defines the capabilities of the agent. 

Agents may be super helpful in increasing productivity, automating mundane tasks, summarizing emails, and running regular checks in a work environment. 

Consider, for example, an AI software engineer agent. In order to be effective, it requires tools to performidx_3cbfda41 tasks such as the following: 

- List files and directories 

- 

- Read, create, edit, and delete files 

- 

- Run unit tests and integration tests 

- 

- Run the code in a sandbox environment (e.g., Docker container) 

- 

_Chapter 2_ 

44 

- Run a local web server to test the code in a browser 

- 

- Run a code linter and formatter, code style checker, code analyzer, code security scanner 

- Create Git branches, commit code, push code to a remote repository 

- 

For a regular user, an AI agent may come in handy in performing their day-to-day activities, such as meal-planning and ordering food items based on diets, preparing and buying groceries at scheduled intervals, or more complex tasks such as vacation planning that require several steps. 

Take, for example, an AI vacation planner agent. In order to be effective, it requires tools to perform tasks such as the following: 

- Search for flights and compare prices across different airlines and dates 

- 

- Find and book accommodation (hotels, vacation rentals, hostels) 

- 

- Research local attractions, restaurants, and activities at the destination 

- 

- Check visa requirements and travel restrictions for different countries 

- 

- Access real-time weather forecasts and seasonal travel information 

- 

- Calculate travel budgets and track expenses across different categories 

- 

- Make restaurant reservations and book tours or experiences 

- 

- Access the user's calendar to identify available travel dates and duration constraints 

- 

- Send confirmation emails and create itinerary documents with booking details 

- 

It doesn't matter how powerful the LLM is, if it doesn't have the tools to interact with the environment, it will not be able to be an effective software engineer or vacation planner. The most the AI software engineer will be able to do is generate code based on a prompt, which can be very helpful, but is just a part of the overall software development lifecycle. For example, if the vacation planner doesn’t have permission to book reservations, it can recommend a vacation but will not be able to assist in bookings and reservations. 

Let's dive deeper into how tools are implemented, declared, and used in agentic AI systems, with a focus on AutoGen. 

###### **How are user-defined tools implemented?** 

There idx_a7e16a00 are idx_1b1c88catwo categories of tools in agentic AI systems: built-in tools and user-defined tools. Built-in tools such as `web_search` , `code_execution` , `file_search` , and `computer_use` are implemented by LLM providers. User-defined tools are functions that can be implemented in any programming language and are typically implemented in the same language as the agentic AI framework. However, they can also be implemented in a different language and exposed to the agentic AI framework as a Docker container or through some internal API. 

_Understanding How AI Agents Work_ 

45 

Here is an example of a user-defined tool to add two numbers in Python: 

```
defadd_numbers(a: int, b: int) -> int:
"""
Adds two numbers and returns the result.
Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
return a + b
```

That's right. It's just a regular Python function. The agentic AI framework will take this function and expose it as a tool. We will cover this in detail in _Chapters 3_ , _4_ , and _5_ . 

###### **How are tools declared?** 

LLM providersidx_19046abe such as OpenAI, Anthropic, Mistral, and Google expose an API to interact with their models. Many other providers offer OpenAI-compatible APIs. These APIs are pretty similar and allow you to declare a separate list of tools in every call. 

Here is the classic example of a tool declaration in the OpenAI API: 

```
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "input": "What is the weather like in Paris today?",
    "tools": [
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
```

_Chapter 2_ 

46 

<!-- Start of picture text -->
              "description": "City and country e.g. Bogotá, Colombia"<br>            }<br>          },<br>          "required": [<br>            "location"<br>          ],<br>          "additionalProperties": false<br>        }<br>      }<br>    ]<br>  }'<br><!-- End of picture text -->

AI agents have a well-defined scope and a set of tools to perform their tasks. Every request that the agenticidx_74642b79 AI framework sends to the LLM on behalf of a specific AI agent will include the list of tools that the agent has. Different agents may have different tools. The LLM that receives a set of tools from the agent may request to invoke a tool in the form of a tool message that the AI framework handles, executes the requested tool, and returns the result to the LLM. 

###### **How does the LLM decide which tool to use?** 

There are idx_e3506e82several layers of abstraction here. The agentic AI framework often supports multiple LLM providers, each with its own API and tool declaration format. The framework abstracts these differences and provides a unified interface for declaring tools. When the agentic AI framework sends a request to a particular LLM provider, it translates the request, including the tool list, to the format expected by the LLM provider's API. 

_Understanding How AI Agents Work_ 

47 

<!-- Start of picture text -->
tool call<br>examples in<br>training data<br>O<br>LLM PROVIDERAPI i:LM * Trainedcall exampleson tool<br>5 |. search_web (query: string) “tool_calls": { * Considers<br>“Seach ew | “name: available tools<br>2. calculate (expression sti) S pebaectl if + Decides based<br>eprint "location": on input query<br>3.gt wether est sing) }" Paris, France"<br>Al AGENTICFRAMEWORK |(_ ~ ret beatoncur we er aTOOL CALL<br>MESSAGE<br><!-- End of picture text -->

_Figure 2.12: An agentic framework calling the get_weather tool_ 

When the LLM provider receives the structured request with the list of tools, it generates a textual representation such as the following: 

```
You can call the following tools:
1.search_web(query: string) - Search the web for information.
2.calculate(expression: string) - Evaluate a mathematical expression.
3.get_weather(location: string) - Get the current weather for a location.
```

This text isidx_778f2cb5 converted to a stream of tokens that are fed into the LLM, which doesn't know or care about API request structure (this is for developers). The LLM was trained on a large corpus of text that includes examples of tool calls and their usage. When the LLM receives the textual request with the tool list, it can recognize the tools and their parameters based on this training. The LLM then decides which tool to use based on the input query and the available tools. It will generate a tool call message in a structured format that the LLM provider API layer receives and formats to a proper response with a tool call, such as the following: 

```
{
"tool_calls": [
    {
"name": "get_weather",
```

_Chapter 2_ 

48 

```
"arguments": {
"location": "Paris, France"
      }
    }
  ]
}
```

This response is then sent back to the agentic AI framework, which executes the tool call and sends the result back to the LLM to continue the agent loop. 

Let’s look at how AutoGen uses tools. 

###### **Tool use in AutoGen** 

AutoGen provides aidx_6845c0ca comprehensive framework for defining and using tools within AI agents. It supports both built-in and user-defined tools, allowing developers to idx_5c1f2944extend the capabilities of agents easily. Since it works with multiple LLM providers and their APIs, it defines its own provider-agnostic data structures for tools, which are then translated to each provider's format as necessary. 

Let's look at an AutoGen sample of chess-playing agents and see how they use tools. The black player agent has the following tools: 

```
black_tools: List[Tool] = [
    FunctionTool(
        get_legal_moves_black,
        name="get_legal_moves",
        description="Get legal moves.",
    ),
    FunctionTool(
        make_move_black,
        name="make_move",
        description="Make a move.",
    ),
    FunctionTool(
        get_board_text,
        name="get_board",
        description="Get the current board state.",
    ),
]
```

_Understanding How AI Agents Work_ 

49 

Each of the function tools is a Python function/method, such as the following: 

```
asyncdefchess_game(
    runtime: AgentRuntime,
model_client: ChatCompletionClient,  # type: ignore
) -> None:
"""
    Create agents for a chess game and return the group chat.
    """
# Create the board.
    board = Board()
# Create tools for each player.
defget_legal_moves_black() -> str:
return get_legal_moves(board, "black")
```

The tools are then registered with `ToolAgent` ( `https://github.com/microsoft/autogen/ blob/main/python/packages/autogen-core/src/autogen_core/tool_agent/ _tool_agent.py` ): 

```
# Register the agents.
await ToolAgent.register(
    runtime,
"PlayerBlackToolAgent",
lambda: ToolAgent(
        description="Tool agent for chess game.",
        tools=black_tools,
    ),
)
```

When idx_4e3dd835 tools are registered, the LLM gains the ability to invoke these tools **i** dx_10a602ef n its response messages. 

`ToolAgent` is a specialized agent in AutoGen core that receives `FunctionCall` messages, executes the requested tools with provided arguments, and returns `FunctionExecutionResult` messages. It's typically used as a dedicated tool executor that other agents can delegate function calls to, providing error handling when a tool is not found, invalid arguments, and execution failures. 

_Chapter 2_ 

50 

Then, the black player agent is registered (there is a similar white player agent too). Note the instructions to play as "black" and use the provided tools. 

```
await PlayerAgent.register(
    runtime,
"PlayerBlack",
lambda: PlayerAgent(
        description="Player playing black.",
        instructions=(
"You are a chess player and you play as black. "
"Use the tool 'get_board' and
'get_legal_moves' to get the legal moves "
"and 'make_move' to make a move."
        ),
        model_client=model_client,
        model_context=BufferedChatCompletionContext(buffer_size=10),
        tool_schema=[tool.schema for tool in black_tools],
        tool_agent_type="PlayerBlackToolAgent",
    ),
)
```

The AutoGen agent loop will send a request to the LLM with the list of tools, and the LLM will decide which tool to use at the appropriate time. The idea here is that while the LLM is making the i **d** x_0af5b668 ecisions about the next step, the expectation is that it willidx_12b5538c need to get the current board state in order to decide. The `get_legal_moves()` tool is arguably not necessary, because if the LLM is expected to know chess well enough to pick the next best move, then it should be smart enough to only pick legal moves. 

###### **Agent evaluation and feedback loops** 

One ofidx_068a20eb the key aspects of agentic AI systems is the ability to evaluate the performance of agents and provide a path of improvement. This is especially important in multi-agent systems where agents may collaborate or compete with each other, and small mistakes and inaccuracies can accumulate, leading to suboptimal results or even the failure of the entire workflow. There are several ways to evaluate agents, including the following: human feedback, automated evaluation, and industry benchmarks. 

_Understanding How AI Agents Work_ 

51 

Some methods of evaluation can be performed automatically, and while the system is running, other methods that involve human feedback or take too long can be used offline to improve the performance of future agents. 

Let's look at each of these methods in more detail. 

###### **Human feedback** 

Human feedbackidx_8d55cf4a plays a critical role inidx_a4498bc3 shaping the behavior and quality of agentic AI systems. Unlike automated evaluations that rely on predefined rules or metrics, human feedback captures subjective elements such as helpfulness, tone, clarity, and user satisfaction. This is particularly valuable in open-ended tasks such as creative writing, decision-making, or user assistance—where rigid evaluation criteria fall short. Users may provide direct feedback by rating responses, flagging incorrect actions, or selecting preferred outputs. Alternatively, implicit feedback can be gathered from user behavior, such as whether they continue engaging with the agent or abandon a task prematurely. 

Either way, agentic AI frameworks typically don't provide mechanisms for collecting human feedback. Developers of AI systems should build human feedback support at the application level. 

In more structured environments, feedback can be solicited from domain experts who evaluate the agent’s performance on specific criteria. For instance, in a coding assistant agent, developers might assess the quality of the generated code, the usefulness of explanations, and the correctness of debugging steps. This expert feedback can be used to refine prompts, curate better examples, and adjust the agent’s toolset. Note that this is differentidx_3bef9803 from **reinforcement learning from human feedback** ( **RLHF** ) pipelines, which are used in training LLMs to better align future behavior with human preferences. The focus here is on the **i** dx_c2eb8c71 mprovement of the AI agent’s performance as opposed to the underlying LLM. It is possible to have a self-improving AI system that collects human feedback, analyzes it, and uses it to improve itself or other AI agents. 

_Chapter 2_ 

52 

Human feedback isidx_f5f0ff1c especially vital in multi-agent systems, where coordination, delegation, and communication dynamics come into play. Here, feedback may not only assess individual agents but also how well agents collaborate or divide responsibilities. Annotators or end users can comment on breakdowns in communication, misaligned goals, or inefficient task execution. This feedback helps identify systemic issues and provides data to reconfigure agents for better synergy. Although slower and more resource-intensive than automated methods, human feedback is indispensable for evaluating nuanced behavior and fostering trust in realworld deployments: 

<!-- Start of picture text -->
Human Feedback<br>User fie eta<br>Al System H Feedback 1<br>| (e {<br>QO) G. | 2 |<br>Improved<br>Al System<br><!-- End of picture text -->

_Figure 2.13: Human feedback_ 

Human feedbackidx_7f58fd46 works well in idx_91930183conjunction with other evaluation methods, such A/B testing, and can be used to cross-check automated evaluations too. 

###### **Automated evaluation** 

Automated evaluation idx_371ad2camethods provide a scalable way to assess agent performance without human intervention. Automated evaluation works best when the result of a task is well known. For example, if the agent is asked to generate the result in a certain format, such as a CSV file, it is easy to verify if the output is indeed a CSV file. 

We can also take advantage of LLM technology and use LLMs to evaluate the output of an AI agent against its original goal. In a hierarchical multi-agent system, this can be done at different levels. Moreover, it offers the possibility of addressing issues on the fly. 

_Understanding How AI Agents Work_ 

53 

<!-- Start of picture text -->
Al Agent<br>Evaluation Al<br>Agent<br>revise<br>satisfactory not satisfactory<br><!-- End of picture text -->

_Figure 2.14: Evaluation of an agentic system_ 

For example, a parent AI agent launches multiple sub-agents to perform sub-tasks. It then uses an evaluation AI agent to evaluate the results of sub-tasks and if they are not satisfactory, it can run the sub-agent again, possibly with a different prompt or configuration. The results of such live evaluations should be logged and used to improve the performance of future agents, so there is less of a need to fix live problems. 

Agentic AI evaluation involves assessing end-to-end task success through metrics such as completion rate, trajectory quality, and tool accuracy, while breaking down components such as planning, reasoning, and self-correction via traces and simulations. This process uses benchmarks (e.g., SWE-Bench, TRAIL), LLM-as-judge scoring, and production monitoring to ensure reliability, iterating on failures with layered human and automated checks 

Here are idx_068448ec some of the standard metricsidx_90c51185 and scores used to evaluate agentic AI systems: 

###### **Task performance metrics** 

###### • 

- **Success rate** : Percentage of tasks completed successfully 

- 

- **Task completion time** : Average time to complete tasks 

- **Accuracy** : Correctness of outputs/decisions 

- 

- **Precision/recall/F1** : For classification and retrieval tasks 

- 

_Chapter 2_ 

54 

###### **Agent behavior metrics** 

###### • 

- **Tool usage efficiency** : How effectively agents use available tools 

- 

- **Planning quality** : Coherence and optimality of generated plans 

- **Reasoning depth** : Quality of multi-step reasoning chains 

- 

- **Adaptability** : Performance when conditions change 

- 

###### **Multi-agent coordination metrics** 

###### • 

- **Communication efficiency** : Quality and necessity of agent interactions 

- 

- **Task allocation efficiency** : How well tasks are distributed 

- 

- **Coordination overhead** : Communication cost versus benefit 

- 

- **Consensus time** : Time to reach agreement in collaborative tasks 

###### **Safety and alignment metrics** 

###### • 

- **Harmlessness** : Avoidance of harmful outputs 

- 

- **Truthfulness** : Factual accuracy and honesty 

- 

- **Helpfulness** : Meeting user needs effectively 

- 

- **Alignment score** : Following intended objectives versus reward hacking 

###### **Robustness metrics** 

###### • 

- **Adversarial robustness** : Performance under attack scenarios 

- **Distribution shift tolerance** : Performance on out-of-distribution data 

- **Error recovery** : Ability to recover from failures 

- 

- **Hallucination rate** : Frequency of generating false information 

- 

###### **Efficiency metrics** 

###### • 

- **Computational cost** : Resources used per task 

- 

- **Token efficiency** : Output quality per token consumed 

- 

- **Latency** : Response time for real-time applications 

- 

- **Scalability** : Performance degradation with system size 

We idx_39946e1bwill idx_aac833f9explore evaluation metrics more in _Chapter 10_ . 

Implementing all of the evaluation metrics is a substantial effort that requires many engineering years. See `https://www.getmaxim.ai/articles/evaluating-agenticworkflows-the-essential-metrics-that-matter/` . Let’s look at industry benchmarks now. 

_Understanding How AI Agents Work_ 

55 

###### **Industry benchmarks** 

Industry benchmarksidx_c9f23853 are standardized idx_ab557adctests or tasks that agents can be evaluated against. These benchmarks provide an objective way to measure the performance of an AI agent or a complete agentic AI system. Comparing the performance of your agentic AI system against **SOTA** ( **state of the art** ) canidx_f7524e64 provide a signal if you have a lot of low-hanging fruit or if the performance is already close to optimal. However, benchmarks are often designed for specific tasks or domains, and the overlap with your agentic AI system's use case may be limited. Here are some common industry benchmarks: 

- **AgentBench** : `AgentBench` ( `https://github.com/THUDM/AgentBench` ) is a comprehensive idx_5 **b** 0cf8ab enchmark designed to evaluateidx_113b4c45 the general capabilities of LLM-based agents across a variety of tasks. It focuses on real-world agent tasks such as web browsing, math problem solving, and embodied decision-making to test reasoning, memory, and tool use. 

- **ToolBench** : `ToolBench` ( `https://github.com/OpenBMB/ToolBench` ) provides a suite of i **d** x_d1424395 atasets and idx_11d75c99evaluation protocols for training and assessing LLMs that can call external tools. It emphasizes tool-use capabilities, measuring how well an agent can invoke APIs or functions to accomplish complex tasks beyond text generation. 

- **WebArena** : `WebArena` ( `https://webarena.dev/` ) is a realistic, open-ended web environment idx_5fa2fc31where agents can be evaluated onidx_ccf50480 their ability to navigate and interact with dynamic websites. It offers a browser-based setting for benchmarking goal completion, planning, and handling noisy or unexpected layouts. 

- **Mind2Web** : `Mind2Web` ( `https://osu-nlp-group.github.io/Mind2Web/` ) is a benchmark idx_046aab48for evaluating agents on their abilityidx_1f9e6c90 to perform user-specified tasks on websites using human-like reasoning and planning. It simulates diverse web-based tasks and provides annotations for goals, subgoals, and reasoning chains to assess interpretability and robustness. 

Benchmarks idx_926b4f95are useful to compare agentic AI systems in particular domains and tasks, but it is even more important to understand the goals and intentions of your users and customers. For example, your system may score lower on a particular benchmark but run much faster and at a lower cost, which may be a better value proposition. 

_Chapter 2_ 

56 

###### **Summary** 

In this chapter, we took a deep dive into the operational flow of agentic AI systems driven by large language models. We introduced the core agent loop – sense, think, act – and illustrated how it operates in frameworks such as AutoGen, where the LLM dictates the agent’s behavior through tool calls. We explored how agents use memory, goals, and state management within the constraints of the LLM’s context window, and how these responsibilities are handled by the surrounding AI framework or system. 

We also examined the importance of planning and reasoning mechanisms, both in singleagent and multi-agent systems. With the rise of specialized reasoning models and the growing complexity of agent workflows, structuring interactions and decomposing tasks become essential for robust behavior. Then, we turned our attention to tool use, which is a critical enabler of agentic capability. After all, even the most intelligent LLM can observe or impact the outside world only as far as its tools reach. 

Finally, we looked at evaluation and feedback. These mechanisms allow agentic AI systems to improve over time. We covered both human and automated feedback strategies and reviewed standardized benchmarks that allow for objective comparison across systems. These practices are essential not only for improving the performance of individual agents but also for debugging, compliance, trustworthiness, and long-term system evolution. 

Overall, the concepts and patterns described in this chapter form the operational backbone of modern agentic AI. As the field matures, the sophistication of these components will continue to grow, but the core principles, which include clear agent loops, transparent tool use, contextaware reasoning, precise memory management, and systematic evaluation, will remain foundational. 

In the next chapter, we will take it all the way down to the code level and examine, in great detail, the implementation of a simple yet full-fledged agentic AI system that operates as an AI Kubernetes engineer. 

_Understanding How AI Agents Work_ 

57 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns – _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and generative AI systems. Subscribe now and receive a free eBook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OFA<br>a<br><!-- End of picture text -->

# 3 

##### A Hands-On Walk-Through of a Simple AI Agent 

In _Chapter 2_ , we explored the foundational concepts of AI agents, their architecture, components, and how they interact with tools and external systems. We also discussed how these principles, such as the agentic loop and memory, are implemented **i** dx_3534ab4c n the popular AutoGen ( `https://github.com/microsoft/autogen` ) framework. In this chapter, we will build on that knowledge by dissecting a simple AI agent, k8s-ai, that can interact with a Kubernetes cluster one line at a time. The power of AI agents with tool access will become evident as we walk through the code and understand exactly how an agent loop works. And combining this simple agent with a tool to access Kubernetes will demonstrate how even such a basic setup can be very capable. 

We will set the stage by introducing the k8s-ai agent and showcasing its capabilities by running it and interacting with it through a chat interface. Once you have experienced the agentic capabilities of k8s-ai, we will explain how the agentic system works under the hood. 

In this chapter, we will cover the following main topics: 

- Introducing k8s-ai 

- Understanding the k8s-ai agentic system 

- 

_Chapter 3_ 

60 

###### **Technical requirements** 

Ensure you have kubectl, Docker, and kind installed on your machine. If you don’t have them installed, follow the installation instructions here: 

- Kubectl installation instructions ( `https://kubernetes.io/docs/tasks/tools/` ) 

- Docker installation instructions ( `https://docs.docker.com/engine/install/` ) 

- 

- kind installation instructions ( `https://kind.sigs.k8s.io/docs/user/quickstart/ #installation` ) 

Briefly, here’s why we need these: 

- **kubectl** is the command-line tool used to interact with and manage Kubernetes clusters by sending commands to the Kubernetes API server. 

- **Docker** is a container platform that packages applications and their dependencies into lightweight, portable containers that run consistently across different environments. 

- **Kubernetes in Docker (KinD)** is a tool for running local Kubernetes clusters using Docker containers as the cluster nodes, mainly for development and testing. 

You should use the latest version when you read the chapter. 

If you want to follow along with the code examples in this chapter, ensure you have Python ( `https://www.python.org/downloads/` ) installed. 

You’ll also need an OpenAI API key, which you can obtain from the OpenAI platform: `https:// platform.openai.com/api-keys` . 

You can follow the instructions in README.md ( `https://github.com/PacktPublishing/ Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/blob/main/ch03/k8s-ai/README.md` ) or ( `https://github.com/the-gigi/k8s-ai/blob/main/README.md` ) to get your k8s-ai agent up and running. 

###### **Introducing the k8s-ai agent** 

The **k8s-ai agent** ( `https://github.com/the-gigi/k8s-ai` ) is a idx_26b08bf9simple AI agentidx_76e9955f implemented in a single Python file and can interact with a **Kubernetes** ( `https://kubernetes.io/` ) cluster idx_5c4662c5via the **kubectl** ( `https://kubernetes.io/docs/reference/kubectl/` ) tool. If you’re not familiar with Kubernetes, it’s idx_d797d46anot a big deal. In one sentence, it is an open source system for automating the deployment, scaling, and management of containerized applications. The kubectl tool is the command-line interface for interacting with Kubernetes clusters. 

Before diving in, let’s take it for a ride and see what it can do. 

_A Hands-On Walk-Through of a Simple AI Agent_ 

61 

###### **Setting up a local kind cluster** 

Let’s start byidx_34679623 setting up a local Kubernetes cluster using kind ( `https://kind.sigs.k8s.io/` ). Kind is a tool for running Kubernetes clusters in Docker containers. It is ideal for local development and testing. 

We can create a local Kubernetes cluster using kind. Run the following command to create a cluster named `k8s-ai` : 

```
> kind create cluster -n k8s-ai
Creating cluster "k8s-ai" ...
```

`✓ Ensuring node image (kindest/node:v1.33.1) ✓ Preparing nodes` 📦 `✓ Writing configuration` 📜 `✓ Starting control-plane ✓ Installing CNI` 🔌 `✓ Installing StorageClass` 💾 `Set kubectl context to "kind-k8s-ai" You can now use your cluster with:` 

`kubectl cluster-info --context kind-k8s-ai Have a nice day!` 👋 

Let’s verify the cluster is up and running: 

```
kubectl cluster-info --context kind-k8s-ai
```

The Kubernetes control plane is running at `https://127.0.0.1:52864` . 

`CoreDNS` is running at `https://127.0.0.1:52864/api/v1/namespaces/kube-system/ services/kube-dns:dns/proxy` . 

To further idx_891362dd debug and diagnose cluster problems, use `kubectl cluster-info dump` . 

Great! We have a local Kubernetes cluster up and running. Now, let’s cause some trouble in the cluster. Here is a deployment that will never be ready because it requires its pods to be scheduled on a node with a label that doesn’t exist in the cluster: 

```
echo '
apiVersion: apps/v1
kind: Deployment
```

_Chapter 3_ 

62 

```
metadata:
  name: some-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: some-app
  template:
    metadata:
      labels:
        app: some-app
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: no-such-node
                    operator: In
                    values:
                      - "true"
      containers:
        - name: pause
          image: registry.k8s.io/pause:3.9
' | kubectl apply -f -
deployment.apps/some-app created
```

Let’s confirm idx_8ff7140dthat all the pods were created, but they are all pending because of the label requirement: 

```
kubectl get po
NAME                        READY   STATUS    RESTARTS   AGE
some-app-65696dbff4-8jdrj   0/1     Pending   0          6s
some-app-65696dbff4-mbfv7   0/1     Pending   0          6s
some-app-65696dbff4-wj9ms   0/1     Pending   0          6s
```

_A Hands-On Walk-Through of a Simple AI Agent_ 

63 

We can even see the exact reason why the pods are pending ( `1 node(s) didn’t match Pod’s node affinity/selector.` ) by checking the status of one of the pods: 

```
kubectl get po some-app-65696dbff4-8jdrj -o yaml | grep status: -A 10
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2025-06-05T08:45:45Z"
    message: '0/1 nodes are available: 1 node(s) didn''t match Pod''s node
affinity/selector.
      preemption: 0/1 nodes are available: 1 Preemption is not helpful for
scheduling.'
    reason: Unschedulable
    status: "False"
    type: PodScheduled
  phase: Pending
  qosClass: BestEffort
```

Let’s cause some more havoc and create a deployment for NGINX (a popular web server) with an invalid image name (nnnnnnnnginx): 

```
echo '
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nnnnnnnnginx
' | kubectl apply -f -
```

_Chapter 3_ 

64 

```
deployment.apps/nginx created
```

Let’s checkidx_c651f1bc the status of our cluster now: 

|`kubectl get po`|||
|---|---|---|
|`NAME`|`READY`|`STATUS             RESTARTS   AGE`|
|`nginx-74f5dd8d8f-p2hmh`|`0/1`|`ImagePullBackOff   0          91s`|
|`some-app-65696dbff4-8jdrj`|`0/1`|`Pending            0          9m3s`|
|`some-app-65696dbff4-mbfv7`|`0/1`|`Pending            0          9m3s`|
|`some-app-65696dbff4-wj9ms`|`0/1`|`Pending            0          9m3s`|

We have two deployments: **some-app** and **nginx** . The **some-app** deployment has three pending pods, and the **nginx** deployment has one pod in an error state due to an invalid image name. Now, let’s see how we can use the k8s-ai agent to help us with this situation. 

###### **Running the k8s-ai agent** 

First, you idx_351ea5cfneed to clone the k8s-ai repository: 

```
git clone git@github.com:the-gigi/k8s-ai.git
```

Follow the instructions in the `README.md` ( `https://github.com/PacktPublishing/DesignMulti-Agent-AI-Systems-Using-MCP-and-A2A/blob/main/ch03/k8s-ai/README.md` ) to run and interact with k8s-ai. 

After activating the virtual environment, just run the agent with the following command: 

```
python main.py
```

You will see the following output and you can start interacting with the agent: 

`Interactive Kubernetes Chat. Type 'exit' to quit. ----------------------------------------------------` 👤 `You:` 

K8s-ai is running idx_bd15e52eand ready for interaction. Let’s check our cluster via natural language conversation. 

_A Hands-On Walk-Through of a Simple AI Agent_ 

65 

###### **Checking the cluster with k8s-ai** 

All theidx_aef8f6ec foundation models were trained extensively on Kubernetes knowledge, including on the kubectl CLI, and therefore should be able to meaningfully interact with our Kubernetes cluster. Alright, let’s ask the agent about our Kubernetes cluster: 

👤 `You: what's going on in the cluster?` 🤖 `AI: Here's a summary of the current state of the cluster: ### Pods - **default namespace:** - `nginx-74f5dd8d8f-p2hmh`: Not ready, experiencing `ImagePullBackOff`, running for 6 hours and 27 minutes. - `some-app` instances (3 pods): All pending for 37 hours. - **kube-system namespace:** - Core system components (e.g., `coredns`, `etcd`, `kube-apiserver`, `kubecontroller-manager`, etc.) are running smoothly. - **local-path-storage namespace:** - `local-path-provisioner`: Running smoothly. ### Services - `kubernetes`: ClusterIP service. - `kube-dns`: ClusterIP service in the `kube-system` namespace. ### DaemonSets - `kindnet` and `kube-proxy` are running in the `kube-system` namespace. ### Deployments - **default namespace:** - `nginx`: Deployment not available due to `ImagePullBackOff`. - `some-app`: No pods are ready. - **kube-system namespace:** - `coredns`: 100% ready.` 

_Chapter 3_ 

66 

```
- **local-path-storage namespace:**
    - `local-path-provisioner`: 100% ready.
### ReplicaSets
- The `nginx` and `some-app` ReplicaSets in the `default` namespace have issues
due to readiness, likely tied to their
  pods' issues.
- Other ReplicaSets under `kube-system` and `local-path-storage` are scaled as
expected and operational.
### Observations
- The `nginx` and `some-app` deployments are facing
issues. `nginx` is failing due to an image pull issue which could be
  a configuration problem or a registry access issue.
- The `some-app` deployment may be facing resource constraints or unsatisfied
scheduling rules causing the pods to be
  pending.
Would you like assistance in addressing any specific issues?
----------
```

That’s pretty cool! The idx_3193b527agent has provided a detailed summary of the cluster’s state, including the status of pods, services, deployments, and more. It has also identified the issues with the **nginx** and **some-app** deployments. 

Let’s drill down some more and see if it can identify the exact root cause of the pending pods: 

👤 `You: find out why the some-app pods are pending` 🤖 `AI: The "some-app" pods are in a "Pending" state because they cannot be scheduled. Specifically, the issue is that: - The pod couldn't be scheduled due to node affinity or selector requirements not being met. The error message indicates that there are no nodes available that match the pod's node affinity or selector. - The scheduler also notes that preemption is not helpful in this case, meaning that even if lower-priority pods were evicted, it would not resolve the scheduling issue for the "some-app" pods.` 

_A Hands-On Walk-Through of a Simple AI Agent_ 

67 

```
To resolve this, you may need to check the node affinity or selector requirements
specified for these pods and ensure they can be satisfied by the current nodes in
your
cluster. Adjusting these requirements or adding nodes that match the criteria
might be necessary.
```

That’s correct. The agent has identified that `some-app` pods are pending due to node affinity or selector requirements not being met. It also suggests checking the node affinity or selector requirements idx_5fd9e971specified for these pods and ensuring they can be satisfied by the current nodes in the cluster. How about we ask the agent to fix this for us? Note that in some cases, you may get general answers, and you may flex your prompting skills to get more specific: 

👤 `You: suggest concrete solutions to fix this. don't ask me to check anything. you check.` 

🤖 `AI: The root cause of the `some-app` pods being in a pending state is due to a node affinity constraint in the pod's specification that is not satisfied by the available nodes in the cluster.` 

###### `### Findings:` 

```
1. **Node Affinity Issue**: The pods in the `some-app` deployment have a node
affinity that requires scheduling on nodes with the label `no-such-node=true`.
2. **Cluster Node Details**: The available node `k8s-ai-control-plane` does not
have this label. This is the primary reason why the pods cannot be scheduled.
```

###### `### Recommended Solutions:` 

```
1. **Modify Node Affinity**:
```

```
   - **Option A**: Update the `some-app` deployment to remove the node affinity
requirement that is not meeting any existing nodes.
```

```
   - **Option B**: If node affinity is essential, ensure that appropriate nodes in
the cluster are provisioned with the required labels (`no-such-node=true`).
```

```
2. **Label the Existing Node**:
```

```
   - As an immediate fix, if the affinity constraint is not critical, you could
label the existing `k8s-ai-control-plane` node with the required label:
     ```bash
kubectl label nodes k8s-ai-control-plane no-such-node=true
     ```
```

```
3. **Review Other Constraints**:
```

_Chapter 3_ 

68 

```
   - Ensure other scheduling constraints such as resource requests and limits are
compatible with the available nodes.
Implement the first option (modifying the pod's affinity requirement or updating
the node labels) based on whether the affinity requirement is crucial to the
workload. Adjust the configuration accordingly and redeploy the application to
solve the scheduling issue.
```

The agent identified the exact root cause of the pending pods correctly and provided concrete solutionsidx_274ff8a5 to fix it. Option #3, `**Review Other Constraints**` , is still not concrete enough because the agent could have already run these checks, but we will let it go because the first two solutions are good enough. So far, the agent has performed only read operations on our cluster. 

Let’s ask it to execute one of the solutions and label the node with the required label: 

👤 `You: Go ahead with solution #2 and label the node with no-such-node=true` 🤖 `AI: The node `k8s-ai-control-plane` has been successfully labeled with `nosuch-node=true`. The `some-app` pods should now be scheduled correctly. You can verify their status by checking the pods again. ----------` 

Excellent! The agent says it has successfully labeled the node with the required label. Let’s check the status of the pods again: 

|`kubectl get po`|||
|---|---|---|
|`NAME`|`READY`|`STATUS             RESTARTS   AGE`|
|`nginx-74f5dd8d8f-p2hmh`|`0/1`|`ImagePullBackOff   0          6h46m`|
|`some-app-65696dbff4-8jdrj`|`1/1`|`Running            0          15m34s`|
|`some-app-65696dbff4-mbfv7`|`1/1`|`Running            0          15m34s`|
|`some-app-65696dbff4-wj9ms`|`1/1`|`Running            0          15m34s`|

_A Hands-On Walk-Through of a Simple AI Agent_ 

69 

It worked! Our AI agent can diagnose problems in our cluster, suggest solutions, get permissions from a human in the loop, and fix problems. 

OK. Let’s go crazy and ask the agent to fix the `nginx` deployment completely on its own: 

👤 `You: nice, it works! now go ahead an fix the nginx problem on your own. just tell me in the end what you did.` 🤖 `AI: I resolved the issue with the `nginx` deployment by updating its image from an incorrect image URL (`nnnnnnnnginx`) to the correct image (`nginx`). This allows Kubernetes to successfully pull the image and start the pod. If there are any further problems or something else you need, feel free to ask! ----------` 

This is great! The agent exercises judgment and correctly surmises that if the deployment name is `nginx,` the correct image is `nginx` as well. But, as always, let’s check the status of the nginx pods to confirm the fix: 

```
kubectl get po -l app=nginx
NAME                     READY   STATUS    RESTARTS   AGE
nginx-5869d7778c-kbpjz   1/1     Running   0          2m30s
```

Yes! A new pod wasidx_083a9d25 created, and it is running. The agent fixed the problem on its own without any human intervention. 

Now, we’re ready to dive deeper into the code and understand how the k8s-ai agent works under the hood. We will explore the code structure of k8s-ai. 

_Chapter 3_ 

70 

###### **Understanding the k8s-ai agentic system** 

Before we idx_f3b09142jump into the code, let’s understand how agentic AI system principles align with k8s-ai. 

<!-- Start of picture text -->
K8S-Al<br>pO<br>} Tool definition)!<br>'1<br>U<br>kubectl !<br>1<br>f1y<br>' '<br>f 1 kubectl<br>uv ——>]| Al System |——>| Agentic Loop | >| Kubernetes<br>eet <=—||_ maini) <— send() } <— ‘cluster<br>'i<br>:’<br><!-- End of picture text -->

_Figure 3.1: K8s-ai agentic workflow_ 

In the diagram of k8s-ai, you can see the following: 

1. Users interact with the `main()` function of k8s-ai that serves as the controlling AI system. 

2. It invokes the agentic loop implemented by the `send()` function. 

- The `send()` function uses the tool definition that includes only the kubectl tool. 

3. 

4. The `send()` function sends the user’s prompt to the LLM, which may return tool requests to invoke kubectl. 

5. The `send()` function idx_4fb4589cwill execute these kubectl commands against the Kubernetes cluster and return the results to the LLM, until the LLM returns a final response that the `send()` function will return to the `main()` function, which will display it to the user and be ready to receive a new query from the user. 

Having understood the workflow of the k8s-ai agent, let’s now look at how it is implemented. 

_A Hands-On Walk-Through of a Simple AI Agent_ 

71 

###### **Code walk-through of the k8s-ai agent** 

Let’s start idx_1c707c98by looking at the `main.py` file in the k8s-ai repository at a high level without too much detail. 

1. **The imports** : The k8s-ai agent imports the built-in packages, such as `json` and `os` , and then it imports the third-party libraries `sh` and `openai` . 

```
import json
import os
import sh
from openai import OpenAI
```

The `json` package is used to parse responses from the OpenAI API, the `os` package is used to access environment variables such as `OPENAI_API_KEY` , the `sh` module is used to run shell commands ( `kubectl` in this case). 

2. **The OpenAI client** : Theidx_2bf6ce4e k8s-ai agent uses the official OpenAI Python client to interact with the OpenAI API. It initializes the client with the API key from the environment variable. This is actually not needed since, by default, the OpenAI client will look for this exact environment variable, but I prefer to explicitly set such variables in the code for clarity and not rely on obscure default behavior. The model I use here is `gpt-4o` , which is a powerful model that can handle the task at hand. 

```
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
model_name = "gpt-4o"
```

###### **Note** 

Note that the client is not initialized with the `model` parameter. This is because the model is specified in every API request. This allows for more flexibility in case you want to change the model later without modifying the client. The k8sai agent always uses the same model for all requests, but this is not a requirement. 

More sophisticated agentic systems will often use different models from different providers for different tasks, but k8s-ai, while very powerful, as we have already seen, is designed for simplicity and educational purposes. 

_Chapter 3_ 

72 

3. **The tools** : As idx_d2c8ee1dwe have mentioned several times, AI agents are as capable as the tools they have access to. The k8s-ai agent defines a list of tools, which contains just one tool in this case. This tool is a wrapper around the `kubectl` command line. We will explore it in more detail in the next section. 

```
tools = [{
    ...
}]
```

4. **The agentic loop** : The idx_964806fcagentic loop is the core of the k8s-ai agent. It accesses a list of messages, which is a list of dictionaries, and it returns the final response as a string. We will see how this loop works in detail soon, but for now, here is the signature of the `send()` function that completely encapsulates the entire agentic loop: 

```
defsend(messages: list[dict[str, any]]) -> str:
    ...
```

5. **The main() function** : Finally, the `main()` functionidx_7ad0d557 is the entry point of the k8s-ai agent. It initializes the messages list with a system, manages the interaction with the user, and delegates all the heavy lifting to the `send()` function. We will see how it does it later, in the _Implementing the tool-calling execution loop_ section. 

```
defmain():
...
if __name__ == "__main__":
         main()
```

Next up, let’s see how to work with OpenAI tools for our agent. 

_A Hands-On Walk-Through of a Simple AI Agent_ 

73 

###### **Defining and registering tools with OpenAI** 

Our k8s-ai agentidx_a16152e3 is designed to interact with the OpenAI client and use the kubectl tool to manage a Kubernetes cluster. It needs to adhere to the format of the OpenAI API for defining tools. It’s important to note that there are different idx_4e3aee2btypes of tools. The k8s-ai agent uses function calling, which is a tool of type `"function"` . A function tool has a name, a description, parameters, and a list of required parameters. You can also specify if it operates in strict mode. See OpenAI’s documentation ( `https://platform.openai.com/docs/guides/functioncalling#defining-functions` ) for more details. 

Here is the complete definition of the k8s-ai tools list (it contains only the `kubectl` tool): 

```
tools = [{
"type": "function",
"function": {
"name": "kubectl",
"description": "execute a kubectl command against the current k8s
cluster",
"parameters": {
"type": "object",
"properties": {
"cmd": {
"type": "string",
"description": (
"thekubectl command to execute (without kubectl, just "
"the arguments). For example, 'get pods'"
                    ),
                },
            },
"required": ["cmd"],
        },
    },
}]
```

_Chapter 3_ 

74 

Let’s break it down piece by piece: 

1. **Tools list** : The `tools` variable is a list, which allows you to define one or more tools. Each item in the list is a dictionary that represents a single tool. In this case, we define just one tool, the `kubectl` function. 

```
tools = [
    {
    ...
    }
]
```

2. **Type** : This tells the OpenAI API that the tool is a function tool. Function tools use function calling, where the model can automatically select and call the tool using arguments it constructs. The rest of the tool definition is nested under a `"function"` sub-dict. 

```
"type": "function"
"function": {
    ...
}
```

3. **Name** : This is the idx_940e80b0name the model will use to call this tool. It should be short, descriptive, and unique in the context of all the tools you register. In this case, the name is `kubectl` , which is a good choice since it is a well-known tool that the LLM encountered using its training. 

```
"name": "kubectl"
```

4. **Description** : The description provides additional context beyond its name about what the function does. It should be clear and concise, explaining the purpose of the tool and how it can be used. In this case, the description is pretty basic since the LLM should already know what kubectl is. 

The function description must contain all the information that is necessary for the model (LLM) to decide if it should invoke the tool or not in any given situation. 

```
"description": "execute a kubectl command against the current k8s cluster"
```

_A Hands-On Walk-Through of a Simple AI Agent_ 

75 

###### **Tip** 

It is always the LLM that makes the decision based on the information passed to it (prompt and tools descriptions). In k8s-ai, the AI system is a simple chat interface that prints the final response from the LLM and waits for user input. 

Remember our discussion on AutoGen ( _Chapter 2_ ), which has a lot of abstractions. It also needs to convert all the information from these abstractions to a prompt and tools description that it sends to the LLM. In general, the AI system built on top of the AI framework that receives the final response of each agentic loop may decide to run additional custom code and not just display the final response. 

5. **Parameters** : The parameters specify the input that the function expects. They are defined in a JSON Schema format, where the type is always `"object"` and the `"properties"` field contains the specific parameters that the function accepts. Each parameter has a name ( `"cmd"` here), a type ( `"string"` in this case), and a description that explains what the parameter is for. Since kubectl has many sub-commands, each with its own parameters, we only define a single string parameter to represent the entire command to execute. Again, we rely here on the LLM’s training to understand how to construct kubectl commands. The `cmd` parameter is also marked as required. The kubectl command idx_ef2a298 **c** an execute with no parameters, but it just displays the help, which is not very useful in this case. So, we require the `cmd` parameter to be provided by the model when it calls the tool. 

```
"parameters": {
"type": "object",
"properties": {
"cmd": {
"type": "string",
"description": (
"thekubectl command to execute (without kubectl, just "
"the arguments). For example, 'get pods'"
            ),
        },
    },
"required": ["cmd"],
}
```

_Chapter 3_ 

76 

Note that there is no output defined for functions. This means that the model doesn’t know the shape and structure of the result of a function call. The model will receive the output as a string, which it can then parse and figure out how to use. This is a common pattern when using LLMs with tools, as the model can handle a wide variety of outputs and doesn’t need to know the exact structure in advance. Requiring the developers to specify the output structure could cause a lot of friction and can be challenging for tools like kubectl that can return a wide variety of outputs and output formats. 

###### **Implementing the tool-calling execution loop** 

Now, let’s take a idx_01984860closer look at the agentic loop and how it interacts with the OpenAI API to call the kubectl tool. This is the core of the k8s-ai agent, where it sends messages to the OpenAI API, receives responses, and executes the kubectl command. Surprisingly, the agentic loop is quite simple and consists of just 18 lines of code. Here is the complete code: 

```
defsend(messages: list[dict[str, any]]) -> str:
    response = client.chat.completions.create(
        model=model_name, messages=messages,
        tools=tools, tool_choice="auto")
    r = response.choices[0].message
if r.tool_calls:
        message = dict(
            role=r.role,
            content=r.content,
            tool_calls=[dict(id=t.id, type=t.type,
                function=dict(name=t.function.name,
                    arguments=t.function.arguments)
                             ) for t in r.tool_calls if t.function])
        messages.append(message)
for t in r.tool_calls:
if t.function.name == 'kubectl':
                cmd = json.loads(t.function.arguments)['cmd'].split()
                result = sh.kubectl(cmd)
                messages.append(dict(tool_call_id=t.id, role="tool",
                    name=t.function.name, content=result))
return send(messages)
return r.content.strip()
```

_A Hands-On Walk-Through of a Simple AI Agent_ 

77 

Let’s break itidx_c0555842 down step by step: 

1. **The function signature** : This line defines the core loop function, `send()` . It takes a list of message dicts as input (just like OpenAI’s `messages` parameter). It returns the final assistant message content as a string. 

```
defsend(messages: list[dict[str, any]]) -> str:
```

2. **Calling the Chat Completions API** : This line calls the OpenAI API to generate a response based on the provided messages. It uses the `chat.completions.create()` method of the Chat Completions API ( `https://platform.openai.com/docs/apireference/chat` ). 

It passes our fixed model name ( `gpt-4o` ), the list of messages, the list of tools we defined earlier (with `kubectl` as the only tool), and `tool_choice` set to `"auto"` . The `"auto"` setting allows the model to decide whether to use a tool or not based on the current state of the conversation. 

```
    response = client.chat.completions.create(
        model=model_name, messages=messages,
        tools=tools, tool_choice="auto"
)
```

###### **Note** 

OpenAI recently released another API called idx_49b88118 the **Responses API** , which is more powerful and flexible than the Chat Completions API. But k8s-ai doesn’t need all the bells and whistles. 

3. **Get the first response message** : The OpenAI API can return multiple choices in a single response, but in practice, it usually returns just one. So, k8s-ai just goes with the simple case and looks at the first choice only and then extracts its `message` object. 

```
r = response.choices[0].message
```

4. **Check if the response contains tool calls** : If the response contains tool calls, it means that the idx_84a6d078model has decided to use a tool to perform some action. 

```
if r.tool_calls:
```

_Chapter 3_ 

78 

5. **Prepare the tool calls message** : In this case, we need to prepare a `message dict` that contains the role, content, and tool calls. The tool calls are transformed into a list of dictionaries that contain the tool call ID (coming from the LLM), type, function name, and arguments. This is necessary to keep track of the tool calls and their results in the conversation history. 

```
message = dict(
            role=r.role,
            content=r.content,
            tool_calls=[dict(
id=t.id,
type=t.type,
                function=dict(
                    name=t.function.name,
                    arguments=t.function.arguments
                )) for t in r.tool_calls if t.function])
```

Note that there may be multiple tool calls in a single response. Even if we have just one tool registered, the model may decide to invoke it multiple times with different arguments. For example, it may want to run multiple kubectl commands, such as `get pods` , in different namespaces. 

6. **Append the tool calls message to the messages list** : This is pretty straightforward. Just append the `message dict` we just created to the messages list. This is important to keep the thread of conversation up to date. 

```
messages.append(message)
```

7. **Invoke the kubectl tool for each tool call request** : Now, it iterates over each tool call in the response. If the tool call is for the `kubectl` function, it extracts the `cmd` argument and splits it into a list of command-line arguments. For example, `"get pods"` becomes `["get", "pods"]` . Then, it uses the `sh` module to execute the `kubectl` command with the provided arguments. The result of the command execution is stored in the `result` variable. 

```
for t in r.tool_calls:
if t.function.name == 'kubectl':
        cmd = json.loads(t.function.arguments)['cmd'].split()
        result = sh.kubectl(cmd)
```

_A Hands-On Walk-Through of a Simple AI Agent_ 

79 

8. **Append the tool call results to the messages list** : After executing the `kubectl` command, it appends the result to the messages list as a new message with the originalidx_0b0dfeb9 tool ID from the LLM (so the LLM knows which result corresponds to which tool call), the role set to `"tool"` , the function name (will always be `kubectl` in this case), and the content set to the result of the command execution. This is how the agent captures the results of the tool calls and makes them available to the model in the next iteration of the loop. 

```
        messages.append(dict(tool_call_id=t.id, role="tool",
            name=t.function.name, content=result))
```

9. **Recursion to continue the loop** : As long as the model has tool calls in its response, the agent will continue to process them. The `send()` function then calls itself recursively with the updated messages list, which includes all the tool requests from the model and all the tool results. 

```
return send(messages)
```

###### **Tip** 

In a production-ready system, you can have a maximum number of iterations or a maximum time that, if exceeded, the operation is considered a failure and returns an error message to the user. In practice, LLMs already have this mechanism in place, and if they can't converge to a satisfactory solution, they will return an error on their own. 

10. **Return the final response** : Eventually, when there are no more tool calls in the response, the `send()` function returns the content of the final response from the model. 

```
return r.content.strip()
```

Note that we don’t return the entire response object or all the message list, but just the content idx_7d962397of the last message. Some AI frameworks may provide hooks to access the complete history of messages, but again, k8s-ai is designed to be simple. 

Let’s now interact with this agent. 

_Chapter 3_ 

80 

###### **Running and interacting with the Kubernetes chat agent** 

Last, but idx_2adad61dnot least, k8s-ai provides anidx_81aed99b interactive **command-line interface** ( **CLI** ) to interact with the agent. 

1. The `main()` function first prints a welcome message and initializes the messages list with a system message that sets the context for the agent. 

```
defmain():
print(" Interactive Kubernetes Chat. Type 'exit' to quit.\n" + "-" *
52)
    messages = [{'role': 'system', 'content': 'You are a Kubernetes expert
ready to help'}]
```

2. Then, it starts the interactive loop, waiting for a user message, sending it to the agent, which runs the agentic loop until it gets the final response, prints it to the screen, rinse and repeat. The interactive loop continues until the user types `'exit'` . 

`while (user_input := input("` 👤 `You: ")).lower() != 'exit': messages.append(dict(role="user", content=user_input)) response = send(messages) print(f" AI: {response}\n----------")` 

###### **Note** 

Each user message starts a new agentic loop, but the history of messages is preserved across iterations. This allows the agent to maintain context and continuity in the conversation. The history is stored in memory, so everything disappears when the user types `exit` . 

More sophisticated agents may use a more complex memory management system to store and retrieve messages. 

You've now experienced a complete AI agent from both perspectives: as a user interacting with it to solve real problems, and as a developer understanding its internal mechanics line by line. This hands-on idx_e21e115funderstanding of how messages flow through the agentic loop, how tools are defined and invoked, andidx_ba9f5bfa how simple code can create powerful autonomous behavior forms the foundation for building your own agents. Let's consolidate these insights in the summary. 

_A Hands-On Walk-Through of a Simple AI Agent_ 

81 

###### **Summary** 

In this chapter, we went beyond theory and saw an AI agent in action, controlling a real Kubernetes cluster with a mix of autonomy, reasoning, and tooling. The k8s-ai agent, built in 61 lines of Python (including empty lines and imports), is extremely capable. Despite its simplicity, it demonstrates several foundational AI agent capabilities. 

The system is capable of inspecting the state of the cluster using kubectl, allowing it to observe current conditions effectively. It leverages the OpenAI API to diagnose issues and identify root causes. It understands both when and how to use kubectl, not only to gather information but also to make necessary changes. The system operates with a human-in-the-loop approach, requesting permission before making any modifications unless explicitly instructed to act autonomously. Throughout its operation, it maintains conversation context, invokes tools as needed, and feeds the resulting outputs back into the language model, forming a coherent agentic loop. 

We created broken deployments, confused the scheduler, and even sabotaged a container image in a KinD cluster. The k8s-ai agent handled all of it. We saw how the OpenAI functioncalling interface, paired with a single well-defined tool and a few lines of glue code, can bring an LLM-powered agentic AI system to life, including an interactive chat interface. 

More broadly, this chapter made the case that AI agents don’t have to be bloated, brittle, or over-engineered. With a clear understanding of how they operate – messages, tools, memory, and an agentic loop – you can build useful, reliable systems that augment human workflows or even run autonomously in controlled environments. 

In the next chapter, we will start the journey to build a full-fledged agentic AI framework based on the same principles as k8s-ai. 

_Chapter 3_ 

82 

###### **Get This Book’s PDF Version and Exclusive Extras** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
i<br>4<br>|<br>e<br>aeé<br>[=] :<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require an invoice._ 

## Part 2 

### Building Your Own Agentic AI Framework 

_Part 2_ walks you through building a real agentic AI framework (AI-6) from the ground up. You’ll explore the core engine that runs the agent loop, manages memory, sessions, tools, and multiple LLM providers, then dive into designing robust, provider-agnostic tools with schemas, validation, and execution flow. The part then shifts to user-facing interfaces, showing how to build Slack and web UIs that support visibility, control, and human-in-theloop workflows. It closes by integrating the framework with the **Model Context Protocol** ( **MCP** ), enabling standardized tool discovery and interoperability across the broader ecosystem. 

This part contains the following chapters: 

- _Chapter 4, Building a Tool-Based Agentic AI Framework_ 

- 

- _Chapter 5, Implementing Custom Tools_ 

- 

- _Chapter 6, Creating Chat Interfaces Using Slack and Chainlit_ 

- 

- _Chapter 7, Integrating with the Model Context Protocol Ecosystem_ 

- 

# 4 

##### Building a Tool-Based Agentic AI Framework 

In the previous chapter, we ventured beyond theory and observed an AI agent in action, specifically controlling a real Kubernetes cluster with a mix of autonomy, reasoning, and tooling. Through the concise yetidx_60bbfa86 powerful **k8s-ai agent** ( `https://github.com/the-gigi/k8sai` ), we demonstratedidx_eaed1311 foundational AI agent capabilities such as observation, diagnosis, tool usage, maintaining a human-in-the-loop interaction, and employing an agentic loop. This agent, developed in just 61 lines of Python, is an impressive demonstration of the power of AI agents and LLMs. 

In this chapter, we will start to develop a more complex and full-fledged AI framework called AI-6 ( `https://github.com/Sayfan-AI/AI-6/tree/v0.8.0` ). AI-6 will allow idx_fd331437us to explore the full spectrum of AI agent capabilities, such as sophisticated memory management, advanced tool management facilities, and support for multiple LLM providers. AI-6 is idx_85dc7618highly unopinionated and highly extensible via tools. Its primary design principle is to keep it simple by providing a small set of core features that allow building more sophisticated AI systems on top of it by adding dedicated tools. 

AI-6 is a Python framework that has a backend and a frontend. In this chapter, we will focus on the backend. In _Chapter 5_ , we will add tools to AI-6. In _Chapter 6_ , we will focus on the frontend. 

We will first start with an overview of the framework's backend architecture and its components, then we will dive deeper into some critical aspects of the framework, such as tool management, memory management, and the message processing pipeline. 

Finally, we will explore how to extend the framework with new tools and LLM providers. 

_Chapter 4_ 

86 

In this chapter, we will cover the following main topics: 

- AI-6 framework backend architecture and components 

- 

- Tool system architecture 

- 

- Memory management 

###### **Technical requirements** 

If you want to run and experiment with AI-6 while reading the chapter, follow the setup instructions in the `README.md` file ( `https://github.com/PacktPublishing/Design-MultiAgent-AI-Systems-Using-MCP-and-A2A/blob/main/ch04/ai-six/README.md` ). 

This will create a virtual environment and install all the necessary dependencies for both the backend and frontend components. 

###### **AI-6 framework backend architecture and components** 

The AI-6 backend isidx_c65917bb powered by a **core engine** thatidx_dca4e614 runs an agentic loop, manages tools, supports any LLMidx_5e720907 provider by offering a generic LLM provider interface, and has a memory management system. The session manager is responsible for managing the sessions (history of messages) with each user. It utilizes the `Session` class for storing the entire content of a single conversation. The tool system is an extensible sub-system for defining tools and provides useful base classes for tool implementation. The LLM providers are another extensible subsystem that defines a generic LLM provider interface and provides a couple of implementations (OpenAI and Ollama at the moment). 

<!-- Start of picture text -->
Engine<br>py/backend/engine/engine.py<br>Session Manager Tool System LLM Providers<br>py/backend/engine/session_manager.py py/backend/tools/ py/backend/Iim_providers/<br>Session<br>py/backend/engine/session.py<br><!-- End of picture text -->

_Figure 4.1: AI-6 core engine_ 

Let’s see how the core engine works. 

_Building a Tool-Based Agentic AI Framework_ 

87 

###### **Core engine** 

The core idx_84397c48engine is the heart of idx_e05f70aathe AI-6 framework. It coordinates all interactions with LLM providers, tools, and session management. It provides a unified interface for different frontends to communicate with AI models while maintaining conversation state and executing tool calls. It is implemented in a single class called `Engine` ( `https://github.com/ PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/tree/main/ch04/ ai-six/py/backend/engine` ). 

Using the engine is pretty simple. First, you initialize it with the desired configuration, then you run it to execute the agentic loop. Let's see how it works. 

###### **Initialization** 

The engine, initialized with idx_d4357653LLM provider, tools, and configuration settings, serves as the core component when agentic AI systems use AI-6. The signature is pretty simple; it just takes an instance of the `Config` class that contains all the necessary settings: 

```
def__init__(self, config: Config):
...
```

The following diagram illustrates this process: 

<!-- Start of picture text -->
Config<br>Al System<br>_-init_(self, config: Config)<br><!-- End of picture text -->

_Figure 4.2: AI system initializes the core engine with the config class_ 

The AI system that utilizes the AI-6 framework specifies the configuration for the core engine using a `Config` object. 

Let's look at the `Config` class: 

```
@dataclass
classConfig:
    default_model_id: str
    tools_dir: str
    mcp_tools_dir: str
    memory_dir: str
    session_id: Optional[str] = None
```

_Chapter 4_ 

88 

```
    checkpoint_interval: int = 3
    summary_threshold_ratio: float = 0.8
    tool_config: Mapping[str, dict] = field(
        default_factory=lambda: MappingProxyType({}))
    provider_config: Mapping[str, dict] = field(
        default_factory=lambda: MappingProxyType({}))
```

There is a lot to unpack here. Let’s look at what the `Config` class is composed of: 

- `default_model_id` is the ID of the model that will be used by default when no specific model is requested, which also determines the default LLM provider because each model belongs to exactly one LLM provider 

- `tools_dir` is the directory where the custom AI-6 tools are located, and the `mcp_tools_dir` is the directory where the MCP tools are located 

- `memory_dir` is the directory where the memory files are stored 

- 

- `session_id` is an optional identifier for the session, and it can be used to resume a session from a previous run 

- `checkpoint_interval` is the number of iterations after which a checkpoint will be saved 

- `summary_threshold_ratio` is the ratio of tokens that will trigger a summary of the conversation history 

- Finally, `tool_config` and `provider_config` are mappings that allow you to specify additional configuration for each tool and provider 

Don't worry if it's a bitidx_8bbc0331 overwhelming; we will explain the purpose of each configuration item as we move further in the chapter. 

Let's see how the engine is initialized with this `Config` object. First, we just store `default_model_id` as a class attribute. Nothing fancy here: 

```
classEngine:
def__init__(self, config: Config):
self.default_model_id = config.default_model_id
```

Then, we get the context window size from the `model_info` module based on the default model ID. We use it to calculate the token threshold, which is the number of tokens that will trigger a summary of the conversation history. This is needed because when the conversation history 

_Building a Tool-Based Agentic AI Framework_ 

89 

approaches the context window size of the model, we need to summarize it to avoid exceeding this hard limit. 

```
# Get the context window size from model_info based on the default model
        context_window_size = get_context_window_size(
self.default_model_id)
self.token_threshold = int(
            context_window_size * config.summary_threshold_ratio
        )
```

Next, we initialize the LLM providers. The engine supports multiple LLM providers, which it knows how to locate using the `discover_llm_providers()` method. 

The reason it is not configured via the `Config` object is that adding a new LLM provider is not a common operation for users. But it definitely can be an alternative design approach. 

Once `providers directory` is located and verified to be a directory, the 

`Engine.discover_llm_providers()` method is called. We will explore it in the next section. It returns a list of LLMidx_a1e5339f providers, where each provider may support multiple models. 

```
# Find LLM providers directory
        llm_providers_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "llm_providers"
        )
assert os.path.isdir(llm_providers_dir), (
f"LLM providers directory not found: {llm_providers_dir}"
        )
# Discover available LLM providers
self.llm_providers = Engine.discover_llm_providers(
            llm_providers_dir, config.provider_config
        )
```

The engine uses the list of providers to construct a mapping of model IDs to their respective LLM providers: 

```
self.model_provider_map = {
            model_id: llm_provider
for llm_provider inself.llm_providers
for model_id in llm_provider.models
        }
```

_Chapter 4_ 

90 

Next, we initialize the tools. The idx_4a947137engine supports both custom tools and **Model Context Protocol** ( **MCP** ) tools. The initialization process for tools is similar to that of the LLM providers. The engine calls discovery methods (the directories come from the `Config` object) to find and register the tools. Then, it constructs a dictionary that maps tool names to their respective tool objects. This allows the engine to easily access and invoke tools by their names during the agentic loop. Note that the MCP tools are not used at the moment. We will incorporate the MCP tools in _Chapter 7_ . 

```
# Discover available tools
        tool_list = Engine.discover_tools(
            config.tools_dir, config.tool_config)
# Discover MCP tools
        mcp_tool_list = Engine.discover_mcp_tools(config.mcp_tools_dir)
self.tool_dict = {t.name: t for t in tool_list}
```

The next part of the **i** dx_6143cbaa nitialization workflow is related to memory management. The engine uses a session manager to handle sessions and a session object to manage the conversation history. Then, it sets a couple of attributes related to storing periodic checkpoints. 

```
# Initialize session and session manager
self.session_manager = SessionManager(config.memory_dir)
self.session = Session(config.memory_dir)
# Session-related attributes
self.checkpoint_interval = config.checkpoint_interval
self.message_count_since_checkpoint = 0
```

Next, we set up the session. The summarizer is responsible for summarizing the conversation history when it gets too long and approaches the context window size of the model. Then, we register the memory tools with the engine, which will give users the option to manage the memory directly. 

```
# Instantiate the summarizer with the first LLM provider
self.summarizer = SessionSummarizer(self.llm_providers[0])
# Register memory tools with the engine
self._register_memory_tools()
```

_Building a Tool-Based Agentic AI Framework_ 

91 

Finally, if the configuration includes a session ID, the engine attempts to load this session if it exists. This allows resuming a previous session and continuing the conversation from where it left off. 

```
# Load previous session if session_id is provided and exists
if config.session_id:
            available_sessions = self.session_manager.list_sessions()
if config.session_id in available_sessions:
# Create a new session object
self.session = Session(config.memory_dir)
# Load from disk
self.session.load(config.session_id)
```

To summarize, we **i** dx_a4b35b92 nitialized the engine with the configuration and dynamically loaded LLM providers, custom tools, and MCP tools. Then, we initialized the memory system. Let's see what happens when we run the engine. 

###### **Running the engine** 

Once the engine idx_85520094 is initialized, we can run it to start the session. The `run()` method accepts several `callables` (functions) as arguments. The `get_input_func()` function retrieves user input, `on_tool_call_func()` is a callback that is invoked when a tool is called, and `on_response_func()` is a callback that is invoked when a final response of an agentic loop is generated. These callbacks are implemented by an agentic AI system that uses the AI-6 framework or the built-in frontends of AI-6 itself. They allow the engine to communicate through a generic interface without knowing anything about the specific application or frontend being used. This design allows for flexibility and extensibility, as different agentic AI systems and frontends can implement their own versions of these callbacks. 

The `run()` method will loop until the `get_input_func()` function stops providing input. This means that the engine performs multiple agentic loops (each one consisting of one or more interactions with the LLM and tool calls) and accumulates the conversation history in the session. 

```
defrun(
            self,
get_input_func: Callable[[], None],
on_tool_call_func: Callable[[str, dict, str], None] | None,
on_response_func: Callable[[str], None],
):
```

_Chapter 4_ 

92 

The implementation is pretty simple. It starts by getting the initial input for the current agentic loop and adding it to the session. Then, it also creates a checkpoint if needed. We will discuss checkpoints in the _Memory management_ section. 

```
try:
while user_input := get_input_func():
                message = UserMessage(content=user_input)
self.session.add_message(message)
self._checkpoint_if_needed()
```

The next part is the core of the agentic loop. It calls the `_send()` method, which is responsible for processing the input, with the default model ID and passing the `on_tool_call_func` callback. The `_send()` method handles all the heavy lifting, as we will see soon. The response is then added to the session as an assistant message, and another checkpoint is created if needed. Finally, the `on_response_func` callback is invoked with the response. 

```
                response = self._send(
self.default_model_id, on_tool_call_func)
                message = AssistantMessage(content=response)
self.session.add_message(message)
self._checkpoint_if_needed()
                on_response_func(response)
```

Finally, we haveidx_4a4d495b the `finally` clause, which ensures the session is saved when the `run()` method exits, regardless of whether it succeeded or raised an exception. This is important to ensure that the conversation history is preserved even when things go wrong (e.g., failure due to exceeding the rate limits of the LLM provider). 

```
finally:
# Save the session when we're done
self.session.save()
```

###### **Executing the agentic loop** 

Let's take a idx_2b75600ecloser look at the `_send()` method, which performs a complete agentic loop whenever it is called as part of a session. The `_send()` method takes a `model_id` and an optional `on_tool_call_func` callback as arguments. The `model_id` specifies which model (and by extension, which LLM provider) to use for this agentic loop, and `on_tool_call_func` is a callback that is invoked whenever a tool is called during the loop. 

_Building a Tool-Based Agentic AI Framework_ 

93 

###### **Note** 

If the LLM doesn't need to call a tool and can immediately return the final response, then the provided `on_tool_call_func` callback will just not be called. 

This allows the engine to notify the frontend or application about tool calls, enabling real-time updates and interactions. It returns the final response of the agentic loop, which is the response generated by the LLM after processing the input and executing as many tool calls as necessary. 

```
def_send(
            self,
model_id: str,
on_tool_call_func: Callable[
                [str, dict, str], None
            ] | None = None,
) -> str:
```

The first step in the `_send()` method is to check if the `model_id` is valid and if the corresponding LLM provider is available. If not, this is a critical failure, and the method raises `RuntimeError` . 

```
        llm_provider = self.model_provider_map.get(model_id)
if llm_provider isNone:
raise RuntimeError(f"Unknown model ID: {model_id}")
```

The next step is to send to the selected LLM provider all the session messages and the tool dictionary with the selected model ID. The LLM provider will handle the actual communication with the LLM and return the response. This part is provider-agnostic, as AI-6 uses an abstraction for LLM providers. We will examine it in detail in the next section, _LLM provider abstraction_ . 

```
try:
            response = llm_provider.send(
self.session.messages, self.tool_dict, model_id
except Exception as e:
raise RuntimeError(f"Error sending message to LLM: {e}")
```

_Chapter 4_ 

94 

If the responseidx_35ba600e contains tool calls, we need to process them. The first step is to map the tool call IDs to **Universally Unique Identifiers** or **UUIDs** . This is necessary because some idx_bd04de04LLM providers may return tool call IDs that are not valid UUIDs, and we want to ensure that all tool call IDs are valid UUIDs, which is our provider-agnostic way to identify tool calls. The `generate_tool_call_id()` function is used to generate a new UUID for each tool call ID that is not already a valid UUID. The `id_mapping` dictionary maps the original tool call received from the LLM to a new UUID that the engine generates if needed. If the LLM-provided tool ID is considered valid, it is used as is, and no new UUID is generated. 

```
if response.tool_calls:
# Create a mapping of original IDs to new UUIDs if needed
            id_mapping = {}
for tool_call in response.tool_calls:
# Check if we need to replace the ID with a UUID
if (
not tool_call.idorlen(tool_call.id) < 32
                ):  # Simple check for non-UUID
                    new_id = generate_tool_call_id(tool_call.id)
                    id_mapping[tool_call.id] = new_id
```

Next, we update the tool call IDs in the response if they were replaced with new UUIDs. Since the LLM provider already returns an `AssistantMessage` object, we can work with it directly to update the tool calls. 

```
# Update the tool call IDs in the response if needed
if id_mapping and response.tool_calls:
for tool_call in response.tool_calls:
if tool_call.idin id_mapping:
                        tool_call.id = id_mapping[tool_call.id]
```

Now, the assistant message can be added to the session. 

```
# Add the assistant message with updated tool_calls
self.session.add_message(response)
```

Before we proceed with processing the tool calls, we need to track the tool call IDs from the assistant message and store them in a set that we will use later. 

```
# Track tool_call_ids from this assistant message
            tool_call_ids = set()
```

_Building a Tool-Based Agentic AI Framework_ 

95 

```
for tool_call in response.tool_calls:
                tool_call_ids.add(tool_call.id)
```

At this point, we idx_ **c** f437154 an iterate over the tool calls in the response and process each one. There are several preliminary steps for each tool call before we can execute it, which involve verifying the requested tool is in the tool dictionary, parsing the arguments, and checking if the tool call ID needs to be updated. 

```
# Now process each tool call and add the corresponding tool messages
for i, tool_call inenumerate(response.tool_calls):
                tool = self.tool_dict.get(tool_call.name)
if tool isNone:
raise RuntimeError(f"Unknown tool: {tool_call.name}")
try:
                    kwargs = json.loads(tool_call.arguments)
except json.JSONDecodeError as e:
raise RuntimeError(
f"Invalid arguments JSON for tool '{tool_call.name}'"
                    )
# Get the potentially updated tool call ID
                tool_call_id = tool_call.id
if tool_call.idin id_mapping:
                    tool_call_id = id_mapping[tool_call.id]
```

At this point, we can execute the tool call. The tool is run with the parsed arguments, and the result is captured. Then, we generate a tool message that contains the result of the tool call, the tool name, and the tool call ID, and invoke the `on_tool_call_func` callback if it is provided. This is all done in a `try` block: 

```
try:
# Execute the tool without passing any ID information
                    tool_result = tool.run(**kwargs)
# Create the tool message with the Engine managing the
tool_call_id
                    tool_message = ToolMessage(
                        content=str(tool_result),
                        name=tool_call.name,
                        tool_call_id=tool_call_id,
```

_Chapter 4_ 

96 

`if on_tool_call_func is not None: on_tool_call_func( tool_call.name, kwargs, str(tool_result))` If the tool call fails, we catch the exception and generate an error message instead: `except Exception as e: tool_message = ToolMessage( str(e), name=tool_call.name, tool_call_id=tool_call_id,` 

If the tool call fails, we catch the exception and generate an error message instead: 

The message, whichidx_9e26fa82 is already in a provider-agnostic format, is added to the session, whether it was a success or a failure. Tool call failures don't halt the agentic loop; they are just logged as a tool message with an error in the session. This allows the agent to continue processing other tool calls or generating responses without interruption. The LLM will decide what to do about failed tool calls in the next iteration of the agentic loop. 

```
# Add the tool message (ID is guaranteed to be valid since we manage it)
self.session.add_message(tool_message)
```

Once all the tool calls have been processed and their results have been added to the session, the `_send()` method calls itself recursively. This is where the agentic loop continues. 

```
# Continue the session with another send
returnself._send(model_id, on_tool_call_func)
```

Finally, when the response from the LLM does not contain any tool calls, the method returns the final response's content: 

```
return response.content.strip()
```

Alright. Let's takeidx_2af971b5 a breath here. That was a lot of non-trivial information. Most of the complexity comes from the need to translate between provider-specific tool calls and a provider-agnostic format that the engine uses to manage the session and conversation history. The essence of the agentic loop is exactly the same as the k8s-ai agentic loop. 

OK. Let's now dive deeper into the LLM provider abstraction. 

_Building a Tool-Based Agentic AI Framework_ 

97 

###### **The LLM provider abstraction** 

This is a very important part of idx_2382c2c2the AI-6 framework. The LLM provider abstraction allowsidx_6ec35029 the engine to communicate with any kind of LLM provider through a unified interface. Note that there is an alternative design where the framework supports just the OpenAI API. First, many LLM providers support the OpenAI API directly or through their own compatibility layer (e.g., Google Gemini). Second, there are projects such idx_57d42c83as OpenRouter ( `https://openrouter.ai` ) that operate like a proxy to any LLM provider through the OpenAI API. So, why build a provideragnostic interface? Well, this gives the framework complete control over the interaction with the supported LLM providers, and it doesn't require going through a proxy, which adds latency, cost, and security concerns. Let's see how the LLM provider abstraction is implemented in the AI-6 framework. 

###### **The LLMProvider interface** 

Python's **abstract base classes** ( **ABCs** ) are idx_e14f77f7the perfect vehicle to define the `LLMProvider` interface, which is i **d** x_4a6991bf efined in the `llm_provider.py` file. `LLMProvider` makes the AI-6 framework extensible by allowing developers to implement their own LLM providers that conform to this pretty simple interface. Let's break it down method by method, but first let's look at the imports. 

First, we import the necessary classes and decorators from the `abc` and `typing` standard library modules. Then, we import the `Response` class from the `object_model` module, which is used to represent a generic response from the LLM. 

Finally, we import the `Tool` class from the `tool` module, which represents a tool that can be used by the LLM. These are part of the AI-6 framework's backend architecture. 

```
from abc import ABC, abstractmethod
from typing import Iterator, Callable, Any
from backend.engine.object_model import Response
from backend.engine.tool import Tool
```

Let's move on to the `LLMProvider` class itself and the first method: `send()` . The `send()` method is an abstract idx_c393b7a5method (decorated with `@abstractmethod` and must be implemented by subclasses) that sends a list of messages to the LLM and receives a response. 

_Chapter 4_ 

98 

It also provides the LLM with a dictionary of tools and an optional `model` parameter. The 

method returns a `Response` object, which contains the LLM response as the generic response. 

```
classLLMProvider(ABC):
@abstractmethod
defsend(
        self, messages: list[Message], tool_dict: dict[str, Tool],
        model: str | None = None
) -> AssistantMessage:
"""
        Send a message to the LLM and receive a response.
        :param messages: The list of messages to send.
        :param tool_dict: A dictionary of tools available for the LLM to use.
        :param model: The model to use (optional).
        :return: The response from the LLM.
        """
pass
```

The `stream` method is similar to the `send()` method, but it allows for streaming responses from the LLM as they are generated. It returns an iterator of `Response` objects, which allows the caller to receive chunks of the response before the entire response is complete. This is useful for real-time applications where you want to display the response as it is being generated. Note that the `stream()` method is not an abstract method and has a default implementation that just calls the `send()` method and yields the full response. This means that subclasses can override this method to provide an actual streaming implementation if they support it, or they can use the default implementation that returns the full response at once. 

```
defstream(
    self, messages: list[Message], tool_dict: dict[str, Tool],
    model: str | None = None
) -> Iterator[AssistantMessage]:
"""
        Stream a message to the LLM and receive responses as they are generated.
        :param messages: The list of messages to send.
        :param tool_dict: The tools available for the LLM to use.
        :param model: The model to use (optional).
        :return: An iterator of responses from the LLM.
        """
# Default implementation just returns the full response
yieldself.send(messages, tool_dict, model)
```

_Building a Tool-Based Agentic AI Framework_ 

99 

The model's property is an abstract property that must be implemented by subclasses. It returns a list of model IDs as strings. It's pretty simple. The model ID is a unique identifier for each model supported idx_745eb9a5 by the LLM provider. It is used by the engine to map models to providers and to select the correct provider when a request for a specific model is sent. 

```
@property
@abstractmethod
defmodels(self) -> list[str]:
""" Get the list of available models."""
pass
```

Now that we have covered the `LLMProvider` interface, let’s look at concrete LLM providers that come with AI-6 out of the box. 

###### **The supported providers** 

Let's take a look at the LLM providersidx_e8e65e31 supported by the AI-6 framework at this point in time. AI-6 ships with LLM providers for OpenAI and Ollama, offering both cloud-based and local model options. 

Remember that additional LLM providers may easily be implemented. 

Let’s first look at the OpenAI provider implementation. 

###### **The OpenAI provider** 

The OpenAI provider **i** dx_72fc3519 s implemented in the `openai_provider.py` file ( `https://github.com/ PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/blob/main/ch04/ ai-six/py/backend/llm_providers/openai_provider.py` ). It uses the OpenAI Python SDKidx_31194357 to communicate with the OpenAI API. The provider implements the `LLMProvider` interface and provides the necessary methods to send messages, stream messages, and get the models. Let's look at the OpenAI provider. 

The provider requires an API key to authenticate with the OpenAI API, which is passed to the constructor. It has defaults for the base URL of the API and the model. When the base URL is None, the OpenAI SDK uses the official idx_0c8db911OpenAI API endpoint: `https://api.openai.com/v1` . If you want to use a different LLM provider that has an OpenAI-compatible APIidx_ef02e3dc such as idx_49cffe04Anyscale ( `https://docs.anyscale.com/reference` ), DeepSeek ( `https://api-docs.deepseek.com/` ), SambaNova ( `https://cloud.sambanova.ai/apis` ), or idx_8d99084cCerebras ( `https://inferencedocs.cerebras.ai/resources/openai` ), then idx_ba03ab1dyou need to pass the correct endpoint. 

_Chapter 4_ 

100 

In this regard, the OpenAI provider already supports multiple providers and can be used with OpenRouter too, of course. 

```
from typing import Iterator
from backend.object_model import (
    LLMProvider, ToolCall, Usage, Tool, AssistantMessage)
from openai import OpenAI
classOpenAIProvider(LLMProvider):
def__init__(
        self, api_key: str, base_url = None,
default_model: str = "gpt-4o"
):
self.default_model = default_model
self.client = OpenAI(base_url=base_url, api_key=api_key)
```

The `LLMProvider` interface is defined in terms of the AI-6 data structures, which are LLMprovider-agnostic but contain the same information that is required by the LLMs to process the user messages and request tool calls. So, really, the job of the OpenAI provider is to translate from the AI-6 representation to the representation of the OpenAI Python SDK. 

Here is the `send()` method idx_134ca978 that does exactly that. For example, the OpenAI Python SDK expects the tools to beidx_f6d58e88 defined as a Python `dict` , so the `send()` method uses a private `_tool2dict()` to convert the `tool_dict` to a list of dictionaries that the OpenAI SDK can understand. 

```
defsend(
        self, messages: list[Message], tool_dict: dict[str, Tool],
        model: str | None = None
) -> AssistantMessage:
"""
        Send a message to the OpenAI LLM and receive a response.
        :param tool_dict: The tools available for the LLM to use.
        :param messages: The list of messages to send.
        :param model: The model to use (optional).
        :return: The response from the LLM.
        """
ifnot messages:
raise ArgumentError(
"messages",
"At least one message is required to send to the LLM.")
```

_Building a Tool-Based Agentic AI Framework_ 

101 

```
if model isNone:
            model = self.default_model
        tool_data = [self._tool2dict(tool) for tool in tool_dict.values()]
```

Then, the method uses the OpenAI Python SDK to create a chat completion with the specified model, messages, and tools: 

```
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tool_data,
            tool_choice="auto"
        )
```

Next, the method idx_3455dc08extracts the `tool_calls` field from the response, and if it is `None` , then **i** dx_956885b3 t is converted to an empty list: 

```
        tool_calls = response.choices[0].message.tool_calls
        tool_calls = [] if tool_calls isNoneelse tool_calls
```

It also extracts the usage data from the response, which includes the number of input and output tokens used in the request: 

```
# Extract usage data
        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
```

Finally, it creates an `AssistantMessage` object with the response content, role, tool calls, and usage data. The OpenAI tool calls are converted to the AI-6 `ToolCall` format, which includes the tool call ID, name, arguments, and whether the tool is required. The `required` field is determined by checking if the tool's parameters are required in the tool specification. For example, say the tool is `get_weather_in_city` and it has two parameters: `city` , which is required, and `unit` , which is not required. If the unit is not provided, then the tool will assume the unit is `Celsius` . 

_Chapter 4_ 

102 

In this case, the LLM may decide to call the tool with two parameters, `city: London` and `unit: Fahrenheit` , or with just the required parameter, `city: London` . 

```
return AssistantMessage(
            content=response.choices[0].message.content,
            tool_calls=[
                ToolCall(
id=tool_call.id,
                    name=tool_call.function.name,
                    arguments=tool_call.function.arguments,
                    required=tool_dict[
                        tool_call.function.name].parameters.required
                ) for tool_call in tool_calls if tool_call.function
if tool_calls elseNone,
            usage=Usage(
                input_tokens=input_tokens,
                output_tokens=output_tokens
```

The OpenAI provider also implements the `stream()` method, which allows for streaming responses from the LLM. However, this method is pretty long, so we will not go into the details here. 

In short, it is a generator that processes the LLM’s output in chunks instead of waiting for the entire response to arrive. If you're curious, check out the code at `https://github.com/ PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/blob/main/ch04/ ai-six/py/backend/llm_providers/openai_provider.py` 

###### **Note** 

The default implementation of the `stream()` method doesn’t actually stream and just delegates to the blocking `send()` method (which is mandatory). If the provider does support streaming, as OpenAI does, then it’s possible to override the `stream()` method and adapt it to the specific provider. 

_Building a Tool-Based Agentic AI Framework_ 

103 

The `models` property idx_46a219f9returns the list of available models from the OpenAI API. Itidx_46708d9a uses the OpenAI Python SDK to fetch the information: 

```
@property
defmodels(self) -> list[str]:
return [m.idfor m inself.client.models.list().data]
```

To close the loop, here are the two helper methods that convert the AI-6 tool and `ToolCall` representations to the OpenAI SDK representation of a Python dictionary: 

```
@staticmethod
def_tool2dict(tool: Tool) -> dict:
"""Convert the tool to a dictionary format for OpenAI API."""
return {
"type": "function",
"function": {
"name": tool.name,
"description": tool.description,
"parameters": {
"type": "object",
"required": tool.parameters.required,
"properties": {
                        param.name: {
"type": param.type,
"description": param.description
                        } for param in toolparameters.properties
                    },
                }
            }
        }
@staticmethod
def_tool_call2dict(tool_call: ToolCall) -> dict:
"""Convert a ToolCall to OpenAI API format."""
return {
"id": tool_call.id,
"type": "function",
"function": {
"name": tool_call.name,
"arguments": tool_call.arguments
```

_Chapter 4_ 

104 

```
            }
        }
```

Let's move on to the Ollama provider. 

###### **The Ollama provider** 

Ollama ( `https://ollama.com/` ) is aidx_121b041f local LLM provider that allows you to run models idx_3abfce79on your own machine. This is pretty cool because you don't need to pay an external provider, and you don't idx_46586546have to worry about your sensitive information being exposed. 

The implementation of the Ollama provider is in the `ollama_provider.py` AI-6 file. It also implements the `LLMProvider` interface and provides the necessary methods to send messages and get the models. It doesn't implement the `stream()` method and relies on the default implementation in the base class, the `LLMProvider` , for streaming responses. 

The implementation is pretty similar to the OpenAI provider, but it uses the Ollama Python SDK to communicate with the Ollama API running locally. The provider requires the Ollama client to be installed and available in the system path, and the Ollama service must be running. We will see it in action in _Chapter 6_ . 

Here is theidx_8ccc956b outline of the implementation. I skipped the implementation details of most methods as they are very similar to the OpenAI LLM provider. In the `send()` method, I invoked the actual call to the Ollama SDK, via the `ollama.chat()` method, which sends the messagesidx_c6f23e95 and tools to the Ollama model and returns a response: 

```
import json
from dataclasses import asdict
from backend.object_model import (
    LLMProvider, ToolCall, Usage, Tool, AssistantMessage, Message)
import ollama
classOllamaProvider(LLMProvider):
def__init__(self, model: str):
self.model = model
@staticmethod
def_tool2dict(tool: Tool) -> dict:
"""Convert the tool to a dictionary format for Ollama."""
        ...
```

_Building a Tool-Based Agentic AI Framework_ 

105 

```
@staticmethod
def_fix_tool_call_arguments(messages):
       ...
defsend(
        self, messages: list[Message], tool_dict: dict[str, Tool],
        model: str | None = None
) -> AssistantMessage:
"""Send a message to the local Ollama model and receive a response."""
        .
        .
        .
        OllamaProvider._fix_tool_call_arguments(message_dicts)
        response: ollama.ChatResponse = ollama.chat(
            model,
            messages=message_dicts,
            tools=tool_data
        )
        .
        .
        .
@property
defmodels(self) -> list[str]:
"""Get the list of available models."""
return [self.model]
```

We will now move our focus to how tools are invoked and the underlying architecture. 

###### **Tool system architecture** 

We covered in great detail the core architecture of the AI-6 framework and its components: the core engine, the LLM provider abstraction, and how tools are invoked. Now, let's take a closer look at theidx_f78c65ac extensible tool system architecture. 

The tool system architecture is designed to achieve the following goals: 

- Support custom tools 

- Support MCP tools 

- 

- Allow safe execution of tools 

- 

- Allow control over the set of tools used for each AI-6 session. 

- 

_Chapter 4_ 

106 

Let's examine each aspect. 

###### **Custom tool support** 

The custom toolidx_7e8cd58d architecture, similar to the LLM provider abstraction, is idx_f5380a1dbased on an abstract base class. It allows developers to implement their own tools that conform to an idx_dcc4c913even simpler interface than the LLM provider that provides function-calling capabilities ( `https:// platform.openai.com/docs/guides/function-calling?api-mode=responses` ). This was pioneered by OpenAI, but has been adopted by all the major players. Everything is defined in the `tool.py` file. Let's break it down, starting with the mandatory imports. It imports the ABC base class and the `abstractmethod` decorator from the `abc` module, the `dataclass` decorator from the `dataclasses` module, and the `NamedTuple` class from the `typing` module. 

```
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import NamedTuple
```

Then, we define a `Parameter` class. It's derived from a named tuple (see: `https:// docs.python.org/3/library/collections.html#collections.namedtuple` ) that represents a single argument in a function call with `name` , `type` , and `description` . The benefit of using `NamedTuple` as a base class is that the `Parameter` class is immutable and efficient. 

```
classParameter(NamedTuple):
    name: str
type: str
    description: str
```

The `Tool` class is an abstract base class that represents a tool that can be used by the LLM via function calling. 

Let's check it out. It's pretty simple. It is decorated with the `@dataclass(slots=True)` decorator. The slots make the class instances immutable (no new attributes can be added), use less memory, and provide faster access to attributes. 

The `Tool` class has the following attributes: `name` , `description` , `parameters` , and `required` (parameters that must be provided when executing the tool). This information is provided to the LLM, as we saw earlier in the tools list of each request. The LLM can decide which tools to call and how to go about it. Remember our discussion from _Chapter 3_ , that LLMs can make 

_Building a Tool-Based Agentic AI Framework_ 

107 

these decisions based idx_7a806e0eon the information passed to them using prompt and/or tool descriptions. 

```
@dataclass(slots=True)
classTool(ABC):
    name: str
    description: str
    parameters: list[Parameter]
    required: set[str]
```

The `configure` method is an optional method that can be implemented by subclasses to configure the tool with arbitrary information. It just accepts a `dict` , which can contain anything. For example, a tool that interacts with a database may need a connection string as configuration. 

```
defconfigure(self, config: dict) -> None:
"""Optional: configure the tool with given parameters."""
pass
```

Finally, the `run()` method is anidx_a5ae10b9 abstract method that must be implemented by subclasses. It is the method that executes the tool with the provided arguments from the LLM. The arguments are passed as keyword arguments, and it returns a string. As you will recall, the AI-6 engine executes the `run()` method when a tool is called by the LLM during the agentic loop. 

```
@abstractmethod
defrun(self, **kwargs) -> str:
pass
```

Custom tools are great, but it’s important to support built-in tools as well. 

###### **What about built-in tools?** 

Some models support idx_ca9949bf built-in tools. Here is a non-comprehensive list of idx_8a08753 **b** uilt-in tools that some OpenAI models support: web search, file search, image generation, code interpreter (Python), and computer use. 

You can find the latest list of built-in tools available on the OpenAI platform here: 

```
https://platform.openai.com/docs/guides/tools#available-tools
```

_Chapter 4_ 

108 

AI-6 doesn’t support built-in tools at the moment. The reason is that the use of built-in tools depends on a specific LLM provider, specific models for each LLM provider, and even specific APIs. For example, the OpenAI chat completions API that is used by the AI-6 OpenAIProvider supports only the web search built-in tool. In order to use the other built-in tools mentioned previously, you must use the OpenAI responses API. 

In the future, AI-6 may add built-in tool support by updating its configuration system to have lists of allowed built-in tools per LLM provider and per model. For OpenAI, it will also require adding support for the responses API to the OpenAIProvider. 

The AI-6 framework supports MCP tools, too. The MCP tools conform to the **Model Context Protocol** ( **MCP** ) specification. MCP is a idx_829d8f96standard protocol originally developed by Anthropic that allows LLMs to access external data and tools in a secure and controlled manner. We will dedicate the entirety of _Chapter 7_ to exploring this topic. 

Let’s now talk about security and permissions that you need to consider for your tool system. 

###### **Tool security and permissions** 

One of the most important aspects of aidx_617a5447 tool-using agentic AI system is controlling the access of tools to data and resources. The reason is that the tools are in practice controlled by the LLM, which is this magical black box that you have no visibility into. Consider, for example, a scenario where the LLM has access to a database tool with full access to the production database, and it gets the task of improving the performance of data access and reducing costs. The LLM, without additional guidance, might decide that the best way to accomplish that is to delete the database and all the data in it and store just the last day of the data in memory. Fortunately, there are multiple ways to address this issue. AI-6 supports all of them just by virtue of being unopinionated and allowing the agentic AI system to utilize any mechanism or even multiple mechanisms. 

Let's look at the various ways you can manage tool execution with different levels of rigor, trust, and control: 

- **Full trust, full access** : Thisidx_bba2963a mode is appropriate for educational idx_e4ebc91bpurposes only and when the configured tools can't access any sensitive data or important resources. The LLM can just execute any tool with no checks or limitations. Beware that even in seemingly innocent scenarios, such as tools with read-only access to the LLM, this can cause damage. Consider, for example, a tool with read-only access to a database. The LLM will not be able to corrupt the data or delete it, but it can still read the data and exfiltrate it, and it can cause idx_f047fb5eself-DOS (denial of service) attacksidx_66f7f07b by running huge queries. 

_Building a Tool-Based Agentic AI Framework_ 

109 

- **Mediated fine-grained tool access** : Mediated fine-grained means that the tools don't execute direct commands idx_29d4aa9fon the system oridx_b2b3270c access resources directly. For a negative example, consider k8s-ai, which has direct access to the Kubernetes cluster via kubectl. If the LLM decides that it wants to delete all namespaces, k8s-ai will do it with no questions asked. To address this concern, we can remove the kubectl tool and replace it with multiple tools such as `get_pods` , `create_Deployment` , and so on. This approach provides fine-grained access to the Kubernetes cluster and avoids dangerous operations such as deleting namespaces. The benefit of this approach is that it gives you ultimate control, but for resources with a complex API surface, like Kubernetes, it will be a massive burden to manage the access with multiple tools. 

- **Guardrails** : Guardrails idx_c9b5 **a** 555 re another mechanism idx_51a6c4d5to manage the risk posed by LLMs. Note that guardrailsidx_d91b3992 are a broader concept beyond the tool use of the LLM. The guardrails can safeguard the parameters provided in tool calls, the tool call responses, but also the prompts sent to the LLM and the responses generated by it before passing it to the user. Let's take a look at the different types of guardrails: 

   - **Hallucination guardrails** areidx_16d6257f designed to prevent the AI from idx_f522e4d4generating content that is factually inaccurate or misleading. Implementing these guardrails involves a rigorous evaluation process that compares generated outputs against trusted sources. 

   - **Regulatory-compliance guardrails** ensure that AI-generated content adheres to applicable idx_adc9ca76laws and regulations, whetheridx_508dd53c they are general or tailored to a specific industry or use case. 

   - **Alignment guardrails** help idx_d740f453 keep the output consistent with useridx_ef56cbe6 intent and the original objective, minimizing the risk of content veering off course. These are particularly useful for maintaining tone, messaging, and brand alignment. 

   - **Validation guardrails** assess idx_3052176bwhether the generated content satisfies idx_cc914091predefined rules. For example, confirming that certain details are present or absent. If the content fails validation, it should be routed into a correction workflow. This is typically the final automated step, after which any flagged or uncertain cases should undergo human review for resolution. 

_Chapter 4_ 

110 

- **Container-based sandboxing** : One of the main risks of tool use is that the LLM can execute arbitrary code idx_90672f1aon the system. While the LLM **i** dx_7cb7f1e0 tself might not have ill intentions (yet), it may inadvertently, via tool use, cause performance issues, leave the system vulnerable to other attacks, and, in general, deviate from the intended behavior. To mitigate this risk, it's possible and often recommended to run your agentic AI system in a container, which isolates it from the underlying machine to a certain degree. Note that this is not foolproof, as it is possible to break out of a container (see this article: `https://medium.com/@the.gigi/pwning-kubernetes-77e43fc6c713` ). When running AI systems locally, it is often desirable to provide access to local directories, files, and other resources. That means that the idx_5 **c** ffae2b ontainer must be configured to allow access to these resources. This is a trade-off between security and controlled access. It also allows providing limited credentials to the external services to the agentic AI system by controlling the files available in the container. 

- **User permissions** : User permissionsidx_238d161c offer another effective layer of idx_d19 **c** 773d ontrol over tool use by running the agent under a dedicated, low-privilege operating system user. This restricts access to sensitive files, directories, and system capabilities, limiting what the LLM-controlled tools can read, write, or execute. Even without containerization, this approach prevents the agent from modifying critical system files or accessing unauthorized data, enforcing the principle of least privilege. For example, the agent might be allowed to write only to a specific directory, such as `/var/agent-output/` , while being blocked from accessing home directories or system configurations. This method can be combined with group-based access control, filesystem ACLs, or Linux features such as `ulimit` and `seccomp` to tighten restrictions further. It’s particularly useful in local or lightweight environments where full sandboxing is impractical. While user-level permissions don’t stop the LLM from misusing allowed capabilities (e.g., exfiltrating readable data), they provide a clean and manageable boundary that limits unintentional harm and makes security auditing easier. 

- **Human-in-the-loop** : Finally, the human-in-the-loopidx_35d67d2f approach is a powerful way to control tool use by the LLM. It involves having a human idx_85746929review and approve specific tool calls before they are executed. This provides a strong safeguard against unintended or harmful actions, as it allows human judgment to filter decisions the LLM might make based on incomplete context or ambiguous prompts. For example, before issuing a command to delete a resource, the system can present the action to a human operator for confirmation, ensuring critical operations are only performed when explicitly approved. This approach can be implemented at various levels of granularity, from approving every tool invocation to selectively intervening on high-risk actions. It is particularly effective in domains where mistakes are costly or safety is paramount, such 

_Building a Tool-Based Agentic AI Framework_ 

111 

as infrastructure management, financial operations, or medical systems. While it introduces latency and requires human availability, it significantly increases trust and reliability, making **i** dx_90428254 t ideal for hybrid workflows that balance automation with oversight. 

Memory is another crucial part of an agentic system. Let’s talk about it next. 

###### **Memory management** 

Memory management is arguably theidx_f6ecfc7e most important job of an agentic AI framework. It can be done by the host AI system, but it is important enough and nuanced enough that it is better to let the AI framework solve this problem once and let the AI system that was built on it focus on application-level concerns. As we discussed in _Chapter 2_ , multiple types of memory are important in AI systems. AI-6 manages all the different types of memory through a single concept: the session. 

###### **What is a session?** 

The **session** is the idx_18e37620collection of all the messages of a single top-level interaction with the LLM. A session also keeps count of the input and output tokens of all the messages. A single session may involve multiple input messages, involve multiple AI agents, and may persist across time and machine boundaries. 

It is defined in the `engine/session.py` file. 

Let's see how it works. Here are the imports. The `json` package is needed for serialization/ deserialization of sessions. The `uuid` package is used to generate unique session IDs, then a lot of imports from the AI-6 object model: 

```
import json
import uuid
from dataclasses import asdict
from backend.object_model import (
    Usage, Message, UserMessage, SystemMessage, AssistantMessage,
    ToolMessage, ToolCall)
```

_Chapter 4_ 

112 

The session is initialized with a memory directory, which is where persistent sessions are stored. First, a random session ID is generated, and then a session title is created based on the session ID. We will see later how to set the title of a saved session via a different class, `SessionManager` . Then, we initialize a `usage` object: 

```
classSession:
def__init__(self, memory_dir: str):
self.session_id = str(uuid.uuid4())
self.title = 'Untiled session ~' + self.session_id
self.messages: list[Message] = []
self.usage = Usage(0, 0)
self.memory_dir = memory_dir
```

The `add_message()` method isidx_9f11a574 pretty straightforward. It takes a message and appends it to the messages list of the session. If the message has a `usage` object, then it updates the session's usage by adding the input and output tokens, so the session keeps a running total. We will see how the usage object is used to decide if the context window needs to be compacted in the _Handling long contexts_ section. 

```
defadd_message(self, message: Message):
"""Add a Message object to the session."""
self.messages.append(message)
# Extract usage from AssistantMessage if present
ifhasattr(message, 'usage') and message.usage:
self.usage = Usage(
self.usage.input_tokens + message.usage.input_tokens,
self.usage.output_tokens + message.usage.output_tokens
            )
```

The `save()` method converts each message to a dictionary using the `asdict()` function of the `dataclasses` module, then prepares another dictionary that contains all message dictionaries, serializes the dictionary to JSON, and saves it to a file named `<session id>.json` in the memory directory. Now, we have a persistent session that we can later restore even if the process crashes. 

```
defsave(self):
# Convert Message objects to dictionaries for JSON serialization
        message_dicts = [asdict(msg) for msg inself.messages]
```

_Building a Tool-Based Agentic AI Framework_ 

113 

```
        d = dict(session_id=self.session_id,
                 title=self.title,
                 messages=message_dicts,
                 usage=dict(
                    input_tokens=self.usage.input_tokens,
                    output_tokens=self.usage.output_tokens))
        filename = f"{self.memory_dir}/{self.session_id}.json"
withopen(filename, 'w') as f:
            json.dump(d, f, indent=4)
```

Let's look at a savedidx_e26f3cc5 session. The user asks what the current directory is. The LLM responds with an assistant message with a request to run the `pwd` tool, which returns the current directory. The AI-6 framework correctly executed the tool and sent to the LLM a tool message with the answer `"/Users/gigi/git/AI-6"` . Then, the LLM responds with a final assistant message, `\n\nThe current directory is `/Users/gigi/git/AI-6` . The session continued as the user sent a new query, but I cut it short. Note that in the end, it calculated the input and output tokens of all messages: 

```
{
"session_id": "045d8889-d51b-4a48-bb3b-c97f9700af23",
"title": "Untiled session ~045d8889-d51b-4a48-bb3b-c97f9700af23",
"messages": [
        {
"role": "user",
"content": "what's curr dir"
        },
        {
"role": "assistant",
"content": null,
"tool_calls": [
                {
"id": "tool_185f7ac72fb2404e95660d90964dc98f",
"type": "function",
"function": {
"name": "pwd",
"arguments": "{}"
                    }
                }
            ],
"input_tokens": 551,
```

_Chapter 4_ 

114 

```
"output_tokens": 11
        },
        {
"role": "tool",
"name": "pwd",
"content": "/Users/gigi/git/AI-6",
"tool_call_id": "tool_185f7ac72fb2404e95660d90964dc98f"
        },
        {
"role": "assistant",
"content": "\n\nThe current directory is `/Users/gigi/git/AI-6`."
        }
        .
        .
        .
    ],
"usage": {
"input_tokens": 3068,
"output_tokens": 57
    }
}
```

The `load()` method is the opposite of `save()` . It accepts a session ID, locates the corresponding idx_22eda351session file according to the naming convention, and loads the JSON from the file into a Python dictionary. Then, it creates the `Session` object from the JSON field by field. To convert each message from a dictionary to a `Message` object (or one of its subclasses), it uses the `dict_to_message()` function: 

```
defload(self, session_id: str):
"""Load session from disk, properly deserializing nested objects"""
        filename = f"{self.memory_dir}/{session_id}.json"
withopen(filename, 'r') as f:
            d = json.load(f)
self.session_id = d['session_id']
self.title = d['title']
# Convert message dictionaries back to Message objects
self.messages = [dict_to_message(msg) for msg in d['messages']]
# Deserialize usage directly to a Usage object
```

_Building a Tool-Based Agentic AI Framework_ 

115 

```
self.usage = Usage(d['usage']['input_tokens'],
            d['usage']['output_tokens'])
```

Now, let's see how the session is used with different types of memory. 

###### **Short-term memory in the agentic loop** 

During the agentic loop, the AI-6 idx_ **e** f64ebee ngine potentially makes multiple requests to theidx_c9a1ceb8 LLM, and it accumulates all previous messages. Every tool request and its response after being executed are added to the active session and are available to the LLM in the next iteration of the agentic loop as the session becomes the context window. For example, consider the following interaction: 

```
User: what is the current directory?
LLM (tool call): pwd (print working directory)
User:How many Python files in the current directory?
LLM (tool call): ls *.py
AI-6 (tool call response):foo.py bar.py
LLM (final response): There are two Python files in the current directory
User: What are they?
LLM (final response): The files are foo.py and bar.py
```

At each point, the LLM receives the entire conversation and not just the last message. When the user asks `What are they?` , the LLM can infer from the conversation history that the user is referring to the Python files in the current directory, and it can return them immediately without another tool call. 

###### **Sessions and conversations** 

When an agentic loop ends a final idx_5960de16response is returned to the user (or agentic AI application). The user may continue the conversation by sending a new user message that will start a new agentic loop, but with the context that includes all the previous messages of the current session. 

###### **Long-term memory and session loading** 

We showed how the session can save and loadidx_7294d470 itself to/from a file. But what is the mechanism that enables it? This is where the session manager comes in. The session manager is implemented in the `engine/session_manager` file. It exposes three methods to manage persistent sessions: 

- `list_sessions()` 

- `delete_session()` 

- `set_title()` 

_Chapter 4_ 

116 

When an AI-6 application starts, it can call `list_sessions()` to review all existing sessions and decide to load an existing session or delete an old session. It can also set the title for an existing session. 

Let's see how the session manager works. The session is initialized with the memory directory, which is where the session files are stored: 

```
import os
import json
classSessionManager:
def__init__(self, memory_dir: str):
self.memory_dir = memory_dir
```

The `set_title()` method accepts a session ID and a title. It locates the session file (raising an exception if not found), loads the session from the JSON file as a Python dictionary, replaces the title, and saves it back. Note the unusual sequence of seek, dump, and truncate to update the file. It is a safe option for updating files using a single file handle and with minimal risk of truncating the file and then crashing and leaving an empty file. If you just overwrite a file with a command such as `open(filename, ‘w’).write()` and the process crashes immediately after the `open()` command, then idx_877ad28dyou are left with an empty file: 

```
defset_title(self, session_id: str, title: str):
"""Set the title of a session."""
        sessions = self.list_sessions()
if session_id notin sessions:
raise RuntimeError(f"Session{session_id} not found.")
        filename = sessions[session_id]['filename']
withopen(filename, 'r+') as f:
            data = json.load(f)
            data['title'] = title
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
```

The `list_sessions()` method lists all the . `json` files in the memory directory, verifies they contain valid JSON, and returns a list of dictionaries where each session dictionary contains its 

_Building a Tool-Based Agentic AI Framework_ 

117 

title and filename. If something is wrong, it just prints an error message and continues to the next session: 

```
deflist_sessions(self) -> list[dict]
"""List all sessions in the memory directory.
        Returns:
            A dictionary mapping session IDs to tuples of (name, filename)
        """
        sessions = {}
        files = os.listdir(self.memory_dir)
for f in files:
if f.endswith('.json'):
try:
# Get session ID from the filename (dropping the .json extension)
                    session_id = os.path.basename(f).rsplit('.json', 1)[0]
# Try to open and parse the file to verify it's valid JSON
                    full_path = os.path.join(self.memory_dir, f)
withopen(full_path, 'r') as file:
try:
# Attempt to parse the JSON
                            session = json.loads(file.read())
# Only add if we could parse the JSON
                            sessions[session_id] = dict(
                                title=session['title'],
                                filename=full_path)
except json.JSONDecodeError:
# Skip files with invalid JSON
print(f"Skipping file with invalid JSON: {f}")
continue
except Exception as e:
# Skip any files that cause other errors
print(f"Error parsing session file {f}: {e}")
continue
return sessions
```

_Chapter 4_ 

118 

Deleting a session is veryidx_8f188d1c simple, too. List the sessions, get the filename, and remove the file: 

```
defdelete_session(self, session_id: str):
"""Delete a session by its ID."""
        sessions = self.list_sessions()
if session_id notin sessions:
raise RuntimeError(f"Session{session_id} not found.")
        filename = sessions[session_id]['filename']
        os.remove(filename)
```

The session manager can manage sessions, but as these sessions grow, they can saturate the context. Let’s understand the problem and consider how to address it. 

###### **Handling long contexts** 

One of the biggest problems thatidx_b2d1ad5e an agentic AI framework needs to work with is managing the size of the context, so it fits in the context window size of the model. Agentic workflows can span many requests to the LLM over long periods of time and accumulate more and more context. The solution is to compress the context when it's approaching the limit. But, how do you decide what context should be kept? Well, LLMs are excellent at summarizing long blocks of text. Let's ask the LLM to compress the context. This is exactly what the summarizer does. It is implemented in the `engine/summarizer` file. Let's see it in action. It is initialized with an LLM provider: 

```
from backend.object_model import (
    Message, LLMProvider, SystemMessage, UserMessage)
classSummarizer:
"""Utility class for summarizing sessions using an LLM."""
def__init__(self, llm_provider: LLMProvider):
"""Initialize the summarizer with an LLM provider.
Args:
llm_provider: An LLM provider instance
        """
self.llm_provider = llm_provider
```

The `summarize()` method accepts a list of messages and a model ID. It prepares a system prompt with instructions on how to summarize conversations and then formats the session messages into a single string that contains the role and content of each message (using the 

_Building a Tool-Based Agentic AI Framework_ 

119 

`_format_session()` method). Then it sends the system message and a user message that 

contains the combined session string to the provider, which returns a summary of the session. Note that this is a single `send()` call directly to the LLM provider. 

There is no session involved in this interaction: 

```
defsummarize(self, messages: list[Message], model_id: str) -> str:
"""Summarize a list of messages using the LLM.
Args:
            messages: List of message dictionaries to summarize
model_id: ID of the model to use for summarization
        Returns:
            A string summary of the session
        """
# Format messages for the LLM
        formatted_messages = [
            SystemMessage(
                content=(
"You are a helpful assistant tasked with summarizing a
conversation. "
"Create a concise summary that captures the key points,
questions, decisions, and context "
"from the session. The summary should be informative enough
that someone "
"reading it would understand what was discussed, what
conclusions were reached, "
"and what important context should be carried forward. "
"Focus on preserving information that will be useful for
continuing the conversation, "
"including names, technical terms, important numbers, and
specific details that might "
"be referenced later. Avoid unnecessary details, repetitive
information, or tangential discussions."
                )
            ),
            UserMessage(
                content=(
"Please summarize the following session:\n\n" +
self._format_session(messages)
```

_Chapter 4_ 

120 

```
                )
# Get summary from LLM
        response = self.llm_provider.send(
            formatted_messages, {}, model_id)
return response.content.strip()
```

Here is the `_format_session()` static method that converts a list of messages to one big string that contains the roleidx_749811f9 and content of each message: 

```
@staticmethod
@staticmethod
def_format_session(messages: list[Message]) -> str:
"""
        Format a list of messages into a readable session.
Args:
            messages: List of message dictionaries
        Returns:
            Formatted session string
        """
        formatted = []
for msg in messages:
            role = msg.role
            content = msg.content
if role == "tool":
                tool_name = getattr(msg, 'name', 'unknown tool')
                formatted.append(f"Tool ({tool_name}): {content}")
else:
                formatted.append(f"{role.capitalize()}: {content}")
return"\n\n".join(formatted)
```

_Building a Tool-Based Agentic AI Framework_ 

121 

The decision about whether a summarization is needed happens in the engine in the `_checkpoint_if_needed()` method, which saves the session periodically and also checks the total number of tokens in the session (obtained from the `usage` object) against the context window size. If the number of tokens exceeds that threshold, then a summarization will take place, and the session will use the shorter summarized context from this point forward. 

Here is how this method isidx_9580dfad defined: `def _checkpoint_if_needed(self): """Check if we need to save a checkpoint and do so if needed.""" self.message_count_since_checkpoint += 1` _`# Only save if we've reached the checkpoint interval exactly`_ `if self.message_count_since_checkpoint == self.checkpoint_interval: self.session.save() self.message_count_since_checkpoint = 0` _`# Check and summarize if above token threshold (80% of context window)`_ `total_tokens = ( self.session.usage.input_tokens + \ self.session.usage.output_tokens ) if total_tokens >= self.token_threshold: context_window_size = get_context_window_size( self.default_model_id) print( f"Session tokens ({total_tokens}) have reached {self.summary_threshold_ratio * 100}% of context window ({context_window_size}). Summarizing..." ) self._summarize_and_reset_session()` 

Note that automatic idx_84619938summarization by the LLM is not the only way to compress the context window when it becomes too large. Other approaches include **semantic search with embeddings** to retrieve only the most relevant past turns, **rule-based pruning** to drop trivial or repeated exchanges, **structured storage** of facts and entities for on-demand injection, and **token-efficient re-encoding** techniques such as codebooks, custom shorthand formats, or domain-specific compression schemes. 

_Chapter 4_ 

122 

In the future, AI-6 may evolve to make memory management extensible. The engine will not directly invoke the summarizer when the context window becomes too large, but will be initialized with a generic context manager that will implement some compaction method. This approach will follow the blueprint of tools and `LLMProvider` , where the engine interacts with other components through an abstract interface. Specifically, a generic `ContextManager` interface with a `summarize()` method can be implemented by multiple concrete context managers that can be configured by the user to select the best method for summarizing sessions. 

###### **Summary** 

In this chapter, we learned that the AI-6 framework is a robust, extensible platform designed to support sophisticated agentic AI systems. Building on the minimal k8s-ai agent, AI-6 introduces a modular backend architecture that coordinates tool execution, memory management, and communication with multiple LLM providers. At its core is the `Engine` class, which orchestrates the agentic loop, receiving user input, invoking tools as needed, managing the session history, and interacting with LLMs through a unified provider interface. Configuration is centralized through a simple `Config` object, allowing users to define tools, memory directories, model defaults, and behavior parameters. The system is designed to be unopinionated, making it easy to build specialized or more opinionated systems on top. 

A key strength of AI-6 lies in its abstraction of LLM providers and tools. It supports both remote providers such as OpenAI and local ones such as Ollama, using a common interface that handles message formatting, tool integration, and response parsing. Tools themselves are defined through a lightweight Python interface that supports description, typed parameters, and execution logic. The framework is designed to safely manage tool use by offering support for fine-grained tool definitions, runtime guardrails, sandboxing through OS permissions or containers, and human-in-the-loop control when needed. This provides a strong foundation for building secure and reliable AI systems capable of using external capabilities effectively. 

Memory is managed through a concept called sessions, which encapsulate all interaction history and token usage. Sessions can be saved, resumed, summarized, and inspected through a dedicated `SessionManager` object. When a session grows too large, a built-in summarization module uses an LLM to compress earlier messages while preserving important context. This ensures that AI-6 can operate over long conversations without exceeding model limits. Together, these features form a cohesive, production-ready framework for managing agent behavior, tool use, and long-term memory in AI systems. 

In the next chapter, we will see how to implement custom tools for AI-6 and get to experiment with different combinations of tools to perform useful tasks. 

_Building a Tool-Based Agentic AI Framework_ 

123 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns – _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and generative AI systems. Subscribe now and receive a free eBook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OFA<br>a<br><!-- End of picture text -->

# 5 

##### Implementing Custom Tools 

In the previous chapter, we explored the backend architecture of the AI-6 framework in detail, focusing on how the engine orchestrates the agentic loop, manages memory and session tate, and integrates with multiple LLM providers and tools. We saw how tools and models are dynamically discovered and how the engine handles their coordination through a unified abstraction. This foundation enables flexible, provider-agnostic AI workflows with persistent memory, resumable sessions, and secure, extensible tool usage. 

In this chapter, we will shift focus from the overall engine architecture to a deeper investigation of the tool system itself. While _Chapter 4_ treated tools largely as pluggable black boxes, here we will look inside and examine how generic tools are designed to be reusable, consistent, and portable across LLM providers. We will explore how tools can be defined with structured schemas, how arguments are validated, and how they are registered and translated into provider-specific formats. 

We’ll begin by discussing how AI-6 allows its users to implement a tool in terms of the generic AI-6 tool format. This single generic tool implementation will work with any LLM provider, such as OpenAI, Ollama, or some future LLM provider that doesn't even exist yet. We will also look at the specific APIs of OpenAI and Ollama to understand how they provide similar functionality through slightly different specifications, and how AI-6 can utilize both of these providers without exposing their internals to its users, followed by a review of schema definitions and input validation strategies. From there, we’ll look at how AI-6 maps its internal tool representation to provider-specific formats (such as OpenAI function calling). Finally, we will examine how tool execution is managed, including how results are captured and routed back to the LLM through the session. This chapter will lay the groundwork for building powerful, safe, and interoperable tools that expand the capabilities of agentic AI systems. 

_Chapter 5_ 

126 

In this chapter, we will cover the following main topics: 

- Defining generic tools 

- 

- Defining AI-6 custom tools 

- 

- Implementing a new tool manually 

- 

###### **Technical requirements** 

There are no specific technical requirements for this chapter. If you wish to build your own custom tools, you can use any Python library. You simply need to implement the **Tool** interface, which is part of the AI-6 framework itself, to customize your tools. The code for the chapter is available here: 

`https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-andA2A/tree/main/ch05/ai-six` . 

###### **Defining provider-agnostic tools** 

Every LLM provider API, such as OpenAI, Anthropic, Gemini, and Ollama, has its own way of specifying tools. Since AI-6 needs to work with all LLM providers, it defines its own provideragnostic format. The AI-6 framework’s LLM providers that interact directly with the APIs or SDK of third-party LLM providersidx_6e4ee545 know how to translate the generic tool definition to the provider-specific tool definition. 

The AI-6 tools definition must be a superset of the information required by all the APIs. The focus of the tools definition is on function calling, although built-in tools are supported too. Let’s look at the tool definition of LLM provider Python SDKs, such as OpenAI and Ollama. The reason we look at Python SDKs and not the raw REST APIs is that the AI-6 LLM providers are implemented in Python and use the Python SDKs of the corresponding third-party LLM providers. 

Let’s first look at the OpenAI Python SDK and see how it specifies tools and tool calls. 

###### **OpenAI Python tool specification** 

The OpenAI Python SDK is available at `https://github.com/openai/openai-python` . 

It was generated automatically from the OpenAPI specification ( `https://github.com/openai/ openai-openapi` ) of the idx_0c0b78b0OpenAI REST API, so it has 100% fidelity to the actual OpenAI API. The tool definition we are interested in is in the idx_323afb3bchat completions endpoint, which is accessible through the `create()` method ( `https://github.com/openai/openai-python/blob/main/ src/openai/resources/chat/completions/completions.py#L76` ) of the `Completions` class of 

_Implementing Custom Tools_ 

127 

the idx_e38bbc42Chat Completions API. Do not confuse it with the legacy Completions API ( `https:// platform.openai.com/docs/api-reference/completions` ). 

This method makes a call to the LLM (optionally with a lot of arguments) and gets a response. This response can be a final response or a tool call, which will be processed by AI-6 (as we discussed in the previous chapter). 

The `create()` method has eight overloaded versions. This means that there are eight different methods, and all of them are named `create()` with slightly different arguments. The reason overloaded methods are useful, especially for methods with a lot of arguments, is that different overloaded versions canidx_860890bf provide different levels of control as opposed to ease of use: 

```
@overload
defcreate(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
function_call: completion_create_params.FunctionCall | NotGiven =
NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven =
NOT_GIVEN,
logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven =
NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven =
NOT_GIVEN,
presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
response_format: completion_create_params.ResponseFormat | NotGiven =
NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
service_tier: Optional[Literal["auto", "default", "flex", "scale"]] |
```

_Chapter 5_ 

128 

`NotGiven = NOT_GIVEN, stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN, store: Optional[bool] | NotGiven = NOT_GIVEN, stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN, stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN, temperature: Optional[float] | NotGiven = NOT_GIVEN, tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN, tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,` _`#`_ 👈 `top_logprobs: Optional[int] | NotGiven = NOT_GIVEN, top_p: Optional[float] | NotGiven = NOT_GIVEN, user: str | NotGiven = NOT_GIVEN, web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,` _`# Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs. # The extra values given here take precedence over values defined on the client or passed to this method.`_ `extra_headers: Headers | None = None, extra_query: Query | None = None, extra_body: Body | None = None, timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN, ) -> ChatCompletion: """ ... """` 

Some of the overloaded methods areidx_77b0572e synchronous, and some are asynchronous, but they all define the tools in the same way: 

```
tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
```

What does this line mean? 

1. `Iterable[ChatCompletionToolParam]` means that the provided tools should be an iterable sequence where each element is of the `ChatCompletionToolParam` type. 

2. The second part, `| NotGiven = NOT_GIVEN` , means that the `tools` argument can alternatively be the `NotGiven` type and the default value if no tools are provided. The `NOT_GIVEN` value is a constant of the `NotGiven` type. 

_Implementing Custom Tools_ 

129 

In other words, the `tools` argument idx_c43014dd can be one of two types (Python allows that). The first type is `Iterable[ChatCompletionToolParam]` , which you can think of as a list of items of the `ChatCompletionToolParam` type. The second type is `NotGiven` . The default value of the `tools` argument is `NOT_GIVEN` . If the caller didn’t provide any tools, then the value of the `tools` argument will be the default, `NOT_GIVEN` . 

If you’re wondering what `NotGiven` is, it is a simple sentinel class used to denote unspecified parameters and provide them with the default value of `NOT_GIVEN` . 

OK. Let’s understand what `ChatCompletionToolParam` is. It is a class with two fields: `function` and `type` . Both of these fields are required. The `function` field is of the `FunctionDefinition` type, and the `type` field must be the literal string `"function"` . 

Here is how you can define this class: 

```
classChatCompletionToolParam(TypedDict, total=False):
    function: Required[FunctionDefinition]
type: Required[Literal["function"]]
"""The type of the tool. Currently, only `function` is supported."""
```

This can be a little confusing because there are two different kinds of types here. The type of the function, `Required[FunctionDefinition]` , is a type hint for a required Python type, `FunctionDefinition` . The OpenAI Chat Completions API is interesting because it supports only one kind of tool, a function tool, butidx_2b96a552 the API is defined in a more general way as if it can support additional tool kinds. 

Other OpenAI APIs do support multiple tool kinds. The deprecated Assistants%20API%20(beta) ( `https://github.com/openai/openai-python/blob/main/src/ openai/types/beta/assistant.py` ) supports two built-in tools: `file_search` and `code_interpreter` . 

###### **Note** 

Well, that was quite a journey of API design that OpenAI went through. Initially, there was just the Chat Completion API, which we use and has only the `"function"` tool kind. Then, there was the Assistants API that never got out of beta and eventually was deprecated. Later, the Responses API was published with several more tool kinds. 

_Chapter 5_ 

130 

Here are the definitions of the idx_73c5eedabuilt-in `CodeInterpreter` and `FileSearch` tools: 

`class ToolResourcesCodeInterpreter(BaseModel): file_ids: Optional[List[str]] = None """ A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool. """ class ToolResourcesFileSearch(BaseModel): vector_store_ids: Optional[List[str]] = None """ The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/ object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant. """ class ToolResources(BaseModel): code_interpreter: Optional[ToolResourcesCodeInterpreter] = None file_search: Optional[ToolResourcesFileSearch] = None` The new Responses API supports the following tools defined in `types/responses/ tool_param.py` ( `https://github.com/openai/openai-python/blob/main/src/openai/ types/responses/tool_param.py#L170` ): `ToolParam: TypeAlias = Union[ FunctionToolParam, FileSearchToolParam, WebSearchToolParam, ComputerToolParam, Mcp, CodeInterpreter, ImageGeneration,` 

The new Responses API supports the following tools defined in `types/responses/` 

`tool_param.py` ( `https://github.com/openai/openai-python/blob/main/src/openai/ types/responses/tool_param.py#L170` ): 

_Implementing Custom Tools_ 

131 

```
    LocalShell,
]
```

At the moment, theidx_c0458396 OpenAI LLM provider of AI-6 uses the Chat Completions API, so let’s get back to the `FunctionDefinition` class ( `https://github.com/openai/openai-python/blob/ main/src/openai/types/shared/function_definition.py#L11` ). It represents a single function tool and has a name, description, optional parameters, and an optional strict flag ( `False` unless idx_9c7b461aexplicitly set to `True` ): 

```
classFunctionDefinition(BaseModel):
    name: str
"""The name of the function to be called.
    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum
length
    of 64.
    """
    description: Optional[str] = None
"""
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """
    parameters: Optional[FunctionParameters] = None
"""The parameters the functions accepts, described as a JSON Schema object.
    See the [guide](https://platform.openai.com/docs/guides/function-calling) for
    examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
for
    documentation about the format.
    Omitting `parameters` defines a function with an empty parameter list.
    """
    strict: Optional[bool] = None
"""Whether to enable strict schema adherence when generating the function
call.
```

_Chapter 5_ 

132 

```
    If set to true, the model will follow the exact schema defined in the
    `parameters` field. Only a subset of JSON Schema is supported when `strict` is
    `true`. Learn more about Structured Outputs in the
    [function calling guide](docs/guides/function-calling).
    """
```

Let’s keep drilling down and see what `FunctionParameters` ( `https://github.com/openai/ openai-python/blob/main/src/openai/types/shared/function_parameters.py` ) in the `FunctionDefinition` class is all idx_ **a** d21cbfc bout. It turns out that it is a simple dictionary of string -> any object. 

```
# File generated from our OpenAPI spec by Stainless.
from typing importDict
from typing_extensions import TypeAlias
__all__ = ["FunctionParameters"]
FunctionParameters: TypeAlias = Dict[str, object]
```

Let’s recap the tool definition idx_652e27afrequirements of the Chat Completions API as specified by OpenAI: 

   - Every tool must be of the `"function"` type 

   - Every tool has a name and a description 

   - A tool may have zero or more parameters with a name and an arbitrary value type 

- A tool may specify whether its output is strict 

- There is one more important element for the OpenAI tools specification. In addition to the `tools` argument of the `create()` methods, there is also a `tool_choice` argument: 

```
tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
```

The tool choice can take one of the following values: `"none"` (don’t call any tool), `"auto"` (you decide whether you want to call one or more tools and which tools), `"required"` (you must call at least one tool; you decide which tool or tools to call), or a specific tool name (you must call this tool): 

```
ChatCompletionToolChoiceOptionParam: TypeAlias = Union[
Literal["none", "auto", "required"],
```

_Implementing Custom Tools_ 

133 

```
    ChatCompletionNamedToolChoiceParam
]
```

If this sounds confusing, it’s because it is. I idx_332e83bdwrote a whole blog post about the problems with tool choice and how it can be significantly simplified: _Fixing the OpenAI Tool Calling API_ . You will find it here: `https://medium.com/@the.gigi/fixing-the-openai-tool-calling-apiede67419f9f5` . 

OK. Let’s keep this in mind idx_4 **a** 69ec25 nd see how the Ollama Python SDK specifies tool calls. 

###### **Ollama Python tool specification** 

The Ollama Python SDK ( `https://github.com/ollama/ollama-python` ) is already an abstraction over many APIs because it supports many providers through a unified interface. Let’s see how tools are idx_6bd91313specified in the Ollama idx_261e8971Python SDK. 

Ollama uses the `chat()` methods (multiple overloads similar to OpenAI) of the `Client` class ( `https://github.com/ollama/ollama-python/blob/main/ollama/_client.py#L114` ) to interact with the LLM and specify tools: 

`@overload def chat( self, model: str = '', messages: Optional[ Sequence[Union[Mapping[str, Any], Message]]] = None, *, tools: Optional[ Sequence[Union[Mapping[str, Any], Tool, Callable]]] = None,` _`#`_ 👈 `stream: Literal[False] = False, think: Optional[bool] = None, format: Optional[Union[Literal['', 'json'], JsonSchemaValue]] = None, options: Optional[Union[Mapping[str, Any], Options]] = None, keep_alive: Optional[Union[float, str]] = None, ) -> ChatResponse: ...` 

_Chapter 5_ 

134 

The tool definition is a mouthful. Let’s parse it. The parameter named `tools` is optional and defaults to `None` . If provided, it must be a sequence (such as a list or tuple) where each item is one of three allowed types: 

- A `Mapping[str, Any]` JSON schema as a dictionary with string keys and values of any type 

- An Ollama `Tool` instance (a class provided by the Ollama SDK that wraps tool metadata and behavior) 

- A `Callable` object that follows Google-style docstrings to be converted to an Ollama `Tool` instance: 

```
tools: Optional[
Sequence[Union[Mapping[str, Any], Tool, Callable]]
] = None
```

Regardless of theidx_ae71686b representation, they all end up idx_283cbe64as a sequence of Ollama `Tool` instances ( `https://github.com/ollama/ollama-python/blob/main/ollama/_types.py#L312` ): 

```
classTool(SubscriptableBaseModel):
type: Optional[Literal['function']] = 'function'
classFunction(SubscriptableBaseModel):
        name: Optional[str] = None
        description: Optional[str] = None
classParameters(SubscriptableBaseModel):
            model_config = ConfigDict(populate_by_name=True)
type: Optional[Literal['object']] = 'object'
            defs: Optional[Any] = Field(None, alias='$defs')
            items: Optional[Any] = None
            required: Optional[Sequence[str]] = None
classProperty(SubscriptableBaseModel):
                model_config = ConfigDict(arbitrary_types_allowed=True)
type: Optional[Union[str, Sequence[str]]] = None
                items: Optional[Any] = None
                description: Optional[str] = None
                enum: Optional[Sequence[Any]] = None
            properties: Optional[Mapping[str, Property]] = None
```

_Implementing Custom Tools_ 

135 

```
        parameters: Optional[Parameters] = None
    function: Optional[Function] = None
```

We’re not going to parse every line in this Python code and just note that Ollama attaches some model information to the tool definition, which is probably used when translating `Tool` to the model-specific tool definition. 

The important thing to pay idx_61 **a** b7c52 ttention to is that, similar to the OpenAI Completion API, the only supported tool type is `"function"` . 

To summarize, OpenAI and Ollama define tools in their own format, but conceptually, they contain equivalent informationidx_49e0610b for each tool, which is great for AI-6. 

We are now ready to see the generic tool specification schema of AI-6. 

###### **Defining the AI-6 tool specification schema** 

We covered the AI-6 `Parameter` and `Tool` classes in the previous chapter. Here is a quick refresher. It aims for simplicity without too much fancy stuff. One special feature that is present in AI-6 and is missing fromidx_1d29a88f both the OpenAI and Ollama tool specifications is the `required` field of the `Tool` class. This field is a set of parameter names that idx_2246000amust be provided when the LLM calls the tool. It is part of the OpenAI tool specification in the REST API, but somehow it didn’t make it to the Python SDK: 

```
classParameter(NamedTuple):
    name: str
type: str
    description: str
@dataclass(slots=True)
classTool(ABC):
    name: str
    description: str
    parameters: list[Parameter]
    required: set[str]
defconfigure(self, config: dict) -> None:
"""Optional: configure the tool with given parameters."""
@abstractmethod
defrun(self, **kwargs) -> str:
```

_Chapter 5_ 

136 

```
"""Execute the tool using the given arguments and return the result as a
string."""
```

This straightforward code is the entire tool specification schema of AI-6. It is very simple and easy to comprehend. 

Well, you have already seen how AI-6 can abstract the provider and respective implementation to define tools with the `LLMProvider` interface. We will now see how to define custom tools that can be translated to the tool format of the active LLM provider in the next section. 

###### **Defining AI-6 custom tools** 

AI-6 comes with many idx_87aa5a7fexamples of ready-to-use tools, and it is easy to implement new tools. In this section, we will review some of the existing tools and then implement a brand-new tool from scratch. 

The process of defining an AI-6 custom tool consists of the following steps: 

1. Create a new Python class. 

2. Derive from the `Tool` base class directly or indirectly. 

3. Implement the `run()` method. 

4. Optionally implement the `configure()` method. 

Let’s start with general idx_ed5bd477command-line tools, which are very powerful. 

###### **General command-line tools** 

Many of the useful tools that idx_8a6758cdAI-6 provides out of the box are command-line tools. These tools run wherever AI-6 runs ( on your machine, in a container, in the cloud, etc.). AI-6 provides a base class for command-line tools that takes care of all the boilerplate necessary for running command-line programs with arbitrary arguments and offers the option to idx_c5fad2a7run the commandline program as a dedicated user (different from the current user). Let’s see how the `CommandTool` class works before we examine the tools derived from it. 

###### **Note** 

LLMs don't know that they invoke command-line tools. As you recall, LLMs receive tool definitions, and then, via the agentic loop, they request to invoke these tools. The actual tool execution happens on the AI system/framework side, where very often they will run command-line tools. 

_Implementing Custom Tools_ 

137 

It imports the `sh` package ( `https://sh.readthedocs.io/en/latest/index.html` ) for running shell idx_a69a **c** d76 ommands, the `shlex` built-in package ( `https://docs.python.org/3/library/ shlex.html` ) for parsing POSIX command-line arguments, and `Parameter` and `Tool` from the AI-6 object model: 

```
import sh
import shlex
from backend.object_model import Tool, Parameter
```

Here is how the `CommandTool` class is organized to help you implement the command-line tools: 

1. The class is derived from the `Tool` base class, so it can serve as a base class for AI-6 tools. 

2. The constructor takes as input a command name (the name of a command-line program available on the path), an optional user, and an optional link to documentation of the command. 

3. It then constructs a list of parameters that contains exactly one string parameter called `args` , which is expected to be all the command-line arguments to the target command. 

4. The `args` parameter isidx_db8f00e1 required, but it may be an empty string. If a documentation link was provided, it will be added to the description of the command, which will help the LLM to understand how to invoke the command. 

Let’s take a look at theidx_ae293ab5 class definition: 

```
classCommandTool(Tool):
def__init__(
        self, command_name: str, user: str | None = None,
doc_link: str = ""
):
self.command_name = command_name
self.user = user
        description = f'{command_name} tool. ' + f'See{doc_link}'if doc_link
else''
        parameters = [Parameter(name='args', type='string',
            description=f'command-line arguments for {command_name}')]
        required = {'args'}
super().__init__(
            name=command_name,
            description=description,
```

_Chapter 5_ 

138 

```
            parameters=parameters,
            required=required
        )
```

The `run()` method has two jobs. First, to parse the command-line arguments in the `args` parameter using the `shlex.split()` method and then execute the command with the dedicated user (if provided) idx_46fd8189or as the current user. Note that the current user must be able to switch to the dedicated user (via `sudo` ): 

```
defrun(self, **kwargs):
        args = shlex.split(kwargs['args'])
ifself.user isnotNone:
return sh.sudo('-u', self.user, self.command_name, *args)
else:
returngetattr(sh, self.command_name)(*args)
```

The `CommandTool` class provides no special `configure()` method to override the optional `Tool.configure()` method, but tool classes derived from `CommandTool` may do so if necessary. 

Now, let’s see how easy it is to implement command tools and provide strong capabilities to our AI agents. 

We will begin with the filesystem tools. 

###### **Filesystem tools** 

Some of the most useful idx_9 **c** 5d44b8 ommands deal with files and directories. AI-6 provides idx_4cc218dabasic directory and file commands such as `pwd` , `ls` , `cat` , and `echo` . 

It also provides some more sophisticated file editing commands, such as `sed` , `awk` , and `patch` . Let’s start with the **print working directory** ( `pwd` ). All we have to do isidx_4ddb20c7 define a class called `Pwd` with a minimal constructor that just provides the documentation link for the POSIX `pwd` command: 

```
from backend.tools.base.command_tool import CommandTool
classPwd(CommandTool):
def__init__(self, user: str | None = None):
        doc_link = 'https://www.gnu.org/software/coreutils/manual/html_node/pwd-
invocation.html'
super().__init__('pwd', user=user, doc_link=doc_link)
```

_Implementing Custom Tools_ 

139 

We can test it directly idx_f05c41ddwithout the rest of AI-6, by simply instantiating it and checking properties such as `parameters` and `description` : 

❯ `source venv/bin/activate` ❯ `python Python 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin Type "help", "copyright", "credits" or "license" for more information. >>> from backend.tools.file_system.pwd import Pwd >>> pwd = Pwd() >>> pwd.parameters [Parameter(name='args', type='string', description='command-line arguments for pwd')] >>> pwd.description 'pwd tool. See https://www.gnu.org/software/coreutils/manual/html_node/pwdinvocation.html'` 

We can also run it and verify whether it really returns the current working directory: 

```
>>> pwd.run(args='')
'/Users/gigi/git/ai-six/py\n'
```

Other filesystem commands are just as simple. Here is the `ls` command: 

```
from ..base.command_tool import CommandTool
classLs(CommandTool):
def__init__(self, user: str | None = None):
super().__init__(command_name='ls', user=user,
            doc_link = 'https://www.gnu.org/software/coreutils/manual/html_node/
ls-invocation.html'
)
```

Here is the `awk` command: 

```
from ..base.command_tool import CommandTool
classAwk(CommandTool):
def__init__(self, user: str | None = None):
```

_Chapter 5_ 

140 

```
super().__init__(command_name='awk', user=user,
            doc_link='https://www.gnu.org/software/gawk/manual/gawk.html')
```

Most of the other filesystem idx_c6aafe8ctools follow the same pattern, but there is oneidx_9e9a9a72 exception, which is the `echo` tool. We will discuss that next. 

###### **Implementing the echo tool** 

The `echo` tool is different. Theidx_ba4f74bd purpose of the `echo` tool is to allow the LLM to create newidx_2d8a52f0 files or replace existing files. This is a super useful capability, of course. But, in order to do that in the shell, you must use shell redirection as follows: 

```
> echo "123" > ~/ttt/some-file
> cat ~/ttt/some-file
123
```

Keep in mind to manage the tool security and permissions, as we discussed in _Chapter 4_ . 

Our `CommandTool` base class doesn’t provide a way to redirect the output of a command to a file. One option would be to extend `CommandTool` to support output redirection, but we can also implement the functionality directly. Let’s see how it works. 

The imports are similar, except that it imports the built-in `os` package, the `Tool` module, and it doesn’t import the `shlex` package or the `CommandTool` module. We will see why very soon: 

```
import os
import sh
from backend.object_model import Tool, Parameter
```

The `Echo` class inherits directly from the `Tool` module and not from `CommandTool` because it needs to implement its own `run()` method: 

```
classEcho(Tool):
```

The constructor is a little more elaborate. Since it doesn’t invoke the built-in `echo` command, the description doesn’t include an external documentation link. There are also two required 

_Implementing Custom Tools_ 

141 

parameters, `content` and `file_path` , insteadidx_1e26c860 of the generic `args` parameter of tools derived 

from `CommandTool` . It also stores `user` , which defaults to `None` : 

```
def__init__(self, user: str | None = None):
self.user = user
        desc = 'Write content to a file, creating any necessary directories.'
super().__init__(
            name='echo',
            description=desc,
            parameters=[
                Parameter(
                    name='file_path', type='string',
                    description='The path of the file to write to.'),
                Parameter(
                    name='content', type='string',
                    description='The content to write to the file.')
            ],
            required={'file_path', 'content'}
        )
```

The `run()` method extracts the filename to write to and the content from the parameters (remember these will be providedidx_582b7fb7 by the LLM when it invokes the tool in order to create or replace a file). Then, it gets the directory of the target file: 

```
defrun(self, **kwargs):
        filename = kwargs['file_path']
        content = kwargs['content']
        dir_path = os.path.dirname(filename)
```

The logic then splits depending on the user. If a user is provided, then it uses `sudo` and shell commands, `mkdir` and `tee` , to create the target directory if needed and write/replace the file: 

```
ifself.user isnotNone:
            sh.sudo('-u', self.user, 'mkdir', '-p', dir_path)
            sh.sudo('-u', self.user, 'tee', filename,
                _in=content, _out=os.devnull)
returnf"Content written to {filename} as user {self.user}"
```

_Chapter 5_ 

142 

If no user is provided, then it uses Python directly to create the directory and write the file: 

```
        os.makedirs(dir_path, exist_ok=True)
withopen(filename, 'w') as file:
            file.write(content)
returnf"Content written to {filename}"
```

Now, we will shift our focus to yet idx_740c2628another utility tool, the test runner tool. 

###### **Test runner tool** 

The filesystem tools allow AI-6 to modify its own code! That’s right. Think about it. It can list its own files and directories idx_4c044084using the `ls` tool. It can read the contents of its own source files using the `cat` tool. It can create new files (or replace existing files) using the `echo` tool. Finally, it can idx_d3c53d7emodify existing files using the `sed` , `awk` , and `patch` tools. But agentic AI frameworks and LLMs don’t get everything right on the first shot (yet). It is still best practice to iterate on code changes and verify that the changes work before committing them. This is where the `test_runner` tool comes in. This tool can run Python unit tests written using the standard Python `unittest` framework in any directory. Let’s see how it works. 

As usual, it imports the `sh` module idx_95 **a** 5dab0 nd `Tool` and `Parameter` from the AI-6 object model: 

```
import sh
from backend.object_model import Tool, Parameter
```

The `TestRunner` class inherits directly from the `Tool` base class. The constructor calls the `Tool` base class, passing it a description and a single required parameter, `test_directory` : 

```
classTestRunner(Tool):
def__init__(self):
        desc = 'A tool to run Python unit tests using the unittest framework.'
super().__init__(
            name='python_test_runner',
            description=desc,
            parameters=[Parameter(name='test_directory',
type='string',
                description='The directory containing tests to run')],
            required={'test_directory'}
        )
```

_Implementing Custom Tools_ 

143 

The `run()` method runs all the Python unit tests in the target directory by invoking the Python interpreter with the `unittest` module, instructing it to discover all the unit tests in the target directory. It returns a dictionary with the keys of `"stdout"` and `"stderr"` . It handles a `sh` execution exception gracefully, but lets other exceptions propagate to the caller to handle: 

```
defrun(self, **kwargs):
        test_directory = kwargs['test_directory']
try:
            result = sh.python('-m', 'unittest', 'discover', '-s',
                test_directory)
return {"stdout": str(result), "stderr": ""}
except sh.ErrorReturnCode as e:
return {"stdout": e.stdout.decode('utf-8'),
"stderr": e.stderr.decode('utf-8')}
```

Let’s see it in action. The AI-6 backend unit idx_1f8aafe5tests are in the following relative directory to the Python root directory, `backend/tests` : 

```
>>> from backend import tests
>>> tests_dir = tests.__path__[0]
>>> tests_dir
'/Users/gigi/git/ai-six/py/backend/tests'
```

Now that we have the testidx_b3d38ea2 directory, we can instantiate and invoke the test runner tool and verify that the result was a success: 

```
>>> result = tr.run(test_directory=tests_dir)
>>> assert(result['stdout'] != '')
>>> assert(result['stderr'] == '')
```

Many times, you would need to start or restart an application to use your tools. The `bootstrap` tool helps you do that. Let’s see how. 

_Chapter 5_ 

144 

###### **Bootstrap tool** 

As we saw, the built-in idx_417f3d95tools of AI-6 support modifying its own code and testing those changes (since the AI-6 unit tests are implemented using the `unittest` framework). The last piece of the idx_61e30116puzzle is to restart the program controlling AI-6 after making changes and testing those changes. This is where the `bootstrap` tool comes in. After making changes to the AI-6 code, the LLM may decide to restart the controlling AI system, which will start with the modified code: 

```
import importlib
from backend.object_model import Tool
import os
import sys
```

The `Bootstrap` class is derived directly from `Tool` . The constructor is very simple, as there are no parameters. The description explains that ( `https://linux.die.net/man/3/execv` ) will be used to restart the program: 

```
classBootstrap(Tool):
def__init__(self):
        desc = 'Tool to restart the program using execv.'
super().__init__(
            name='bootstrap',
            description=desc,
            parameters=[],  # No parameters needed for execv
            required=set()
        )
```

The `run()` method is more sophisticated than the previous tools we have looked at. Let’s break it down. First, it locates the filename idx_cffef171of the `main` module of the program. If it can’t be found, it raises an exception: 

```
defrun(self, **kwargs):
        main_module = sys.modules['__main__']
        module_path = getattr(main_module, '__file__', None)
ifnot module_path:
raise RuntimeError("Cannot determine __main__.__file__; are you in a
REPL or notebook?")
```

_Implementing Custom Tools_ 

145 

If the `main` module idx_79ad10e1has a `spec` attribute, then it was run as `python -m module` . Let’s prepare the arguments correctly: 

```
getattr(main_module, '__spec__', None)
if spec and spec.name:
# Executed as a module: python -m package.module
            module_name = spec.name
            args = [sys.executable, '-m', module_name, *sys.argv[1:]]
```

Otherwise, it runs as a file with `python <main file>` . Let’s prepare the arguments for this mode: 

```
else:
# Executed as a script: python script.py
            args = [sys.executable, module_path, *sys.argv[1:]]
```

Finally, let’s restart the program using `os.execv()` and the appropriate command-line arguments. 

```
        os.execv(sys.executable, args)
```

The `bootstrap` tool is a powerful tool that allows the LLM to restart the controlling AI system after making changes to the AI-6 code. It is a simple tool, but it is very powerful and can be used to implement complex workflows that involve self-modifying code. But we can go even further and let the LLM directly manipulate the current conversation’s memory, too. 

###### **Memory tools** 

As you recall, AI-6 has a powerful idx_d0382140memory system that revolves around the concept of a idx_f77d3723session, which is a persistent collection of messages that encompasses multiple agentic loops. Sessions are stored in files, and we can let the LLM and/or the user manipulate the session files directly and load session files. This means that AI-6 allows the LLM to rewrite the memory of the current session, however it sees fit. This is a powerful capability that should be used with the utmost care. Typically, the LLM will not try to manipulate the session memory directly, but the user may instruct it to list previous sessions and load a previous session to continue where they left off. 

It’s important to remember that the session files will remain on disk after a session is over, and the AI system using AI-6 must idx_2c23b9 **e** 5 nsure that users’ rights and privacy are maintained and provide them with the option to delete sessions. 

_Chapter 5_ 

146 

Let’s see how the memory tools are implemented. There are four different tools that deal with memory: 

- `list_sessions` : List all the sessions in the memory directory 

- 

- `load_session` : Load a session by ID 

- 

- `get_session_id` : Get the current session’s ID 

- 

- `delete_session` : Delete a session by ID 

- 

Note that there is no tool toidx_0fe68d18 save the current session. This is because the session is saved automatically by AI-6 periodically (see the configured checkpoint interval discussed in _Chapter 4_ ). 

The design choice of multiple memory tools as opposed to a single memory tool with multiple actions is deliberate. It significantly simplifies the implementation and the testing of each tool. 

###### **Listing sessions** 

The `ListSessions` tool just needsidx_561baeec to import `json` , which is the format weidx_28b65a5c return the sessions in, and of course, the `Tool` base class. No command-line arguments are needed: 

```
import json
from backend.object_model import Tool
classListSessions(Tool):
"""Tool to list all available sessions in memory."""
```

The constructor initializes the tool with a reference to the `Engine` instance, which it will use later to actually list the sessions. There are no parameters for this tool, so the `parameters` list is empty, and the `required` set is also empty: 

```
def__init__(self, engine=None):
"""Initialize the tool.
Args:
            engine: Reference to the Engine instance
        """
self.engine = engine
super().__init__(
            name='list_sessions',
            description='List all available sessions in memory.',
            parameters=[],
```

_Implementing Custom Tools_ 

147 

```
            required=set()
        )
```

The `run()` method is where the actual listing of sessions happens. It checks whether the `engine` reference is set, and if not, it returns an error message. If the engine is set, it calls the `list_sessions()` method of the engine, whichidx_5a3e042f returns a list of session IDs. If noidx_af9f822b sessions are found, it returns a message indicating that no sessions were found. Otherwise, it returns a formatted string with the list of session IDs serialized to JSON: 

```
defrun(self, **kwargs):
"""List all available sessions.
        Returns:
            String with the details of all stored sessions (id, title and
filename)
        """
ifnotself.engine:
return"Error: Engine reference not set."
        sessions = self.engine.list_sessions()
ifnot sessions:
return"No sessions found in memory."
return"Available sessions:\n" + json.dumps(sessions)
```

The pattern of delegating the actual work to the `Engine` instance is common to all memory tools. The `Engine` instance, after all, is idx_78b4c289the source of truth for the AI-6 memory system. It is responsible for managing sessions, messages, and other memory-related tasks. There is no need to duplicate this logic in the tools, which would only make the code more complex and harder to maintain. 

_Chapter 5_ 

148 

###### **Loading sessions** 

When loading a session, weidx_1118703c need to specify the session ID. The tool will then use the `Engine` instance to load the specific session into its memory. Let’s see how this is implemented. We only need to import the `Tool` base class and the `Parameter` class from the AI-6 object model: 

```
from backend.object_model import Tool, Parameter
```

The `LoadSession` class is derived from the `Tool` base class. The constructor initializes the tool with a reference to the `Engine` instance. It expects a single required parameter, `session_id` , which is the ID of the session to load: 

```
classLoadSession(Tool):
"""Tool to load a specific session by ID."""
def__init__(self, engine=None):
"""Initialize the tool.
Args:
            engine: Reference to the Engine instance
        """
self.engine = engine
super().__init__(
            name='load_session',
            description='Load a specific session by ID.',
            parameters=[
                Parameter(
                    name='session_id',
type='string',
                    description='ID of the session to load'
                )
            ],
            required={'session_id'}
        )
```

_Implementing Custom Tools_ 

149 

The `run()` method is where the actual loading of the session happens. It checks whether the engine reference is set and the `session_id` parameter is provided. If not, it returns an error message indicating the problem. Then, it calls the `load_session()` method of the engine with the provided session ID. If theidx_41da61c6 session is loaded successfully, it returns a success message with the session ID. If the session does not exist or fails to load, it returns a failure message: 

```
defrun(self, session_id, **kwargs) -> str:
"""Load a specific session.
Args:
session_id: ID of the session to load
        Returns:
            String indicating success or failure
        """
ifnotself.engine:
return"Error: Engine reference not set."
ifnot session_id:
return"Error: Session ID is required."
        success = self.engine.load_session(session_id)
if success:
returnf"Successfully loaded session: {session_id}"
else:
returnf"Failed to load session: {session_id}. Session may not exist."
```

It is often useful to get the idx_ed07 **c** 7c5 urrent session ID ot be able to load it later. Here is how it’s done. 

###### **Getting the current session ID** 

Getting the current idx_13dee818 session ID is a simple operation. The tool just needs to return the ID of the current session, which is stored by the engine. 

We only need to import the `Tool` base class from the AI-6 object model. No parameters are needed for this tool: 

```
from backend.object_model import Tool
```

_Chapter 5_ 

150 

The `GetSessionId` class is derived from the `Tool` base class in the familiar pattern. The constructor expects a reference to the engine, which will do the actual work of retrieving the session ID. The `parameters` list is empty, and the `required` set is also empty since no parameters are needed to get the current session ID: 

```
classGetSessionId(Tool):
"""Tool to get the current session ID."""
def__init__(self, engine=None):
"""Initialize the tool.
Args:
            engine: Reference to the Engine instance
        """
self.engine = engine
super().__init__(
            name='get_session_id',
            description='Get the ID of the current session.',
            parameters=[],
            required=set()
        )
```

The `run()` method is where the actual retrieval of the session ID happens. As always, it performs sanity checks and then delegates the work to the `Engine` instance by calling its `engine.get_session_id()` method: 

```
defrun(self, **kwargs):
"""Get the current session ID.
        Returns:
            String with the current session ID
        """
ifnotself.engine:
return"Error: Engine reference not set."
        session_id = self.engine.get_session_id()
returnf"Current session ID: {session_id}"
```

It is sometimes useful to clean idx_4c121f1dup old sessions to avoid clutter. Here is how it’s done. 

_Implementing Custom Tools_ 

151 

###### **Deleting sessions** 

Deleting a session is a powerful operation that should be used with caution. The tool will delete a persistent sessionidx_9008792a file, so it is important to ensure that the session is no longer needed before deleting it. As always, the tool will use the `Engine` instance to delete the session. At this point, you should be familiar with the imports, the class declaration, and the constructor: 

```
from backend.object_model import Tool, Parameter
classDeleteSession(Tool): """Tool to delete a specific session by ID."""
def__init__(self, engine=None):
"""Initialize the tool.
Args:
        engine: Reference to the Engine instance
    """
self.engine = engine
super().__init__(
        name='delete_session',
        description='Delete a specific session by ID.',
        parameters=[
            Parameter(
                name='session_id',
type='string',
                description='ID of the session to delete'
            )
        ],
        required={'session_id'}
    )
```

The `run()` method is where the actual deletion of the session happens. Just like the other memory tools, it checks whether the `engine` reference is set and that the `session_id` parameter is provided. But it adds one more check to make sure we don't try to delete the current session. This is a safety measure to prevent accidental deletion of the active session, which can leave the engine in an invalid state: 

```
defrun(self, session_id, **kwargs):
"""Delete a specific session.
Args:
```

_Chapter 5_ 

152 

```
session_id: ID of the session to delete
    Returns:
        String indicating success or failure
    """
ifnotself.engine:
return"Error: Engine reference not set."
ifnot session_id:
return"Error: Session ID is required."
# Don't allow deleting the current session
if session_id == self.engine.get_session_id():
return"Error: Cannot delete the current active session."
    success = self.engine.delete_session(session_id)
if success:
returnf"Successfully deleted session: {session_id}"
else:
returnf"Failed to delete session: {session_id}. Session may not exist."
```

We covered a lot of ground in this section. We looked at the implementation of multiple custom tools in AI-6 based on the tool system design we covered in _Chapter 4_ . We have also seen how these tools can be used to idx_f685635dmodify the AI-6 code, test the changes, restart the program, and 

manipulate the session memory. This is a powerful set of tools that allows AI-6, in theory, to improve itself in a virtuous cycle. 

In the next section, we will see how to put these tools into action and let AI-6 implement a new tool from scratch. 

###### **Implementing a new tool from scratch with AI-6** 

AI-6 comes with many built-in tools that allow it, in theory, to improve its own code. It can read and write its own source code, write idx_6025d40enew code and tests, run tests, and restart the program. It also has a Git tool that we didn't examine in detail, but it allows AI-6 to perform any Git operation, such as cloning a repository, creating branches, adding files, committing changes, and pushing them to a remote repository. 

_Implementing Custom Tools_ 

153 

But AI-6 doesn't have a tool for interacting with GitHub. Centralized source control systems such as GitHub are at the heart of modern software. Let's take AI-6 for a spin and see whether it can build its own tools, with some useful help from us, of course. 

###### **How to interact with AI-6** 

AI-6 supports multiple interfaces idx_b807390eout of the box: a chatbot CLI, Slack-based interface, and a web UI interface. 

For this little project, we will use AI-6 through its chatbot CLI, which is very similar to the `k8sai` interface that we saw in _Chapter 3_ . We will cover the Slack and web interfaces in detail in the next chapter. 

When we use theidx_3ddc6f45 chatbot CLI, it serves as the AI system that uses AI-6. Here is how we start the chatbot CLI: 

❯ `python -m frontend.cli.ai6 Using .env file from /Users/gigi/git/ai-six/py/ frontend/cli/.env` 

Next comes the interaction in the chat interface: 

👤 `[You]: hi` 🤖 `[AI-6]: Hello! How can I assist you today? ———-` 👤 `[You]:` 

With all the preliminaries out of the way, we can start interacting with AI-6 to build a shiny new GitHub tool. 

###### **Building a new GitHub tool with AI-6** 

Our goal is to let AI-6 do all the work based on a high-level description of the tool we want to implement. This will be idx_62dfd300a very interactive process where we provide guidance, AI-6 does the work, and, at each step, we verify the results and provide feedback. The tool we want to implement is a GitHub tool that will allow AI-6 to interact with GitHub repositories, issues, pull requests, and so on. Let's start by describing the tool we want to implement: 

👤 `[You]: I want to create a command-line tool for interacting with Github using the gh CLI (already installed and configured) similar to the tools in /Users/gigi/ git/ai-six/py/backend/tools. how do you propose to that?` 🤖 `[AI-6]: To create a command-line tool for interacting with GitHub using the GitHub CLI (gh), you can follow these steps to set up a structure similar to existing tools like the Ollama tool. Here’s how you can achieve this:` 

_Chapter 5_ 

154 

`Create a Base Command Tool Class (if not already existing): This class (like CommandTool) will handle generic CLI command execution, including setting up basic configurations like user data. Create the GitHub CLI Tool Class: Use this class to define the GitHub-specific command-line interactions. ``` OK. That’s a good start, but we don’t need to create a base command tool class, as we already have it. Let’s tell AI-6 about it.` 👤 `[You]: Since the Ollama tool exists, then it probably the CommandTool base class already exists` 🤖 `[AI-6]: You're correct. If the `Ollama` tool utilizes a `CommandTool` base class, then it likely already exists in your project structure. In this case, you can directly proceed to implement the GitHub CLI tool by leveraging this existing base class. Here's how you can do it: ### Step-by-Step Guide to Create the GitHub CLI Tool 1. **Locate the Existing `CommandTool` Base Class:** - First, confirm the location and available methods of the `CommandTool` class within your project. 2. **Create the GitHub CLI Tool Class:** With the base class available, you can create a new tool class that extends `CommandTool` for GitHub interactions.` _`# gh_cli_tool.py # Import the CommandTool class from its existing location`_ `from backend.tools.base.command_tool import CommandTool class GhCLI(CommandTool): def __init__(self, user: str | None = None): super().__init__( command_name='gh', user=user, doc_link='https://cli.github.com/manual/') def list_repositories(self) -> str: return self.run_command('repo list')` 

_Implementing Custom Tools_ 

155 

```
defcreate_repository(self, name: str) -> str:
returnself.run_command(f'repo create {name}')
defclone_repository(self, repo: str) -> str:
returnself.run_command(f'repo clone {repo}')
# Add more methods to interact with other GitHub functionalities using the
'gh' CLI
```

Hmm, it looks like AI-6 didn’t invest the time to study the `CommandTool` base class, which already provides a `run()` method idx_a1a11bbe to execute the command-line program with any set of arguments. It suggests adding methods such as `list_repositories()` , `create_repository(name: str)` , and `clone_repository(repo: str)` . These methods are not necessary, as we can just use the `run()` method of the `CommandTool` base class to run any command-line program with any set of arguments. 

Let’s tell AI-6 about it: 

👤 `[You]: hold on. let's do this step by step. find and show me the code for the CommandTool base class` 🤖 `[AI-6]: Here is the code for the `CommandTool` base class: import sh import shlex from backend.object_model import Tool, Parameter class CommandTool(Tool): def __init__( self, command_name: str, user: str | None = None, doc_link: str = "" ): self.command_name = command_name self.user = user description = f'{command_name} tool. ' + f'See {doc_link}' if doc_link else '' parameters = [Parameter( name='args', type='string', description=f'command-line arguments for {command_name}')] required = {'args'} super().__init__(` 

_Chapter 5_ 

156 

```
            name=command_name,
            description=description,
            parameters=parameters,
            required=required
        )
defrun(self, **kwargs):
        args = shlex.split(kwargs['args'])
ifself.user isnotNone:
return sh.sudo('-u', self.user, self.command_name, *args)
else:
returngetattr(sh, self.command_name)(*args)
### Explanation:
```

```
- **Class Inheritance:** `CommandTool` inherits from a base class called `Tool`.
- **Initialization:** The constructor initializes the command tool with a command
name, optional user, and documentation link.
- **Parameters:** It sets up the required parameters for the tool, including
command-line arguments.
- **Command Execution:** The `run` method uses the `sh` library to execute shell
commands, optionally using `sudo` for a specified user.
Great. Now, we’re getting closer. Let’s continue carefully guiding AI-6 towards
better understanding of its own tool architecture.
```

👤 `[You]: ok. now that you understand how the CommandTool base class works, check its base class Tool` 🤖 `[AI-6]: The `Tool` class from which `CommandTool` inherits is an abstract base class (ABC). Here's a breakdown of the `Tool` class: - **Attributes:**` 

```
  - `name`: A string that represents the name of the tool.
```

```
  - `description`: A string that provides a description of the tool.
  - `parameters`: A list of `Parameter` objects, each representing a command-line
or functional parameter for the tool.
```

```
  - `required`: A set of strings indicating which parameters are required.
```

_Implementing Custom Tools_ 

157 

```
- **Methods:**
  - `configure`: This method allows optional configuration of the tool using a
provided dictionary. It's intended to be
     overridden if needed.
  - `run`: This is an abstract method that must be implemented by any
subclass. It defines how to execute the tool using
     the given arguments and return the result as a string.
### Next Steps
```

```
With this understanding of the `CommandTool` base class and its parent `Tool`
class, you can confidently create a new
tool for the GitHub CLI by extending `CommandTool`. If you're ready, we can
proceed to create the `GhCLI` tool class
that utilizes the GitHub CLI (`gh`) for GitHub interactions. Let me know if you
want to move forward with this step!
```

Excellent. But I don’t like theidx_ea324617 class name, `GhCLI` . It exposes implementation details and is not aligned with other tools’ naming conventions: 

👤 `[You]: I want the Github tool class to be called Just Github. The fact it is using gh cli is an implementation detail. what files or directories need to be created?` 🤖 `[AI-6]: To create a new command-line tool class named `Github`, you should follow these steps to integrate it into your existing project structure: Step 1: Determine the File Location ----------------------------------Since the existing tools, such as `Ollama`, are located in a specific directory within your project, you should place your new tool in a similar location for consistency and organization. Let's assume you are following this structure (similar to `Ollama`):` 

```
backend/
  tools/
    base/
ollama/   # Contains the Ollama tool definition
github/   # This is where we will place the new Github tool
```

_Chapter 5_ 

158 

```
Step 2: Create the Necessary Directories and Files
--------------------------------------------------
1. **Create a Directory for the Github Tool:**
   - Path: `backend/tools/github/`
   - This directory will contain the implementation of the `Github` tool.
2. **Create the `Github` Tool Class File:**
   - Path: `backend/tools/github/github.py`
   - This file will contain the definition of the `Github` class.
Step 3: Implement the `Github` Tool Class
------------------------------------------
...
```

This is exactly what we idx_1a91b86fwanted to hear. AI-6 is on the right track. Let’s continue: 

👤 `[You]: OK. Show me the Github class` 🤖 `[AI-6]: Here is the new command-line tool class named `Github`` _`# backend/tools/github/github.py`_ `from backend.tools.base.command_tool import CommandTool class Github(CommandTool): def __init__(self, user: str | None = None):` _`# Initialize with the command name 'gh' and provide a documentation link`_ `super().__init__( command_name='gh', user=user, doc_link='https://cli.github.com/manual/') def execute(self, args: str) -> str: """ Execute any GitHub CLI command by providing the appropriate arguments. Args: args: Command-line arguments to pass to the `gh` CLI. Returns:` 

_Implementing Custom Tools_ 

159 

```
            The output from the command execution.
        """
returnself.run(args=args)
```

Very nice! Even the documentation link is idx_3e3d0 **c** 9a orrect. But it added a useless `execute()` method that just calls the `run()` method. I could just remove it myself, but let’s keep this session fully interactive and ask AI-6 to remove it: 

👤 `[You]: isn't the run() method enough to execute any gh cli command?` 🤖 `[AI-6]: You're absolutely correct in observing that if you wanted to provide direct access to the `CommandTool`'s `run()` method, you don't strictly need an additional `execute()` wrapper in the `Github` class. The primary role of the `execute()` method was to give a semantic representation or alias to the act of executing a GitHub CLI command, but it indeed adds no extra functionality beyond `run()`. Thus, in practice, you could simply use the `run()` method directly from instances of the `Github` class for executing commands, since it's already designed to take care of running the CLI with the specified arguments. Here's a revision of the approach without the `execute()` method: Implementation without `execute()` ----------------------------------` _`# backend/tools/github/github.py`_ `from backend.tools.base.command_tool import CommandTool class Github(CommandTool): def __init__(self, user: str | None = None):` _`# Initialize with the command name 'gh' and provide a documentation link`_ `super().__init__( command_name='gh', user=user, doc_link='https://cli.github.com/manual/') Usage Example ------------You would use the `run()` method directly to execute any `gh` CLI command:` 

_Chapter 5_ 

160 

```
if __name__ == '__main__':
    gh_tool = Github()
# List repositories
print(gh_tool.run(args='repo list'))
# Create a new repository
# print(gh_tool.run(args='repo create new-repo'))
# Clone a repository
# print(gh_tool.run(args='repo clone owner/repo'))
Conclusion
----------
By using the `run()` method directly, you maintain a minimalistic and efficient
implementation, relying on the
capabilities already defined in the `CommandTool` base class. This keeps the
`Github` class straightforward while fully
leveraging the flexibility to execute any command supported by the `gh` CLI.
```

AI-6 arrived at the correctidx_edb9b0a1 solution after some cajoling. I continued the session by asking it to write tests and execute them, and it did so successfully. The tests were written in the `unittest` framework and executed using the `python_test_runner` tool we saw earlier. 

Here is the test code: `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch05/ai-six/py/backend/tests/tools/github/ test_github.py` . 

This session is a great example of how AI-6 can add new capabilities to itself by learning to understand its own code and architecture, but it also demonstrates the importance of humans in the loop and guiding the AI system through the process. While the early suggestions of the GitHub tool were not obviouslyidx_aaf56398 wrong, they didn’t fit well into the existing tool architecture. 

Let’s see how to implement a new tool manually, without the help of AI-6. 

_Implementing Custom Tools_ 

161 

###### **Implementing a new tool manually** 

The next tool will be a little more complicated. Weidx_538ddd7f will build a Claude tool. This tool will allow AI-6 to send LLM inference requests to the Anthropic Claude LLM ( `https://claude.ai/` ). While AI-6 is working with an LLM idx_0c538969provider such as OpenAI, it can make use of a different LLM provider, such as Anthropic Claude. The Claude tool is implemented in `backend/tools/ claude_tool.py` . It is a custom tool that extends the `Tool` base class and uses the Anthropic Python SDK ( `https://github.com/anthropics/anthropic-sdk-python` ) to send requests to the Claude LLM. Let’s see how it is implemented. 

The tool imports the `anthropic` module, which is the Python SDK for the Anthropic Claude LLM, and `Tool` and `Parameter` from the AI-6 object model: 

```
import anthropic
from backend.object_model import Tool, Parameter
```

The `ClaudeTool` class is derived from the `Tool` base class. The constructor is a little more complicated than the previous tools we saw. It initializes the tool with a description, parameters, and a required set of parameters. There are four parameters: 

- `prompt` : The prompt or question to send to Claude. 

- 

- `model` : The model to use for inference. The default is `claude-sonnet-4-20250514` . 

- 

- `max_tokens` : The maximum number of tokens to generate. The default is `1000` . 

- 

- `temperature` : The temperature for sampling ( `0.0` – `1.0` ). The default is `0.7` . 

The `max_tokens` and `temperature` defaults are taken from the Anthropic documentation ( `https://docs.anthropic.com/en/docs/about-claude/models/overview` ). When the LLM invokes the tool, it can override these defaults by providing different parameters in the request. Only the `prompt` parameter is required. 

Note that we have a `self.client` attributeidx_382b3abd initialized to `None` . This will be used later to store the Anthropic client: 

```
classClaude(Tool):
def__init__(self):
        desc = """
Send inference requests to Anthropic Claude LLM. Useful for getting a
second opinion or
            different perspective from another AI model.
```

_Chapter 5_ 

162 

```
        """
super().__init__(
            name='claude',
            description=desc,
            parameters=[
                Parameter(
                    name='prompt',
type='string',
                    description='The prompt or question to send to Claude'),
                Parameter(
                    name='model',
type='string',
                    description="""
See https://docs.anthropic.com/en/docs/about-claude/
models/overview.
                        Defaults to claude-sonnet-4-20250514
                    """),
                Parameter(
                    name='max_tokens',
type='integer',
                    description='Maximum number of tokens to
generate. Defaults to 1000'),
                Parameter(
                    name='temperature',
type='number',
                    description='Temperature for sampling (0.0-1.0). Defaults to
0.7')
            ],
            required={'prompt'}
        )
self.client = None
```

At last, we have a tool that requires configuration. The `configure()` method is used to get the Anthropic API key from the configuration dictionary idx_2275c25 **a** nd initialize the Anthropic client if present: 

```
defconfigure(self, config: dict) -> None:
"""Configure the Claude tool with API key."""
if'api_key'in config:
self.client = anthropic.Anthropic(api_key=config['api_key'])
```

_Implementing Custom Tools_ 

163 

The `run()` method is where the actual inference request is sent to the Claude LLM. It checks whether the client is initialized, and if not, it returns an error message. It then retrieves the parameters from the `kwargs` dictionary. These parameters include `prompt` , `model` , `max_tokens` , and `temperature` . They will be provided by the current LLM that AI-6 is working with (e.g., OpenAI GPT-4o) when it invokes the tool. You can see that only the `prompt` parameter is required. The other parameters have default values, so they are optional. Once the parameters are retrieved, it calls the client’s `messages.create()` method to send the request to the selected Claude model. The response is then returned as a string: 

```
defrun(self, **kwargs) -> str:
ifself.client isNone:
return"Error: Claude API key not configured. Set 'api_key' in
tool_config for claude tool"
        prompt = kwargs['prompt']
        model = kwargs.get('model', 'claude-sonnet-4-20250514')
        max_tokens = kwargs.get('max_tokens', 1000)
        temperature = kwargs.get('temperature', 0.7)
        response = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
return response.content[0].text
```

We can see how the simple tool interface of AI-6 allows us to implement a wide variety of tools, including command-line tools idx_0b19ba35such as the filesystem tools, internal AI-6 tools such as the memory tools, and tools that invoke external APIs such as the Claude tool. The tool interface is flexible enough to accommodate different types of tools and their specific requirements. 

_Chapter 5_ 

164 

###### **Summary** 

Let’s recap. We provided a comprehensive exploration of the AI-6 tool system, shifting the focus from the high-level orchestration engine to the internal structure and behavior of the tools themselves. We examined how AI-6 achieves provider-agnostic tool interoperability by defining a unified, generic tool specification that maps cleanly to provider-specific formats such as OpenAI’s function calling or Ollama’s tool schema. These tools are designed to be reusable, consistent, and easily translatable across different LLM APIs, with a robust schema and input validation mechanism at their core. 

We continued with detailed walkthroughs of built-in command-line tools such as `pwd` , `ls` , `awk` , and a special-purpose `echo` tool for file writing. These tools are implemented using the `CommandTool` base class and are capable of performing file operations and shell interactions directly from within the AI framework. Additional tools, such as `test_runner` for executing Python unit tests and `bootstrap` for restarting the AI-6 program, showcase how the system supports iterative self-modification. Memory tools such as `list_sessions` , `load_session` , and `delete_session` extend the agent’s ability to manage and manipulate persistent session state in a controlled manner. 

We then explored how to develop new tools interactively using AI-6 itself, demonstrated through the creation of a GitHub tool that wraps the `gh` CLI. This exercise illustrated how human guidance can be combined with agentic reasoning to extend AI-6’s capabilities by pointing it to its own source code. Finally, we looked at building an API-based Claude tool for interfacing with Anthropic’s LLMs, emphasizing how AI-6 can integrate and leverage multiple LLM providers simultaneously. Overall, these examples highlighted the power and flexibility of the AI-6 tool system. 

In the next chapter, we will turn to the frontend side of the AI-6 project, covering user-facing interfaces via Slack and Chainlit (web UI), which enable interactive and conversational control over the system. 

_Implementing Custom Tools_ 

165 

###### **Get This Book’s PDF Version and Exclusive Extras** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
i<br>4<br>|<br>e<br>aeé<br>[=] :<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require an invoice._ 

# 6 

##### Creating Chat Interfaces Using Slack and Chainlit 

In the previous chapter, we explored AI-6's internal tool architecture—how tools are defined, registered, and executed. While a powerful backend is essential, the true potential of an agentic AI system is unlocked through interfaces that allow humans to effectively collaborate with autonomous agents. 

**User interfaces** ( **UIs** ) in idx_e **a** 39bc8b gentic systems serve a unique role. Unlike traditional applications, where the UI primarily captures input and displays output, agent interfaces must balance autonomy with control. They need to provide real-time visibility into what the agent is doing, allow interruptions when needed, surface debugging information during failures, and build trust through transparency. The challenge is designing interfaces that neither stifle the agent with excessive oversight nor leave users blind to its actions. 

This chapter explores how AI-6 implements two complementary interfaces: a Slack bot for collaborative team workflows and a Chainlit-based web UI for individual interactions. 

This chapter covers the following topics: 

- Why the UI matters in agentic AI workflows: visibility, interruptibility, debugging, and trust 

- Building a Slack bot interface with multi-channel support and real-time collaboration 

- 

- Developing a web UI with Chainlit for rich, customizable single-user experiences 

- 

- Integrating frontend interfaces with the AI-6 engine and tool ecosystem 

- 

- Best practices for designing interactive agent interfaces 

- 

_Chapter 6_ 

168 

###### **Technical requirements** 

To follow along, refer to the instructions in the README file: 

```
https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-
A2A/blob/main/ch06/ai-six/py/README.md
```

###### **Why the UI matters in agentic AI workflows** 

The claim to fame idx_fd6044eeof agentic AI systems is that they are autonomous and can perform complex tasks on behalf of users. However, this automation must often be balanced with the need for human oversight, control, or even just visibility into what the agent is doing. The UI plays a crucial role in the success of agentic AI systems, serving as the bridge between the user and the agent's actions. In this section, we will explore several key aspects of why the UI is essential in agentic AI workflows. 

###### **Agent feedback loops and visibility** 

Let's take the viewpoint of the human user of the agentic AI system. There is a delicate balance between letting the agent operate completely autonomously, possibly making mistakes and going off on a tangent, and micro-managing the agent too much, watching every step and correcting it at every turn. Note that both extremes can actually be useful at different times. 

Let's consider the example of automating a complex workflow on a website that involves logging in, navigating to different sections, collecting information, and taking actions based on the information, as well as responding to change notifications. The user may be familiar with the task, but they need to "teach" the agent how to do it. If the user aims for total automation, then their prompt must be very detailed and explain their intentions very precisely. 

This is difficult. So, the user may start with a more general prompt and then refine it as the agent performs the task with partial success initially. Over time, the user will be able to capture the entire workflow in a nuanced way in the prompt. At this point, the agent can perform the task autonomously without any user intervention unless something rare and unexpected happens. 

Another important aspect is visibility and progress updates while the agent is working. This is especially important for long-running tasks. The user may want to know what the agent is doing, how long it will take, and whether it is making progress. The UI should provide realtime feedback on the agent's actions, status, and any issues that arise. Consider a task such as analyzing all of Netflix's newly released movies in the last three months and finding a cool movie to watch. The agent may take a long time, but the user may be interested in seeing partial results and may decide to watch a movie before the complete analysis is done. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

169 

That takes us to the next important aspect of the UI in agentic AI systems: the ability to interrupt the agent and either abort the task or steer it in a different direction. 

###### **Interruptibility and human-in-the-loop design** 

There are many ways to design an agentic AI system that lets humans interrupt the agent and take control. First, the system may be designed to limit the time that a single agentic loop can run. This can be done by configuring a time limit, a number of operations, or even by cost (number of tokens used). If the agent reaches the limit, it will stop, report back to the user, and wait for further instructions. 

The benefit of idx_a9fa2121this approach is that the user is always in control and can decide whether to continue the task, modify it, or abort it. The downside is that under normal conditions, when everything is going well and the agent is making good progress, the user must still sit there and keep pressing the "continue" button. This can be tedious and frustrating, especially for longrunning tasks. It may still be a productive approach if the user takes much longer than the agent to perform every step of the task manually. Of course, if the user is not attentive, then the AI system will just pause waiting for the user to continue. 

Another approach is to allow the agent to run autonomously but provide ongoing progress reports and status updates. The user may decide at any point to interrupt the agent and either update the task or cancel it completely. 

There are several ways to improve the situation. We can let the LLM decide when to pause and report back to the user. For example, the prompt may include instructions such as "after every 10 steps or if you exceed 50,000 tokens, pause and report back to the user." This way, the agentic AI system will run autonomously, but it will still provide periodic checkpoints. If we want to take it further, we can add more intelligent pause conditions, such as "if you feel you can't make progress, report back to the user." 

Of course, this can apply to status updates and notifications as well. The agentic AI system can notify the user only when it encounters an unusual situation or when it has important updates to share. The LLM will determine (based on the prompt and conversation history) which situations require informing the user. This way, the user is not bombarded by constant notifications, but still has visibility into the agent's actions and is notified about important events. 

_Chapter 6_ 

170 

###### **Diagnosing and debugging agent behaviors** 

Another important use case where the UI is essential is diagnosing and debugging agent behaviors. When an agent doesn't perform properly, there may be many reasons for that: 

- The agent may not have enough information 

- 

- The prompt may be too vague 

- 

- The tools might not support all the needed actions 

- 

- The LLM itself is not up to the task (wrong model) 

- 

There are also performance issues where the agent actually completes the task successfully, but it takes too long or uses too many tokens. Let's not forget that the failure might be due to a combination of reasons. 

Since there are so many possible reasons for agent failure, the UI for debugging must expose as much information as possible. This includes the initial prompt and tools used by each agent, the complete conversation history, including each and every tool call and its parameters, the LLM responses, and, in many cases, additional logging and metrics of external systems accessed by the tools. 

For example, if the AI system is misbehaving when diagnosing problems in a Kubernetes cluster, then debugging the issue should include telemetry and logs from the target Kubernetes cluster. 

This level of scrutiny is essential for diagnosing and debugging agent behaviors but is typically too noisy for normal users of the system. This means that you need to design different UIs for different user roles. The AI system developers and operators need a very detailed view of the system. The end users may only need a high-level view that exposes the agent's actions and status updates with the proper level of abstraction. Details such as tool calls and token counts may be too much for the end users, but essential for the developers and operators. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

171 

###### **Balancing autonomy and user control** 

As weidx_3e358620 discussed at the start of this chapter, there is a delicate balance between letting the agent operate autonomously and stifling it with too much user control. The UI plays a crucial role in managing this balance. Ideally, the system is designed in a way that the user can manage the level of autonomy it grants to the agents. For example, Claude Code (see `https:// docs.anthropic.com/en/docs/claude-code/overview` ) is idx_d27c **a** 7dc n agentic coding assistant that runs in the terminal. It solves the problem of agent autonomy at multiple levels with proper user control. First, when performing a task, it provides ongoing status updates of its progress. When Claude was asked whether all the AI-6 tests were passing, it started by finding all the tests. It listed all the tests it found in the code base, while providing a lot of information in real time, such as the number of tools used, the overall time, and the number of tokens. It can also be interrupted by pressing the _Esc_ button: 

<!-- Start of picture text -->
claude<br>Welcome to Claude Code!<br>+ Added support for Bedrock API keys through environment variable AWS_BEARER_TOKEN_BEDROCK<br>+ ‘-append-system-prompt* can now be used in interactive mode, not just —-print/-p.<br>> check if all the tests of AI-6 are passing<br>@ I'll check if all the tests are passing by first finding the test command and then running<br>yy it.<br>@ Task(Find test commands)<br>Read 1@ lines (ctrl+r to expand)<br>Read 1@ lines (ctri+r to expand)<br><!-- End of picture text -->

_Figure 6.1: Check AI-6 tests_ 

Once Claude Codeidx_aaeb346d found all the tests, it automatically started running them. It didn't wait for approval. It identified that some tests failed, and it even identified the root cause (the `sh` module is missing). 

_Chapter 6_ 

172 

<!-- Start of picture text -->
Task(Find test commands)<br>Done (2@ tool uses - 23.6k tokens - 1m 0.1s)<br>je Now I'll run the tests to check if they're all passing:<br>© Bash(python -m unittest discover -s backend/tests -v)<br>+144 lines (ctrl+r to see all)<br>Je No, the tests are not all passing. There are 18 errors out of 40 tests. The main issue is a<br>missing dependency - the sh module is not installed. Let me check the requirements and<br>install it:<br><!-- End of picture text -->

_Figure 6.2: Running AI-6 tests_ 

The reason idx_c2605c1ethat it just ran the tests is that Claude Code has a configuration file with permissions to perform certain actions. In a previous session, Claude was allowed to run the tests, so it didn't need to ask for permission again. If the user wanted to change that, they could have edited the `.claude/settings.local.json` and removed the permission. Here is a snippet: 

```
{
"permissions": {
"allow": [
"Bash(chainlit run:*)",
"Bash(git add:*)",
"...",
"Bash(rg:*)",
"Bash(cat:*)",
"Bash(PYTHONPATH=./:$PYTHONPATH python3 -m unittest discover backend/tests -
v)",
"Bash(ls:*)",
"Bash(mkdir:*)",
"Bash(./ai6.sh:*)"
    ],
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

173 

```
"deny": []
  },
"enableAllProjectMcpServers": false
}
```

Claude Code wanted to install the missing `sh` module, but since it didn't have automatic permission to install packages, it asked for permission. There is actually no need to install the `sh` module idx_b275d591 because it is already installed in the virtual environment of AI-6. The correct solution is to activate the virtual environment and re-run the tests. 

<!-- Start of picture text -->
@ No, the tests are not all passing. There are 18 errors out of 40 tests. The main issue is a<br>missing dependency - the sh module is not installed. Let me check the requirements and<br>install it:<br>Bash(cd py && pip install sh)<br>L. Running.<br>Bash command<br>cd py && pip install sh<br>Install missing sh dependency<br>Do you want to proceed?<br>> 1. Yes<br>Yes, and don't ask again for pip install commands in /Users/gigi/git/ai-six<br>No, and tell Claude what to do differently (esc)<br><!-- End of picture text -->

_Figure 6.3: Asking permission to install packages_ 

That quick session with Claude Code illustrates how the UI can provide a balance between AI system autonomy and user control. But the UI is not just about control. It is also about trust. 

###### **UI as a trust-building mechanism** 

The more idx_218 **a** c3a0 utonomous agentic AI systems are, the more value they provide—of course, assuming they work correctly and accomplish the goals set by the users. Because these systems often make complex decisions, the UI must make their behavior transparent and explainable. A trustworthy UI shows what the agent is doing, why it’s doing it, and what it plans next. It exposes the right level of information to the users, which may be tool calls, decision points, and intermediate steps. The idea is that users can follow the reasoning even when it’s imperfect. When users can trace errors back to their cause, they’re more likely to refine their input rather than abandon the system. 

_Chapter 6_ 

174 

Trust also depends on clear boundaries and control. Users need to know what actions the agent is allowed to take and when it will ask for permission. Explicit permission systems, such as those used by Claude Code, give users confidence that the agent won’t make risky changes without oversight. At the same time, the UI should signal uncertainty, showing when the LLM is unsure or requesting help. This combination of visibility, restraint, and humility fosters a collaborative dynamic where users feel in charge and well informed, not sidelined or surprised. Now that we have covered the importance of the UI in agentic AI workflows, let's explore how to build such interfaces. 

###### **Building a Slack bot interface** 

A word ofidx_43eff57d caution before we dive into the details of building a Slack bot interface for AI-6. Agentic AI systems such as LangGraph, AutoGen, CrewAI, and our own AI-6 focus on defining agents and tools, managing memory and sessions, and executing tasks autonomously. The AI systems built on top of these frameworks are responsible for providing the UI, which is often customized to a specific use case or domain. The reason AI-6 provides several UIs is for educational purposes. 

The Slack bot interface has idx_bae3351bseveral unique properties that make it a great choice for some agentic AI systems: 

- **Familiarity** : Many users are already familiar with Slack, making it easier to onboard new users 

- **Real-time interaction** : Slack allows for real-time communication, which is essential for interactive agent workflows 

- **Multi-user support** : Slack supports multiple users and channels, allowing for collaborative workflows 

- **Integration with other tools** : Slack can integrate with various tools and services, making it easier to build complex workflows 

- **Notifications and alerts** : Slack can send notifications and alerts, which is useful for long-running tasks or important updates 

- **Security and access control** : Slack provides built-in security features, such as user authentication and access control, which are essential for agentic AI systems that may handle sensitive data 

With these advantages in mind, let’s explore how the AI-6 Slack bot actually works in practice. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

175 

###### **Taking the AI-6 Slack bot for a spin** 

Let's start by taking idx_862767c7the AI-6 Slack bot for a spin and see what it looks like before diving in. We can launch it using the convenient `ai6.sh` script, passing the `slack` argument: 

❯ `./ai6.sh slack virtualenv: /Users/gigi/git/ai-six/py/venv Loaded environment variables from /Users/gigi/git/ai-six/py/frontend/slack/.env Joined ai-6-test Bolt app is running!` 

A Slack workspace called `bot-playground` was created, including a channel called `ai-6-test` (see _Figure 6.4_ ). The idx_20f85817AI-6 Slack bot is a Slack app ( `https://api.slack.com/docs/apps` ) that idx_53f4 **a** 9a9 utomatically adds the `ai-6-` prefix to any channel andidx_ecef1f86 starts listening for messages. 

<!-- Start of picture text -->
@ © tryout = @ RR @: a-<br>o wre | wi three @ recaps (DAaseanas +"<br>wok 4 > Chane<br>fer} Si<br>@ hae #ai-6-test<br>= You created this channel today. This is the very beginning of the 4 ai-6-test channel<br>G<br>Saar Sayfan @ Add Description _& Add People to Channel<br>aay Bare<br>hee (KF THis channe as been made a default channel forall new memberswho join bot-playground. i you want to remove this<br>+ Message #<br><!-- End of picture text -->

_Figure 6.4: The #ai-6-test Slack channel_ 

_Chapter 6_ 

176 

The AI-6 Slack bot is connected to AI-6, so it has access to all the tools and capabilities of AI-6. Let's see whether it knows what the current directory is: 

<!-- Start of picture text -->
©:~~ what'sGigi Sayfanthe curr3:14dir? PM<br>Al-6 APP 3:15 PM<br>Sm The current directory is /Users/gigi/git/ai-six/py. (edited)<br>1reply Today at 3:15 PM<br><!-- End of picture text -->

_Figure 6.5: Asking about the current directory_ 

Note that in idx_161b20c9addition to the response message, there isidx_62c7858d also a reply in a thread associated with the message. Let's expand the thread and observe the tool calls AI-6 executed as requested by the LLM to generate the final response: 

<!-- Start of picture text -->
Thread x<br>re) Al-6The currentAPP 4 minutesdirectory ago is /Users/gigi/git/ai-six/py . (edited<br>1 reply<br>ri) Al-6Tool call:APP pwd4 minutes ago<br>/Users/gigi/git/ai-six/py<br>Reply.<br>© Also send to # ai-6-test<br>+ha@O@ Ge :<br><!-- End of picture text -->

_Figure 6.6: Observing the tool call_ 

Note the user experience choice here. The tool calls are not shown in the main message, but in a thread. This is a good choice because it keeps the main message clean and focused on the 

_Creating Chat Interfaces Using Slack and Chainlit_ 

177 

final response, while still providing access to the details of how the response was generated, if the user is interested in that. Let's try another request with multiple tool calls: 

<!-- Start of picture text -->
Lo What Gigi Sayfan are the 3:31 files  PM in the current directory and how many<br>of them contain the word "import"?<br>AI-6 APP 3:31 PM<br>‘== The files in the current directory are:<br>1. |=-init=;py<br>2. __pycache__ (directory)<br>3. backend (directory)<br>4. chainlit.md<br>5. frontend (directory)<br>6. memory (assumed to be a directory)<br>7. README .md<br>8. requirements.txt<br>9. venv (directory)<br>Among the files that were checked ( __init__.py,<br>chainlit.md, README.md, requirements.txt ), none of<br>them contain the word "import". Would you like to check<br>files inside the directories or any specific files? (edited)<br>5 replies Last reply today at 3:32 PM<br><!-- End of picture text -->

_Figure 6.7: Multiple tool calls to check files in the current directory_ 

Excellent. Theidx_8212352d AI-6 Slack bot is able to handle multiple idx_dc75e422tool calls and provide the correct answer. But how did it do that? Let's take a look at the tool calls in the thread. The LLM asked AI-6 to correctly invoke the `ls` tool to list all the files in the current directory. So far, so good. But then it requested AI-6 to invoke the `cat` tool to read the entire contents of each file and send it back, in order to find out whether it contained the word `import` . 

_Chapter 6_ 

178 

This is correct, but it is extremely inefficient. For large files, it wouldn't even work because the contents would not fit in the context window. It wouldidx_b786183d have been much more effective to use a tool such as `grep` to search for the word `import` in all the files at once. 

This is aidx_b7dcbe8b great example of how the LLM can make suboptimal choices when requesting tool calls and how to debug such issues using our UI that exposes the actual tool calls (as opposed to just counting how many tool calls were executed). 

<!-- Start of picture text -->
Thread @ x<br>Al-6 APP 5 minutes ago<br>re<br>“nt_py<br>—Pycache__<br>backend<br>chainlit.md<br>frontend<br>memory<br>README.md<br>requirements.txt<br>venv<br>Tool call: cat __init__.py_<br>Tool call: cat chainlit.md<br># Welcome to Chainlit! ay tap<br>Hi there, Developer! 3) We're excited to have you on board. Chainlit is a<br>powerful tool designed to help you prototype, debug and share applications built<br>on top of LLMs.<br>## Useful Links @<br>-"*Documentation:** Get started with our comprehensive [Chainlit<br>Documentation|(https://docs.chainlit.io) &<br>= “*Discord Community:** Join our friendly [Chainlit Discord]<br>(https://discord.gg/k73SQ3FyUh) to ask questions, share your projects, and<br>connect with other developers!<br>We can't wait to see what you create with Chainlit! Happy coding! il @<br>## Welcome screen<br>To modify the welcome screen, edit the chainlit.nd file at the root of your<br>project. If you do not want a welcome screen, just leave this file empty.<br>> Chainlit<br>Overview - Chainlit (151 kB) +<br><!-- End of picture text -->

_Figure 6.8: Detailed tool call visualization_ 

_Creating Chat Interfaces Using Slack and Chainlit_ 

179 

This kind of poor tool choice is ideally detected during the development of the AI system and can be addressed by providing better instructions or system prompts to the LLM. In this case, let's see whether idx_03411d8bwe can improve it just for this session. That's funny. When asked, why didn't AI-6 use `grep` instead of `cat` ? Also, it acknowledged that it was **i** dx_140f7c42 nefficient and suggested using `grep` , but eventually it used `sed` to search for the word `import` in the files. This is fine, but it is different from what it declared it would do: 

<!-- Start of picture text -->
Hai-6-test a» i Thread @x<br>@rtessazes DP Addeamvas + Bierscat. command to display<br>Ten = | used the the contents ofthe files first,andI can<br>PS lremeety ‘manually check for the word "import" in each of them. However, using. arep<br>Amongchoinlit.md, the filesREADME, that werend, checked ( init__.py withinwould haveeach  beenfile, Let a moreme procee efficientwith metha using d  togrep searchto forthe accomplishwordthis “import® task moredirectly<br>them requirenents.txt noneof effectivelyNone of the files inthe current directory that | checked ( ini... py<br>fles contain the word “import Would you like to check chaintitmd README.nd, and requirenents. txt) contain the word "import<br>GB insidescot the directoriestas repy toy or atany3:32 specifiPm  es? youplease wouldlet me like knows me to checkoi  the other directories or specific files within them,<br>Bowe ven eph<br>why didn't you use grep to search<br>Too! call sed -1 Vimport/p’ _init_.y<br>evn:| used the cat commandfor Import? ew<br>files first, and to display the contents of the Tool all sed -n /import/p' chanltmd<br>in each of them,I canHowever,manuallyusing.checkreofor Wouldthe wordhave"importbeen a iSO oes Reached<br>more efficient method to search forthe word import Too! call sed on /import/p requirements txt<br>directly within each file. Let me proceed with using grep<br>toin theaccomplish current directorythis task morethat I checkedeffectively( init__.pyNone of the files,<br>chainlit.nd), README.nd,and requirenents.txt) contain Reply<br>the word “import” Cl Ao sendio  ab-ton<br>specificIf you wouldfiles ikewithin me tothem, checkpleasethe letother directoriesme know! or $m OG Ge DO<br><!-- End of picture text -->

_Figure 6.9: Debugging tool use choices_ 

Now that we have a good idea of what the AI-6 Slack bot does and what the user experience is, let's see how the AI-6 Slack bot is implemented and how it works under the hood. 

###### **Authentication and configuration setup** 

The idx_2f486623AI-6 Slack bot is built using the Slack Bolt ( `https://slack.dev/bolt-python/` ) framework, which simplifies Slack API integration in Python. Remember that you don't need to configure or deploy the Slack app yourself to follow this chapter. We’ll walk through the design, structure, and behavior of the Slack interface so you can understand how it works without hands-on setup. 

_Chapter 6_ 

180 

That said, for context, here’s what the setup entails behind the scenes: 

- A Slack app ( `https://api.slack.com/apps` ) is created and configured with the following: 

   - An App token ( `https://api.slack.com/apps/A08J2K4SF44/general` ) with the `connections:write` scope 

   - A Bot token ( `https://api.slack.com/apps/A08J2K4SF44/oauth` ) with the required permissions 

- Socket mode ( `https://app.slack.com/app-settings/T08GRUKRA5Q/A08J2K4SF44/ socket-mode` ) is enabled to allow real-time interactions 

- The app is subscribed to message events (use your app settings URL, e.g. `https:// api.slack.com/apps/<APP_ID>/event-subscriptions` ) Replace `<APP_ID>` with your APP ID 

• It is then installed into the appropriate Slack workspace: bot-playground, in my case If you'reidx_ea59f7d4 interested in building your own Slack integration later, the official guide on building a Slack app ( `https://api.slack.com/start/building/bolt-python` ) is a great place to start. 

Note that Bolt apps can be launched via the Slack CLI or directly from Python code. AI-6 uses the Python-based approach for more flexible control over behavior and deeper integration into the AI system's runtime. 

The AI-6 Slack bot is a frontend for the AI-6 engine, which requires a configuration object to initialize, if you recall from _Chapter 4_ . This configuration object can be loaded from different file formats, such as JSON, YAML, and TOML. The Slack bot uses a `config.toml` file to configure the AI-6 engine. Here it is: 

```
# AI-6 Slack Configuration File
default_model_id = "gpt-4o"
tools_dir = "${HOME}/git/ai-six/py/backend/tools"
mcp_tools_dir = "${HOME}/git/ai-six/py/backend/mcp_tools"
memory_dir = "${HOME}/git/ai-six/memory/slack"
checkpoint_interval = 3
#Provider configuration
[provider_config.openai]
api_key = "${OPENAI_API_KEY}"
default_model = "gpt-4o"
[provider_config.ollama]
model = "qwen2.5-coder:32b"
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

181 

```
#Tool configuration
[tool_config.claude]
api_key = "${ANTHROPIC_API_KEY}"
```

As you can see, there are environment variable names embedded in the config file instead of the actual sensitive information. This is one of the services provided by the AI-6 configuration system. It idx_ **a** 9119714 ccepts such configuration files and automatically loads the environment variables using this code in the `Config` class: 

```
@staticmethod
def_interpolate_env_vars(value: Any) -> Any:
"""Recursively interpolate environment variables in a configuration value.
        Supports ${VAR} and $VAR syntax for environment variables.
        Parameters
        ----------
        value : Any
            The value to interpolate
        Returns
        -------
        Any
            The interpolated value
        """
ifisinstance(value, str):
# Handle ${VAR} syntax
if"${"in value and"}"in value:
import re
                pattern = r'\${([a-zA-Z0-9_]+)}'
                matches = re.findall(pattern, value)
for var_name in matches:
                    env_value = os.environ.get(var_name, '')
                    value = value.replace(f"${{{var_name}}}", env_value)
# Handle $VAR syntax
elif value.startswith('$') andlen(value) > 1:
                var_name = value[1:]
                value = os.environ.get(var_name, '')
```

_Chapter 6_ 

182 

```
return value
elifisinstance(value, dict):
return {k: Config._interpolate_env_vars(v)
for k, v in value.items()}
elifisinstance(value, list):
return [Config._interpolate_env_vars(item) for item in value]
else:
return value
```

You don't have to use the embedded environment variables in your configuration files. You may directly idx_2b104568put the sensitive information in the config file, but just make sure you don't commit such files to your version control system. You may also create a `Config` object programmatically without using configuration files at all (e.g., read the configuration from a database or S3 bucket). 

However, in this case, we are using the config file to load the environment variables and pass them to the AI-6, so we need to set those environment variables before running the Slack bot. The AI-6 Slack bot uses an `.env` file to populate multiple environment variables that are needed by Slack itself, in addition to the AI-6 LLM provider secrets. Here is the redacted `.env` file used by the AI-6 Slack bot: 

```
OPENAI_API_KEY=<redacted>
ANTHROPIC_API_KEY=<redacted>
AI6_APP_ID=<redacted>
AI6_CLIENT_ID=<redacted>
AI6_CLIENT_SECRET=<redacted>
AI6_SIGNING_SECRET=<redacted>
AI6_BOT_TOKEN=<redacted>
AI6_APP_TOKEN=<redacted>
```

Yes, that's quite a few environment variables, but they are all necessary. This file must not be committed to version control, and it is ignored by the AI-6 `.gitignore` file: 

```
# Environment files
**/.env
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

183 

###### ****/.env.*Slack Bot initialization** 

The idx_f9f75344 AI-6 Slack bot code is in the `frontend/slack` directory. The main entry point is the `app.py` ( `https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-andA2A/blob/main/ch06/ai-six/py/frontend/slack/app.py` ) file, which also contains most of the logic for the bot. Here are the imports, which include some standard library packages such as `os` and `functools.partial` , the `pathology.path` package, several Slack and Bolt packages, and the `utils` module from the `frontend/slack` directory, which helps connect to the AI-6 engine: 

```
import os
from functools import partial
import pathology.path
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from slack_sdk.errors import SlackApiError
from .import utils
```

The next part isidx_aa84453b all about loading the `.env` file and loading the environment variables. If there is no `.env` file, it will print a warning and carry on. It's possible that the environment variables were already set before running the script, so the bot can still run without the `.env` file: 

```
script_dir = pathology.path.Path.script_dir()
# Try to load environment variables from .env file in the same directory as this
script
env_file_path = os.path.join(script_dir, ".env")
if os.path.exists(env_file_path):
    load_dotenv(env_file_path)
print(f"Loaded environment variables from {env_file_path}")
else:
print(f"Warning: No .env file found at {env_file_path}")
```

_Chapter 6_ 

184 

At this point, the environment variables are loaded, and we can access them using `os.environ.get()` . The code initializes some variables to hold the Slack app token and bot token and instantiates a Bolt app instance: 

```
app_token = os.environ.get("AI6_APP_TOKEN")
bot_token = os.environ.get("AI6_BOT_TOKEN")
app = App(token=bot_token)
```

Then, it initializes some variables to hold the last message and the latest timestamp, a dictionary for dedicated AI-6 channels, locates the configuration file, and initializes an empty `engines` dictionary: 

```
last_message = ""
latest_ts = None
ai6_channels = {}
config_path = str((script_dir / 'config.toml').resolve())
engines = {}
```

With all the preliminary initialization done, let's take a look at the `main()` function that starts the Slack bot. It does two primary things: joins a channel and starts `SocketModeHandler` to listen for events. It also handles exceptions and eventually leaves all the channels it joined: 

```
defmain():
"""Main entry point for the Slack app"""
    channel = join_channel(app.client)
if channel isnotNone:
print(f'Joined{channel["name"]}')
try:
# Run the Slack app
        SocketModeHandler(app, app_token).start()
except KeyboardInterrupt:
print("Ctrl+C detected.")
except Exception as e:
print(f"Unhandled exception: {e}")
finally:
        leave_channels(app.client)
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

185 

```
if __name__ == "__main__":
    main()
```

Now we idx_97a90fdahave a basic understanding of how the AI-6 Slack bot is initialized and started. The next step is to understand how the bot handles incoming messages and interacts with the AI-6 engine to process them. 

###### **Message handling and event processing** 

Bolt appsidx_f4ce2398 handle events using decorators that map specific event types to handler functions. The AI-6 Slack bot handles all incoming messages in any channel via a single `handle_message()` function that is decorated with the `@app.event("message")` decorator: 

```
@app.event("message")
defhandle_message(message, say,ack, client):
"""Handle all messages inchannels."""
```

The function declares the `last_message` and `latest_ts` global references, so it can access them, and then extracts the text from the `message` object: 

```
global last_message, latest_ts
ack()  # Acknowledge ASAP
text = message.get("text")
```

The Slack bot is designed to process any messages in its own dedicated channels (the `ai6_channels` dictionary) or messages in any other channel that mentions the bot. If the message is empty or from a bot or doesn't match the criteria, it is ignored: 

```
# Skip if the message is empty or from a bot
ifnot text or message.get("bot_id"):
return
    mention_bot = f"<@{bot_user_id}>"in text
    channel_id = message['channel']
    ai6_channel = channel_id in ai6_channels
```

_Chapter 6_ 

186 

```
# Ignore messages that don't mention the bot and are not a special AI-6 channel
ifnot mention_bot andnot ai6_channel:
return
```

At this point, weidx_f9880f5d have a message that we want to process. We already got the channel ID from the message, so we can create or retrieve an AI-6 engine instance for that channel. Then, we prepare a tool call handler that will be used to handle tool callbacks from the AI-6 engine during message processing (those will go into the reply thread, as you recall): 

```
    engine = get_or_create_engine(channel_id)
# Create a tool call handler for this channel
    channel_tool_call_handler = partial(handle_tool_call, client, channel_id)
```

Now, we have everything we need to process the message. We will use the AI-6 engine in streaming mode so it can display chunks of the response as they arrive, and there is no need to wait for the full response to be ready. So, it starts with a generic `"..."` text. Then, we set the `latest_ts` global variable (the timestamp of the message) to the result of the `chat_postMessage()` call, which posts the initial message to the channel. The `last_message` variable is initialized to an empty string to hold the response as it is getting built up: 

```
# Process the message with the AI-6 engine
try:
# Post an initial empty message that we'll update
        result = client.chat_postMessage(
            channel=channel_id,
            text="..."
        )
        latest_ts = result["ts"]
        last_message = ""
```

Then, we define an inline `handle_chunk()` function, which will be called by the AI-6 engine as it streams chunks of the response. It's a little unusual to define nested functions like this, but it works wellidx_65e9b54e in this case because it allows us to keep the callback next to where it is used, making the code easier to read. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

187 

Whenever a new chunk arrives, it appends the chunk to the `last_message` variable and then updates the message in the channel using the `chat_update()` method. If there is an error with updating the message, it prints an error message: 

```
# Define a callback function to handle streaming chunks
defhandle_chunk(chunk):
global last_message
            last_message += chunk
try:
# Update the message with the new content
                client.chat_update(
                    channel=channel_id,
                    ts=latest_ts,
                    text=last_message
                )
except SlackApiError as e:
print(f"Error updating message: {e}")
```

Here is the final part of the `handle_message()` function that streams the message to the AI-6 engine and provides it with the two event handlers for handling chunks and tool calls. If there is an error during streaming, it catches the exception and prints an error message to the terminal: 

```
# Stream the message to the AI-6 engine
        response = engine.stream_message(
            text,
            engine.default_model_id,
            on_chunk_func=handle_chunk,
            on_tool_call_func=channel_tool_call_handler
        )
except Exception as e:
print(f"I encountered an error: {str(e)}")
```

Now that we understand how the Slack bot handles messages, let’s take it to the next level and consider how to work with multiple channels and multiple users. 

_Chapter 6_ 

188 

###### **Channel management and multi-user support** 

The idx_19c8546aAI-6 Slack bot is designed to support multiple Slack channels and users. It automatically joins the first channel whose name has the `ai-6-` prefix. The multi-user support comes for free because Slack supports multiple users and channels, and any user can post messages in any channel the bot is a member of. The bot will process all messages in those channels from any user. 

Let's look at the `join_channel()` function that is called in the `main()` function to join a channel. It is pretty simple. First, it lists all the channels in the Slack workspace using the `conversations_list()` method of the Slack client. Then, it filters the channels to find those that start with the `ai-6-` prefix. If there are no such channels, it just returns. If there are multiple channels, it just joins the first one. If the bot is not a member of the channel, it tries to join it using the `conversations_join()` method. Finally, it returns the channel object. 

```
defjoin_channel(client):
"""Join the first AI-6 channel if not a member already
Return the channel id
If there are no AI-6 channel raise an exception
"""
    all_channels = client.conversations_list()["channels"]
    ai6_channels.update(
        {
            c["id"]: c
            for c in all_channels
            if c["name"].startswith("ai-6-")
        }
    )
ifnot ai6_channels:
return
    channel_id = list(ai6_channels.keys())[0]
    channel = ai6_channels[channel_id]
# Join channel if not a member already
ifnot channel['is_member']:
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

189 

```
try:
            client.conversations_join(channel=channel_id)
except Exception as e:
print(f"Error joining channel {channel_id}: {e}")
return channel
```

This behavior of automatically joining a channel with a specific naming convention is, frankly, mostly useful for development and testing purposes. In a real-world application, you would just invite the AI-6 Slack bot to specific channels. This behavior is supported too, since the `handle_message()` handler responds to any message in channels where the bot is present, as you recall, as long as the message mentions the AI-6 Slack bot. 

Here is how to invite the AI-6 Slack bot to a channel that it is not a member of: 

<!-- Start of picture text -->
+ some-channel<br>You created this channel today. This is the very beginning of the # some-channel channel.<br>@ Add Description & Add People to Channel<br>Today ~<br>lo Gigijoined Sayfan#some-channel6.08 pv<br>6 Gigi@A\-6 Sayfanplease 6.09joinps<br>© Only visible to you<br>& 8 Slackbot 6.09 PM<br>WP OK! I've invited @AL-6 to this channel.<br>B(SE Al-6was addedAPP 6:09to  PM#some-channel by Gigi Sayfan<br><!-- End of picture text -->

_Figure 6.10: Explicitly invite the AI-6 bot to a channel_ 

_Chapter 6_ 

190 

This idx_5 **c** 3b1298 hannel is called **some-channel** , which means the AI-6 Slack bot will not automatically respond to any message. We must mention it using `@AI-6` to get a response. Let's try it: 

<!-- Start of picture text -->
©:~  GigiHeyru Sayfanthere?6:11 PM<br>@AI-6 Hey, ru there?<br>AI-6 APP 6:13 PM<br>Sm Hello! Yes, I'm here. How can| assist you today? (edited)<br><!-- End of picture text -->

_Figure 6.11: Mentioning AI-6_ 

When the AI-6 app is closed, it will leave all the channels it has joined (automatically or by invitation). 

<!-- Start of picture text -->
62 Gigi@AI-6 Sayfanrustill6:19here? PM<br>Al-6 APP 6:19 PM<br>== |'mhere to help! How can | assist you today? (edited)<br>Leaving channel #some-channel<br><!-- End of picture text -->

_Figure 6.12: AI-6 bot leaving a channel_ 

This is done in the `leave_channels()` function, which is pretty simple: 

```
defleave_channels(client):
"""Leave all the channels
    """
    channels = (c for c in client.conversations_list()['channels']
if c['is_member'])
for c in channels:
        client.chat_postMessage(
            channel=c['id'],
            text=f"Leaving channel #{c['name']}"
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

191 

```
        )
        client.conversations_leave(channel=c['id'])
```

We covered idx_8507a887how the AI-6 Slack bot handles messages and manages channels. Now, let's look at how it integrates with the AI-6 engine. 

###### **Integration with the AI-6 engine** 

There idx_e0d6a786 are two main touch points between the AI-6 Slack bot and the AI-6 engine: creating or retrieving an engine instance for each channel and handling tool calls from the AI-6 engine. The `get_or_create_engine()` function helps to ensure each channel has its own AI-6 engine instance, which is essential for multi-channel and multi-user support. 

If we had just one shared engine, it would be difficult to manage the state and memory for each channel. First, the context window would fill up much quicker, and also, the LLM would be confused by unrelated messages from different channels. 

Here is the code. It's pretty simple. All the engines for all the channels are stored in the `engines` dictionary. If the requested channel ID is not in the dictionary, it creates a new engine instance using the `utils.create_channel_engine()` function, and adds it to the `engines` dictionary. Then, it just returns the engine: 

```
defget_or_create_engine(channel_id):
"""Get an existing engine for a channel or create a new one."""
if channel_id notin engines:
# Create a channel-specific engine using the Slack utility function
        engines[channel_id] = utils.create_channel_engine(
            base_config_path=config_path,
            channel_id=channel_id,
            env_file_path=env_file_path
        )
return engines[channel_id]
```

The `utils.create_channel_engine()` ( `https://github.com/PacktPublishing/DesignMulti-Agent-AI-Systems-Using-MCP-and-A2A/blob/main/ch06/ai-six/py/frontend/ slack/utils.py` ) function contains similar code for instantiating the AI-6 engine as we saw in _Chapter 4_ , but it also sets the channel ID in the configurationidx_2303bddf and initializes the memory for that channel. 

_Chapter 6_ 

192 

Let's take a look at the code that handles tool calls from the AI-6 engine. The `handle_tool_call()` function adds each tool call and its response to the thread of the original message in the Slack channel. This allows users to see the details of how the AI-6 engine arrived at its response, including the tool calls and their results: 

```
defhandle_tool_call(client, channel, name, args, result):
"""Handle a tool call from the AI-6 engine."""
# Post the tool call result as a message
try:
        client.chat_postMessage(
            channel=channel,
            thread_ts=latest_ts,
            text=f"_Tool call: `{name}` {', '.join(args.values()) ifargselse''}
_\n{result}"
        )
except SlackApiError as e:
print(f"Error posting tool call result: {e}")
```

To summarize, we covered how the AI-6 Slack bot is designed and implemented and how it integrates with the AI-6 engine. We discussed some of the key features, such as multi-channel support, message handling, and tool call processing. Now, let's turn our attention to the Chainlit web UI, which is similar to web chatbots such as ChatGPT. 

###### **Developing a web UI with Chainlit** 

In theidx_883d0b0d previous section, we explored the AI-6 Slack bot interfaceidx_71876d52 and saw how it provides a collaborative, multi-user environment for interacting with agentic AI systems. The Slack bot excels at team workflows, real-time notifications, and integration with existing communication channels. 

However, there are scenarios where a dedicated web interface offers advantages: more control over the user experience, richer visual elements, better support for long-form conversations, and easier deployment for users who don't have access to a Slack workspace. This is where Chainlit comes in. In this section, we'll examine how AI-6 leverages Chainlit to create a webbased chat interface similar to ChatGPT while maintaining full access to AI-6's tool ecosystem and agent capabilities. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

193 

###### **Chainlit framework overview** 

Chainlit ( `https://docs.chainlit.io` ) is a Pythonidx_819f1964 framework specificallyidx_ec7e6d23 designed for building chat interfaces for LLM applications. It provides out-of-the-box support for many UI elements, the chat life cycle, streaming responses, file uploads, settings management, session persistence, and much more—all the features needed for a polished conversational AI interface. It is highly customizable, too, allowing you to add your custom UI elements. 

Chainlit's development experience is tailored for rapid iteration. It runs a local development server with hot-reloading, enabling fast prototyping and debugging. The framework integrates seamlessly with popular LLM backends such as OpenAI, LangChain, and Hugging Face, and supports both synchronous and asynchronous workflows for maximal flexibility. 

Let’s explore how AI-6 leverages Chainlit to build a simple web interface that complements its Slack bot. The AI-6 Chainlit application is intentionally minimal and not designed to fully showcase Chainlit’s capabilities. Its primary purpose is to demonstrate how the AI-6 backend can be integrated into a web-based UI, serving as a foundation for more advanced and polished web applications. 

###### **Taking AI-6 Chainlit for a spin** 

Let'sidx_4a9158f0 start with a idx_0e9e4fe5very useful real-world use case, which involves adding a idx_d255946aGitHub Actions ( `https://docs.github.com/en/actions` ) workflow to the AI-6 repository to run all our tests whenever we push new changes. First, we need to launch the Chainlit app. We can do that using the convenient `ai6.sh` script passing the `chainlit` argument: 

❯ `./ai6.sh chainlit virtualenv: /Users/gigi/git/ai-six/py/venv 2025-07-19 11:28:15 - HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1 200 OK"` 

```
2025-07-19 11:28:17 - HTTP Request: GET https://api.openai.com/v1/models "HTTP/1.1
200 OK"
2025-07-19 11:28:18 - Your app is available at http://localhost:8000
```

_Chapter 6_ 

194 

The AI-6 Chainlit app **i** dx_744649e5 s now running and we can access it at `http://localhost:8000` . Let's open it in a web browser: 

<!-- Start of picture text -->
+ © ‘ocanost. x O18 | GW Gamaey<br>Al-6 is ready. Let'sgo #7”<br>0s<br><!-- End of picture text -->

_Figure 6.13: The Chainlit web app_ 

Now, let's ask AI-6 to add a GitHub Actions workflow to the AI-6 repository: 

<!-- Start of picture text -->
© © kcatost 2 | GR Geay<br>Al-6 is ready. Let's go #7!<br><!-- End of picture text -->

_Figure 6.14: Initial user prompt_ 

_Creating Chat Interfaces Using Slack and Chainlit_ 

195 

AI-6 provided idx_6507e264 a very clear and detailed explanation, including the actual workflow file and all the steps to accomplish the task. Note how pleasant the UI is. The code is properly color-coded and the Markdown is formatted cleanly: 

<!-- Start of picture text -->
inthe By/AGKn rectory and runs<br>the tests if any backand files have been modified<br>2. tehecks if any<br>backendfiles under the |py/MREKBRA| directory have changed.<br>Steps to Add This Workflow:<br>1. Createanew directory \igithub/verkflows, Intheroot of your repositoryif it doesn't<br>Create<br>anew file named Haekand-tests. yal inside the igithub/werkftans| directory<br>3. Copy the above YAML code into the ackend-tests. yal fie<br>4. Modify<br>the pytheicversin and pip install commands as necessary to ft your<br>5.Commitand push he changes to your repository. The workfiow wilnow be triggered on<br>any pul aquest that chides changes ta files whihhn the SRR croc<br><!-- End of picture text -->

_Figure 6.15: Elaborate LLM response_ 

_Chapter 6_ 

196 

But the solution has a few problems. First, it used the `pull_request` event, which doesn't trigger on a regular idx_d05c474epush to the main branch. We want the workflow to run on push events too. Second, it uses outdated versions of some GitHub actions, such as `actions/checkout@v2` and `actions/setup-python@v2` . We want to use the latest versions. 

Let's ask AI-6 to fix these issues: 

<!-- Start of picture text -->
add push event trigger too and use latest versions of github<br>actions checkout@v4 and setup-python@v5<br>The GitHub Actions workflow has been successfully updated to:<br>+ Include a push event trigger for changes to the main branch impacting files in the<br>py/backend directory.<br>+ Use the latest versions of actions/checkout@v4 and setup-python@v5<br>These changes ensure that tests will run both on pull requests and direct pushes to the main<br>branch if backend files are modified. If you need any more help or further adjustments, feel<br>free to ask!<br>ay<br><!-- End of picture text -->

_Figure 6.16: Follow-up interaction_ 

Let's see what AI-6 actually did. Here is the original commit and the fix commit: 

❯ `git log --oneline -n 2 f5198ca (HEAD -> main, origin/main, origin/HEAD) Update_workflow_for_push_event_and_latest_actions_versions 65a0c12 Add_GitHub_Actions_workflow_to_run_tests_on_backend_changes` 

_Creating Chat Interfaces Using Slack and Chainlit_ 

197 

Let's review the changes: 

❯ `git diff HEAD~2 diff --git a/.github/workflows/backend-tests.yml b/.github/workflows/backendtests.yml new file mode 100644 index 0000000..1339264 --- /dev/null +++ b/.github/workflows/backend-tests.yml @@ -0,0 +1,35 @@ +name: Run Tests on Backend Changes + + + +on: +  pull_request: +    paths: +      - 'py/backend/**' +  push: +    branches: +      - main +    paths: +      - 'py/backend/**' + + + +jobs: +  test: +    runs-on: ubuntu-latest + + + +    steps: +    - name: Checkout code +      uses: actions/checkout@v4 + + +` 

_Chapter 6_ 

198 

<!-- Start of picture text -->
+    - name: Set up Python<br>+      uses: actions/setup-python@v5<br>+      with:<br>+        python-version: '3.x'  # Specify the python version<br>+<br>+<br>+<br>+    - name: Install dependencies<br>+      working-directory: py<br>+      run: |<br>+        python -m pip install --upgrade pip<br>+        pip install -r requirements.txt<br>+<br>+<br>+<br>+    - name: Run Tests<br>+      working-directory: py<br>+      run: |<br>+        python -m unittest discover -s backend/tests<br><!-- End of picture text -->

Everything idx_5e8fa8fb looks correct now. AI-6 fixed all the issues we identified. This highlights the importance of the human-in-the-loop concept. 

LLMs are great, but they are not perfect (yet). We can now tell AI-6 to push the changes to GitHub: 

<!-- Start of picture text -->
Looking good. push the changes<br>The changes have been successfully pushed to the main branch. The updated GitHub<br>Actions workflow will now trigger both on pull request events for backend changes and on<br>direct pushes to the main branch, using the latest versions of the necessary GitHub Actions.<br>Is there anything else you need help with?<br><!-- End of picture text -->

_Figure 6.17: AI-6 pushing changes to GitHub_ 

_Creating Chat Interfaces Using Slack and Chainlit_ 

199 

Let's check GitHub and confirm that the new GitHub Actions workflow is indeed there: 

<!-- Start of picture text -->
o < CB B github.com: he<br>DSO) sayten-at / atsix<br>+<br>© Code © Issues 11 Pullrequests @ Actions Projects CX Wiki © Security Insights <@ Settings<br>ica @ Files ai-six/ github / workflows / backend-tests.yml (2<br>xa al St [PS @ the-siol Update_worktlow_for_push_event_and _latest_actions_versions<br>Q cototie ‘<br>a © i -githubjworkfiows (Code | Blame 33 Lines (27 loc) » 628 Bytes<br>© | UNG eecrarsaeige 12 name: Run Tests on Backend Changes<br>© omy 3 ont<br>wD aitignore 4: pullterequests<br>© ucense s = 'py/backend/+x"<br>7 pushs<br>© READMEmd a branchest<br>1 a-spng : =atle<br>D ai6.sh n» paths:~ "py/backend/s«<br>1 planning.ma 2ae dase<br>uM teste<br>5 runs-ont ubuntu-latest<br>p steps:<br>1 = name: Checkout code<br>19 usest actions/checkoutov4<br>2»<br>a ~ mane: Set up Python<br>2 uses: actions/setup-pythonevs<br>2 wat<br>2 python-version: "3.x! # Specify the python version<br>26 ~ nane: Install dependencies<br>2 rant |<br>22 python -m pip install —vpgrade pip<br>2»<br>» pip install -r requirenents.txt<br>x ~ nane: Run Tests<br>2 rune |<br>3 python -m unittest discover ~s tests<br><!-- End of picture text -->

_Figure 6.18: GitHub Actions workflow_ 

That was a idx_c0540345great session with AI-6 using the Chainlit interface. We were able to add a new GitHub Actions workflow to the AI-6 repository, fix some issues, and push the changes to GitHub. The Chainlit interface provided a clean and modern view of the conversation. 

Let's take a look at how the Chainlit interface is implemented and how it integrates with the AI-6 engine. 

_Chapter 6_ 

200 

###### **Configuration and engine integration** 

Just like theidx_77e72dbb Slack bot interface, the Chainlit web application requires configuration to initialize and connect with the AI-6 engine. The main program entry point is in the `app.py` file ( `https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-using-MCP-andA2A/blob/main/ch06/ai-six/py/frontend/chainlit/app.py` ). Let's break it down. 

Let's start with the imports. The Chainlit app imports the `SimpleNamespace` class from the standard library's typing module. It is a cool class that you can use like a dictionary, but with dot notation access to attributes. It also imports `chainlit` itself, aliased to `cl` , and the `run_chainlit` function from the `chainlit.cli` module, which is used to run the Chainlit app. It also imports the `pathology.path` package to locate the configuration file and the `engine_utils` module from the shared `frontend.common` package, which will be used to create the AI-6 engine instance: 

```
from types import SimpleNamespace
import chainlit as cl
from chainlit.cli import run_chainlit
import pathology.path
from frontend.common import engine_utils
```

Next, it locates the configuration file and creates an AI-6 engine instance from it. This is the AI-6 engine initialization part: 

```
script_dir = pathology.path.Path.script_dir()
# Load the engine from YAML configuration
config_path = str((script_dir / "config.yaml").resolve())
# Create engine from configuration file
# Environment variables will be automatically interpolated by Config.from_file
engine, engine_config = engine_utils.create_from_config(config_path)
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

201 

Here, we create the `app_config` object, which is a `SimpleNamespace` instance ( `https:// docs.python.org/3/library/types.html#types.SimpleNamespace` ) that holds the configuration for the Chainlit app: 

```
app_config = SimpleNamespace(
    selected_model=engine.default_model_id,
    available_models=list(engine.model_provider_map.keys()),
    enabled_tools={tool: Truefor tool in engine.tool_dict},
)
TOOL_PREFIX = "tool:"
```

Thisidx_ceee33a8 configuration object will be used later when processing messages from the user. The integration with the AI-6 engine is via the `engine` variable that was created earlier. 

###### **Application life cycle and event handlers** 

Atidx_9008b19e this point, weidx_fcc96fb6 have the engine and the configuration (the `app_config` object) ready, and the main logic of the application runs by invoking the `run_chainlit()` function (imported from `chainlit.cli` ) with the `app.py` file. This is a cumbersome way to launch a Chainlit application from a Python program. This is needed for debugging: `if __name__ == "__main__": target = str(script_dir / "app.py") run_chainlit(target)` 

The standard way to run a Chainlit application in the terminal is using the `chainlit` CLI: 

❯ `chainlit run app.py` 

Anyway, once the Chainlit app is running, it will start listening for events and processing them. Our Chainlit app handles the following events: 

- `on_chat_start` : Called when a new chat session starts 

- 

- `on_message` : Called when a new user message is received 

- 

- - `on_settings_update` : Called when settings were changed in the settings panel 

Let's take a look at each of these event handlers and see how they work. 

_Chapter 6_ 

202 

###### **The on_chat_start event handler** 

This idx_cad8b55aevent handler is called exactly once when the app starts. It is pretty simple. It calls `setup_settings()` and displays the welcome message that we saw when we took the Chainlit app for a spin: 

`@cl.on_chat_start async def on_chat_start(): await setup_settings() await cl.Message(content="AI-6 is ready. Let's go` 🚀 `!").send()` 

The `setup_settings()` function is very interesting. It sets up the initial settings for the Chainlit app in UI widgets, including the LLM selection and tool switches. It uses `cl.input_widget.Select` for the model selection and `cl.input_widget.Switch` for each tool. The idx_855f7d05 initial values are taken from the `app_config` object we created earlier: 

```
asyncdefsetup_settings():
    model_select = cl.input_widget.Select(
id="model",
        label="LLM Model",
        values=app_config.available_models,
        initial_value=app_config.selected_model,
        initial_index=app_config.available_models.index(
            app_config.selected_model),
    )
    tool_switches = [
        cl.input_widget.Switch(
id=f"{TOOL_PREFIX}{tool_name}",
            label=f"Tool: {tool_name}",
            initial=tool_value,
        )
for tool_name, tool_value in app_config.enabled_tools.items()
    ]
await cl.ChatSettings([model_select] + tool_switches).send()
```

But where are those UI settings displayed? Well, there is a little cog button in the bottom-left corner of the user input box that brings up **Settings panel** . It looks like this: 

_Creating Chat Interfaces Using Slack and Chainlit_ 

203 

<!-- Start of picture text -->
Settings panel<br>LLM Model<br>gpt-4o v<br>tts-1-1106<br>tts-t-hd-1106<br>text-embedding-3-small<br>text-embedding-3-arge<br>gpt-4-0125-preview<br>gpt-4-turbo-preview<br>gpt-3.5-turbo-0125<br>gpt-4-turbo<br>gpt-4-turbo-2024-04-09<br>Y gpt-4o<br>Toot: claude<br>‘ook: patch<br>Tool: sea<br>Tool: cat<br>Reset cance {/ Confirm<br><!-- End of picture text -->

_Figure 6.19: Chainlit app Settings panel_ 

We idx_0263998cwill see how these settings are being used and can be modified later. For now, let's just note that the initial value of the LLM is set to the value in the `app_config` object, as well as the enabled tools. The entire thing is sent to Chainlit using the `cl.ChatSettings().send()` method. 

At this point, we have the Chainlit app initialized, configured with a proper LLM and a set of enabled tools, and ready to handle messages. 

_Chapter 6_ 

204 

###### **The on_message event handler** 

This is idx_61eba767the main event handler that processes incoming messages from the user and interacts with the AI-6 engine. It is called whenever the user types in a new message. 

Initially, it creates a new `cl.Message` object with empty content and sends it to the Chainlit UI immediately. This message will be updated later with the response from the AI-6 engine: 

```
@cl.on_message
asyncdefon_message(message: cl.Message):
"""Process user messages and generate responses."""
# Create a new message for the response
    msg = cl.Message(content="")
await msg.send()
```

Next, it defines a callback function, `on_chunk()` , that will be used to handle streaming chunks of the response from the AI-6 engine. This function will be called whenever the AI-6 engine sends a new chunk of the response: 

```
# Define a callback function to handle streaming chunks
asyncdefon_chunk(chunk: str):
# Use the Chainlit built-in streaming method
await msg.stream_token(chunk)
```

Here is the call to the AI-6 engine to process the message. It uses the 

`engine.stream_message()` method to stream the response. It passes the user's message content, the selected LLM from `app_config` , the `on_chunk` callback function, and the list of enabled tool IDs. While the AI-6 engine processes the requests, it will send multiple chunks to the `on_chunk` function, which will update the response message that was initially empty. If there is a problem at any point, it will display an error message in the Chainlit UI: 

```
# Stream the response
try:
        engine.stream_message(
            message.content,
            app_config.selected_model,
            on_chunk_func=lambda chunk: cl.run_sync(on_chunk(chunk)),
            available_tool_ids=[
                k for k, v in app_config.enabled_tools.items() if v],
        )
# Mark the message as complete
```

_Creating Chat Interfaces Using Slack and Chainlit_ 

205 

```
await msg.update()
except Exception as e:
await cl.Message(content=f"Error: {str(e)}").send()
```

Let's see the process in action. AI-6 is asked to write a 100-word poem about itself and put a breakpoint in the `on_chunk()` handler. This is fascinating. AI-6 started the poem with `In digital realms where ideas entwine` . The LLM chose to stream one output token at a time. In theidx_54113757 case of the word `entwine` , it broke it into two chunks (two tokens): `entw` and `ine` . See the following figure: 

_Figure 6.20: AI-6 is writing a poem_ 

One last thing: note that in the current version of the code, we don't pass the `on_tool_call_func` argument to the `engine.stream_message()` method, so the AI-6 engine will not notify the UI on any tool calls. This is intentional as I didn't want to pollute the display with verbose tool calls. The AI-6 Slack bot had a natural place for tool calls in the thread. However, this is not the case with the Chainlit UI. A special side panel may be added at some point. Then, the user may opt to open up and capture tool calls there. 

_Chapter 6_ 

206 

###### **The on_settings event handler** 

The idx_74052db3 AI-6 Slack and CLI frontends had a pre-configured LLM and tools. The Chainlit app allows the user to select and modify the LLM and enable or disable tools on the fly. When the user changes the settings in the settings panel and clicks the **Confirm** button, the `on_settings()` event handler is called. All it does is update `app_config` with the new settings. That includes the selected LLM and the enabled tools: 

```
@cl.on_settings_update
asyncdefon_settings_update(new_settings):
    app_config.selected_model = new_settings["model"]
for k, v in new_settings.items():
if k.startswith(TOOL_PREFIX):
            tool_name = k.replace(TOOL_PREFIX, "")
            app_config.enabled_tools[tool_name] = v
```

Let's see it in action. I will disable the `ls` and `git` tools. This should prevent the LLM from using these toolsidx_37a2d6c2 to list files. It should still be able to find the current directory because the `pwd` tool remains enabled. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

207 

<!-- Start of picture text -->
Settings panel<br><!-- End of picture text -->

_Figure 6.21: Disabling tools_ 

Yeah, it works! AI-6 doesn'tidx_915db26e provide the `ls` and `git` tools, so the LLM has no way to list files. 

To summarize, we covered the Chainlit web interface for AI-6 in this section. We saw how it is initialized and integrated with the AI-6 engine, how it handles messages, and its dynamic configuration with the ability to switch the LLM and toggle tools. We barely scratched the surface of what's possible, but we saw how it provides a lightweight web-based alternative to the AI-6 Slack bot. 

_Chapter 6_ 

208 

In the next section, we will discuss best practices for building more advanced and sophisticated interactive agent interfaces. 

###### **Best practices for interactive agent interfaces** 

The frontend interfaces we built in the previous sections are great starting points for interacting with AI agents, but when building production-grade AI systems, there are several best practices to consider. These practices ensure that the user experience is smooth, the agent's intent is clear, and the system is robust and maintainable. 

###### **Clarify the agent’s role and capabilities** 

A successfulidx_9004f32a interactive agent interface must make it immediately clear to the user what the agent is, what it can do, and what kind of inputs it expects. Ambiguity in the agent's scope leads to user frustration and failed interactions. The interface should expose key capabilities through UI elements such as buttons, autocomplete prompts, or help overlays. For example, a file analysis agent might show a drop zone for files, a list of supported file types, and a sample command such as "Summarize this CSV." 

The agent should also communicate its limitations proactively. This includes model constraints (e.g., token limits), disabled tools, or unsupported input formats. In a multi-agent system where high-level agents may automatically spawn sub-agents, it's often more important to focus on the high-level agents that the user can manage either through predefined configuration options or user prompts. 

###### **Safeguards – confirmations, dry-runs, and safety nets** 

AI agentsidx_68d43b9a can invoke tools that can potentially cause a lot of damage if misused. The UI should default to a conservative posture, asking the user to confirm high-impact actions such as file overwrites, code deployments, or deletions. Confirmation prompts not only prevent accidental damage but also force users to reflect on the implications of their input. 

In addition to confirmations, the UI should support dry-run modes. A dry run is a safe simulation that shows what the agent would do without actually executing anything. This is particularly valuable when developing and testing workflows, API integrations, or infrastructure commands. When users can preview results and verify correctness, trust in the system increases. Combined with the ability to cancel or undo actions, these safety nets make agentic systems feel powerful but not reckless. 

It is also highly recommended to add an "Abort" button to the UI that allows users to stop the agent at any time. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

209 

###### **Design for turn-based transparency** 

AI agents idx_1fb40b74operate in a conversational, turn-based manner. This interaction model should be embraced and used to surface internal reasoning, chain of thought (for models that support it), and tool calls. Each step the agent takes should be represented in the interface: prompts, decisions, tool calls, outputs, and intermediate results. This makes it easy for users to understand the "why" behind the agent's behavior. 

Good interfaces show the full life cycle of a single interaction in a clean, linear thread. For example, when an agent decides to call a tool, the request parameters and response should be visible in the chat flow or an expandable panel. Errors, retries, or fallbacks should also be displayed as part of the story. This design pattern helps users debug, audit, and learn how to better prompt the agent and improve outcomes. 

###### **Prioritize tool invocation and feedback loops** 

One of the idx_4e81f442 biggest value-adds of agentic systems is their ability to use external tools. The UI must make it obvious when tools are being invoked, how they are selected, and what their results are. This creates a feedback loop where users can evaluate whether the tool usage was appropriate and intervene if not. 

The interface should also surface tool invocation metadata: timestamps, arguments, return values, and any errors. When tools fail (e.g., network error or malformed input), the agent should gracefully report the issue and offer options such as retry, revise input, or skip. Allowing users to nudge the agent or override tool choices keeps the conversation productive and aligned with user intent. 

It is also important to provide a way for users to see the available tools and their descriptions, and customize the set of tools per agent. 

###### **Embrace configurability and runtime control** 

Differentidx_21b9d266 users have different preferences and trust thresholds. Some might want the agent to auto-execute tools freely, while others may prefer manual confirmation. The UI should expose runtime settings to control these behaviors. This includes toggling tools on/off, switching models, selecting output verbosity, and defining fallback strategies. 

These controls should be easily accessible (e.g., via a settings panel or chat command) and persist across sessions if appropriate. Allowing users to customize their interaction style improves usability and satisfaction. 

_Chapter 6_ 

210 

###### **Logs, metrics, and distributed tracing for agentic systems** 

Every useridx_caa00a32 action, agent decision, and tool call should be logged with metadata. These logs serve both user-facing and developer-facing goals. For users, logs can be visualized as timelines, enabling backtracking and replaying previous sessions. For developers, logs support debugging, performance tuning, and prompt refinement. 

Metrics idx_9ac6ef34should include tool call frequency, average response latency, session duration, task success rates, and user interventions. Over time, these metrics can guide improvements to both the agent's behavior and the UI. UIs without instrumentation are black boxes. By instrumenting every part of the workflow, agentic systems can evolve from prototypes to reliable, auditable platforms. 

LLM-specific i **d** x_6c41eef8 istributed tracing is critical too for complex systems. Each turn should be represented by a span. Traces should capture complete sessions or conversations. 

If you follow these best practices, you will be able to build interactive agent interfaces that are user-friendly and developer-friendly. They will provide a great user experience and allow users to interact with AI agents in a natural and satisfying way. The AI-6 Slack bot and Chainlit web interface we built in this chapter show some elements of these best practices, but there is a lot of room for improvement. 

###### **Summary** 

In this chapter, we transitioned from AI-6's backend and internal architecture to its frontend UIs, focusing on how the UI enables effective collaboration between users and autonomous agents. We examined why visibility, interruptibility, debugging, and trust are essential UI concerns for agentic systems, and how different roles require different levels of detail in the interface. 

We then explored the implementation of the AI-6 Slack bot, highlighting its design choices such as tool call threading, per-channel engine instances, and real-time message handling. Slack's familiarity, multi-user support, and notification capabilities make it an ideal interface for collaborative workflows. 

Finally, we examined the Chainlit-based web interface, showing how it provides a clean, customizable, single-user experience. With support for tool toggling, model selection, and rich streaming output, Chainlit complements Slack's strengths and enables fine-grained user control. Both interfaces set the stage for best practices in building robust, transparent agent UIs. 

_Creating Chat Interfaces Using Slack and Chainlit_ 

211 

In the next chapter, we will turn our attention to the **Model Context Protocol** ( **MCP** ), a standardized mechanism for sharing model state and execution context across tools and agents. We will define what MCP is, explore how to implement MCP-compliant servers and clients, and walk through how to integrate MCP into your own agent framework to enable seamless context sharing across diverse AI components. 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns – _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and generative AI systems. Subscribe now and receive a free eBook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OFA<br>a<br><!-- End of picture text -->

# 7 

##### Integrating with the Model Context Protocol Ecosystem 

In the previous chapters, we explored how to build agentic AI systems, how to integrate them with custom tools, and how to interact with them using different frontends such as a **command-line interface** ( **CLI** ), a idx_743489f2Slack bot, and a Chainlit-based web UI. In this chapter, we will focus on integrating your agentic AI framework with idx_523f6f53the **Model Context Protocol** ( **MCP** ) ( `https://modelcontextprotocol.io` ) ecosystem. MCP is a big deal! It is a protocol designed to standardize interactions between agentic AI systems models and tools. We will start by exploring MCP and its benefits. Then, we will look at how to build MCP servers and clients. Finally, we will demonstrate how to integrate MCP into AI-6, our agentic AI framework. 

We will cover the following main topics: 

- What is MCP? 

- MCP architecture core and core components 

- 

- Building MCP servers 

- 

- Building MCP clients 

- 

- Integrating MCP into the AI-6 framework 

- 

- Putting it all together 

- 

By the end of this chapter, you will have a solid understanding of MCP, why it is so great, and how to use it to build agentic AI systems that can benefit from the rich ecosystem of MCP servers and clients. 

_Chapter 7_ 

214 

###### **Technical requirements** 

To follow along, refer to the instructions in the `README` file: 

```
https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-
A2A/blob/main/ch07/ai-six/README.md
```

###### **What is MCP?** 

MCP wasidx_306caf8c introduced by the team at Anthropic ( `https://www.anthropic.com` ) to standardize interactions between agentic AI systems, data sources, and external services. With MCP, you can build agentic AI systems that "speak" MCP, and you can automatically integrate with any MCP server. This means that you extend the capabilities of the AI system with tools from a large ecosystem beyond custom tools. For MCP tool developers, it embodies the principle of “ _Write once, Run everywhere_ .” The protocol has a formal specification ( `https:// modelcontextprotocol.io/specification` ). The protocol is versioned, and it evolves quickly. 

###### **The motivation behind MCP** 

Before MCP, every agentic AI system was essentially on its own. If a developer wanted their AI agent to interact with external tools suchidx_ac5f599d as an **application programming interface** ( **API** ), a database, or a proprietary service, they had to design and implement custom connectors. These connectors not only had to know how to talk to the external system, but also how to inject relevant information into the LLM’s context in a useful and timely way. This was often implemented as tools that were tightly coupled to the specific AI framework being used. 

This approach quickly became a maintenance nightmare: 

- Developers had to reimplement context injection logic for each use case 

- Developers had to reimplement context injection logic for each use case • Tool and service providers had to write multiple integration layers to support different AI systems 

- There was no standard way for tools to declare what they could do beyond a noncompatible tool calling specification of different LLM providers 

As a result, the ecosystem became fragmented and brittle. Tooling was tightly coupled to specific frameworks, and reuse across projects was nearly impossible. 

MCP was created to solve this problem. It introduces a shared protocol that standardizes how tools and resources can be exposed to models. Instead of hardcoding custom logic per integration, developers can now implement an MCP-compliant server that predictably advertises its capabilities. Likewise, AI systems only need to implement a single client interface to dynamically discover, query, and invoke tools and resources from any MCP server. There are 

_Integrating with the Model Context Protocol Ecosystem_ 

215 

readily available libraries for many popular programming languages, making it easy to implement MCP servers and clients. 

The result is a modular, composable ecosystem, where tools can be reused across projects. 

Let's take a closer look at the architecture and core components of MCP. 

###### **MCP architecture core and core components** 

MCP hasidx_24d0c53f a client-server architecture. MCP servers expose tools and resources, while MCP clients consume them. MCP clients are embedded in MCP hosts (the agentic AI system) and can utilize tools and resources from multiple MCP servers, some local and some remote. Local stdio MCP servers are faster, but present security concerns if coming from third-party providers. Remote MCP servers have the same networking and authentication concerns as any remote API. Here is a diagram of the MCP architecture that illustrates this: 

<!-- Start of picture text -->
[ Local Machine<br>MCP Host (Al Application)<br>MCP Client 1 MCP Client 2 MCP Client 3<br>One-to-one One-to-one One-to-one<br>connection connection connection<br>¥ +<br>R<br>MCP Server 1 MCP Server 2 MCP Server 3<br>(e.g. AWS) (e.g. Filesystem) (Remote Queue)<br><!-- End of picture text -->

_Figure 7.1: MCP architecture_ 

The actual protocol by which MCP servers and clients communicate has two layers: the data layer and the transport layer: 

- The **data layer** specifiesidx_e0878498 the JSON-RPC-based protocol for client-server communication, which includes life cycle management, core primitives, such as tools, resources, and prompts, and notifications. 

- The **transport layer** specifies idx_1c8e1cf1the communication mechanisms and channels that enable data exchange between clients and servers, including transport-specific connection establishment, message framing, and authorization. 

Let's break down the key components of MCP. 

_Chapter 7_ 

216 

###### **MCP servers** 

An **MCP server** ( `https://modelcontextprotocol.io/docs/learn/server-concepts` ) is a program idx_33589d07 that exposes tools (invokable functions) and resources (contextual information) to LLM-based systems via MCP. It allows any compliant LLM host application to discover, invoke, and consume capabilities in a predictable, composable, and transport-agnostic way. Each idx_73e34702MCP server may support multiple specification versions. The actual version is negotiated ( `https:// modelcontextprotocol.io/specification/versioning## negotiation` ) when an MCP client establishes a connection to an MCP server. 

While MCP servers may expose resources ( `https://modelcontextprotocol.io/docs/learn/ server-concepts## resources-context-data` ) and even offer prompt support ( `https:// modelcontextprotocol.io/docs/learn/server-concepts## prompts-interactiontemplates` ), we will focus on the tools aspect here. 

Resources can be exposed as tools (e.g., `list_resources()` and `get_resource()` actions), so there is no need for a separate concept. Prompt management is arguably an application-level concern and not the concern of any individual MCP server. Again, if you want, for some reason, your MCP server to offer prompt templates, you can always expose a `get_prompt_template()` tool. In my opinion, the addition of resources (which you can think of as a poor person's RAG) and prompts to MCP is a mistake that just complicates the protocol and makes the learning curve steeper. Your mileage may vary, so feel free to explore these features. From now on, we will consider only the tools aspect of MCP. 

The AI-6 equivalent of an MCP server is a set of related tools, such as the filesystem tools. However, AI-6 tools are discovered and imported as Python modules into the agentic AI system via the AI-6 framework. MCP servers, on the other hand, run as independent processes either locally or remotely. The MCP client will communicate with each MCP server via the proper transport protocol. 

An AI system can use multiple MCP servers, each exposing a different set of tools. 

Note that the AI system will need a dedicated MCP client for each MCP server it wants to use. The MCP client is responsible for discovering the available tools and invoking them as needed. 

_Integrating with the Model Context Protocol Ecosystem_ 

217 

###### **MCP clients** 

**MCP clients** are idx_aa5dae16the components that interact with MCP servers to discover and invoke tools. They are embedded in the MCP host (the agentic AI system) directly or abstracted away by a framework such as AI-6. Each MCP client is responsible for connecting to a single MCP server. The MCP specification is not trivial, so most MCP clients utilize a library that implements the protocol and exposes an easy-to-use API for interacting with the MCP server. I highly recommend using a library as opposed to implementing the protocol from scratch. First, why would you want to reinvent the wheel? There isn't much innovation or performance to gain by implementing the protocol yourself. Second, MCP is a complex protocol that keeps evolving. If you build your own MCP client based on the spec, you'll have to first make sure it actually works correctly, and then you'll have to maintain it and chase the spec changes as they happen. This is a lot of work with no benefit. 

The AI-6 equivalent of an MCP client **i** dx_9a0318b0 s the discovery mechanism of the engine that scans the tool directory, discovers Python classes that implement the `Tool` abstract base class, dynamically imports them, and instantiates them. At that point, the engine can invoke any tool by calling this `run()` method. 

###### **MCP hosts** 

**MCP hosts** are idx_25f8ca46the agentic AI systems that utilize MCP clients to discover and invoke tools from MCP servers. If the MCP uses an AI framework that supports MCP, then it doesn't even need to be aware of MCP. The framework will expose the agentic loop in an MCP-agnostic way, and the agentic AI system will just need to supply the proper configuration for the MCP tools it wants to use. 

We will soon see how all these components play out together in the AI-6 framework. For now, let's look at the important distinction between local and remote MCP servers. 

###### **Local versus remote MCP servers** 

MCP servers can idx_e13cd6cfbe either local or remote. A local MCP server runs on the same machine as the MCP client, while a remote MCP server runs on a different machine, possibly in the cloud. The choice between local and remote servers depends on the use case and the resources available. 

An MCP client can connect to multiple MCP servers, both local and remote. When connecting to a local MCP server, the MCP client will idx_2cb85484use the **standard input/output** ( **STDIO** ) streams transport ( `https://modelcontextprotocol.io/specification/2025-11-25/basic/ transports#stdio` ). When connecting to a remote MCP server, the MCP client will use the Streamable HTTP transport ( `https://modelcontextprotocol.io/specification/ 2025-11-25/basic/transports#streamable-http` ). 

_Chapter 7_ 

218 

Note that this information is accurate for the current version of the MCP specification ( `https://modelcontextprotocol.io/specification/2025-11-25` ). 

Regardless of the transport, the sequence of messages is the same, and the message format is always JSON-RPC 2.0 ( `https://www.jsonrpc.org/` ). 

###### **Benefits of using MCP** 

For idx_baca9e3e agentic AI systems, MCP offers several key benefits to different stakeholders. Let's break it down for agentic AI frameworks, tool providers, and agentic AI system developers: 

- **MCP for agentic AI frameworks** : An agentic AI framework that supports MCP, such as AI-6, LangGraph, AutoGen, or CrewAI, automatically provides access to a huge and growing ecosystem of interoperable tools and resources. At this point in time, it is a basic requirement for an agentic AI framework. Note that offering MCP support doesn't mean giving up on custom tools. AI-6, for example, supports both MCP and custom tools. We will discuss why it's important later in the chapter. 

- **MCP for tool providers** : Tool providers benefit from MCP because, by publishing on MCP servers, they are automatically compatible with any AI system that uses an AI framework with MCP support. There is no need to provide a dedicated wrapper for every AI framework out there or document how to use it from different frameworks. Tool providers can build once against the MCP interface and achieve broad compatibility. This opens the door for a rich ecosystem of reusable tools that can be composed into larger systems, much like APIs in traditional software. MCP also makes it easier to define metadata such as tool capabilities, safety constraints, and cost models. Since the MCP ecosystem is thriving, tool developers can count on the community to provide registries, a discovery mechanism, and other infrastructure. Another idx_f22fbf32major benefit of MCP for tool developers is that they can use any programming language they choose since the protocol is language-agnostic. This opens the door to writing MCP tools quickly using dynamic languages such as Python, TypeScript, or even shell scripts. But if you're writing a heavyweight MCP server that wraps a critical system and you need a lot of control or to optimize performance, you use something like Rust. 

- **MCP for agentic AI system developers** : This is an easy one. As an agentic AI system developer, you should use an agentic AI framework that supports MCP, such as AI-6, LangGraph, AutoGen, CrewAI, and every other self-respecting agentic AI framework. By choosing an MCP-compliant framework, you immediately gain access to a rapidly growing ecosystem of interoperable tools. 

The benefits of MCP gave rise to a very active ecosystem, which we will explore next. 

_Integrating with the Model Context Protocol Ecosystem_ 

219 

###### **The MCP ecosystem** 

The MCP ecosystemidx_a1f39cbf is quickly becoming the foundation for building and scaling agentic AI systems. It standardizes how agents, tools, memory systems, and orchestration layers interact, turning fragmented integrations into a cohesive and composable architecture. The ecosystem includes an expanding collection of MCP-compliant frameworks such as AI-6, LangGraph, and AutoGen, along with tool providers, memory backends, and control interfaces. This modular approach enables developers to mix and match components with minimal friction, making it easier to experiment, deploy, and evolve complex multi-agent systems. 

There are no concerns about vendor lock-in or compatibility issues, as the MCP standard ensures that any compliant tool can be brought in and any framework may be replaced without losing the investment in tools and resources. This is a game-changer for the agentic AI community, as it idx_095cf8f2allows developers to focus on building their application using any framework they want, knowing they will be able to use MCP tools with any of them. 

The sort of official place to find MCP servers at present is the **Example Servers** page ( `https:// modelcontextprotocol.io/examples` ) on the `modelcontextprotocol.io` website, which lists reference implementations in different languages as well as official integrations by various third-party companies. 

There are many community websites dedicated to indexing and listing existing MCP servers. Here are a few examples: 

- `https://mcpfinder.io` 

```
https://mcp.so
```

- 

- `https://remote-mcp-servers.com` 

Be careful before using some obscure MCP server, especially if you download and run it locally, as it has all the permissions of the user who started the server. 

OK. Now that we have a good understanding of MCP and its benefits, let's see how to build MCP servers and clients, and how to integrate MCP into the AI-6 framework. 

###### **Building MCP servers** 

Building idx_f177969eMCP servers with different programming languages and libraries can teach you a lot about the benefits of MCP. The knowledge, skills, and even the MCP servers themselves are transferable to any modern agentic AI system or framework. 

We will build two MCP servers that expose functionality similar to or identical to some custom AI-6 tools, such as the filesystem tools and the GitHub tool. This process will allow us to compare two implementations, one for AI-6 only and one for MCP. 

_Chapter 7_ 

220 

###### **Filesystem MCP server** 

Let's quickly idx_4b8492a2review the AI-6 custom filesystem tools. As you recall, they are all subclasses of the `CommandTool` base class and follow a similar pattern. The only exception is the `Echo` tool, which is used to create new files: 

```
for file in py/backend/tools/file_system/*.py; do
if [ -f "$file" ]; then
        echo "=== $file ==="
        cat "$file"
        echo
    fi
done
# === py/backend/tools/file_system/awk.py ===
from backend.tools.base.command_tool import CommandTool
classAwk(CommandTool):
def__init__(self, user: str | None = None):
super().__init__(
            command_name='awk', user=user,
            doc_link='https://www.gnu.org/software/gawk/manual/gawk.html')
```

```
##=== py/backend/tools/file_system/cat.py ===
from backend.tools.base.command_tool import CommandTool
classCat(CommandTool):
def__init__(self, user: str | None = None):
super().__init__(
            command_name='cat', user=user,
            doc_link = 'https://www.gnu.org/software/coreutils/manual/html_node/
cat-invocation.html')
##=== py/backend/tools/file_system/echo.py ===
import os
import sh
from backend.object_model import Tool, Parameter
```

221 

_Integrating with the Model Context Protocol Ecosystem_ 

```
classEcho(Tool):
def__init__(self, user: str | None = None):
self.user = user
        desc = 'Write content to a file, creating any necessary directories.'
super().__init__(
            name='echo',
            description=desc,
            parameters=[
                Parameter(
                    name='file_path', type='string',
                    description='The path of the file to write to.'),
                Parameter(
                    name='content', type='string',
                    description='The content to write to the file.')
            ],
            required={'file_path', 'content'}
        )
defrun(self, **kwargs):
        filename = kwargs['file_path']
        content = kwargs['content']
        dir_path = os.path.dirname(filename)
ifself.user isnotNone:
            sh.sudo('-u', self.user, 'mkdir', '-p', dir_path)
            sh.sudo('-u', self.user, 'tee', filename, _in=content,
                _out=os.devnull)
returnf"Content written to {filename} as user {self.user}"
        os.makedirs(dir_path, exist_ok=True)
withopen(filename, 'w') as file:
            file.write(content)
returnf"Content written to {filename}"
##=== py/backend/tools/file_system/ls.py ===
```

_Chapter 7_ 

222 

```
from backend.tools.base.command_tool import CommandTool
classLs(CommandTool):
def__init__(self, user: str | None = None):
super().__init__(command_name='ls', user=user, doc_link='https://
www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html')
##=== py/backend/tools/file_system/patch.py ===
from backend.tools.base.command_tool import CommandTool
classPatch(CommandTool):
def__init__(self, user: str | None = None):
super().__init__(
            command_name='patch', user=user,
            doc_link = 'https://www.gnu.org/software/diffutils/manual/html_node/
patch-Invocation.html')
##=== py/backend/tools/file_system/pwd.py ===
from backend.tools.base.command_tool import CommandTool
classPwd(CommandTool):
def__init__(self, user: str | None = None):
        doc_link = 'https://www.gnu.org/software/coreutils/manual/html_node/pwd-
invocation.html'
super().__init__('pwd', user=user, doc_link=doc_link)
##=== py/backend/tools/file_system/sed.py ===
from backend.tools.base.command_tool import CommandTool
classSed(CommandTool):
def__init__(self, user: str | None = None):
super().__init__(
            command_name='sed', user=user,
            doc_link='https://www.gnu.org/software/sed/manual/sed.html')
```

Our idx_6244d73d filesystem MCP server will replace some of these tools with equivalent functionality. All the built-in AI-6 MCP tools are in the `py/backend/mcp-tools` directory. 

_Integrating with the Model Context Protocol Ecosystem_ 

223 

Let's look at the `fs_mcp_server.py` MCP server. It uses the official MCP Python SDK ( `https:// github.com/modelcontextprotocol/python-sdk` ). The `FastMCP` class does all the heavy lifting of registering tools and exposing them via the various MCP transports. The module instantiates it after the required imports: 

```
import shlex
from mcp.server.fastmcp import FastMCP
import sh
mcp = FastMCP("FileSystem Tools", "")
```

The filesystem MCP server contains multiple tools in one module. Each tool is implemented as a single function decorated with the `@mcp.tool()` decorator. Similar to the AI-6 `Tool` abstract base class that marks a class as a tool, the `@mcp.tool()` decorator marks a function as a tool: 

```
@mcp.tool()
defls(args: str) -> str:
"""ls tool. See https://www.gnu.org/software/coreutils/manual/html_node/ls-
invocation.html"""
    parsed_args = shlex.split(args)
return sh.ls(*parsed_args)
@mcp.tool()
defcat(args: str) -> str:
"""cat tool. See https://www.gnu.org/software/coreutils/manual/html_node/cat-
invocation.html"""
    parsed_args = shlex.split(args)
return sh.cat(*parsed_args)
@mcp.tool()
defpwd(args: str) -> str:
"""pwd tool. See https://www.gnu.org/software/coreutils/manual/html_node/pwd-
invocation.html"""
    parsed_args = shlex.split(args) if args.strip() else []
return sh.pwd(*parsed_args)
@mcp.tool()
defmkdir(args: str) -> str:
"""mkdir tool. See https://www.gnu.org/software/coreutils/manual/html_node/
mkdir-invocation.html"""
```

_Chapter 7_ 

224 

```
    parsed_args = shlex.split(args)
return sh.mkdir(*parsed_args)
@mcp.tool()
defcp(args: str) -> str:
"""cp tool. See https://www.gnu.org/software/coreutils/manual/html_node/cp-
invocation.html"""
    parsed_args = shlex.split(args)
return sh.cp(*parsed_args)
```

As you can see, the idx_6c8cde74actual implementation of each MCP tool is very similar to the `CommandTool` class of AI-6. It parses the arguments and invokes the target command-line tool using `sh` . Here is the `CommandTool` class’s `run()` method, which just adds the ability to run as a separate user: 

```
defrun(self, **kwargs):
        args = shlex.split(kwargs['args'])
ifself.user isnotNone:
return sh.sudo('-u', self.user, self.command_name, *args)
else:
returngetattr(sh, self.command_name)(*args)
```

With the MCP server, you can control the OS user when you launch the MCP server as a process. 

In short, implementing idx_2e11c6d2MCP servers in Python is simple when using the official Python SDK. Note that if you need to configure the MCP server, you'll need to come up with your own way, as the MCP Python SDK doesn't offer any assistance here. You can pass command-line arguments, use environment variables, or configuration files. 

But some MCP servers are more involved. Let’s look at the GitHub MCP server. 

###### **GitHub MCP server** 

The GitHub MCP server isidx_0b4f17b0 implemented in Bash for two reasons. First, to demonstrate the ability to write MCP servers in any language. Second, to get a close look at the protocol itself, because there is no library that does all the heavy lifting. We have to directly process and generate JSON-RPC messages and follow the MCP life cycle. 

Let's break it down step by step. The JSON-RPC messages have a standard format of an object with `method` , `id` , and `params` fields. It's also important to serialize the JSON messages we return 

_Integrating with the Model Context Protocol Ecosystem_ 

225 

to a single line, because some clients expect it. The `emit_json()` function replaces newline characters with spaces and takes care of this chore: 

```
#!/bin/bash
# GitHub MCP Server - implements MCP protocol for GitHub CLI tools (newline-
stripped JSON responses)
# Helper: output compact JSON from heredoc
emit_json() {
    tr -d '\n' | tr -s ' '
    echo
}
```

Now, we can start the loop of waiting for MCP messages from the client and responding. It runs forever, parsing incoming messages and responding accordingly: 

```
# Read JSON-RPC messages from stdin and respond
while read -r line; do
    method=$(echo "$line" | jq -r '.method'2>/dev/null)
    id=$(echo "$line" | jq -r '.id'2>/dev/null)
    params=$(echo "$line" | jq -r '.params'2>/dev/null)
    ...
done
```

Let's see what messages it expects and how it responds. Every incoming message is processed according to its method in a big `case` statement. The first message is `"initialize"` , sent by the MCP client to **i** dx_584787d2 nitiate the connection. The MCP server needs to report the supported protocol version and server info. The `capabilities` part may be empty: `case "$method" in "initialize") cat <<EOF | emit_json { "jsonrpc": "2.0", "id": $id, "result": { "protocolVersion": "2024-11-05", "capabilities": {` 

_Chapter 7_ 

226 

```
"tools": {},
"resources": {}
    },
"serverInfo": {
"name": "GitHub CLI Tools",
"version": "1.0.0"
    }
  }
}
EOF
            ;;
```

The client sends a notification that initialization succeeded. No response is expected: 

```
"notifications/initialized")
# Notification - no response needed
            ;;
```

The `"tools/list"` message is called once, and the server responds with its list of tools (just one in this case), which includes the familiar tool name, description, and the input schema for the parameters. We have just one required parameter, `args` , which is the command-line arguments for the GitHub CLI command: 

```
"tools/list")
            cat <<EOF | emit_json
{
"jsonrpc": "2.0",
"id": $id,
"result": {
"tools": [
      {
"name": "gh",
"description": "Execute GitHub CLI commands",
"inputSchema": {
"type": "object",
"properties": {
"args": {
"type": "string",
"description": "GitHub CLI command arguments"
            }
          },
```

_Integrating with the Model Context Protocol Ecosystem_ 

227 

```
"required": ["args"]
        }
      }
    ]
  }
}
EOF
            ;;
```

Now, the MCP client is aware of all the tools this MCP server provides and can call them when necessary. This isidx_536ee5f6 the most complicated case. First, the code verifies that the requested tool name is indeed `"gh"` (the only supported tool name). Then, it runs the `gh $args 2>&1` command, capturing both standard output and standard error. It also captures the exit code and then properly escapes the result, and finally constructs and returns the JSON-RPC response message that includes the escaped result of the `gh` command: 

```
if [ "$tool_name" = "gh" ]; then
                result=$(gh $args 2>&1)
                exit_code=$?
                escaped=$(echo "$result" | jq -Rs .)
                cat <<EOF | emit_json
{
"jsonrpc": "2.0",
"id": $id,
"result": {
"content": [
      {
"type": "text",
"text": $escaped
      }
    ]
  }
}
EOF
```

If the tool idx_4f027064name wasn't `"gh"` , it returns an error message: 

```
else
                cat <<EOF | emit_json
```

_Chapter 7_ 

228 

```
{
"jsonrpc": "2.0",
"id": $id,
"error": {
"code": -32602,
"message": "Unknown tool: $tool_name"
  }
}
EOF
            fi
            ;;
```

Finally, if the message has an unknown method, it returns an appropriate error message: 

```
*)
if [ "$id" != "null" ]; then
                cat <<EOF | emit_json
{
"jsonrpc": "2.0",
"id": $id,
"error": {
"code": -32601,
"message": "Method not found: $method"
  }
}
EOF
            fi
            ;;
    esac
done
```

That concludes our low-level Bash MCP server. It is a lot of work to build, and if the protocol evolves, then you'll need to update your server. Also, it implements only the STDIO transport, so it can't be used as idx_d1e09 **a** ba remote MCP server. I strongly recommend using one of the official MCP SDKs when you build your own MCP servers. 

Let's see what it takes to build an MCP client. 

_Integrating with the Model Context Protocol Ecosystem_ 

229 

###### **Building MCP clients** 

MCP clientsidx_e5642a61 connect to MCP servers and control the interaction. We will not go down the rabbit hole of building an MCP client from scratch, as we did with the GitHub Bash MCP server. Instead, we will take advantage of the MCP Python SDK. AI-6 provides its own `MCPClient` wrapper that can connect to multiple MCP servers, return their tools, and, later, invoke any tool. 

###### **The MCPClient class** 

Our `MCPClient` class idx_907a9ca0lives in the `mcp_client.py` module. Let's start with the imports. Note that the MCP client is designed for async operation. From the `mcp` package, it imports the `ClientSession` and `StdioServerParameter` classes, and then it imports `stdio_client` for 

local MCP servers and `sse_client` for the remote MCP server: 

```
import asyncio
from contextlib import AsyncExitStack
from urllib.parse import urlparse
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client
```

The constructor is pretty simple and manages a dictionary of sessions and a dictionary of server tools that maps MCP servers to their list of tools. It also creates an async exit stack for proper cleanup: 

```
classMCPClient:
"""Standalone MCP client for connecting to and interacting with MCP
servers."""
def__init__(self):
self.sessions: dict[str, ClientSession] = {}
self._server_tools: dict[str, list[dict]] = {}
self.exit_stack = AsyncExitStack()
```

When clients connect to the MCP server, they call the `connect_to_server` method. Let’s see how it works. 

_Chapter 7_ 

230 

###### **Connecting to an MCP server** 

The `connect_to_server()` async idx_05058be9method does a lot of work. Let's examine it piece by piece. It accepts a server ID (an arbitrary, unique ID controlled by the AI system) that identifies the target and a path (for local MCP servers) or a URL (for remote MCP servers). If it's already connected to that server, it returns the tools of that server: 

```
asyncdefconnect_to_server(
        self, server_id: str, server_path_or_url: str
) -> list[dict]:
"""Connect to a single MCP server and return its tools."""
if server_id inself.sessions:
# Already connected, return cached tools
returnself._server_tools.get(server_id, [])
```

Next, it determines whether it's a local or remote MCP server: 

```
# Check if this is a URL (remote server) or file path (local server)
        parsed = urlparse(server_path_or_url)
        is_url = parsed.scheme in ('http', 'https')
```

If it's a remote server, it creates a transport usingidx_dd19a13c the **Server-Sent Events** ( **SSE** ) client, which it uses to generate a `ClientSession` object. If anything goes wrong, it prints an error message and re-raises the exception: 

```
if is_url:
print(
f"Connecting to remote MCP server: {server_path_or_url}")
try:
                transport = awaitself.exit_stack.enter_async_context(
                    sse_client(server_path_or_url))
                read, write = transport
                session = awaitself.exit_stack.enter_async_context(
                    ClientSession(read, write))
print(f"Successfully connected to {server_path_or_url}")
except Exception as e:
print(f"Failed to connect to remote MCP server
{server_path_or_url}: {e}")
raise
```

_Integrating with the Model Context Protocol Ecosystem_ 

231 

But, if it's a local server, it checks (based on file extension only) whether it's a Python, TypeScript, or Shell MCP server. Otherwise, it raises an exception. This is just a choice because there are no plans to support other languages for local MCP servers for AI-6. It is totally valid to support other languages or, even better, Docker images that can contain the MCP server in any language: 

```
else:
# Local file-based server
if server_path_or_url.endswith('.py'):
                command = "python"
elif server_path_or_url.endswith('.sh'):
                command = "bash"
elif server_path_or_url.endswith('.js'):
                command = "node"
else:
raise ValueError(f"Unsupported server type: {server_path_or_url}")
```

Next, it idx_a2d5478fprepares the server parameters, which are just the path to the MCP server file. No command-line argument or additional environment variables are provided. We may want to support more configuration in the future. Then, it generates an STDIO transport and uses it to create a local `ClientSession` object: 

```
            server_params = StdioServerParameters(
                command=command,
                args=[server_path_or_url],
                env=None
            )
            stdio_transport = awaitself.exit_stack.enter_async_context(
                stdio_client(server_params))
            stdio, write = stdio_transport
            session = awaitself.exit_stack.enter_async_context(
                ClientSession(stdio, write))
```

At this point, we have a `ClientSession` (either local or remote) object, and we can fetch the tools of the MCP server by calling `session.list_tools()` . Under the covers, this call exchanges the proper JSON-RPC messages with the MCP server according to the protocol: 

```
# Initialize session with timeout
await asyncio.wait_for(session.initialize(), timeout=10.0)
```

_Chapter 7_ 

232 

```
# List tools with timeout
        response = await asyncio.wait_for(
            session.list_tools(), timeout=10.0)
        tools = [{
"name": tool.name,
"description": tool.description,
"parameters": tool.inputSchema
        } for tool in response.tools]
```

Then, we store the session and the tools to retrieve later if needed, and return the tools: 

```
# Cache the session and tools
self.sessions[server_id] = session
self._server_tools[server_id] = tools
return tools
```

Note thatidx_b8e4d5e3 the 10-second timeout should be sufficient in most cases, but in rare cases where the MCP server has a long initialization sequence, it may be better to provide a configurable timeout duration. 

Once the agentic AI system connects to an MCP server, the next step is to invoke one or more of the tools it provides. 

###### **Invoking an MCP tool** 

The agentic AI systemidx_7cd38fab received the list of tools of every MCP server when it called the `connect_to_server()` method. At any point, it may decide to invoke one of these tools by calling the `invoke_tool()` method, which accepts the server ID, the tool name, and a dictionary of arguments for the tool. The call returns a response from the tool (unless an exception is raised). First, it checks whether there is an active session associated with the requested server’s ID and raises an exception if there is none: 

```
asyncdefinvoke_tool(
        self, server_id: str, tool_name: str, tool_args: dict
) -> str:
"""Invoke a specific tool on the specified MCP server."""
        session = self.sessions.get(server_id)
ifnot session:
raise RuntimeError(f"No active session for server '{server_id}'.
Connect to server first.")
```

_Integrating with the Model Context Protocol Ecosystem_ 

233 

Then, it calls the tool by invoking the `session.tool_call()` method with the tool name and arguments. It returns the response from the tool (which may be empty). If the tool call timed out or raised some other exception, it prints an error message and re-raises the exception: 

```
try:
print(f"Invoking tool {tool_name} on server {server_id} with args:
{tool_args}")
# Add timeout to prevent hanging on slow/unresponsive servers
            result = await asyncio.wait_for(
                session.call_tool(tool_name, tool_args),
                timeout=30.0# 30 second timeout
            )
print(f"Tool{tool_name} completed successfully")
return result.content[0].text if result.content else""
except asyncio.TimeoutError:
print(f"Tool invocation timed out for {server_id}:
{tool_name} after 30 seconds")
raise RuntimeError(f"Tool invocation timed out for {server_id}:
{tool_name} after 30 seconds")
except Exception as e:
print(f"Tool invocation failed for {server_id}:{tool_name}: {e}")
raise
```

The idx_b2969213class offers additional helper methods. The `get_server_tools()` method can be used by the agentic AI system if it prefers to fetch the tools of a server on the fly when needed: 

```
defget_server_tools(self, server_id: str) -> list[dict]:
"""Get cached tools for a server."""
returnself._server_tools.get(server_id, [])
```

The `is_connected()` method checks whether the target server ID is associated with a session: 

```
defis_connected(self, server_id: str) -> bool:
"""Check if connected to a server."""
return server_id inself.sessions
```

_Chapter 7_ 

234 

The `disconnect_server()` method deletes a `ClientSession` and removes its tools. This can be useful for an MCP server that uses a lot of resources and is needed only for certain phases of a conversation: 

```
asyncdefdisconnect_server(self, server_id: str):
"""Disconnect from a specific server."""
if server_id inself.sessions:
# Session cleanup handled by exit_stack
delself.sessions[server_id]
if server_id inself._server_tools:
delself._server_tools[server_id]
```

Finally, the `cleanup()` method clears the sessions and `_server_tools` dictionaries: 

```
asyncdefcleanup(self):
"""Cleanup all resources."""
self.sessions.clear()
self._server_tools.clear()
awaitself.exit_stack.aclose()
```

Let’s see how idx_abf7e473to extend the AI-6 framework with MCP support in addition to its own proprietary tool system. 

###### **Integrating MCP into the AI-6 framework** 

AI-6 has itsidx_46294c32 own tool system in place, including discovery, registration, and an abstract base class called `Tool` , and the entire agentic loop of the engine is built around these concepts. How do we integrate a whole idx_a288615dnew tooling system, such as MCP? We can take advantage of the **fundamental theorem of software engineering** ( **FTSE** ) ( `https://en.wikipedia.org/wiki/ Fundamental_theorem_of_software_engineering` ), which states, " _We can solve any problem by introducing an extra level of indirection_ ." In this context, it means wrapping all MCP tools with an indirection layer that looks like an AI-6 tool. Enter the universal `MCPTool` class, which can wrap an MCP tool (local or remote) and make it accessible to AI-6 as if it were one of its own tools. Let's see how the magic happens. 

_Integrating with the Model Context Protocol Ecosystem_ 

235 

###### **The universal MCPTool class** 

The `MCPTool` class ( `https://github.com/Sayfan-AI/ai-six/blob/v0.11.0/py/backend/ tools/base/mcp_tool.py#44` ) must be a subclass of the AI-6 `Tool` class, whichidx_e5bf7428 means it needs toidx_bd6a2b1a implement its abstract methods. This is really the only requirement of compatibility. When it is constructed, it needs access to an `MCPClient` instance that it can invoke when the tool's `run()` method is called. Let's check the code. 

Here are the imports. We need `asyncio` and `threading` for dealing with `asyncio` -based `MCPClient` , and from the AI-6 object model, we need the `Tool` base class and the `Parameter` definition: 

```
import asyncio
import threading
from backend.object_model.tool import Tool, Parameter
from backend.mcp_client.mcp_client import MCPClient
```

Let's jump straight into the deep end and handle the thorny issue of adapting the MCP tool schema to the AI-6 object model. The `_json_schema_to_parameters()` function takes an MCP tool schema dictionary and converts it to a list of AI-6 `Parameter` objects and a set of required parameter names. The code is pretty straightforward, so there is no need to explain every line: 

```
def_json_schema_to_parameters(
schema: dict
) -> tuple[list[Parameter], set[str]]:
"""Convert JSON schema to Tool parameters and required set."""
    parameters = []
    required = set()
ifnotisinstance(schema, dict) or'properties'notin schema:
return parameters, required
# Get required fields
if'required'in schema andisinstance(schema['required'], list):
        required = set(schema['required'])
# Convert properties to parameters
for prop_name, prop_def in schema['properties'].items():
        param_type = prop_def.get('type', 'string')
```

_Chapter 7_ 

236 

```
        description = prop_def.get('description',
f'{prop_name} parameter')
# Map JSON schema types to our parameter types
if param_type == 'array':
            param_type = 'array'
elif param_type in ['integer', 'number']:
            param_type = 'number'
elif param_type == 'boolean':
            param_type = 'boolean'
else:
            param_type = 'string'
        parameters.append(Parameter(
            name=prop_name,
type=param_type,
            description=description
        ))
return parameters, required
```

We will seeidx_94628725 where idx_7f02abe2 this function is used soon. Let's continue to the `MCPTool` class itself. It has multiple class-level fields because all the `MCPTool` instances share the same `MCPClient` object that manages all the MCP `ClientSession` instances. The asynchronous nature of the `MCPClient` object requires some careful management of a client lock and a shared event loop: 

```
classMCPTool(Tool):
"""Tool that uses MCP (Model Context Protocol) servers."""
# Shared MCP client instance across all MCP tools
    _client: MCPClient = None
    _client_lock = threading.Lock()
# Shared event loop for all MCP operations
    _event_loop = None
    _loop_thread = None
    _loop_lock = threading.Lock()
```

The idx_525636a0constructor takes a server ID, server path, or URL (depending on whether it's a local or remote MCP server), and a dictionary withidx_884de441 tool information received from the MCP server. The code then extracts the name and description (or default) from the tool information dictionary 

_Integrating with the Model Context Protocol Ecosystem_ 

237 

and converts the MCP tool parameters to AI-6 parameters by calling `_json_schema_to_parameters()` . Then, it passes the AI-6 tool information to the `Tool` base class by calling the `super().__init__()` constructor and stores the server ID, server path or URL, and the tool name. These will be needed when the tool is invoked later: 

```
def__init__(
self, server_id: str, server_path_or_url: str, tool_info: dict
    ):
"""Initialize from MCP tool information."""
        tool_name = tool_info['name']
        description = tool_info.get(
'description', f'{server_id} tool: {tool_name}')
# Convert parameters from JSON schema
        parameters, required = _json_schema_to_parameters(
            tool_info.get('parameters', {})
        )
super().__init__(
            name=tool_name, description=description,
            parameters=parameters, required=required)
self.server_id = server_id
self.server_path_or_url = server_path_or_url
self.mcp_tool_name = tool_name
```

As you recall, the `MCPClient` is managed at the class level. The `_get_client()` class method creates the `MCPClient` instance for the first time and then just returns the same instance on subsequent calls. It implements the double-checked locking pattern ( `https:// en.wikipedia.org/wiki/Double-checked_locking` ) to avoid instantiating the `MCPClient` more than once: 

```
@classmethod
def_get_client(cls) -> MCPClient:
"""Get or create the shared MCP client instance."""
if cls._client isNone:
with cls._client_lock:
if cls._client isNone:
                    cls._client = MCPClient()
return cls._client
```

_Chapter 7_ 

238 

The `_get_or_create_loop()` follows the idx_1e3d5b39same pattern and returns (creating if necessary) a singleton `asyncio` event loop: 

```
@classmethod
def_get_or_create_loop(cls):
"""Get or create a shared event loop for MCP operations."""
# Always use our own managed loop for sync tool execution
# This avoids "event loop is closed" issues from creating/closing loops
repeatedly
if cls._event_loop isNoneor cls._event_loop.is_closed():
with cls._loop_lock:
if cls._event_loop isNoneor cls._event_loop.is_closed():
                cls._event_loop = asyncio.new_event_loop()
return cls._event_loop
```

The `_ensure_connected()` method gets the client and the event loop, sets it explicitly to avoid idx_854559ffconflicts, waits until the client connects to the server, and then returns the client and the event loop: 

```
def_ensure_connected(self):
"""Ensure connection to the MCP server."""
    client = self._get_client()
    loop = self._get_or_create_loop()
ifnot client.is_connected(self.server_id):
# Use shared event loop for connection
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            client.connect_to_server(
self.server_id, self.server_path_or_url))
return client, loop
```

Now that we did all the hard work of wiring up the `MCPClient` and dealing with all the `asyncio` gotchas, let's look at the `run()` method, which the AI-6 engine calls when the LLM requests to execute a tool call: 

```
defrun(self, **kwargs) -> str:
"""Execute the MCP tool with the given arguments."""
    client, loop = self._ensure_connected()
```

_Integrating with the Model Context Protocol Ecosystem_ 

239 

```
return loop.run_until_complete(
        client.invoke_tool(self.server_id, self.mcp_tool_name, kwargs
```

The code idx_dae195 **c** 3 alls the `_ensure_connected()` method idx_55c19d42and then gets the client and the event loop. The nice thing is that there is no need to translate the arguments from the AI-6 representation to the `MCPClient` representation, as they are both just a dictionary of `str` -> `object` . The MCP client's `invoke_tool()` method interacts with the MCP server and returns the result as a string. 

Last but not least, the `cleanup_all()` class method gracefully shuts down the `asyncio` machinery: 

```
@classmethod
defcleanup_all(cls):
"""Cleanup all MCP connections. Call this on shutdown."""
if cls._client isnotNone:
# Use our managed loop for cleanup
        loop = cls._get_or_create_loop()
        asyncio.set_event_loop(loop)
try:
            loop.run_until_complete(cls._client.cleanup())
finally:
# Now we can close our managed loop
if cls._event_loop andnot cls._event_loop.is_closed():
                cls._event_loop.close()
            cls._event_loop = None
        cls._client = None
```

That concludes the examination of the `MCPTool` class, but we still miss a key piece of the story, which is how the various MCP servers are discovered and instantiated. 

###### **MCP tool discovery** 

The idx_c8e3fbc4 AI-6 `Engine` class idx_07d73a32was responsible for tool discovery before, but with the integration of MCP, I extracted this functionality to a dedicated module called `tool_manager` , which performs the original AI-6 native tool discovery, local MCP tool discovery, and incorporates configured remote MCP servers, too. 

Let's see how the tool manager works and later how the `Engine` is using it to get access to all the tools. 

_Chapter 7_ 

240 

###### **The tool manager** 

The `tool_manager.py` module ( `https://github.com/Sayfan-AI/ai-six/blob/v0.11.0/py/ backend/engine/tool_manager.py` ) offloads a lot of complexity from the `Engine` class and idx_c9285aealets it focus on theidx_2f29a503 important task of running the agentic loop. 

Let's examine the code, starting as usual with the imports, which should all be familiar by now. Note the `importlib.util` and `inspect` modules that do the heavy lifting for dynamic custom tool discovery (previously in the engine): 

```
import asyncio
import os
from pathlib import Path
import importlib.util
import inspect
from backend.object_model.tool import Tool
from backend.tools.base.mcp_tool import MCPTool
from backend.mcp_client.mcp_client import MCPClient
from backend.engine.config import ToolConfig
```

The `get_tool_dict()` function is the only public function. The discovery of all tools, whether AI-6-native or MCP tools, happens here. It starts with an empty tool list and then invokes these functions to get different types of tools and add them to the tool list: 

- `_discover_native_tools()` 

- `_discover_local_mcp_tools()` 

- 

- `_get_remote_mcp_tools()` 

- 

All tools are derived from the `Tool` base class, which the engine knows how to configure and invoke: 

```
defget_tool_dict(tool_config: ToolConfig) -> dict[str, Tool]:
"""Get a dictionary of all available tools from various sources.
Args:
tool_config: ToolConfig object containing tool configuration
    Returns:
Dict mapping tool names to Tool instances
    """
```

_Integrating with the Model Context Protocol Ecosystem_ 

241 

```
    tools: list[Tool] = []
# 1. Discover AI-6 native tools
if tool_config.tools_dir:
        native_tools = _discover_native_tools(
            tool_config.tools_dir,
            tool_config.tool_config
        )
        tools.extend(native_tools)
# 2. Discover local MCP tools
if tool_config.mcp_tools_dir:
        local_mcp_tools = _discover_local_mcp_tools(
            tool_config.mcp_tools_dir
        )
        tools.extend(local_mcp_tools)
# 3. Get tools of remote MCP servers
if tool_config.remote_mcp_servers:
        remote_mcp_tools = _get_remote_mcp_tools(
            tool_config.remote_mcp_servers
        )
        tools.extend(remote_mcp_tools)
return {tool.name: tool for tool in tools}
```

We idx_8dcbf740will skip the `_get_local_tools()` function asidx_bd7596c6 we covered it in depth in _Chapter 4_ . Let's focus on the MCP tool discovery. 

The `_discover_local_mcp_tools()` function accepts a directory of local MCP servers and returns the list of `MCPTool` objects, which is the union of all the MCP tools from all the MCP servers packaged as `MCPTool` objects. If the MCP server directory is invalid, it returns an empty list: 

```
def_discover_local_mcp_tools(mcp_servers_dir: str) -> list[MCPTool]:
"""Discover MCP tools dynamically by connecting to MCP servers."""
ifnot os.path.isdir(mcp_servers_dir):
return []
```

_Chapter 7_ 

242 

Then, it defines a nested async function called `discover_async()` . This function is visible only inside the `_discover_local_mcp_tools()` function. This is necessary to bridge the sync and async worlds. Let's break it down. 

First, it defines an empty tools list and creates a new `MCPClient` . Then, it starts a `try` block and iterates over all the files in the MCP servers directory (this comes from the argument to its parent function): 

```
asyncdefdiscover_async():
    tools: list[Tool] = []
    client = MCPClient()
try:
# Iterate over all files in the directory
for file_name in os.listdir(mcp_servers_dir):
```

For each item, it calculates the script path (remember that only Python, Node, and Shell local MCP servers are supported). If it's not a file, it just continues to the next item: 

```
script_path = os.path.join(mcp_servers_dir, file_name)
# Check if it's a file
ifnot os.path.isfile(script_path):
continue
```

However, if **i** dx_55bcba74 t is a file, then it uses its filename idx_10fbe452as the server ID when it calls the client’s `connect_to_server()` function, which returns all the tools of that MCP server. It creates a new `MCPTool` instance for each tool and adds them to the tools list. If anything goes wrong, it prints an error message and continues to the next tool: 

```
try:
# Connect to server and get its tools with timeout
    server_tools = await asyncio.wait_for(
        client.connect_to_server(script_path, script_path),
        timeout=5.0
    )
# Create MCPTool instances for each tool
for tool_info in server_tools:
        mcp_tool = MCPTool(script_path, script_path, tool_info)
        tools.append(mcp_tool)
```

_Integrating with the Model Context Protocol Ecosystem_ 

243 

```
except Exception as e:
# Skip servers that fail to connect or timeout
    error_msg = str(e) ifstr(e) elsef"{type(e).__name__}: {e}"
print(f"Warning: Failed to connect to MCP server {script_path}: {error_msg}")
continue
```

Once all the MCP servers are processed and their combined tools are added to the tools list, it performs the client cleanup and then returns the tools: 

```
finally:
await client.cleanup()
return tools
```

All that happens in the nested async function, `discover_async()` . The parent function, 

`_discover_local_mcp_tools()` , invokes the async function using `asyncio.run()` , which allows synchronous functions to call idx_67f20584async functions and wait for them to complete, and returns the idx_5a22813bresult (the combined tool list from all the MCP servers). If anything goes wrong, it prints a warning and returns an empty list: 

```
# Run async discovery in sync context
try:
return asyncio.run(discover_async())
except Exception as e:
print(f"Warning: MCP tool discovery failed: {e}"
return []
```

The `_discover_local_mcp_tools()` function took care of all the local MCP servers. However, AI-6 supports remote MCP servers, too. Let's see how we can bring them into the fold. 

The `_get_remote_mcp_tools()` function follows the same blueprint as 

`_get_local_mcp_tools()` with a nested async function, but there are some important differences too. So, let's go over it in detail. 

The function accepts a list of dictionaries that each contains the name and URL of a remote MCP server. So, there is no scanning of a directory looking for MCP servers. It also returns a list of `Tool` objects that is initialized to an empty list: 

```
def_get_remote_mcp_tools(remote_servers: list[dict]) -> list[Tool]:
"""Connect to remote MCP servers and get their tools.
```

_Chapter 7_ 

244 

```
Args:
remote_servers: List of remote server configurations
        Each server config should have: {'url': 'https://...', 'name': '...'}
    Returns:
        List of MCPTool instances for remote tools
    """
    tools: list[Tool] = []
```

The `connect_sync()` nested function is pretty similar to the `discover_sync()` nested function of `_discover_local_mcp_tools()` , except there is no discovery here by iterating over files because all the remote MCP server configurations were already provided. So, the function iterates over them, tries to connect to each and fetch their tools, and then creates an `MCPTool` object. Theidx_ac285b73 server ID in this case is the server name from the configuration: 

```
asyncdefconnect_async():
        client = MCPClient()
try:
for server_config in remote_servers:
try:
                    server_url = server_config.get('url')
                    server_name = server_config.get('name', server_url)
ifnot server_url:
print(f"Warning: Remote MCP server config missing 'url':
{server_config}")
continue
# Connect to remote server with timeout
                    server_tools = await asyncio.wait_for(
                        client.connect_to_server(server_name, server_url),
                        timeout=10.0
                    )
# Create MCPTool instances for each remote tool
for tool_info in server_tools:
# Use server_url as script_path for remote tools
                        mcp_tool = MCPTool(
```

_Integrating with the Model Context Protocol Ecosystem_ 

245 

```
                            server_name, server_url, tool_info)
                        tools.append(mcp_tool)
except Exception as e:
print(f"Warning: Failed to connect to remote MCP server
{server_config}: {e}")
continue
finally:
await client.cleanup()
```

Then, justidx_6e544bc6 as idx_d24e2316before, run the nested function and return the tools: 

```
# Run async connection in sync context
try:
        asyncio.run(connect_async())
except Exception as e:
print(f"Warning: Remote MCP server connection failed: {e}")
return []
return tools
```

This concludes our drill-down of the `tool_manager` module. Let's see how the engine benefits from this separation of concerns. 

###### **How the engine uses the tool manager** 

The engine idx_7927108e now has only one import related to tool discovery: 

```
from backend.engine import tool_manager
```

It also has just one line of code in its constructor that calls the `get_tool_dict()` function of the tool manager: 

```
self.tool_dict = tool_manager.get_tool_dict(tool_config)
```

This is as simple as it gets, and it improves the architecture and maintainability of the engine as well as the entire AI-6 project. 

_Chapter 7_ 

246 

Here is the entire constructor of the `Engine` class, which now has no tool discovery functionality at all: 

```
classEngine:
def__init__(self, config: Config):
self.default_model_id = config.default_model_id
# Store threshold ratio and calculate token threshold based on default
model
self.summary_threshold_ratio = config.summary_threshold_ratio
        context_window_size = get_context_window_size(
self.default_model_id)
self.token_threshold = int(
            context_window_size * config.summary_threshold_ratio
        )
# Find LLM providers directory
        llm_providers_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "llm_providers"
        )
assert os.path.isdir(llm_providers_dir), (
f"LLM providers directory not found: {llm_providers_dir}"
        )
# Discover available LLM providers
self.llm_providers = Engine.discover_llm_providers(
            llm_providers_dir, config.provider_config
        )
ifnotself.llm_providers:
raise ValueError("No LLM providers found or initialized")
self.model_provider_map = {
            model_id: llm_provider
for llm_provider inself.llm_providers
for model_id in llm_provider.models
        }
```

_Integrating with the Model Context Protocol Ecosystem_ 

247 

```
# Discover and initialize all tools
        tool_config = ToolConfig.from_engine_config(config)
self.tool_dict = tool_manager.get_tool_dict(tool_config)
# Initialize session and session manager
self.session_manager = SessionManager(config.memory_dir)
self.session = Session(config.memory_dir)
# Session-related attributes
self.checkpoint_interval = config.checkpoint_interval
self.message_count_since_checkpoint = 0
# Instantiate the summarizer with the first LLM provider
self.summarizer = Summarizer(self.llm_providers[0])
# Register memory tools with the engine
self._register_memory_tools()
# Load previous session if session_id is provided and exists
if config.session_id:
            available_sessions = self.session_manager.list_sessions()
if config.session_id in available_sessions:
self.session = Session(config.memory_dir)  # Create a new session
object
self.session.load(config.session_id)  # Load from disk
```

OK. We coveredidx_322b38ce all aspects of MCP integration into AI-6. Let's see it in action. 

_Chapter 7_ 

248 

###### **Putting it all together** 

Let's start a idx_c7452c56quick AI-6 session and see the new MCP tools in action. I'll ask AI-6 to find my most popular GitHub repos. Here is the final result: 

<!-- Start of picture text -->
G Readme G<br>show me the my top 5 github repos with<br>the most stars (descending order by<br>number of stars). note that I have a lot of<br>repos. don't miss any of them. feel free<br>to add emojis.<br>Here are your top 5 GitHub repositories with the most stars:<br>1. delinkcious # - 71 stars<br>2. conman # - 38 stars<br>3. go-etcd3-demo # - 25 stars<br>4. deep # - 15 stars<br>5. modern-go-programming # - 10 stars<br>If you have any questions or need further details about any of<br>these repositories, feel free to ask!<br>f +<br>with <> Chante<br><!-- End of picture text -->

_Figure 7.2: AI-6 accessing GitHub via MCP_ 

This is a great idx_d662995dsuccess! The LLM was able to access GitHub via our MCP server, extract the necessary information, which requires authentication too, and distill a useful answer. 

But it took quite a few tries because the LLM kept requesting invalid `gh` CLI commands for pagination. Eventually, it just settled for requesting 300. This works in this case because I have just a little over 100 repos, but it is not a general solution. But, as you can see, it definitely used the GitHub MCP server (implemented from scratch in Bash): 

```
Invoking tool gh on server /Users/gigi/git/ai-six/py/backend/mcp_tools/
github_mcp_server.sh with args: {'args': 'repo list --sort=stars --limit=5'}
```

_Integrating with the Model Context Protocol Ecosystem_ 

249 

```
Tool gh completed successfully
2025-08-03 17:11:59 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
Invoking tool gh on server /Users/gigi/git/ai-six/py/backend/mcp_tools/
github_mcp_server.sh with args: {'args': 'repo list --json "name,stargazersCount"
--limit 100'}
Tool gh completed successfully
2025-08-03 17:12:00 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
Invoking tool gh on server /Users/gigi/git/ai-six/py/backend/mcp_tools/
github_mcp_server.sh with args: {'args': 'repo list --json name,stargazerCount --
limit 100'}
Tool gh completed successfully
2025-08-03 17:12:04 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
2025-08-03 17:14:02 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
2025-08-03 17:14:18 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
Invoking tool gh on server /Users/gigi/git/ai-six/py/backend/mcp_tools/
github_mcp_server.sh with args: {'args': 'repo list --json name,stargazerCount --
limit 100 --page 2'}
Tool gh completed successfully
2025-08-03 17:14:25 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
2025-08-03 17:15:12 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
Invoking tool gh on server /Users/gigi/git/ai-six/py/backend/mcp_tools/
github_mcp_server.sh with args: {'args': 'repo list --json name,stargazerCount --
limit 300'}
Tool gh completed successfully
2025-08-03 17:15:18 - HTTP Request: POST https://api.openai.com/v1/chat/
completions "HTTP/1.1 200 OK"
```

This incorrectidx_fa8e4fea and inefficient use of tools is one of the major problems of LLMs, and we will address this problem in _Chapter 10_ . 

_Chapter 7_ 

250 

###### **Summary** 

Let's recap. In this chapter, we explored the **Model Context Protocol** ( **MCP** ) – a cornerstone for standardizing tool and context integration in advanced agentic AI systems. We examined the ecosystem and motivations behind MCP, covering its architecture, benefits, and both its protocol layering and practical implementations. We showed how MCP server and client concepts map cleanly onto the AI-6 framework’s own tool abstractions, and how integrating MCP brings broad, frictionless interoperability: any compatible tool can be connected, reused, or swapped out, freeing you from vendor lock-in and custom integration overhead. 

We compared implementing command-line tools as both custom AI-6 tools and as MCP servers and saw that MCP makes it just as easy to build and share tools across languages and platforms. Note that testing MCP servers may require additional effort as the tools run in a separate process. You learned how localized and remote MCP servers can be discovered and consumed, with the AI-6 tool manager abstracting away the entire discovery and registration process. This approach lets AI-6 (and any similar agentic AI framework) seamlessly compose its internal tools and external MCP tools into a unified, dynamic toolset accessible to any agent, with zero extra logic required in the AI-6 engine. 

Finally, we looked at practical, real-world integration: how an agentic AI system, such as AI-6, now delegates all tool handling (discovery, invocation, and management) to a robust tool manager, making its agents vastly more extensible. As the MCP ecosystem grows, your agentic AI can instantly leverage any new tool, service, or resource published to the open protocol, enabling rapid experimentation and scaling in complex, multi-agent systems. Integration is as simple as configuration, not rewriting code. 

In the next chapter, we will take it to the next level and dive deep into the design of multiagent AI systems. 

_Integrating with the Model Context Protocol Ecosystem_ 

251 

###### **Get This Book’s PDF Version and Exclusive Extras** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
i<br>4<br>|<br>e<br>aeé<br>[=] :<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require an invoice._ 

## Part 3 

### Constructing Multi-Agent Systems 

_In Parts 1 and 2_ , you built the core foundations for agentic systems and constructed your own framework (AI-6). Part 3 takes you into multi-agent systems at full scale: designing agent teams, orchestration patterns, role prompts, tool scoping, and context strategies, then implementing real multi-agent workflows with idx_b4f45300the **Agent-to-Agent** ( **A2A** ) protocol. You’ll build a practical **multi-agent Kubernetes DevOps system** ( **MAKDO** ), learn how toidx_d38dbe1d test and debug agent coordination failures, and apply resilience patterns like redundancy, graceful degradation, and human escalation. The part then moves into production deployment, walking through a realistic multi-cluster setup with secure communication and service discovery. It concludes with advanced topics and future directions, including massive context windows, long-horizon planning, multimodal systems, and the broader implications of increasingly capable agents. 

This part contains the following chapter: 

- _Chapter 8, Designing Multi-Agent Systems_ 

- 

- _Chapter 9, Implementing Multi-Agent Systems with A2A_ 

- 

- _Chapter 10, Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

- 

- _Chapter 11, Deploying Multi-Agent Systems_ 

- 

- _Chapter 12, Advanced Topics and Future Directions_ 

- 

# 8 

##### Designing Multi-Agent Systems 

While single-agent systems can accomplish impressive tasks, many real-world problems require coordination between multiple specialized agents working together. This chapter focuses on designing multi-agent AI systems that can collaborate to solve complex problems beyond the capabilities of any single agent. 

Multi-agent systems represent the next frontier in agentic AI architecture. Instead of relying on one agent to handle all aspects of a problem, we can create teams of specialized agents, each with its own expertise, tools, and responsibilities. We’ll explore multi-agent orchestration patterns, agent decomposition strategies, system prompt design for different agent roles, tool assignment frameworks, context engineering for multi-agent environments, and conflict resolution mechanisms. We will enhance AI-6 with explicit agent support and integrate the **Agent-to-Agent** ( **A2A** ) protocolidx_553c1525 to demonstrate these concepts practically. 

The following key topics will be covered: 

- What is multi-agent orchestration and why does it matter? 

- 

- Introduction to the A2A protocol 

- 

- Designing collaborative agent workflows 

- 

- Conflict resolution and role assignment in multi-agent systems 

- 

_Chapter 8_ 

256 

###### **Technical requirements** 

To follow along, refer to the instructions in the README file: 

`https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-andA2A/blob/main/ch08/ai-six/py/README.md` . 

###### **What is multi-agent orchestration and why does it matter?** 

So far in the book, we have talked a lot idx_0267 **a** c0d bout the agentic tool-calling loop and emphasized that all the thinking is done by the LLM. The AI-6 engine is very capable of supporting such agentic workflows, but what are these agents? In this section, we will define exactly what an AI agent is in familiar terms, extend AI-6 to support explicit agents, discuss why multi-agent systems are important, and finally, explore different ways to orchestrate multiple agents effectively. 

###### **What is an AI agent?** 

An **AI agent** is a idx_30d0ed94component in an AI system that has some goals and knowledge encoded as a system prompt. It has access to a set of tools that it can use to achieve its goals. Finally, it has an LLM client that it can use to reason about the world, its goals, and how to use its tools. The AI agent interacts with the outside world by receiving user messages (where the user can be the host AI system or another agent) and returning responses. The agent maintains its own internal state (e.g., conversation history, tool usage history, etc.) and only returns the final response to the user. 

The fact that each agent is a self-contained component that hides its internal state means we can construct multi-agent systems without saturating the context window of a single LLM. The sub-agent may run its own agentic loop and burn through a lot of tokens without cluttering the context of the parent. If you think an AI agent sounds very similar to the AI-6 engine, you are not wrong. Let’s see how to extend AI-6 to support agents more explicitly. 

###### **Adding explicit agents to AI-6** 

The AI-6 engine can be used as is idx_4555caf5to construct multi-agent systems in the following manner: 

- Define an AI-6 agent tool. 

1. 

2. Create a parent AI-6 engine instance and provide it with the other AI-6 agents as tools. 

3. The parent AI-6 engine may invoke the other AI-6 agents as tools to delegate work. 

_Designing Multi-Agent Systems_ 

257 

This is fine, but there are some small gaps to address: 

- Currently, the AI-6 engine doesn’t have a system prompt. This means that whenever calling an AI-6 agent tool, the caller must provide the system prompt in addition to the actual user message. 

- Defining and configuring the different AI-6 agents is not trivial. 

- 

- AI-6 has a global configuration for tools, but agents should have their own subset of tools. 

Let’s address all of these issues by making the following changes to AI-6: 

1. Rename `Engine` to `Agent` (this is just terminology and not a functional change). 

- Add a system prompt to the agent configuration. 

2. 

3. Add `enabled_tools` and `disabled_tools` fields to the agent configuration. 

4. Add a idx_b78808eenew `AgentTool` that wraps an AI-6 `Agent` instance. 

Besides the renaming of `Engine` to `Agent` , which mostly establishes the terminology, the other changes are just additive. We don’t remove or modify any of the existing capabilities and workflows. 

###### **Renaming Engine to Agent** 

The idx_b853c051 entire `backend.engine` package is now named `backend.agent` . The `engine.py` file is now `agent.py` . The `Engine` class is now `Agent` . All references to `Engine` in the code and documentation have been changed to `Agent` . 

Nothing special here, just a find-and-replace. 

###### **Adding a system prompt to the Agent configuration** 

This change is pretty idx_fdeeff57simple too. Here is the new field added to the `Config` class in `backend/ agent/config.py` : 

```
system_prompt: Optional[str] = None
```

Note that it is optional, which means it is backward compatible and can work just like before and interact with LLMs without a specific goal or knowledge. 

_Chapter 8_ 

258 

###### **Adding enabled_tools and disabled_tools fields to the Agent configuration** 

This isidx_8a4fa732 also a simple change. Here are the idx_e9433f6cnew fields added to the `Config` class in `backend/ agent/config.py` : 

```
enabled_tools: Optional[List[str]] = None
disabled_tools: Optional[List[str]] = None
```

The semantics are that if `enabled_tools` is provided, only those tools will be available to the agent. If `disabled_tools` is provided, all tools except those tools will be available to the agent. If none are provided, all tools are available. It is an error to provide both fields. This is again backward compatible and provides complete control over the set of tools that any agent can use. 

###### **Adding a new AgentTool that wraps an AI-6 Agent instance** 

This is the most **i** dx_fd44b13d nteresting change. We add a new tool type that wraps an `Agent` instance. However, the `Agent` instance itself doesn’t have any new code for launching sub-agents. The LLM receives the list of available sub-agents as part of the available tools, and then the LLM may decide to launch one of the sub-agents with a tool call. Each such sub-agent may have the `Agent` tool in its own set of tools, which means when the LLM interacts with the sub-agent, it may decide to launch another sub-agent, and so on. This means we can have an arbitrary tree of agents running and collaborating to solve a problem. 

The `AgentTool` class is defined in `backend/object_model/agent_tool.py` . Let’s break it down. 

The import statements reflect the entities that this tool relies on and interacts with: 

```
from typing importCallable, Optional
from backend.object_model import Tool, Parameter
from backend.agent.agent import Agent
from backend.agent.config import Config
```

Now, the `AgentTool` class inherits from the `Tool` base class. The constructor takes an agent configuration object that has all the information needed to create an `Agent` instance. First, it creates the `Agent` instance and initializes the `_on_tool_call_func` callback to `None` . The agent will already be configured with its system prompt and the set of enabled/disabled tools: 

```
classAgentTool(Tool):
"""Tool that wraps an Agent and allows sending messages to it."""
```

_Designing Multi-Agent Systems_ 

259 

```
def__init__(self, agent_config: Config):
"""Initialize the AgentTool with a Config."""
self.agent = Agent(agent_config)
self._on_tool_call_func: Optional[
Callable[[str, dict, str], None]] = None
```

Then, it creates the parameters for the tool call. In this case, the tool takes a single parameter called `message` , which is the message to be set to the agent. Then, it calls the superclass (the `Tool` class) constructor and passes the name, description, parameters, and required fields ( `message` is required): 

```
# Create tool definition
parameters = [
    Parameter(
        name='message',
type='string',
        description='The message to send to the agent'
    )
]
super().__init__(
    name=f"agent_{agent_config.name}",
    description=f"Send a message to the {agent_config.name} agent.
{agent_config.description}",
    parameters=parameters,
    required={'message'}
)
```

The `set_tool_call_callback()` method is called by the agent during initialization to set a callback function that will be called whenever the sub-agent makes a tool call. This optional callback function comesidx_bc865eb9 from the host AI system. This allows the host AI system to intercept and handle tool calls made by any agent: 

```
defset_tool_call_callback(
self, callback: Optional[Callable[[str, dict, str], None]]
    ):
"""Set the callback function for tool calls made by this agent."""
self._on_tool_call_func = callback
```

_Chapter 8_ 

260 

Finally, the `run()` method sends the message to the agent, which may start its own agentic loop and eventually return a response: 

```
defrun(self, message: str, **kwargs) -> str:
"""
Send a message to the agent and return the response.
Args:
    message: The message to send to the agent
    **kwargs: Additional arguments (ignored)
Returns:
    The agent's response
"""
returnself.agent.send_message(
            message, self.agent.default_model_id,
            on_tool_call_func=self._on_tool_call_func)
```

At the end of the day, from the perspective of the AI-6 agentic loop, sub-agents are tools that can be invoked to delegate work. The LLM decides when and how to invoke sub-agents based on their description, just like it decides to call any other tool. The fact that `AgentTool` wraps an AI-6 Agent instance is irrelevant to the LLM. 

At this point, we understand how AI-6 enables multi-agent systems. Now is a good time to discuss why multi-agent systems are so important. 

###### **Why do we need multi-agent systems?** 

In theory, a single idx_dc19a3fdsufficiently capable agent could handle any task. However, as task complexity increases, this approach quickly runs into several limitations. 

###### **Context window limitations** 

LLMs have limited context windows and can only consider a certain amount of information at once. For complex tasks requiring extensive background knowledge, multiple steps, or large datasets, a single agent may not fit all of the necessary information into its context window. Model performance degrades when context grows too large, especially when filled with step details that are mostly irrelevant to subsequent steps. 

_Designing Multi-Agent Systems_ 

261 

###### **Specialization challenges** 

Different tasks require different expertise and skills. A single agent may not master all necessary skills, and uber-agents with huge system prompts confuse today’s models. Just as human organizations rely on specialists, AI systems benefit from specialized agents focusing deeply on their domain of expertise (See `https://www.moltbook.com` to realize how AI agents can imitate human interaction patterns and organize themselves accordingly). Complex tasks may require hundreds of tools, overwhelming single agents, and leading to poor tool selection or hallucination of capabilities. 

###### **Model selection constraints** 

Different tasks benefit from different models. Single agents tied to one model aren’t optimal for all task aspects. Some tasks require advanced reasoning from large models such as GPT-5, while others can be handled by smaller, faster models. Monolithic systems force you to either overpay for simple tasks or underperform on complex ones. 

Multi-agent systems address these limitations by creating specialized agents focusing on specific task aspects. Each agent has its own system prompt, tool set, and model, operating within its own context window while leveraging expertise and tools to contribute to the overall solution. 

###### **Cognitive load distribution** 

Multi-agent systems distribute cognitive load across specialized agents, mirroring human teams where complex problems are broken down and assigned to domain experts. Research shows that sequential multi-agent processing achieves significantly higher accuracy compared to single-agent approaches, with specialized agents maintaining focused attention on their domains. 

###### **Fault tolerance and resilience** 

Multi-agent systems offer inherent fault tolerance advantages by distributing responsibilities across multiple agents. These systems continue operating when individual components fail through recovery strategies such as retrying with different parameters or routing to alternative agents. Critical agents can be deployed with redundancy, allowing seamless failover when issues arise. 

_Chapter 8_ 

262 

###### **Testability and debugging** 

The modular nature idx_c5f7c14f enables targeted testing, better observability, and improved debugging. Each agent can be tested in isolation, similar to unit testing, while inter-agent communications provide exceptional observability. Granular performance profiling allows independent monitoring of each agent’s resource consumption, execution time, and token usage. 

###### **How to orchestrate multiple agents** 

Now that we understand what AI agents are and why multi-agent systems are beneficial, let’s explore the different strategies for orchestrating multiple agents to work together effectively. Agent orchestration refers to the coordination, communication, and management of multiple agents to achieve a common goal. The orchestration approach you choose significantly impacts the system’s performance, reliability, and complexity. 

###### **Sequential orchestration** 

Sequential idx_c5baf75forchestration is theidx_5db72386 simplest and most intuitive pattern, where agents work in a predefined order, with each agent passing its output to the next agent in the chain. This linear workflow resembles a traditional pipeline where each stage processes the output from the previous stage. The flow is predefined and predictable. But each agent can still have its own internal agentic loop and call tools as needed. 

Sequential orchestration is ideal for tasks that have a natural linear progression, such as content creation workflows (research, outline, draft, review, and publish), data processing pipelines, or any process where each step logically depends on the completion of the previous step. 

The orchestrator agent maintains a list of agents in order and iteratively calls each agent with the accumulated results from previous agents. Each agent’s output becomes part of the input for the next agent (see _Figure 8.1_ ): 

<!-- Start of picture text -->
Input > Agent1 * Agent2 > Agent3 > Output<br><!-- End of picture text -->

_Figure 8.1: Sequential orchestration_ 

_Designing Multi-Agent Systems_ 

263 

Here are the advantagesidx_64f09ba1 associated with sequential orchestration: 

   - Simple to understand and implement 

   - Predictable execution order 

   - 

   - Easy to debug and trace issues 

   - 

   - Natural fit for many real-world workflows 

- The following are the i **d** x_52addd51 isadvantages: 

   - Sequential bottleneck; that is, if one agent fails, the entire process stops 

   - 

   - No parallelization opportunities 

   - Can be slow for long chains 

   - 

   - Rigid structure that doesn’t adapt to changing requirements 

Whileidx_36b6d6bd sequential orchestration offers simplicity and predictability, its linear nature can become a bottleneck when speed and fault tolerance are priorities. This is where parallel orchestration shines, allowing multiple agents to work simultaneously and leverage the power of concurrent processing. 

###### **Parallel orchestration** 

Parallel orchestration involves idx_ddd87be6running multiple agents simultaneously on theidx_96b1bd85 same input or different aspects of a problem, then combining their results. This pattern maximizes throughput and can provide diverse perspectives on the same problem. Note the two styles of parallel orchestration: 

- Each agent works independently on the same input and produces its own output. The orchestrator then aggregates or synthesizes these outputs into a final result, possibly with an LLM judge to score and choose a winner. 

- The orchestrator decomposes the input into independent subtasks that can be run in parallel and assigns each subtask to a different agent. The agents work in parallel on their assigned subtasks, and the orchestrator combines their outputs. 

Parallel orchestration is effective for tasks where multiple independent analyses are needed, such as sentiment analysis from different perspectives, multi-source data gathering, competitive research, or when you want to validate results through consensus. 

_Chapter 8_ 

264 

The orchestrator dispatches the same or related tasks to multiple agents simultaneously, then collects and synthesizes their responses. This often requires sophisticated result aggregation logic (see _Figure 8.2_ ): 

<!-- Start of picture text -->
Input<br>€ | ¥<br>Agent 1 Agent 2 Agent 3<br>(MS | Ze<br>Aggregator<br>t<br>Output<br><!-- End of picture text -->

_Figure 8.2: Parallel orchestration_ 

Here are the idx_63 **a** 5d232 dvantages: 

- Maximizes throughput and speed 

- Provides multiple perspectives 

- Natural fault tolerance (if one agent fails, others continue) 

- Canidx_5ef1b354 implement consensus mechanisms for higher reliability 

The following are the i **d** x_db119ac9 isadvantages: 

- Requires result synthesis logic 

- Potential resource contention 

- May produce conflicting results that need resolution 

- 

- More complex error handling 

Parallel orchestration excels idx_d9cc2319at maximizing throughput, but managing multiple concurrent agents and synthesizing their results can become unwieldy as complexity grows. For idx_244f7cc6tasks that naturally break down into manageable subtasks with clear delegation paths, hierarchical orchestration provides the structure and clarity that parallel approaches may lack. 

_Designing Multi-Agent Systems_ 

265 

###### **Hierarchical orchestration** 

Hierarchical orchestration organizes idx_46c248c5agents in a tree-like structure where higher-levelidx_2faed30d agents coordinate and manage lower-level agents. This pattern mimics organizational structures where managers delegate tasks to specialists. 

This approach works well for complex tasks that naturally decompose into subtasks, such as project management, research coordination, or any scenario where you need different levels of abstraction and delegation. 

A coordinator agent at the top level breaks down complex tasks and delegates them to specialized agents. These specialist agents might further delegate to sub-specialists, creating a hierarchy of responsibility (see _Figure 8.3_ ): 

<!-- Start of picture text -->
Input<br>Coordinator Agent<br>SS aS<br>¢= | a<br>Specialist Agent 1 Specialist Agent 2<br>/\<br>+ia> ~\ ¥ |<br>Sub-Agent 1A Sub-Agent 1B Sub-Agent 2A Specialist Agent 3<br>QR ( ] 2<br>“Ss i a, =<br>SS ~ a a<br>~——s ——<br>Results Aggregation<br>Output<br><!-- End of picture text -->

_Figure 8.3: Hierarchical orchestration_ 

_Chapter 8_ 

266 

The following idx_395b **a** 7c8 re its advantages: 

   - Natural task decomposition 

   - Clear responsibility boundaries 

   - Scalable architecture 

- Matches human organizational patterns 

- Here are the idx_57225d85 disadvantages: 

   - Communication overhead between levels 

   - Potential single points of failure at higher levels 

   - Complexity in task decomposition logic 

   - May introduce delays due to coordination overhead 

Hierarchical orchestration works idx_c2f3b272well for problems with clear decomposition, but it relies on predetermined task breakdowns and can struggle with dynamic, rapidly changing environments. When your system needs to react to unpredictable events and changing conditions in real time, event-driven orchestration offers the responsiveness that hierarchical approaches cannot match. 

###### **Event-driven orchestration** 

Event-driven orchestration allows idx_0dbf3b54agents to react to events or state changes **i** dx_65b9f509 n the system, creating more dynamic and responsive workflows. Agents subscribe to events and trigger actions based on specific conditions or triggers. 

This pattern is ideal for reactive systems, monitoring scenarios, real-time processing, or any situation where agents need to respond to changing conditions rather than follow predetermined workflows. 

Agents register their interest in specific events or conditions. When these events occur, the relevant agents are notified and can take appropriate action. 

_Designing Multi-Agent Systems_ 

267 

This requires an event system or message queue infrastructure: 

<!-- Start of picture text -->
Event Source<br>ke<br>4 ki<br>+<br>Event Bus/Queue<br>event triggers-ribes / "event triggers:ribes<br>a - may generate event triggers subscribes | may generate = —_ may generate<br>4 \. ™.<br>Agent 1 Agent 2 Agent 3<br>( {\<br>\Ne \. a<br>Action/Tool Use Action/Tool Use Action/Tool Use<br><!-- End of picture text -->

_Figure 8.4: Event-driven orchestration_ 

Here are the idx_d90b662e advantages: 

   - Highly responsive to changing conditions 

   - Decoupled agent interactions 

   - Natural support for asynchronous processing 

- Scales well with system complexity 

- Here are the i **d** x_db6a780c isadvantages: 

   - Complex debugging due to the asynchronous nature 

   - Requires robust event infrastructure 

   - Potential race conditions 

   - Harder to predict execution flow 

Event-driven orchestration provides excellent idx_1f051ef6responsiveness to changing conditions, but its reactive nature means agents still work within predefined roles and responses. For truly complex, open-ended problems where the solution approach itself must emerge from agent interactions, collaborative orchestration allows agents to transcend their individual limitations through dynamic negotiation and collective problem-solving. 

_Chapter 8_ 

268 

###### **Collaborative orchestration** 

Collaborativeidx_4aa0c299 orchestration enables idx_c6030 **a** e5 gents to dynamically negotiate, communicate, and coordinate with each other to solve problems collectively. This pattern allows for emergent behaviors and adaptive problem-solving approaches. 

Use collaborative orchestration for complex, open-ended problems where the solution approach isn’t predetermined, such as creative projects, complex research tasks, or scenarios requiring negotiation and consensus-building. 

Agents idx_b11f27 **c** f an initiate communication with each other, propose solutions, negotiate idx_704 **a** a2ee pproaches, and dynamically form working groups. This requires sophisticated communication protocols and coordination mechanisms. 

<!-- Start of picture text -->
Dynamic Communication<br>Proposal * — Counter-Proposal > Consensus Input/Problem<br>Agent1<br>negotiate/communicate<br>Agent 2 negotiate/communicate<br>negotiate/communicate,<br>Agent3<br>Collaborative Solution<br>Output<br><!-- End of picture text -->

_Figure 8.5: Collaborative orchestration_ 

_Designing Multi-Agent Systems_ 

269 

Here are the idx_4cecc26e advantages: 

   - Highly adaptive and flexible 

   - 

   - Can handle unexpected situations 

   - 

   - Leverages collective intelligence 

   - 

- Allows for emergent solutions 

- Here are the idx_9213a8a0 disadvantages: 

   - Complex to implement and debug 

   - Potential for infinite loops or deadlocks 

   - 

   - Difficult to predict outcomes 

   - 

   - Requires sophisticated coordination protocols 

   - 

While idx_5ae0b6a1collaborative orchestration offers the ultimate flexibility and adaptability, its complexity can be overwhelming for many practical applications. The reality is that most successful multiagent systems don’t rely on a single orchestration pattern but instead combine the strengths of multiple approaches to create robust, efficient solutions tailored to their specific requirements. 

###### **Hybrid orchestration** 

Real-world systems often idx_0cff794dbenefit from combining multiple orchestration patterns. For idx_5042 **e** 959 xample, you might use sequential orchestration for the main workflow while employing parallel orchestration for specific validation steps, or implement hierarchical coordination with event-driven responses to handle exceptions: 

_Chapter 8_ 

270 

<!-- Start of picture text -->
Exception Handling<br>Error Event * Recovery Agent *  Retry/Altemative Input<br>Sequential Phase<br>Agent 1<br>Parallel ase<br>rs + +<br>Agent 24 Agent 28 Agent 2¢<br>Validation Aggregator<br>Event-Driven Phase<br>Monitor Agent<br>triggers<br>Response Agent<br>output<br><!-- End of picture text -->

_Figure 8.6: Hybrid orchestration_ 

We have covered various orchestration strategies. Let’s see how to decide which strategy is best for a specific situation. 

###### **Design considerations** 

When choosing an idx_781e2184orchestration strategy, consider these key factors: 

- **Task complexity** : Simple, linear tasks favor sequential orchestration, while complex, multi-faceted problems may require hierarchical or collaborative approaches 

_Designing Multi-Agent Systems_ 

271 

- **Performance requirements** : If speed is critical, parallel orchestration can help, but if consistency is more important, sequential processing might be better 

- **Resource constraints** : Consider the computational and memory overhead of each approach, especially for parallel and hierarchical patterns 

- **Fault tolerance needs** : Event-driven and parallel patterns generally offer better fault tolerance than sequential approaches 

- **Debugging and maintenance** : Sequential orchestration is easiest to debug, while collaborative orchestration is the most challenging 

The key to successful multi-agent orchestration is matching the orchestration pattern to your specific use case requirements and being prepared to adapt as those requirements evolve. Of course, you should take into account the disadvantages of each approach and how they accumulate and mitigate them as much as possible. For example, in sequential orchestration, you can add retry mechanisms and timeouts to avoid bottlenecks. In parallel orchestration, you can add a judge agent to resolve conflicts. In hierarchical orchestration, you can add redundancy to critical agents. In event-driven orchestration, you can add logging and tracing to improve observability. In collaborative orchestration, you can add limits to the number of interactions between agents to avoid infinite loops. 

Now that we have a good understanding of multi-agent orchestration patterns, let’s explore how agents can communicate with each other effectively using the A2A protocol. 

###### **Introduction to the A2A protocol** 

While orchestration patterns define the high-level coordination strategies between agents, effective multi-agent systems require robust communication mechanisms that allow agents to exchange information, coordinate activities, and collaborate seamlessly. The A2A protocol ( `https://a2a-protocol.org/latest/` ) provides idx_b42f9 **a** 2f standardized framework for AI agents to communicate and collaborate across different systems, offering capabilities that go beyond what MCP was designed for. 

The A2A protocolidx_1d31bf4f is built around several core actors and concepts that enable sophisticated agent interactions. At its foundation are three key actors: the **user** who initiates idx_86659cfarequests (a human or an AI agent), the **A2A client** (client agent) that communicates on behalf of the user, and idx_ba4a74b8the **A2A server** (remote agent) that processes messages and tasks and returns results. This creates a structured yet flexible communication model that supports both simple interactions and complex, multi-turn collaborations. 

_Chapter 8_ 

272 

###### **Core components of the A2A protocol** 

The A2A protocol **i** dx_5a0988be s built around several fundamental elements that work together to enable sophisticated agent interactions: 

- **Agent card** : JSONidx_88f5cbc9 metadata that describes an agent’s capabilities, allowing for automatic discovery and capability matching 

- **Task** : A statefulidx_3b27dec2 work unit with a unique identifier that enables tracking of longrunning operations and multi-turn interactions 

- **Message** : Individual idx_3af5da9acommunication turns between the client and agent, supporting rich content exchange 

- **Part** : Content idx_7382a **c** 2b ontainers that can hold different types of data (text, file, or data), enabling modality-independent communication 

- **Artifact** : Tangible outputsidx_f5fc22ba generated during task execution, such as PDF files or images, providing concrete deliverables from agent interactions 

Here is the agent card of the k8s-ai A2A server I have running locally: 

```
% http -b GET http://localhost:9999/.well-known/agent-card.json
{
    "capabilities": {
        "streaming": true
    },
    "defaultInputModes": [
        "text/plain"
    ],
    "defaultOutputModes": [
        "text/plain"
    ],
    "description": "Kubernetes AI assistant with kubectl access for context: kind-
k8s-ai",
    "name": "k8s-ai Agent",
    "preferredTransport": "JSONRPC",
    "protocolVersion": "0.3.0",
    "security": [
        {
            "BearerAuth": []
        }
    ],
    "securitySchemes": {
        "BearerAuth": {
```

_Designing Multi-Agent Systems_ 

273 

```
            "scheme": "bearer",
            "type": "http"
        }
    },
    "skills": [
        {
            "description": "Execute kubectl commands and provide Kubernetes
cluster insights, troubleshooting, and management",
            "examples": [
                "show me all pods",
                "what is the status of the cluster?",
                "describe the nginx deployment",
                "get service endpoints",
                "check node health",
                "troubleshoot pending pods"
            ],
            "id": "kubectl_operations",
            "name": "Kubernetes Operations",
            "tags": [
                "kubernetes",
                "kubectl",
                "cluster",
                "pods",
                "deployments",
                "services"
            ]
        }
    ],
    "supportsAuthenticatedExtendedCard": true,
    "url": "http://127.0.0.1:9999/",
    "version": "1.0.0"
}
```

Now that we understand the core components of the A2A protocol, let’s discuss its communication mechanisms. 

_Chapter 8_ 

274 

###### **A2A communication mechanisms** 

The A2A protocol supports multiple interactionidx_1e3f917f patterns to accommodate different use cases: 

- **Request/response (polling)** : Traditional synchronous communication for simple interactions involving messages 

- **Streaming with SSE** : Real-time communication for ongoing tasks and live updates 

- **Push notifications** : Asynchronous notifications for event-driven workflows 

Built on HTTP(S) for transport and using JSON-RPC 2.0 payload format, A2A provides a familiar yet powerful foundation for agent communication. Unlike traditional protocols, A2A is specifically designed for autonomous agents that need to maintain stateful, trackable interactions across potentially long-running collaborative processes. 

###### **Adding A2A support to AI-6** 

At the moment, AI-6 has A2A idx_5ba8af3csupport in the form of an A2A tool that can be used to call remote agents that implement the A2A protocol. It is conceptually similar to the `MCPTool` and `AgentTool` classes in the sense that it encapsulates complex interactions with another system behind a simple tool interface. 

###### **Integrating A2A client capabilities into AI-6** 

The A2A integration in AI-6 follows aidx_a18cd218 layered architecture that provides both synchronous tool-based access and asynchronous message-passing capabilities. The integration consists of four main components that work together to enable seamless agent-to-agent communication. We are not going to cover them in detail, as they are quite complex, but we will provide an overview of each component and how it fits into the overall architecture. You can follow the links to the source code for more details. 

The A2A client ( `https://github.com/PacktPublishing/Design-Multi-Agent-AI-SystemsUsing-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/a2a_client/a2a_client.py` ) serves as the foundational component that handles direct communication with remote A2A agents. It manages A2A agent discovery by fetching agent cards, establishes authenticated connections, and provides streaming message capabilities for real-time communication. 

_Designing Multi-Agent Systems_ 

275 

The A2A manager ( `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/a2a_client/ a2a_manager.py` ) acts as a singleton coordinator that manages the life cycle of all A2A infrastructure. It handles initialization, maintains client registries, coordinates with the message pump for async operations, and ensures proper resource cleanup. This centralized approach prevents resource leaks and provides consistent state management across the system. 

The A2A message pump ( `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/a2a_client/ a2a_message_pump.py` ) operates in the background to handle long-running conversations and task management. It maintains a persistent state, tracks active tasks, and provides the async infrastructure needed for streaming responses while integrating with AI-6’s message injection system. 

The A2A executor ( `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/a2a_client/ a2a_executor.py` ) provides a clean abstraction layer that handles the complexity of bridging synchronous tool execution with asynchronous A2A operations. It encapsulates the logic for detecting running event loops, managing thread-safe execution, and providing a simple synchronous interface for A2A skill execution. 

Finally, the configuration integration ( `https://github.com/PacktPublishing/DesignMulti-Agent-AI-Systems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/agent/ config.py` ) ensures that A2A servers are configured alongside other tools in the agent configuration, allowing for declarative setup of remote agent connectionsidx_b9f25466 through declarative configuration files. 

This architecture enables AI-6 agents to seamlessly interact with remote A2A agents while maintaining the familiar tool-based interface, effectively bridging synchronous tool execution with asynchronous agent communication patterns. 

_Chapter 8_ 

276 

The following diagram illustrates the A2A communication flow within AI-6: 

_Figure 8.7: An overview of the A2A communication flow_ 

We will not get into the details of each component, as they are quite complex and require a deep understanding of the A2A protocol and async programming in Python. However, we will focus on the most important part of using A2A in AI-6, which is the `A2ATool` class. 

_Designing Multi-Agent Systems_ 

277 

###### **The A2ATool class** 

`A2ATool` ( `https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-UsingMCP-and-A2A/blob/main/ch08/ai-six/py/backend/tools/base/a2a_tool.py` ) inherits from the `Tool` base class and provides a clean, simpleidx_49a679f7 interface to A2A agents. The import statements reflect the entities the tool relies on and interacts with. The `AgentSkill` class contains the name and description of the skill, which are used to create the tool definition. The `Tool` and `Parameter` classes from the AI-6 object model are used to define the tool interface. `A2AManager` provides access to the executor that handles all the complex A2A coordination: 

```
from a2a.types import AgentSkill
from backend.object_model.tool import Tool, Parameter
from backend.a2a_client.a2a_manager import A2AManager
```

The constructor takes a `server_name` string and an `AgentSkill` object. Each A2A server can have multiple skills. The AI-6 A2A support creates a separate tool for each skill in each server: 

```
classA2ATool(Tool):
"""Tool that communicates with A2A (Agent-to-Agent) servers using async-to-
sync pattern."""
def__init__(self, server_name: str, skill: AgentSkill):
"""Initialize from A2A skill information.
Args:
server_name: Name of the A2A server
            skill: Skill object from agent card
        """
```

A2A skills don’t takeidx_7f48c5e2 structured arguments. The input to a skill is a natural language message. The output is also a natural language message, but A2A servers may also create artifacts. However, you may want to interact with multiple A2A tasks by invoking the same skill, so the tool defines two standard parameters— `message` for the input text and `task_id` for the optional existing task ID: 

```
self.server_config = server_config
self.skill_name = skill.name
# A2A skills are conversational - create standard parameters
        parameters = [
```

_Chapter 8_ 

278 

```
            Parameter(
                name='message',
type='string',
                description=f'Natural language request for the `{skill.name}`
skill'
            ),
            Parameter(
                name='task_id',
type='string',
                description='Optional: ID of existing task to send message to'
            )
        ]
        required = {'message'}  # message parameter is required, task_id is
optional
super().__init__(
            name=f"{server_name}_{skill.name}",
            description=skill.description,
            parameters=parameters,
            required=required
        )
self.server_name = server_name
self.skill_name = skill.name
```

The `run()` method isidx_d9bafe40 extremely simple thanks to the `A2AExecutor` abstraction. All the complex async-to-sync bridging logic is handled by the executor: 

```
defrun(self, **kwargs) -> str:
"""Execute the A2A skill using the A2AExecutor."""
        task_id = kwargs.get('task_id')
        message = kwargs.get('message', '')
        executor = A2AManager.get_executor()
ifnot executor:
return"Error: A2A not initialized. Please configure A2A integration."
```

_Designing Multi-Agent Systems_ 

279 

```
return executor.execute_skill(
self.server_name,
self.skill_name,
            message,
            task_id
        )
```

This clean separation of concerns makes `A2ATool` easy to understand, test, and maintain while keeping all the complex async coordination logic centralized in the `A2AExecutor` component. 

###### **Configuration and setup** 

Setting up A2A integration inidx_8edc5086 AI-6 requires minimal configuration. A2A servers are defined in the agent configuration alongside other tools: 

```
# config.yaml
a2a_servers:
  - name: "k8s-ai"
    url: "http://localhost:9999"
    timeout: 30.0
```

The tool manager ( `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/agent/ tool_manager.py#L380-L410` ) automatically discovers A2A agents at startup, fetching their agent cards and creating `A2ATool` instances for each skill. No manual tool registration is required. 

_Chapter 8_ 

280 

###### **A2A tool discovery flow** 

The following sequence shows how idx_bce9b10cA2A servers become available tools in AI-6: 

<!-- Start of picture text -->
‘Tool Manager 2AManager ‘A2ACtient ADAServer A2sToot<br>ensure client(server_contig)<br>create AZACHient<br>‘Get sklls(server_name)<br>GET /.well-known/agent-card, json<br>Rsebenee<br>agent card with skills<br><<br>Uist of Agentskil objects<br>loop {or each skit)<br>new A2ATool(server_name, skil)<br>tool instance<br>tools ready for agent<br>“<br>‘Tool Manager ‘A2A Manager ‘A2AClient. ‘A2AServer A2kToot<br><!-- End of picture text -->

_Figure 8.8: An overview of the A2A tool discovery flow_ 

This discovery flow happens idx_06d2458dautomatically during AI-6 idx_f06efdb7agent initialization. The **Tool Manager** reads the A2A server configuration, ensures each client exists throughidx_6006c630 the **A2A Manager** , and then fetches the agent card from each remote server. The agent card’s `skills` array is processed to create individual **A2ATool** instances, that is, one per skill per server. For the k8s-ai server shown previously, this creates a single tool named `k8s-ai_kubectl_operations` that AI-6 agents can invoke to interact with Kubernetes through natural language requests. 

Once discovered, A2A skills become regular AI-6 tools that agents can invoke through their standard tool-calling mechanism, seamlessly bridging local and remote agent capabilities. Now that we have covered the A2A protocol in depth, let’s change gears and discuss how to design collaborative agent workflows. 

_Designing Multi-Agent Systems_ 

281 

###### **Designing collaborative agent workflows** 

Earlier in the chapter, we discussed different agent orchestration paradigms. Now, let’s explore how to design effective workflows for multi-agent systems. Designing collaborative agent workflows involves decomposing complex tasks into manageable subtasks, assigning appropriate roles to each agent, and establishing clear communication protocols. Let’s start with answering the most basic question: How do you divide a complex task into a pipeline of multiple agents? 

###### **Agent decomposition strategies** 

One of the most critical decisions in idx_5f4caed6multi-agent system design is how to decompose complex tasks into manageable agent roles. Effective decomposition requires identifying natural boundaries where different types of expertise, tools, or responsibilities can be cleanly separated. Here are the key strategies and practical examples. 

###### **Decomposition by domain expertise** 

The most intuitive approach is toidx_0dee23ac divide agents based on specialized knowledge domains, similar to how human teams organize around expertise areas. 

Here is an example of a software development pipeline: 

<!-- Start of picture text -->
Requirements Development Testing<br>agent agent agent<br>System prompt: System prompt: System prompt:<br>Analyze user needs and Write clean, well- Create comprehensive<br>create detailed documented code that test suites and validate<br>specifications and follows best practices and quality, performance, and<br>functional requirements architectural standards for security of the<br>based on input and context. the given task. implemented solutions.<br>Tools: Tools: Tools:<br>» Web search * Code editor + Test frameworks<br>» Document creator * Git operations * Code analyzer<br>* Userinterviewer » Package managers * CI/CD tools<br><!-- End of picture text -->

_Figure 8.9: Software development pipeline_ 

_Chapter 8_ 

282 

The workflow divides the software development pipeline into three specialized AI agents— requirements, development, and testing—each with tailored system prompts and tools. The requirements agent analyzes user needs and generates specs, passing them to the development agent for clean code implementation, which then flows to the testing agent for validation via idx_8e1b6a17comprehensive suites. This modular chain mimics human expertise silos for efficient, domainfocused automation. 

###### **Decomposition by workflow stage** 

Organize agents around sequential stagesidx_6f900f05 of a process, where each agent handles a specific phase of the overall workflow. 

Here is an example of a content creation pipeline: 

<!-- Start of picture text -->
| Research | > Planning |») writing | Editing Publishing<br>agent agent => agent agent agent<br>Tools: Tools: Tools: Tools: Tools:<br>* Search * Outline * Editor + Grammar + CMS<br>* Archive *Mindmap —* Voice + Style * Social<br>* Analysis * Planner + Images + Fact check + Metrics.<br><!-- End of picture text -->

_Figure 8.10: Content creation pipeline_ 

This content creation pipeline uses five specialized AI agents in sequence: **Research** gathers data, **Planning** structures outlines, **Writing** generates drafts, **Editing** refines for quality, and **Publishing** deploys with analytics. Each agent leverages domain-specific tools to hand off refined outputs, automating end-to-end production like a human editorial team. The modular design ensures focused expertise at every stage. 

###### **Decomposition by capability pattern** 

Structure agents around fundamental idx_1 **c** 5f98e6 apabilities rather than domain knowledge, creating more reusable and flexible architectures. These may seem more like tools than full-fledged agents, but each one of these capabilities has enough nuance and complexity to warrant a dedicated agent. 

_Designing Multi-Agent Systems_ 

283 

Here is an example of a data analysis system: 

<!-- Start of picture text -->
Collector agent Processor agent Visualizer agent<br>Capability: Capability: Capability:<br>Data ingestion from Transform + clean Present insights in<br>any source : any data format any format<br>Can handle: Can handle: ; Can handle:<br>° APIs « Filtering ° Charts<br>Files * Aggregation * Reports<br>* Databases * Calculations * Dashboards<br>* Streams * Validation * Alerts<br><!-- End of picture text -->

_Figure 8.11: A data analysis system_ 

The **Collector agent** ingests i **d** x_0d6b6636 ata from diverse sources, the **Processor agent** transforms andidx_7d78fc72 cleans it, and the **Visualizer agent** generates outputs such as charts or alerts (see _Figure 8.11_ ). By focusing onidx_71f521ba fundamental functions rather than domains, the pipeline handles varied workloads flexibly without specialized retraining. Each agent chains outputs sequentially for end-to-end automation. 

These decomposition idx_047a09f4strategies align with the orchestration patterns discussed earlier in the chapter: sequential orchestration works well with workflow stage decomposition, hierarchical orchestration naturally supports domain expertise separation, and parallel orchestration enables validation and consensus patterns. 

###### **Decomposition decision framework** 

When i **d** x_cea0b8a9 eciding how to split a complex task, consider these questions: 

- **Natural boundaries** : Where does the task naturally break into distinct phases or domains? 

- **Tool clustering** : Which tools naturally group together for specific subtasks? 

- 

- **Context requirements** : What different types of context or expertise are needed? 

- **Parallelization opportunities** : Which subtasks can run concurrently? 

- 

- **Error isolation** : Where do you want to contain failures to prevent cascade effects? 

- 

_Chapter 8_ 

284 

Here is another example of a decision process for a market research report: 

<!-- Start of picture text -->
Question 1- Natural Boundaries Question 2 - Tool Clustering Question 3 - Context<br>Generate a comprehensive Requirements<br>market research report * Collection Agent: * Collection Agent: Market<br>* Data Collect web_search, survey_tools, knowledge, search<br>Data Collection social_media_apis strategies<br>web research, surveys,<br>competitor analysis Analysis Agent: * Analysis Agent: Statistical<br>5 (Date Analysts data_processor, expertise, pattern<br>trends, eit statistical_tools, recognition<br>iS<br>insightsstatistics, Talmedele<br>a * Writing Agent: * Writing Agent:<br>* Reportstructure,Writingnarrative,—— document_editor,grammar_checker, Communicationreport structure skills,<br>recommendations citation_manager<br>Presentation Creation © Design Agent: * Design Agent: Visual<br>visualizations, chart_creator, design, presentation best<br>executive summary presentation_software, practices<br>image_tools<br>| Result: 4-agent pipeline with clear handoffs and specialized expertise |<br><!-- End of picture text -->

_Figure 8.12: Creating a market research report_ 

This shows how a single complex task for creating a market research report is decomposed into four specialized agents by asking three design questions about natural task boundaries, tool groupings, and required context. Each question refines the roles of the collection, analysis, writing, and design agents, clarifying what they do, which tools they use, and what expertise they need. The idx_1fae1b18result is a four-agent pipeline with clear handoffs and minimal overlap, making the system easier to scale and reuse. 

Now that we have covered how to divide and conquer complex tasks using multiple agents, let’s turn our attention to the system prompt design for each agent. 

###### **System prompt design patterns** 

Effective system prompts are crucial for multi-agent systems because they define each agent’s personality, expertise, constraints, and collaboration patterns. We will look at some proven templates and patterns for i **d** x_51191c97 ifferent agent types. 

Let’s start with the specialist agent. 

_Designing Multi-Agent Systems_ 

285 

###### **The specialist agent template** 

Here is a general template for creating specialist idx_6594e7f0agents with clear roles and responsibilities. Note that the tools are not specified here, as they will be provided separately when invoking idx_3137ed88the agent: 

```
You are a [DOMAIN] specialist agent in a multi-agent system.
```

###### `EXPERTISE:` 

- `Your primary domain is [SPECIFIC_EXPERTISE]` 

- `You excel at [KEY_CAPABILITIES]` 

- `You have deep knowledge of [KNOWLEDGE_AREAS]` 

###### `RESPONSIBILITIES:` 

- `[PRIMARY_RESPONSIBILITY_1]` 

- `[PRIMARY_RESPONSIBILITY_2]` 

- `[PRIMARY_RESPONSIBILITY_3]` 

###### `COMMUNICATION STYLE:` 

- `Be precise and technical when discussing [DOMAIN] topics` 

- `Always explain your reasoning and cite sources when possible` 

- `Ask clarifying questions if requirements are ambiguous` 

- `Collaborate respectfully with other agents` 

###### `CONSTRAINTS:` 

- `Only work within your area of expertise` 

- `Escalate out-of-scope requests to appropriate agents` 

- `Always validate inputs before processing` 

- `Maintain focus on [SPECIFIC_FOCUS_AREA]` 

```
When collaborating with other agents, provide clear, structured output that can be
easily consumed by the next agent in the workflow.
```

Let’s look at an example of a data analysis specialist: 

```
You are a Data Analysis specialist agent in a multi-agent system.
```

###### `EXPERTISE:` 

- `Your primary domain is quantitative data analysis and statistical modeling` 

- `You excel at finding patterns, trends, and insights in complex datasets` 

- `You have deep knowledge of statistics, machine learning, and data visualization` 

_Chapter 8_ 

286 

###### `RESPONSIBILITIES:` 

- `Process and clean raw data from various sources - Perform statistical analysis and identify significant patterns` 

- `Create data models and predictive analyses` 

- `Generate actionable insights and recommendations` 

###### `COMMUNICATION STYLE:` 

- `Be precise and cite statistical significance when making claims` 

- `Always explain your methodology and assumptions` 

- `Ask for clarification on analysis objectives and success metrics - Present findings with appropriate confidence intervals` 

```
CONSTRAINTS:
```

- `Only analyze data that has been properly validated` 

- `Escalate data quality issues to the Data Collection agent` 

- `Focus on statistical rigor over speed` 

- `Maintain objectivity and avoid confirmation bias` 

```
When collaborating with other agents, provide structured analysis reports with
clear methodology, findings, and recommendations that can be easily interpreted by
non-technical agents.
```

The idx_cfd000f7 specialist agents are the experts. But someone (an agent) needs idx_575acbb4to coordinate all the experts, and that requires a different prompt. 

###### **The coordinator agent template** 

The idx_e3811b8ecoordinator agent promptidx_775cc5fe focuses on coordination and orchestration concerns, such as the overall decision-making process, delegation principles, and conflict resolution. It also includes the list of agents that require coordination: 

```
You are a Coordinator agent responsible for orchestrating a multi-agent workflow.
```

###### `ROLE:` 

- `Decompose complex requests into subtasks for specialist agents` 

- `Coordinate communication and handoffs between agents` 

- `Synthesize results from multiple agents into coherent outputs` 

- `Monitor progress and handle exceptions` 

- `DECISION-MAKING PROCESS: 1. Analyze the incoming request for scope and requirements` 

_Designing Multi-Agent Systems_ 

287 

`2. Identify which specialist agents are needed` 

`3. Create a workflow plan with clear handoffs` 

`4. Monitor execution and adjust as needed` 

`5. Integrate specialist outputs into final deliverable` 

###### `DELEGATION PRINCIPLES:` 

- `Match tasks to agent expertise and available tools` 

- `Provide clear, specific instructions to each agent` 

- `Define success criteria and quality standards` 

- `Set appropriate timeouts and escalation paths` 

```
CONFLICT RESOLUTION:
```

- `When agents provide contradictory information, gather additional context` 

- `Escalate unresolvable conflicts to human oversight` 

- `Make decisions based on agent confidence levels and expertise match` 

- `Document resolution rationale for future reference` 

###### `QUALITY ASSURANCE:` 

- `Validate that each subtask has been completed satisfactorily` 

- `Ensure consistency across agent outputs` 

- `Perform final integration and formatting` 

- `Conduct overall quality review before delivery` 

```
AVAILABLE AGENTS:
```

```
[LIST_OF_SPECIALIST_AGENTS_AND_CAPABILITIES]
```

```
Always maintain visibility into the overall workflow progress and be prepared to
adapt the plan if circumstances change.
```

Here is anidx_41a86f77 example of a coordinator agent managing a security analyst idx_7c6190eeagent (specialist) and a test runner agent (validator) to generate a high-quality report: 

```
 You are a Coordinator agent responsible for orchestrating a multi-agent workflow
for code review and security fixes.
ROLE:
```

- `•Decompose complex code review requests into subtasks for specialist agents` 

```
•Coordinate communication and handoffs between agents
•Synthesize results from multiple agents into coherent outputs
```

- `•Monitor progress and handle exceptions` 

```
DECISION-MAKING PROCESS:
```

```
1.Analyze the incoming code review request for scope and requirements
```

_Chapter 8_ 

288 

```
2.Identify which specialist agents are needed (Security Expert Agent, Validator
Agent)
3.Create a workflow plan: Security Expert → Validator → Integration
4.Monitor execution and adjust as needed
5.Integrate specialist outputs into final deliverable
DELEGATION PRINCIPLES:
•Match tasks to agent expertise: Security Expert for vulnerability analysis/fixes,
Validator for testing/validation
•Provide clear, specific instructions to each agent with code snippets and
criteria
•Define success criteria: fixes must pass all tests, no new vulnerabilities
introduced
•Set appropriate timeouts and escalation paths
CONFLICT RESOLUTION:
•When agents provide contradictory fixes/results, gather additional context or re-
run analysis
•Escalate unresolvable conflicts to human oversight
•Make decisions based on agent confidence levels and test coverage
•Document resolution rationale for future reference
QUALITY ASSURANCE:
•Validate that security analysis is comprehensive and fixes are implemented
•Ensure tests cover 100% of identified issues with no regressions
•Perform final integration and formatting into a review report
•Conduct overall quality review before delivery
AVAILABLE AGENTS:
•Security Expert Agent: Analyzes code for vulnerabilities (SQL injection, XSS,
etc.), suggests secure fixes, provides reasoning with OWASP references
•Validator Agent: Runs unit/integration tests, validates fixes, confirms no
performance/security regressions, generates test reports
```

In the idx_5e35ceccquality assurance section, the guidance is to validate eachidx_d9434ab6 subtask. This is done using yet another agent. Let’s look at that validator agent’s template. 

###### **The validator agent template** 

The strength idx_6f **a** 42627 nd reliability idx_33a4860aof agentic AI systems come from strong guardrails. A dedicated validator agent that can be invoked as part of a workflow can substantially improve the outcome. Here is a solid prompt for such an agent: 

```
You are a Validator agent focused on quality assurance and verification.
```

```
PURPOSE:
```

_Designing Multi-Agent Systems_ 

289 

- `Review outputs from other agents for accuracy and completeness` 

- `Verify that requirements have been met` 

- `Identify potential issues or improvements` 

- `Ensure consistency with project standards` 

###### `VALIDATION CRITERIA:` 

- `Accuracy: Are facts correct and sources reliable?` 

- `Completeness: Have all requirements been addressed?` 

- `Quality: Does the output meet professional standards?` 

- `Consistency: Is the output coherent and well-structured?` 

###### `REVIEW PROCESS:` 

`1. Compare output against original requirements` 

`2. Fact-check claims and verify sources` 

`3. Assess quality and professional standards` 

`4. Check for logical consistency and flow` 

`5. Provide specific, actionable feedback` 

###### `FEEDBACK FRAMEWORK:` 

- `APPROVED: Output meets all criteria and standards` 

- `CONDITIONAL: Minor issues that can be addressed with specific changes` 

- `REJECTED: Significant problems requiring substantial rework` 

###### `When providing feedback, always:` 

- `Be specific about what needs improvement` 

- `Suggest concrete solutions when possible` 

- `Acknowledge what was done well` 

- `Maintain professional and constructive tone` 

###### `ESCALATION CRITERIA:` 

- `Fundamental disagreement with the producing agent` 

- `Repeated quality issues from the same agent` 

- `Requirements that cannot be validated with available information` 

- `Critical errors that could impact system integrity` 

Here is an idx_65c1 **e** a4b xample of a validator idx_e88cc742agent for code quality and security: 

```
You are a Validator agent focused on quality assurance and verification for code
reviews and security fixes.
PURPOSE:
```

- `Review outputs from other agents for accuracy and completeness` 

_Chapter 8_ 

290 

|`- Verify that security fixes meet coding standards and eliminate vulnerabilities`<br>`- Identify potential issues, regressions, or improvements in fixed code`<br>`- Ensure consistency with security best practices and project standards`<br>`VALIDATION CRITERIA:`|
|---|
|`- Accuracy: Do fixes correctly address identified vulnerabilities (e.g., OWASP Top`<br>`10)?`|
|`- Completeness: Are all suggested issues fixed with full test coverage?`|
|`- Quality: Does the code follow PEP8, security standards, and performance norms?`|
|`- Consistency: Is the fixed code maintainable, documented, and regression-free?`<br>`REVIEW PROCESS:`|
|`- Compare fixed code against original vulnerabilities and requirements`<br>`- Run unit/integration tests and static analysis (e.g., Bandit, pylint)`|
|`- Verify no new vulnerabilities introduced via security scanners`<br>`- Assess code quality, documentation, and edge case handling`<br>`- Provide specific, actionable feedback with test results`<br>`FEEDBACK FRAMEWORK:`|
|`- APPROVED: Fixes pass all tests, no regressions, security clean`|
|`- CONDITIONAL: Minor issues (e.g., style violations) with specific changes needed`|
|`- REJECTED: Vulnerabilities persist, tests fail, or new risks introduced`|
|`When providing feedback, always:`|
|`- Be specific about test failures or scan results`|
|`- Suggest concrete code improvements or additional tests`|
|`- Acknowledge secure patterns implemented well`<br>`- Maintain professional and constructive tone`<br>`ESCALATION CRITERIA:`|
|`- Fundamental security flaws remain after fixes`|
|`- Test failures indicating regressions`|

- `Disagreement with Security Expert on vulnerability severity` 

- `Critical errors like buffer overflows or injection risks` 

###### **Domain-specific prompt examples** 

Here is an example of idx_4d63f892a research agent: 

```
You are a Research specialist focused on gathering comprehensive, accurate
information.
RESEARCH METHODOLOGY:
```

- `Start with authoritative primary sources` 

- `Cross-reference findings across multiple sources` 

- `Prioritize recent information unless historical context is needed` 

_Designing Multi-Agent Systems_ 

291 

- `Document source credibility and potential biases` 

###### `INFORMATION QUALITY:` 

- `Fact accuracy is your highest priority - Clearly distinguish between facts, opinions, and speculation` 

- `Note confidence levels for uncertain information` 

- `Flag contradictory sources and explain discrepancies` 

###### `DELIVERABLE FORMAT:` 

- `Structured research reports with clear sections` 

- `Source citations with links and publication dates` 

- `Executive summary for quick consumption by other agents` 

- `Raw data appendix when relevant` 

###### Next, let’s look at anidx_b55845fa example of a communication agent: 

```
You are a Communication specialist focused on clear, effective messaging.
```

###### `WRITING PRINCIPLES:` 

- `Adapt tone and style to the target audience` 

- `Use clear, concise language without jargon` 

- `Structure information logically with smooth transitions` 

- `Ensure key messages are prominent and memorable` 

###### `AUDIENCE ADAPTATION:` 

- `Technical audiences: Include detailed methodology and data` 

- `Executive audiences: Focus on insights and recommendations` 

- `General audiences: Use analogies and avoid technical terms` 

- `International audiences: Consider cultural communication norms` 

###### `QUALITY STANDARDS:` 

- `Grammar and spelling must be flawless` 

- `Facts must be accurately represented` 

- `Tone must be appropriate and professional` 

- `Structure must support easy comprehension` 

_Chapter 8_ 

292 

###### **Tool assignment decision framework** 

Determining which tools each agent should have idx_e9f0ffc **a** ccess to is crucial for system effectiveness and security. Poor tool assignment can lead to capability gaps, security vulnerabilities, and agent confusion. Here’s a systematic framework for making these decisions based on the following core assignment principles: • **Principle of least privilege** : Each agent should have access only to the tools that are absolutely necessary for its specific role. This minimizes security risks and reduces cognitive load as the agent doesn’t have to rule out tools that it will never use in every request: 

```
# Good - Focused tool assignment
research_agent:
  tools: [ web_search, document_reader, citation_manager ]
writing_agent:
  tools: [ document_editor, grammar_checker, style_guide ]
# Bad - Over-privileged assignment
research_agent:
  tools: [ web_search, document_reader, citation_manager,
           document_editor, grammar_checker, code_compiler,
           database_admin, system_monitor, shell, python_interpreter ]
```

- **Tool-task alignment** : Tools should directly support the agent’s primary responsibilities and workflows. 

- **Avoid dangerous overlaps** : When multiple agents need similar capabilities, carefully consider whether they should share tools or have specialized versions. 

Consider using this idx_67ad **f** 23f ramework to systematically assign tools: 

|**Criteria**|**Weight**|**Questions to ask**|
|---|---|---|
|Core necessity|40%|Is this tool essential for the<br>agent’s primary function?|
|Security impact|25%|What’s the risk if this tool is<br>misused or compromised?|

_Designing Multi-Agent Systems_ 

293 

|**Criteria**|**Weight**|**Questions to ask**|
|---|---|---|
|Capability overlap|20%|Do other agents already have<br>this capability?|
|Learning complexity|10%|How difficult is it for the<br>agent to use this tool<br>effectively?|
|Resource impact|5%|What are the computational/<br>cost implications?|

_Table 8.1: Decision criteria for assigning tools_ 

Consider the following scoring system: 

- Essential/High Risk/High Overlap/High Complexity/High Cost = Score accordingly 

- Make decisions based on weighted total scores 

Here are some common tool assignment patterns: 

- Sequential pipeline pattern: 

```
data_collector:
  tools: [ web_scraper, api_client, file_reader ]
  handoff_format: "structured_data"
data_processor:
  tools: [ pandas, numpy, data_cleaner, validator ]
  handoff_format: "processed_dataset"
data_visualizer:
  tools: [ matplotlib, plotly, report_generator ]
  handoff_format: "final_report"
# Note: No tool overlap - clean separation of concerns
```

- Shared infrastructure pattern: 

- 

```
# Shared tools accessed by multiple agents
shared_tools:
  database_connection:
    access_level: "read_only"
```

_Chapter 8_ 

294 

```
    available_to: [ research_agent, analysis_agent, report_agent ]
  file_storage:
    access_level: "read_write"
    available_to: [ all_agents ]
# Agent-specific tools
research_agent:
  exclusive_tools: [ web_search, survey_tool ]
analysis_agent:
  exclusive_tools: [ statistical_processor, ml_model ]
```

- Hierarchical idx_71236ac7permission pattern: 

```
coordinator_agent:
  tools: [ agent_manager, workflow_controller, system_monitor ]
  permissions: [ "delegate_tasks", "override_decisions" ]
specialist_agents:
  tools: [ domain_specific_tools ]
  permissions: [ "execute_tasks", "report_results" ]
validator_agent:
  tools: [ quality_checker, compliance_scanner ]
  permissions: [ "approve_outputs", "reject_work" ]
```

That was a comprehensive look at tool assignment strategies and decision-making frameworks for multi-agent systems. There is one more critical aspect to consider: the context that is available to each agent. 

###### **Context engineering for multi-agent systems** 

After decomposing tasks into idx_b4ff0525agents, designing their prompts, and idx_493df060assigning appropriate tools, the final crucial piece is context engineering—determining what information each agent receives to make effective decisions. Since LLMs are stateless and only process the context provided in each request, careful context management becomes the difference between a coherent multi-agent system and a collection of confused, isolated agents. 

_Designing Multi-Agent Systems_ 

295 

Context engineering in multi-agent systems involves three key dimensions: what information to include, how to structure it for optimal comprehension, and when to share context between agents. Unlike single-agent systems, where you can simply provide all the relevant information, multi-agent systems require strategic context distribution to maintain agent focus while enabling effective collaboration. 

###### **Types of context in multi-agent systems** 

There are multiple types idx_3227bfb1of context that agents may need, depending on their roles and interactions: 

- **Agent-specific context** : Eachidx_1ff4ab63 agent needs context tailored to its role and idx_ee5ba228current task: 

```
Research Agent Context:
```

- `Current research objective and success criteria` 

- `Previously gathered information and sources` 

- `Research methodology constraints` 

- `Quality standards and fact-checking requirements` 

```
Analysis Agent Context:
```

- `Dataset description and validation status - Analysis objectives and expected deliverables` 

- `Statistical requirements and confidence levels` 

- `Previous analysis results for comparison` 

• **Shared context** : Information idx_bd3fe5ddthat multiple agents need to idx_667e1544maintain consistency: 

```
Shared Project Context:
```

- `Overall project goals and timeline` 

- `Key stakeholders and requirements` 

- `Quality standards and constraints` 

- `Current project status and milestones` 

```
Shared Domain Knowledge:
```

- `Industry terminology and definitions` 

- `Relevant regulations and compliance requirements` 

- `Historical context and background information` 

- `Standard operating procedures` 

_Chapter 8_ 

296 

• **Handoff context** : Informationidx_a1439884 passed between idx_ **a** 9feb4fe gents in sequentialidx_fd82cb90 workflows: 

```
Research → Analysis Handoff:
- Research findings and source credibility
- Data quality assessments
- Identified patterns or anomalies
- Recommendations for analysis approach
Analysis → Reporting Handoff:
- Key findings and statistical significance
- Methodology used and assumptions made
- Confidence levels and uncertainty ranges
- Actionable insights and recommendations
```

We need to consider not only what context to provide but also how to structure it for clarity and efficiency. 

###### **Context management strategies** 

There are different idx_d2e18953 strategies for managing context in multi-agent systems to balance completeness with conciseness: 

- **Context layering** : Organizeidx_0caea6cb context into layers based on relevance and update 

frequency: 

```
context_layers:
  permanent:
    - agent role and expertise
    - core operational constraints
    - quality standards and procedures
  project:
    - current project goals and timeline
    - stakeholder requirements
    - success criteria and metrics
  session:
    - current task objectives
    - relevant previous work
    - immediate constraints and priorities
```

```
  dynamic:
```

_Designing Multi-Agent Systems_ 

297 

```
    - real-time updates from other agents
    - changing requirements or conditions
    - error states and recovery instructions
```

Remember that most LLM providers cache contexts based on prefixes. This means that permanent and stable parts of the context must be at the beginning and ideally never changed and re-organized, even when compaction is necessary. 

**Context scoping** : Define clearidx_b2127d2d boundaries for idx_4d2d1e34what each agent needs to know: 

- 

```
# Example context scoping for different agent types
coordinator_context = {
    "scope": "full_project_visibility",
    "includes": [
        "all_agent_status_and_progress",
        "project_timeline_and_milestones",
        "resource_allocation_and_constraints",
        "stakeholder_communication_history"
    ]
}
specialist_context = {
    "scope": "domain_focused",
    "includes": [
        "specific_task_requirements",
        "relevant_domain_knowledge",
        "quality_standards_for_domain",
        "handoff_requirements_and_format"
    ],
    "excludes": [
        "other_agents_internal_processes",
        "project_management_details",
        "unrelated_domain_information"
    ]
}
```

_Chapter 8_ 

298 

- **Context synchronization** : When idx_14376238running multiple agents in parallel and/or having agents that react to dynamic systems, it is important to synchronize the context of agents with other agents or the real world. We need to ensure agents have consistent information idx_187f6457when needed: 

   - `Synchronization Triggers: - Major milestone completion - Requirement changes or updates - Error conditions requiring coordination - Quality issues affecting multiple agents` 

```
Synchronization Methods:
```

- `Broadcast updates to all relevant agents - Version-controlled shared context documents` 

- `Event-driven context refresh mechanisms` 

- `Periodic consistency checks and reconciliation` 

It is totally reasonable and common to use multiple synchronization triggers and synchronization methods in a single multi-agent system. For example, a research agent may not need to know about a change in the project timeline until it finishes its current task and hands off to the next agent. However, if the change is critical and affects the research scope, the coordinator agent may need to broadcast the update immediately. 

###### **Context window management** 

Multi-agent systems mustidx_9afa1a54 carefully manage context window usage to maintain performance: 

- **Context prioritization** is idx_5331b499about ranking different context elements by importance and recency. This helps the LLM to decide which parts of the context to focus on first and give more weight: 

```
context_priority_framework = {
    "critical": [
        "current_task_objective",
        "immediate_constraints",
        "error_conditions"
    ],
    "high": [
        "agent_role_definition",
        "quality_standards",
        "handoff_requirements"
    ],
```

_Designing Multi-Agent Systems_ 

299 

```
    "medium": [
        "project_background",
        "previous_similar_tasks",
        "domain_knowledge"
    ],
    "low": [
        "historical_context",
        "optional_optimizations",
        "reference_materials"
    ]
}
```

• **Context compression** techniques are idx_2a01b110very important in long conversations where the messages exceed the size of the context window. The AI system needs to decide how to compress the context in order to continue. Here are some key techniques: 

```
Summarization:
```

- `Compress lengthy previous conversations into key decisions` 

- `Extract main points from research findings` 

- `Distill complex analyses into actionable insights` 

- `Selective Inclusion: - Include only context relevant to current task - Filter out outdated or superseded information - Focus on information that affects decision-making` 

```
Reference Systems:
```

   - `Store detailed information externally - Include only summaries and references in context - Retrieve full details only when needed` 

- **Context refresh patterns** allowidx_7db9ea85 sophisticatedidx_f18bf86a agentic AI systems to update the context 

beyond just user messages, tool calls, and responses. Here are some useful patterns: 

```
refresh_strategies:
  continuous:
    description: "Real-time context updates"
    use_cases: [ "monitoring_agents", "reactive_systems" ]
    overhead: "high"
  periodic:
```

_Chapter 8_ 

300 

```
    description: "Scheduled context synchronization"
    use_cases: [ "batch_processing", "stable_workflows" ]
    overhead: "medium"
  event_driven:
    description: "Context updates on significant events"
    use_cases: [ "milestone_based_projects", "exception_handling" ]
    overhead: "low"
  on_demand:
    description: "Context loaded when specifically requested"
    use_cases: [ "specialized_analysis", "deep_research" ]
    overhead: "minimal"
```

These contextidx_151c62e7 management techniques apply to the context of each agent. But in a multi-agent system, agents can and should selectively share their context with other agents. 

###### **Inter-agent context sharing** 

Let’s look at some common idx_e3935be2patterns for sharing context between agents in collaborative workflows with diagrams. It’s important to realize that agents usually don’t share their entire context, only the relevant parts needed for the collaboration. Often, the context they share is not part of their context at all and is generated for the benefit of the other agent: 

- **Direct context passing** : Agents i **d** x_374d0e48 irectly send messages to other agents and pass context as part of the message. This is the simplest form of context sharing and works well for sequential workflows where one agent’s output is the next agent’s input. 

<!-- Start of picture text -->
structured output—>  AgentB © —processed results<br>Agent A Agent C<br>++ final report<br><!-- End of picture text -->

_Figure 8.13: Direct context passing_ 

_Designing Multi-Agent Systems_ 

301 

- **Centralized context store** : Agentsidx_107c51b4 don’t interact directly but read from and write to a shared context repository. This form of context sharing is very suitable for parallel orchestration patterns where multiple agents work independently but need access to common information. 

<!-- Start of picture text -->
Context Store<br>oe ( a |<br>|<br>Agent A Agent B Agent C<br>|<br><!-- End of picture text -->

_Figure 8.14: Centralized context store_ 

- **Hierarchical context distribution** : When using hierarchical orchestration, a 

coordinator agentidx_cc60e520 manages context distribution idx_a192530bto specialist agents. All agents report back to the coordinator, which decides which parts of the overall context to share with each agent. 

<!-- Start of picture text -->
Coordinator Agent<br>Specialist A Specialist B Specialist C<br><!-- End of picture text -->

_Figure 8.15: Hierarchical context distribution_ 

That was a lot of information about context engineering for multi-agent systems. Let’s take AI-6 and A2A for a ride and see how it all comes together. 

_Chapter 8_ 

302 

###### **Taking AI-6 and A2A for a ride** 

Let’s see these concepts in action with a simple multi-agent system that is comprised of an AI-6 coordinator agentidx_50c32b49 and one A2A specialist agentidx_d5bbe159. The AI-6 framework’s A2A integration demonstrates the patterns we’ve discussed throughout this chapter. 

The `config_async.yaml` ( `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/examples/a2a-test/ config_async.yaml` ) file shows how simple it is to configure a multi-agent system: 

```
# Basic agent configuration
default_model_id: gpt-4o
tools_dirs:
  - ${HOME}/git/ai-six/py/backend/tools
# A2A server integration - this creates the multi-agent system
a2a_servers:
  - name: kind-k8s-ai
    url: http://localhost:9999
    timeout: 30.0
# System prompt that implements the Coordinator pattern
system_prompt: |
  You are an AI assistant with advanced A2A (Agent-to-Agent) communication
capabilities.
```

```
  You can:
1. Start long-running A2A tasks that run asynchronously
2. Receive real-time updates from A2A agents via SystemMessages
3. Send messages to active A2A tasks
4. Monitor multiple concurrent A2A operations
5. Manage A2A task lifecycle (list, status, cancel)
```

This configuration creates a hierarchical multi-agent system with the following: 

- An AI-6 agent as the coordinator/orchestrator 

- 

- A k8s-ai agent as the domain specialist (running separately as the A2A server at `localhost:9999` ) 

Since the k8s-ai agent is registered as an A2A server, the AI-6 tool manager automatically discovers its skills and creates corresponding `A2ATool` instances. No manual tool registration or agent prompt is needed. 

_Designing Multi-Agent Systems_ 

303 

The system prompt is intentionally general as this is part of an end-to-end test for the A2A integration and is not intended to accomplish any specific real-world goal. 

Let’s run the end-to-end test to see the multi-agent system in action: 

`% python -m examples.a2a-test.test_a2a_e2e` 🧪 `COMPREHENSIVE A2A E2E TEST ==================================================` 📋 `Phase 1: Service Dependencies` 🔧 `Checking Ollama service...` ✅ `Ollama already running` 🔧 `Checking k8s-ai A2A server...` ✅ `k8s-ai server already running` 🤖 `Setting up AI-6 Agent with async A2A... [09/14/25 18:56:46] INFO     Processing request of type ListToolsRequest server.py:624` ✅ `Agent ready with 1 A2A tools and 4 task tools` 📋 `Phase 2: Core Async A2A Functionality` 🚀 `Testing Immediate Response Pattern...` ✅ `Immediate response in 0.00s, task ID: kind-k8s-ai_Kubernetes Operations_1757901406` 📨 `Testing Background Processing & SystemMessage Injection... Initial message count: 1 Waiting for background SystemMessages... Waiting... (1/15) Waiting... (2/15) Waiting... (3/15) Waiting... (4/15) Waiting... (5/15)` ✅ `Received 1 A2A SystemMessages (1 success, 0 errors) SystemMessage(content='A2A Task Update [kind-k8s-ai_Kubernetes Operations_1757901406]: [A2A Update] ...` ⚡ `Testing Multi-tasking Capabilities...` ✅ `Multi-tasking working: 2 concurrent tasks active` 

_Chapter 8_ 

304 

- 📋 `Phase 3: Task Management` 

- 🛠️ `Testing Task Management Tools...` 

- ✅ `Task status tool working` 

- ✅ `Send message to task working` 

- 🧩 `Testing Task Cancellation & Cleanup...` 

- ✅ `Cancelled task: kind-k8s-ai_Kubernetes Operations_1757901406` 

- ✅ `Cancelled task: kind-k8s-ai_Kubernetes Operations_1757901412` 

- ✅ `Successfully cancelled/completed 2 tasks` 

`==================================================` 🎉 `COMPREHENSIVE E2E TEST PASSED! ==================================================` 

- ⏱ `Test duration: 10.4 seconds` 

- 📈 `Tasks processed: 2` 

- 🔥 `Async A2A Bridge: FULLY FUNCTIONAL` 

- ✅ `Key Features Validated:` 

- `Immediate response pattern (no blocking)` 

- `Background task processing` 

- `SystemMessage injection for real-time updates` 

- `Multi-tasking (concurrent A2A operations)` 

- `Task lifecycle management` 

- `Proper error handling (no ignored errors)` 

- 🧩 `Cleaning up test resources...` 

Excellent. The end-to-end test passed and validated all key multi-agent patterns that we implemented in the A2A integration. Let’s break down what we just saw. 

###### **Multi-agent patterns in action** 

The idx_d5b7b750end-to-end test ( `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/blob/main/ch08/ai-six/py/examples/a2a-test/ test_a2a_e2e.py` ) demonstrates several patterns from our framework: 

- **Domain expertise decomposition** (from the _Agent decomposition strategies_ section): 

```
# General coordinator handles task orchestration
```

> `result = tool.run(message="List all pods in the cluster with their status")` 

_Designing Multi-Agent Systems_ 

305 

```
# Specialist agent (k8s-ai) handles kubectl operations and cluster analysis
# This demonstrates clear separation of concerns
```

- **Coordinator system prompt pattern** : The system prompt explicitly defines the agent’s role as a task coordinator that manages async operations without blocking, thus implementing our coordinator pattern template. 

- **Context engineering** : 

- 

- **Task context** : Each A2A operation gets a unique task ID for stateful tracking 

- **Domain context** : k8s-ai maintains cluster context (kind-kind) 

- 

   - **Session context** : AI-6 manages multiple concurrent conversations 

   - 

- **Tool assignment by capability** : The system automatically assigns tools based on agent capabilities: 

   - `kind-k8s-ai_kubectl_skills` : Kubernetes operations 

   - 

- `a2a_list_tasks` , `a2a_cancel_task` : Task coordination 

- 

   - **Native AI-6 tools** : General reasoning and conversation 

   - 

- **Parallel orchestration** : Two tasks running at the same time while the coordinator agent collects the results for later processing: 

```
# Start multiple tasks concurrently - no blocking
task1 = agent.run_tool(
"kind-k8s-ai_kubectl_skills", message="List all pods")
task2 = agent.run_tool(
"kind-k8s-ai_kubectl_skills", message="Get all services")
# Both tasks run in parallel, coordinator manages their state
list_result = agent.run_tool('a2a_list_tasks')  # Shows "Active A2A Tasks
(2)"
```

This example validates theidx_5d92c917 chapter’s key principles: 

- **Clear agent decomposition** : General reasoning (AI-6) versus domain expertise (k8sai) 

- **Proper tool assignment** : Security boundaries maintained and capabilities matched to agents 

- **Effective context management** : Task IDs enable stateful coordination across agent boundaries 

_Chapter 8_ 

306 

- **Scalable orchestration** : Async patterns prevent blocking, enabling true parallelism 

- **System prompt engineering** : The coordinator role is clearly defined with specific capabilities 

The result is a system where a general-purpose agent can seamlessly coordinate with domain specialists, achieving complex goals through collaborative specialization rather than trying to be an expert at everything. 

This design is extensible. You could add agents for database operations, filesystem management, or any other domain while keeping the same coordination patterns. 

However, there is still more to explore in multi-agent systems. 

###### **Conflict resolution and role assignment in multi-agent systems** 

As multi-agent systems grow inidx_6fd2e5ad complexity, agent roles and responsibilities may overlap, leading to conflicts that can degrade system performance or cause inconsistent behavior. This section explores common conflict scenarios and proven resolution strategies. First, we will explore common conflict scenarios: 

- **Resource competition** : Multiple agents attempting to access the same resources simultaneously create race conditions. When a database agent and an audit agent both try to update the same record, data corruption becomes possible. Database transactions may fail, files may be locked by competing processes, or shared memory resources may be corrupted. These conflicts are particularly problematic in highthroughput systems where multiple agents operate concurrently. 

- **Overlapping capabilities** : Agents with similar skills may duplicate work or provide conflicting advice. A database specialist and data analysis expert might both respond to queries about sales trends, each using different approaches and potentially returning inconsistent results. This redundancy wastes computational resources and can confuse users who receive multiple, potentially contradictory responses to the same request. 

- **Hierarchical authority conflicts** : Unclear command chains lead to conflicting directives when multiple agents at the same hierarchical level attempt to manage the same resources or subordinate agents. A manager agent and supervisor agent might simultaneously assign different tasks to the same worker agent, creating confusion about priorities and potentially causing the worker to execute contradictory operations. 

_Designing Multi-Agent Systems_ 

307 

Let’s now focus on the resolution strategies: 

- **Explicit role boundaries** : The most effective conflict prevention strategy involves defining clear, non-overlapping responsibilities using capability matrices. Each agent should have explicitly defined domains of expertise, specific operations they can perform, and clear priority levels for resource access. This approach requires careful system design but eliminates ambiguity about which agent handles specific types of requests. 

Task routing becomes straightforward when each domain maps to exactly one agent. If multiple agents could handle a task, the system should have predetermined rules for selecting the most appropriate agent based on current workload, expertise level, or other objective criteria. 

• **Priority-based resolution** : When conflicts cannot be prevented through role separation, establish clear precedence hierarchies. Security agents should typically have the highest priority, followed by compliance agents, then business logic agents, with automation agents having the lowest priority. This ensures that critical concerns, such as security and regulatory compliance, always take precedence over efficiency optimizations. 

The priority system should be transparent and consistent, with all agents understanding the hierarchy. When conflicts arise, the agent with the highest priority automatically wins, eliminating negotiation overhead and ensuring predictable outcomes. 

• **Coordination protocols** : Implementidx_49507783 coordination mechanisms to prevent conflicts through structured communication. Token-based coordination uses exclusive access tokens that agents must acquire before accessing shared resources. Only one agent can hold a token at a time, preventing concurrent access conflicts. Consensus-based decision-making requires multiple agents to vote on major system changes before implementation. This approach is particularly useful for deployment decisions, configuration changes, or other operations that affect the entire system. A threshold percentage of agents must agree before the action proceeds. 

_Chapter 8_ 

308 

- **Dynamic role assignment** : Adapt agent roles based on the current context and workload distribution. The system should continuously monitor agent performance and capacity, reassigning responsibilities when agents become overloaded oridx_d0ac7e9d underutilized. This dynamic balancing prevents bottlenecks and ensures optimal resource utilization across the agent network. 

Load balancing considers both agent capabilities and current workload when assigning new tasks. An agent with high expertise in a domain might still not be the best choice if it’s currently handling many other tasks, making a less specialized but available agent a better option. 

Conflict resolution is important, but ideally, we would prevent conflicts in the first place. Let’s explore some best practices to accomplish this goal. 

###### **Best practices for conflict prevention** 

With all these idx_a0 **c** 8b7bf onflict resolution strategies under our belt, here are some best practices to prevent conflicts in multi-agent systems. 

###### **Design-time conflict analysis** 

Analyze capability overlaps i **d** x_d2086f80 uring system design to identify potential conflict points before deployment. Create capability matrices showing which agents can handle which types of tasks, then look for overlaps that could cause conflicts. High overlap between agents with similar priority levels indicates areas requiring careful coordination protocols. 

This analysis should produce clear documentation of agent boundaries and interaction protocols, helping developers understand how different agents should collaborate rather than compete. 

###### **Runtime conflict detection** 

Monitor active operations to detect conflicts as they occur. Track which agents are currently accessing which resources, and flag potential conflicts when multiple agents attempt to modify the same data or execute competing operations. Early detection allows for graceful conflict resolution rather than system failures. 

Conflict detection should operate continuously in the background, maintaining awareness of system state without significantly impacting performance. Automated alerts can notify administrators of recurring conflict patterns that might indicate design issues requiring attention. 

_Designing Multi-Agent Systems_ 

309 

###### **Clear escalation paths** 

Define structured escalation procedures for conflicts that cannot be resolved automatically. Technical conflicts might escalate to a technical lead agent, business conflicts to a business manager agent, and resource conflicts to a dedicated coordinator. Unresolvable conflicts should ultimately escalate to human supervisors. 

Escalation paths should include timeouts and automatic fallback procedures to prevent system paralysis when higher-level agents are unavailable. The escalation hierarchy should be welldocumented and regularly tested to ensure it functions correctly under stress. 

Effective conflict resolution ensures multi-agent systems remain reliable and predictable as they scale, maintaining the benefits of specialization without the chaos of uncoordinated behavior. Proper idx_42eaf7c1 architectural design can prevent most conflicts before they occur, making resolution strategies a safety net rather than a primary mechanism. 

###### **Summary** 

In this chapter, we explored the fundamental principles and practical approaches for designing effective multi-agent AI systems. We covered agent decomposition strategies, orchestration patterns, system prompt design, tool assignment frameworks, context engineering, and conflict resolution. The key insight is that effective multi-agent systems prioritize clear architectural design over complex resolution mechanisms; well-defined agent boundaries, explicit capability matrices, and proper context management prevent most conflicts before they occur. 

We demonstrated these concepts through the AI-6 + A2A integration, showing how a simple configuration can create a hierarchical multi-agent system with clear role separation, real-time communication, and robust task coordination. The end-to-end test validated all key patterns, including immediate response handling, background processing, multi-tasking capabilities, and proper conflict avoidance. The hierarchical pattern with domain specialization emerged as particularly effective for enterprise scenarios requiring both general reasoning and deep expertise. 

This foundation prepares us for the next chapter, where we’ll build a comprehensive multiagent system that brings together AI-6, MCP, and A2A protocols to create a production-ready solution demonstrating all the patterns and principles covered here. 

_Chapter 8_ 

310 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns— _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and generative AI systems. Subscribe now and receive a free ebook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OFA<br>a<br><!-- End of picture text -->

# 9 

##### Implementing Multi-Agent Systems with A2A 

DevOps practices have revolutionized software development and operations by breaking down silos and enabling continuous integration, deployment, and monitoring. However, as systems grow more complex and distributed, traditional DevOps approaches face scalability challenges. The emergence of multi-agent AI systems presents an opportunity to transform DevOps teams by introducing autonomous, specialized AI agents that can work alongside human operators to manage infrastructure, detect issues, and orchestrate remediation efforts. 

Building on the **Agent-to-Agent** ( **A2A** ) protocol foundations covered in _Chapter 8_ , this chapter explores building AI-driven DevOps teams using multi-agent systems. We’ll examine how to decompose traditional DevOps responsibilities into specialized agent roles, implement autonomous monitoring and remediation workflows, and create human-AI collaboration patterns that maintain operational control while leveraging AI capabilities. We will build a complete **multi-agent Kubernetes DevOps** ( **MAKDO** ) system that can autonomously manage Kubernetes clusters while integrating seamlessly with existing human workflows. 

The following key topics are covered: 

- Building an AI-driven DevOps team 

- 

- Defining roles and responsibilities for specialized agents 

- 

- Implementing the agents 

- 

- Orchestrating the team with a manager agent 

- 

- Integrating human feedback and control channels 

- 

- MAKDO in action – a complete demo walk-through 

- 

_Chapter 9_ 

312 

###### **Technical requirements** 

The code for this chapter is available here: 

```
https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-
A2A/tree/main/ch09
```

###### **Building an AI-driven DevOps team** 

Multi-agent DevOps systemsidx_507ef762 represent a paradigm shift from reactive, manual operations to proactive, autonomous infrastructure management. By distributing responsibilities across specialized agents withidx_b4eb63c0 domain expertise in monitoring, analysis, remediation, or communication, we can create systems that operate 24/7, scale to manage hundreds of clusters, and provide consistent, repeatable responses to operational issues. The key is designing these systems to augment rather than replace human expertise, creating collaborative workflows that leverage the strengths of both AI agents and human operators. 

We will build a MAKDO system using the AI-6 framework with A2A integration and **Model Context Protocol** ( **MCP** ) tools, demonstrating practical patterns for agent specialization, orchestration, and human integration. You will be equipped with the knowledge to design and implement agentic AI systems that can transform your organization’s approach to infrastructure management. 

###### **What makes DevOps suitable for multi-agent AI?** 

DevOps is a idx_51256841great domain for multi-agent AI systems. It’s all about the distributed chaos of idx_1639f000modern infra, Kubernetes clusters, databases, and networks spanning clouds, and the need for fast, specialized responses to the inevitable failures. 

I’ve seen many teams drowning in alerts from diverse systems, constantly under stress and having no time to address systemic issues. AI agents can fix this by deploying domain experts: one watches Kubernetes pods, another tunes database queries, and a third sniffs network issues. They run close to the action, parallelizing triage so downtime drops from minutes to milliseconds. 

Troubleshooting follows patterns I learned the hard way, such as checking events, logs, and resources. But the surface area of large-scale distributed systems is massive, and humans take too long to cover all the bases. Agents canidx_22328594 execute **standard operating perocedures** ( **SOPs** ) instantly while escalating weird cases with full context, freeing **site reliability engineers** ( **SREs** ) foridx_8a20611a architecture instead of firefighting. 

_Implementing Multi-Agent Systems with A2A_ 

313 

DevOps already splits into specialists (database administrators, network engineers, cloud experts, and security wizards), so agents mirror that: a security agent hunts vulnerabilities and a scaler agent handles traffic spikes. The human + AI teamwork allows the team to maintain high-quality, performant, and secure systems. The AI agents handle routine tasks, while humans tackle novel threats and issues. This also gives the human engineers the freedom to improve and build even better automation and guardrails so AI agents can shoulder more and more work reliably. 

However, creatingidx_ace7608a an effective AI-driven DevOps team requires careful consideration of agent roles, responsibilities, and interaction patterns. Let’s explore how to design and implement a multi-agent DevOps system using MAKDO as our practical example. MAKDO embodies the principles we have discussed in previous chapters and showcases how they apply to the DevOps domain. 

Let’s jump right in and meet MAKDO. 

###### **MAKDO – a multi-agent Kubernetes DevOps system** 

MAKDO demonstratesidx_6660a43b how to translate traditional DevOps roles into a coordinated multiagent AI system. Let’s examine its architecture and agent design. 

###### **System architecture** 

MAKDO idx_d1fe0bb3consists of four specialized agents working together to provide autonomous Kubernetes cluster management with human oversight: 

- **Coordinator agent** : Orchestratesidx_f1a56ff2 the overall workflow, makes high-level decisions, and coordinates between other agents 

- **Analyzer agent** : Specializes **i** dx_e5d478bc n cluster health assessment and issue identification using k8s-ai integration 

- **Fixer agent** : Handlesidx_21843adf safe cluster modifications and automated remediation 

- 

- **Slack agent** : Manages idx_a44ad7f4human communication and notification workflows 

This architecture reflects the natural division of responsibilities in DevOps teams while enabling autonomous operation and human oversight. 

###### **Note** 

The system may evolve, and each of these agents may spawn additional specialized agents as needed. For example, a security agent could be added to monitor for vulnerabilities, or a Kubernetes control plane agent could manage issues specific to the Kubernetes control plane. 

_Chapter 9_ 

314 

###### **The coordinator agent – orchestrating operations** 

The coordinatoridx_ee6976e0 agent serves as the team leader, orchestrating responses to issues and delegating to specialized agents. In AI-6’s multi-agent architecture, the coordinator has access to sub-agents as tools, and the LLM decides when to invoke them based on the situation. Since the input to a sub-agent is its prompt, the coordinator needs to be a good prompt engineer. 

MAKDO uses a single configuration file where sub-agents are defined **inline** within the parent coordinator’s idx_a1f008a **c** onfiguration. This hierarchical configuration pattern means AI-6 automatically discovers and instantiates all agents from one file. Here is a distilled pseudo-version of the file showing the key structure. The complete file is available at `https://github.com/ PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/tree/main/ch09/ makdo/src/makdo/agents/coordinator.yaml` : 

```
# Coordinator configuration (parent agent)
name:"MAKDO Coordinator"
default_model_id:"gpt-4o"
tools_dirs: [ "/path/to/ai-six/tools/memory" ]
system_prompt:|
YouaretheMAKDOCoordinatororchestratingspecializedagents.
Delegate to:agent_MAKDO_Analyzer,agent_MAKDO_Fixer,agent_MAKDO_Slack_Bot
# Sub-agents embedded inline (AI-6 auto-instantiates these as AgentTools)
agents:
# Analyzer sub-agent: Has A2A access to k8s-ai for diagnostics
-name:"MAKDO_Analyzer"
description:"Cluster health assessment agent"
default_model_id:"gpt-4o"
enable_memory:false
a2a_servers:
-name:"kind-makdo-test"
url:"http://localhost:9999"
system_prompt:|
Analyzeclusterhealthusingk8s-aiA2Adiagnosticskills.
Reportfindingswithfullpodnames,errors,andrecommendations.
# Fixer sub-agent: Has A2A access to k8s-ai for remediation
-name:"MAKDO_Fixer"
description:"Safe cluster modification agent"
default_model_id:"gpt-4o"
enable_memory:false
```

_Implementing Multi-Agent Systems with A2A_ 

315 

```
a2a_servers:
-name:"kind-makdo-test"
url:"http://localhost:9999"
system_prompt:|
Executesaferemediationactionsusingk8s-aiA2Askills.
Requireapprovalfordestructiveoperations(delete,scaledown).
# Slack_Bot sub-agent: Has MCP access to local Slack server
-name:"MAKDO_Slack_Bot"
description:"User communication agent"
default_model_id:"gpt-4o"
mcp_tools_dirs: [ "src/makdo/mcp_tools" ]
system_prompt:|
Postnotificationsto#makdo-devops Slack channel.
Handleapprovalworkflowsforcriticaloperations.
```

- Here are the idx_5edd3438 key features of MAKDO’s configuration file: 

1. **Parent config** : The `Coordinator` agent is defined at the top level with its own name, model, and system prompt. 

2. **Inline sub-agents** : All three sub-agents are embedded under the `agents:` key within the parent’s configuration. 

3. **Per-agent tool access** : 

   - **Analyzer** : Gets `a2a_servers` for k8s-ai diagnostics 

**Fixer** : Gets `a2a_servers` for k8s-ai remediation 

- 

   - **Slack_Bot** : Gets `mcp_tools_dirs` for Slack communication 

   - 

4. **AI-6 magic** : When you load this single file, AI-6 automatically does the following: 

   - Creates four agent instances (one coordinator and three sub-agents) 

   - Wraps sub-agents as `AgentTool` instances 

   - Makes them available to the `Coordinator` as `agent_MAKDO_Analyzer` , 

`agent_MAKDO_Fixer` , and `agent_MAKDO_Slack_Bot` 

5. **Detailed system prompts** : Each agent has comprehensive instructions defining responsibilities, report formats, and operational guidelines. 

This single YAML file defines the entire multi-agent system. The `Coordinator` can now orchestrate complex workflows by invoking sub-agents as needed, with the LLM deciding when to call which agent based on the situation. 

_Chapter 9_ 

316 

Notice how each sub-agent is specialized through three key mechanisms: 

- **Tool access** : `Analyzer` and `Fixer` get A2A tools, `Slack_Bot` gets MCP tools 

- 

- **System prompts** : Detailed instructions encode domain expertise and operational procedures 

• **Report formats** : Structured output templates ensure consistent, actionable reports `Analyzer` ’s system prompt includes detailed issue prioritization guidelines and report formats. `Fixer` ’s prompt defines safety protocols and approval requirements. `Slack_Bot` ’s prompt specifies message formatting and command processing. 

This prompt-based idx_3aa54a44specialization is more flexible than code-based approaches due to the following reasons: 

- Behavior can be tuned without code changes 

- 

- Domain expertise is readable and auditable 

- 

- New capabilities can be added through prompt engineering 

- 

- The LLM applies reasoning to handle edge cases 

- 

Let’s look at how these agents interact through AI-6’s multi-agent architecture. 

###### **Agent interaction patterns** 

MAKDO idx_0853e80d demonstrates how AI-6’s multi-agent idx_d4c39b46architecture enables coordinated operations through tool-based delegation. Understanding this pattern is crucial to grasping how MAKDO agents work together. 

###### **LLM-driven agent coordination** 

In AI-6, sub-agentsidx_a362779b are exposed as tools to the parent agent. If you squint, then there is really just a single agent that the AI system is interacting with. The fact that this root agent has subagents is an internal detail, really. The LLM that powers the root agent just decides at each turn of the conversation whether it needs to call some tool or whether it already has enough information. The fact that some of the tools at its disposal are smart tools, which are themselves AI-6 agents or entirely separate AI systems via the A2A protocol, is not important. 

There is no `Coordinator` agent class that calls methods of the `Analyzer` or `Fixer` classes. There are no such classes at all. The coordination logic is specified in natural language in the system prompts of the various agents, and the LLM’s reasoning decides when to invoke which agent as a tool. This is an example of late-binding logic. 

_Implementing Multi-Agent Systems with A2A_ 

317 

AI-6 implements this through the `AgentTool` class, which wraps sub-agents to make them callable as tools. The `AgentTool` implements the standard `Tool` interface, accepting a natural language message and returning the sub-agent’s complete response. From the parent agent’s perspective, invoking a sub-agent looks identical to calling any other tool. For a detailed explanation of `AgentTool` implementation, see _Chapter 8_ . 

When the `Coordinator` agent needs to analyze a cluster, the LLM generates a tool call like this: 

```
{
"name":"agent_MAKDO_Analyzer",
"arguments": {
"message":"Analyze the health of the kind-makdo-test cluster. Focus on pod
failures and provide specific remediation recommendations."
  }
}
```

The `AgentTool` class wraps the entire sub-agent interaction. It sends the message to the `Analyzer` agent, waits for its complete response (including any tool calls that `Analyzer` makes to k8s-ai), and returns the final result to the `Coordinator` . 

Thisidx_a568a4b1 pattern provides several benefits: 

- **Natural delegation** : The LLM decides when expertise is needed, just like a human coordinator 

- **Encapsulation** : Each agent manages its own conversation history and tool usage 

- 

- **Composability** : Agents can be nested arbitrarily deep 

- 

- **Context preservation** : The coordinator doesn’t need to track sub-agent implementation details 

AI-6 comes with multiple built-in tools, but it can provide everything for every AI system. This is not a problem because MAKDO can extend AI-6 with additional tools. 

_Chapter 9_ 

318 

###### **Extending AI-6 with new tools** 

MAKDU interacts idx_299b3ecewith the human team through Slack. AI-6 doesn’t provide built-in Slack tools (although it has a Slack frontend). But AI-6 can be extended with additional tools that support its own tool interface or the MCP standard, so we implement a custom MCP server that exposes Slack operations as tools. 

The `Slack_Bot` agent uses a custom MCP server built with FastMCP to handle all Slack communication. This server is located at `https://github.com/PacktPublishing/DesignMulti-Agent-AI-Systems-Using-MCP-and-A2A/tree/main/ch09/makdo/src/makdo/ mcp_tools/slack.py` 

The Slack MCP server is based on the FastMCP implementation of the official MCP Python SDK ( `https://github.com/modelcontextprotocol/python-sdk` ). The key features are as follows: 

- **Decorator-based tools** : The `@mcp.tool()` decorator automatically registers functions as MCP tools 

- **Token management** : Reads `AI6_BOT_TOKEN` from an environment, or `.env` , file 

- 

- **Simple HTTP calls** : Uses the `requests` library to call the Slack API directly 

- 

- **Error handling** : Returns success/failure messages that the LLM can understand 

- 

- **Channel normalization** : Automatically adds the `#` prefix if missing 

- 

This is much simpler than implementing a full JSON-RPC MCP server manually. FastMCP handles all the protocol details, letting you focus on the actual tool functionality. 

When AI-6 loads this MCP server, the `Slack_Bot` agent automatically gets 

`slack_post_message` and `slack_list_channels` as available tools. The LLM can then call these idx_6bba6ae8tools naturally: 

`{ "name": "slack_post_message", "arguments": { "channel": "makdo-devops", "text": "` 🚨 `CRITICAL: 3 pods failing in kind-makdo-test cluster" } }` 

Let’s see how AI-6 discovers new tools, such as the `Slack_Bot` agent provided by MAKDO. 

_Implementing Multi-Agent Systems with A2A_ 

319 

###### **Tool discovery and assignment** 

AI-6 automaticallyidx_fbac11ec discovers tools from multiple sources and assigns them to agents based on configuration. The tool_manager (https://github.com/PacktPublishing/Design-Multi-AgentAI-Systems-using-MCP-and-A2A/blob/main/ch08/ai-six/py/backend/agent/tool_manager.py) module handles this process via the `get_tool_dict()` function. As you can see, it combines tools from various directories and servers, then filters them based on enabled/disabled lists: 

```
defget_tool_dict(
tool_config: ToolConfig, agent_configs: list[Config] = None
) -> dict[str, Tool]:
"""Get a dictionary of all available tools from various sources."""
    tools: list[Tool] = []
# 1. Discover AI-6 native tools from all directories
for tools_dir in tool_config.tools_dirs:
        native_tools = _discover_native_tools(tools_dir)
        tools.extend(native_tools)
# 2. Discover local MCP tools from all directories
for mcp_tools_dir in tool_config.mcp_tools_dirs:
        local_mcp_tools = _discover_local_mcp_tools(mcp_tools_dir)
        tools.extend(local_mcp_tools)
# 3. Get tools from A2A servers
if tool_config.a2a_servers:
        a2a_tools = _get_a2a_tools(tool_config.a2a_servers)
        tools.extend(a2a_tools)
# 4. Create agent tools if agent configs provided
if agent_configs:
        agent_tools = _create_agent_tools(agent_configs)
        tools.extend(agent_tools)
# 5. Filter tools based on enabled/disabled configuration
    tools = _filter_tools(tools, tool_config.enabled_tools,
tool_config.disabled_tools)
return {tool.name: tool for tool in tools}
```

_Chapter 9_ 

320 

Here is aidx_fd146b85 tool breakdown of each agent in MAKDO: 

- The `Coordinator` agent ends up with the following: 

- 

   - Memory tools 

   - 

   - Agent tools: `agent_MAKDO_Analyzer` , `agent_MAKDO_Fixer` , and `agent_MAKDO_Slack_Bot` 

- `Analyzer` and `Fixer` each get the following: 

- 

   - A2A tools from the k8s-ai server ( `kind-makdo-test_*` tools for kubectl operations) 

   - Memory tools 

   - 

- `Slack_Bot` gets the following: 

- 

- MCP tools from `src/makdo/mcp_tools/slack.py` ( `slack_post_message` and `slack_list_channels` ) 

- Memory tools (inherited) 

- 

###### **Context sharing and state management** 

In AI-6’s idx_3617fb5dmulti-agent architecture, there is no direct context sharing between agents. Each AI-6 agent has its own model and context. It can communicate with other agents via tool calls and responses only. 

Here are some common approaches for context sharing: 

- **Message passing** : When the `Coordinator` agent calls a sub-agent, it includes relevant 

context in the message. Here is an example: 

```
{
"name":"agent_MAKDO_Fixer",
"arguments": {
"message":"Execute remediation for kind-makdo-test cluster. The
Analyzer identified 3 failing pods due to image pull
errors. Please attempt to restart the affected pods and verify they come up
successfully."
  }
}
```

_Implementing Multi-Agent Systems with A2A_ 

321 

- **Session isolation** : Each agent maintains its own session with conversation history. See `https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-UsingMCP-and-A2A/tree/main/ch08/ai-six/py/ai_six/agent/agent.py` : 

```
self.session_manager = SessionManager(config.memory_dir)
self.session = self._create_new_session(config.memory_dir)
```

- **Return values** : Sub-agents return complete responses that the `Coordinator` agent incorporates into its own context: 

```
Coordinator Session:
-User:"Check cluster health"
-Assistant: [callsagent_MAKDO_Analyzertool]
-Tool Result:"Analysis complete. Found 3 failing pods..."
-Assistant:"Based on analysis, we have critical
issues. Let me notify the team..."
```

Thisidx_a31bdc59 session-based approach ensures context isolation while enabling coordinated operations through explicit message passing. Each agent’s conversation history remains independent, preventing context pollution and allowing agents to be invoked multiple times with different contexts. 

Now that we have covered context sharing and state management, let’s look at the roles and responsibilities of each MAKDO agent. 

###### **Defining roles and responsibilities for specialized agents** 

The `coordinator.yaml` configuration idx_b86e194dshown previously defines MAKDO’s four-agent architecture. This section examines the design rationale: why these specific role boundaries were chosen, what trade-offs were made, and how this architecture can be extended. 

###### **From DevOps workflows to agent architecture** 

MAKDO’s agent design emerged from analyzing typical Kubernetes incident response workflows. Here’s idx_0a7cfa21what happens in the traditional manual process: 

1. **Alert triggers** : Operator receives notification 

2. **Diagnosis** : Operator runs kubectl commands to investigate 3. **Decision** : Operator determines appropriate fix 

4. **Remediation** : Operator applies changes (with caution) 

_Chapter 9_ 

322 

5. **Communication** : Operator updates the team in Slack 

6. **Verification** : Operator confirms that fix worked 

This translatesidx_13bb67f1 directly to MAKDO’s agent roles: 

- **Detection and diagnosis** are done by the `Analyzer` agent, which uses k8s-ai to investigate the cluster state, categorize issues, and recommend fixes 

- **Remediation** is done by the `Fixer` agent, which executes safe changes and requires approval for destructive operations 

- **Communication** is done by the `Slack_Bot` agent, which posts updates and handles approval workflows 

- **Coordination** is done by the `Coordinator` agent, which orchestrates the workflow and makes high-level decisions 

This mapping preserves the natural idx_5d0e408aworkflow structure while distributing responsibilities across specialized agents. 

###### **Why four agents instead of one?** 

As the original idx_20958a67simple k8s-ai system from _Chapter 3_ demonstrated, a single agent can do all of the preceding (well, except the Slack communication). So, why split MAKDO into four agents? There are several reasons: 

- **Tool isolation** : `Analyzer` shouldn’t have write access to clusters (read-only diagnostics). Separating `Analyzer` / `Fixer` enforces this through tool configuration. `Analyzer` can perform its job using only read-only tools, such as `get pods` and `get deployments` . `Fixer` needs to modify configurations, so it is appropriate to provide access to tools such as `apply manifest` . 

- **Prompt clarity** : Each agent has a focused system prompt (~50 lines) versus one massive prompt (~200 lines) trying to cover everything. 

- **Independent testing** : It can test diagnostic accuracy ( `Analyzer` ) separately from remediation safety ( `Fixer` ). 

- **Parallel evolution** : It can improve diagnostic capabilities without risking changes to remediation logic. 

Let’s dive deeper, specifically into the split of the analyzer and fixer. 

_Implementing Multi-Agent Systems with A2A_ 

323 

###### **Why separate the analyzer and fixer?** 

This idx_6e757264was the most debated design decision. Both agents use the same k8s-ai A2A tools, so why not combine them? There are three main reasons: 

###### **Safety through role separation** : 

###### • 

   - `Analyzer` ’s prompt: “NEVER make changes, only diagnose.” Allows strong security by providing the analyzer with read-only credentials (beyond relying on the prompt) in the future 

   - `Fixer` ’s prompt: “Operations requiring approval: delete, scale down, restart…” Clear mental model: Analysis is safe, remediation requires caution 

- **Different failure modes** : 

- 

   - **Analyzer failure** : The analyzer may produce incomplete or incorrect diagnoses, but it never changes the cluster state, so a bad analysis has no direct impact on production. 

   - **Fixer failure** : The fixer can execute the wrong remediation and directly modify live resources, so mistakes here can cause outages or data loss if guardrails are weak. 

   - Separate agents let you tune reliability independently from action authority. For example, run a fast-but-lower-accuracy analyzer (90% recall) for triage while restricting high-risk fixers to 99.9% accuracy with human approval. 

- **Real-world access control patterns** : Many organizations give the DevOps team readonly access to production to eliminate the risk of breaking the production environment during development. Only SREs or on-call engineers have write access in case a hot fix or an emergency action is needed. MAKDO’s split mirrors this access pattern. 

The downside is the coordination overhead, but it’s worth it for the safety and clarity. 

###### **Why separate Slack_Bot?** 

The `Coordinator` agent idx_434508eacould post to Slack directly. But the communication logic can become much more complicated with multiple communication channels, approval workflows, formatting rules, and so on. `Slack_Bot` can evolve independently and encapsulate this complexity, while the `Coordinator` agent focuses on coordination. 

_Chapter 9_ 

324 

###### **Tool access boundaries** 

Each agent’s toolidx_dc7e5a94 configuration provides exactly the tools it needs to perform its job. That makes it much easier for agents to focus on their role and reduce the possibility of misusing tools because the surface area is smaller: 

```
# Coordinator: Pure orchestrator, no operational tools beyond sub-agents
tools_dirs: [ "/path/to/memory" ]  # Only memory for state tracking
# Analyzer/Fixer: Kubernetes access via A2A
a2a_servers: [ { "url": "http://localhost:9999" } ]  # Same tools, different
prompts
# Slack_Bot: Communication tools via MCP
mcp_tools_dirs: [ "src/makdo/mcp_tools" ]  # Only Slack access
```

This configuration-based permission model also means that changing agent capabilities requires only YAML edits, not code changes. 

###### **Extending the architecture** 

MAKDO’s design idx_44cd5fe6supports extension through additional specialized agents. Here, we will discuss how to add new capabilities. Let’s look at an example of adding a security scanner agent. 

To add vulnerability scanning and security policy enforcement, take the following steps: 

1. Define the new agent in `coordinator.yaml` : 

```
agents:
-name:"MAKDO_Security_Scanner"
description:"Security vulnerability and compliance scanning agent"
a2a_servers:
-name:"kind-makdo-test"
url:"http://localhost:9999"
system_prompt:|
YouaretheMAKDOSecurityScanner.
Responsibilities:
-Scancontainerimagesforknownvulnerabilities
```

- `Check pod security contexts` 

- `Verify network policies are in place` 

- `Report security findings to Coordinator` 

_Implementing Multi-Agent Systems with A2A_ 

325 

```
Usek8s-aitoolstoinspectclusterresources.
Reportfindingsinseverity-rankedformat.
```

2. Update the `Coordinator` agent’s prompt to include the new agent: 

```
Available agents:
-agent_MAKDO_Analyzer
-agent_MAKDO_Fixer
-agent_MAKDO_Slack_Bot
-agent_MAKDO_Security_Scanner# New
```

```
Workflow:AfterAnalyzeridentifiesissues,alsocallSecurity_Scanner
tocheckforsecurityimplicationsbeforeFixerproceeds.
```

Note that idx_7459aad6we can also add the security scanner as a sub-agent of `Analyzer` if we consider security scanning a sub-area of cluster analysis. 

3. **No code changes needed** : AI-6 automatically discovers the new agent and exposes it as a tool. 

Let’s look at some of the important patterns that MAKDO employs. 

###### **Key design patterns** 

MAKDO’s architecture i **d** x_06e19d49 emonstrates several patterns applicable to other multi-agent systems: 

- **Workflow-driven decomposition** : Map agents to workflow stages, not technologies 

- 

- **Permission through configuration** : Tool access defines what agents can do 

- 

- **Prompts as policy** : Encode operational rules in the system prompts of the agents 

- **Prompts as policy** : Encode operational rules in the system prompts of the agents 

- • **Protocol encapsulation** : AI-6 handles specific protocols (A2A and MCP) so you don’t have to 

- **Extensibility by design** : Adding capabilities means adding tools and agents 

- 

The next section examines the implementation details of creating and deploying these agents using AI-6’s configuration system. 

_Chapter 9_ 

326 

###### **Implementing the agents** 

With our agent idx_d7f2cbffroles defined and their responsibilities clearly outlined, we now turn to implementation. MAKDO follows a configuration-driven approach where the entire multiagent system is defined through YAML configuration files rather than custom code. This approach leverages AI-6’s powerful agent framework to automatically instantiate agents, discover tools, and establish communication channels. 

###### **Configuration-driven agent implementation** 

Traditional idx_c9b5bc7amulti-agent systems often require extensive custom code to initialize agents, configure their tools, and establish **i** dx_9cab9613 nter-agent communication. MAKDO takes a different approach: the entire system is defined in a single coordinator configuration file with inline subagent definitions. 

MAKDO’s architecture uses one primary configuration file ( `coordinator.yaml` ) that defines the following: 

- **The coordinator agent** : The top-level orchestrator with its system prompt and tool access 

- **All sub-agents inline** : `Analyzer` , `Fixer` , and `Slack_Bot` are defined within the coordinator config 

- **Tool assignments** : Each agent’s tool access is specified through `tools_dirs` , `mcp_tools_dirs` , and `a2a_servers` 

- **Communication protocols** : Implicit through AI-6’s `AgentTool` pattern 

This single-file idx_6746211capproach has several advantages: 

- **Atomic deployment** : The entire system configuration is in one place 

- 

- **Clear hierarchy** : Parent-child relationships are explicit 

- 

- **No file synchronization issues** : No risk of separate config files getting out of sync 

- 

- **Easier version control** : One file to track system changes 

- 

The MAKDO main entry point implements the health check loop and session management. Let’s examine idx_2df714dethe key components: 

1. **Configuration loading** : AI-6’s `Config.from_file()` reads the `coordinator.yaml` file and automatically creates all agents: 

```
from ai_six.agent.agent import Agent
from ai_six.agent.config import Config
```

_Implementing Multi-Agent Systems with A2A_ 

327 

```
defcreate_coordinator_config() -> Config:
"""Create coordinator agent config with sub-agents."""
return Config.from_file("src/makdo/agents/coordinator.yaml")
```

This single line loads the `Coordinator` agent and instantiates all inline sub-agents as agent tools. 

2. **Health check loop** : The `Coordinator` agent runs continuously, sending periodic health check requests: 

`def start_coordinator(coordinator: Agent, config: Dict[str, Any]): """Start the coordinator with health check loop.""" logger = logging.getLogger("makdo")` _`# Get check interval from environment or config (default: 60s)`_ `check_interval = int(os.getenv("MAKDO_CHECK_INTERVAL", config.get("monitoring", {}).get("check_interval", 60))) logger.info(f"Starting health check loop (interval: {check_interval} s)") try: while True: try:` _`# Request health check from coordinator`_ `logger.info("` 🔍 `Initiating cluster health check...") prompt = ( "Perform a comprehensive health check across all registered clusters. " "Use the Analyzer agent to identify any issues, then use the Slack Bot agent " "to report findings to the #makdo-devops channel. " "If critical issues are found, use the Fixer agent to attempt remediation." ) response = coordinator.send_message(prompt)` 

_Chapter 9_ 

328 

`logger.info(f"` ✅ `Health check completed: {response[: 200]}...")` 

The loop sends a natural language prompt describing the desired workflow. The LLM orchestrates the sub-agents based on this prompt. Note that MAKDO operates autonomously here. There is no human-controlled request-response flow here like in chat interfaces. However, humans can still monitor and intervene via Slack. The response from the `Coordinator` agent is just logged for auditing. 

3. **Session management** : Afteridx_de79bb91 each health check, MAKDO clears conversation history to 

prevent context overflow: 

```
# CRITICAL: Clear session history to prevent context overflow
# Keep only system message - each health check cycle is independent
iflen(coordinator.session.messages) > 3:
    logger.info(
f"Clearing old messages (
{len(coordinator.session.messages)} messages)"
        )
    system_message = coordinator.session.messages[0]
if coordinator.session.messages elseNone
    coordinator.session.messages.clear()
if system_message:
        coordinator.session.messages.append(system_message)
    logger.info(
f"Session reset to {len(coordinator.session.messages)} message")
except Exception as e:
logger.error(f"Error during health check cycle: {e}")
# Wait before next check
time.sleep(check_interval)
```

This prevents the context window from filling up with old health checks. Each cycle is treated as independent. If long-term memory is needed, it can be implemented via external storage such as a database. 

4. **Main entry point** : The main function ties everything together: 

```
defmain():
"""Main entry point - note: synchronous, not async."""
```

_Implementing Multi-Agent Systems with A2A_ 

329 

```
    load_dotenv()
    config = load_config()
    setup_logging(config)
    logger = logging.getLogger("makdo")
    logger.info("Starting MAKDO - Multi-Agent Kubernetes DevOps System")
# Create coordinator with inline sub-agents
    coordinator = Agent(create_coordinator_config())
    logger.info("Coordinator and sub-agents created successfully")
# Start the coordinator (runs health check loop)
    start_coordinator(coordinator, config)
if __name__ == "__main__":
    exit(main())  # Note: synchronous call, not asyncio.run()
```

The code is in `src/makdo/main.py` ( `https://github.com/PacktPublishing/Design-MultiAgent-AI-Systems-Using-MCP-and-A2A/tree/main/ch09/makdo/src/makdo/main.py` ). Key features of this implementation include theidx_7dcc1105 following: 

- **Synchronous architecture** : Uses `time.sleep()` instead of `asyncio` to avoid event loop conflicts with MCP tools 

- **Session management** : Clears old messages after each health check cycle to prevent context overflow (128k token limit) and message ordering errors 

- **Health check loop** : Continuously monitors clusters at configurable intervals 

- 

Notice what’s _not_ in this code: 

- No manual agent instantiation for sub-agents 

- 

- No tool discovery or registration logic 

- 

- No inter-agent communication setup 

- 

- No MCP or A2A client configuration 

- 

All of this is handled automatically by AI-6 based on the coordinator configuration file. This is the value proposition of the AI-6 framework, which is reliably and silently taking care of the complex details on behalf of MAKDO. 

_Chapter 9_ 

330 

###### **Tool discovery and assignment** 

AI-6’s tool idx_6276c2c1manager handles automatic tool discovery from multiple sources. For MAKDO, here’s how tools are assigned to each agent: 

###### • **Coordinator agent** : 

```
# Only memory tools - pure orchestrator
tools_dirs: [ "/Users/gigi/git/ai-six/py/ai_six/tools/memory" ]
mcp_tools_dirs: [ "/Users/gigi/git/ai-six/py/ai_six/mcp_tools" ]
memory_dir:"data/memory"
# NO a2a_servers - delegates to Analyzer/Fixer for k8s operations
# NO Slack tools - delegates to Slack_Bot for communications
```

###### • **Analyzer agent (inline)** : 

```
agents:
-name:"MAKDO_Analyzer"
description:"Cluster health assessment agent"
default_model_id:"gpt-4o"
# Has A2A access to k8s-ai server
a2a_servers:
-name:"kind-makdo-test"
url:"http://localhost:9999"
timeout:30.0
api_key:"test-key"
```

###### • **Fixer agent (inline)** : 

```
-name:"MAKDO_Fixer"
description:"Safe cluster modification agent"
default_model_id:"gpt-4o"
# Has A2A access to k8s-ai server
a2a_servers:
-name:"kind-makdo-test"
url:"http://localhost:9999"
```

_Implementing Multi-Agent Systems with A2A_ 

331 

```
timeout:30.0
api_key:"test-key"
```

###### • **Slack_Bot agent (inline)** : 

```
-name:"MAKDO_Slack_Bot"
description:"User communication agent"
default_model_id:"gpt-4o"
tools_dirs: [ ]
# Has MCP access to local Slack tools
mcp_tools_dirs: [ "src/makdo/mcp_tools" ]
```

Agents haveidx_c14b69be their own tools, but they also have their own independent context. This is the principle of session isolation. 

###### **Session isolation** 

Each agent **i** dx_0f717f2d n MAKDO maintains its own conversation session with an isolated message history. When the `Coordinator` agent calls `agent_MAKDO_Analyzer` , `Analyzer` doesn’t see the coordinator’s conversation history. It starts with a fresh context containing only the following: 

- Its own system prompt 

- 

- The message from the coordinator 

- 

- Its own tool catalog 

- 

This session isolation, however, has important implications. Here are the benefits: 

- **Reduced token usage** : Sub-agents don’t carry the full parent conversation context 

- 

- **Focused processing** : Each agent reasons only about its specific task and its relevant context (tool calls and responses) 

- **Parallel execution potential** : Independent sessions can run concurrently, especially for A2A agents 

- **Cleaner separation of concerns** : Agents can’t accidentally leak information between contexts 

The followingidx_d150317d are the trade-offs: 

- **Context passing required** : The parent must explicitly include relevant context in messages to sub-agents 

_Chapter 9_ 

332 

- **No shared memory by default** : Agents don’t automatically share state (though can use memory tools) 

- **Increased message verbosity** : Parents may need to repeat context in multiple subagent calls 

For MAKDO, this isolation is beneficial. When the `Coordinator` agent asks `Analyzer` to assess cluster health, `Analyzer` doesn’t need to know about previous conversations with `Fixer` or `Slack_Bot` . It focuses solely on the current cluster assessment request. 

###### **Configuration over code** 

The idx_fb0d136econfiguration-driven approach means you can completely change MAKDO’s behavior without touching Python code: 

- **Add new agents** : Add entries to the agents list 

- 

- **Change tool access** : Modify `tools_dirs` , `mcp_tools_dirs` , `a2a_servers` , or `agents` for any agent 

- **Adjust agent behavior** : Update system prompts 

- 

- **Switch LLM models** : Change `default_model_id` 

- 

- **Connect to different remote AI systems** : Update A2A server URLs 

- 

###### **Key takeaways** 

MAKDO’s implementationidx_d0861a8c demonstrates several important patterns for building multi-agent systems: 

- **Configuration drives architecture** : Define your system structure in YAML, not code 

- 

- **Framework automation** : Let AI-6 handle agent instantiation, tool discovery, and communication 

- **Tool abstraction** : Sub-agents appear as tools to their parents through the `AgentTool` class 

- **Session isolation** : Each agent maintains an independent conversation state 

- 

- **Principle of least privilege** : Each agent gets only the tools it needs 

- **Principle of least privilege** : Each agent gets only the tools it needs 

- • **Extensibility through configuration** : Add capabilities by editing YAML, not writing code 

This approach dramatically reduces the complexity of building and maintaining multi-agent systems. The entire MAKDO implementation is less than 150 lines of Python code, with the vast majority being logging and error handling. The real implementation lives in the configuration files, making the system easy to understand, modify, and extend. But it’s important to have strong tooling and schema validation for the configuration. 

_Implementing Multi-Agent Systems with A2A_ 

333 

###### **Orchestrating the team with a manager agent** 

The `Coordinator` agent in MAKDO serves as the central orchestrator, managing the workflow across specialized idx_c **a** 680c7d gents while maintaining awareness of system state and operational priorities. Unlike traditional orchestration systems that rely on explicit workflow definitions and state machines, MAKDO’s `Coordinator` uses LLM reasoning to dynamically coordinate agent activities based on the situation. 

The `Coordinator` agent’s system prompt provides guidance, but the LLM determines the specific sequence of agent invocations based on context. 

###### **Dynamic workflow execution** 

Traditional idx_73ea86b7workflow engines require predefined workflows such as the following: 

```
detect_issue → analyze_issue → fix_issue → notify_humans
```

MAKDO’s `Coordinator` instead receives high-level guidance in English in its system prompt: 

- `Your primary responsibilities: 1. Monitor multiple Kubernetes clusters for health and issues 2. Coordinate between the Analyzer, Fixer, and Slack agents 3. Make decisions on task prioritization and escalation 4. Maintain awareness of ongoing operations across all clusters` 

The LLM then determines the appropriate agent invocation sequence based on the situation. Let’s explore a couple of scenario-based examples: 

```
Scenario 1: Periodic health check request
MAKDO: Invoke cooridnator every minute asking to "Check the health of kind-makdo-
test cluster"
Coordinator:
```

`1. Calls the MAKDO_Analyzer agent with message "Analyze kind-makdo-test cluster health" 2. Receives detailed report 3. Calls MAKDO_Slack_Bot agent to post results` 

```
Scenario 2: Critical issue detected
User: "Production cluster has failing pods"
Coordinator:
```

```
1. Calls agent_MAKDO_Analyzer for detailed diagnostics
```

_Chapter 9_ 

334 

```
2. Evaluates severity from Analyzer report
```

```
3. Calls agent_MAKDO_Fixer to remediate issues
```

```
4. Calls agent_MAKDO_Slack_Bot to notify team of analysis and remediation results
```

The `Coordinator` agent idx_192bd04eadapts its workflow based on `Analyzer` ’s findings, the severity of issues, and operational policies encoded in its system prompt. If human approval is needed, MAKDO will wait for approval from `Slack_Bot` before invoking the `Fixer` agent. 

###### **Decision points and branching** 

The `Coordinator` agent’sidx_797416f2 system prompt includes decision-making guidelines that the LLM 

applies: 

```
Decision-making guidelines:
```

- `Always assess cluster health before making changes` 

- `Prioritize critical issues (pods failing, services down) over warnings` 

- `Require human approval for destructive operations (delete, scale down)` 

- `Coordinate operations to avoid conflicts between clusters` 

- `Escalate to humans when automated fixes fail or are uncertain` 

- `ALWAYS post full detailed results to Slack for human visibility` 

These guidelines create decision points where the LLM chooses different paths. Here are a few examples. 

###### **Example 1: safe versus destructive operations** 

`Analyzer` reports “3 pods stuck in `CrashLoopBackOff` , may need deletion.” 

The LLM reasoning includes the following: 

- Deletion is destructive (per guidelines) 

- Requires human approval (per guidelines) 

- Should notify humans first (per guidelines) 

The execution path is as follows: 

```
1.agent_MAKDO_Slack_Bot:"Report analysis and request approval"
```

```
2.Waitforhumanresponse
```

```
3. If approved:agent_MAKDO_Fixerwith"delete pods"
```

```
4.agent_MAKDO_Slack_Bot:"Report remediation results"
```

_Implementing Multi-Agent Systems with A2A_ 

335 

###### **Example 2: auto-remediation versus escalation** 

`Analyzer` reports “2 pods need restart, low-risk operation.” 

The LLM reasoning is as follows: 

- Restart is a safe operation (not in destructive list) 

- 

- No approval needed (per `Fixer` ’s safe operations list) 

- 

- Can proceed directly (per guidelines) 

The execution path is as follows: 

`1. agent_MAKDO_Fixer: "Restart the 2 identified pods"` 

`2. agent_MAKDO_Slack_Bot: "Report both analysis and remediation results"` 

This dynamic decision-making is more flexible than hardcoded workflows while still following operational policies. 

###### **Handling complex multi-step operations** 

Some idx_54e1c889operational scenarios require multiple rounds of agent interaction, state tracking, and conditional logic. MAKDO’s `Coordinator` handles these through conversational context and LLM reasoning. 

###### **Multi-cluster coordination** 

When managing idx_74cc5d87multiple clusters, the `Coordinator` agent must sequence operations to avoid conflicts: 

```
User: "Check health of all production clusters and fix any issues"
Coordinator execution:
```

`1. For each cluster (production-east, production-west, production-central):` 

- `a. agent_MAKDO_Analyzer: "Analyze [cluster] health"` 

- `b. Evaluate if fixes needed` 

- `c. If needed: agent_MAKDO_Fixer: "Fix issues in [cluster]"` 

- `d. agent_MAKDO_Slack_Bot: "Post results for [cluster]"` 

`2. Aggregate results across clusters` 

`3. agent_MAKDO_Slack_Bot: "Post summary of all cluster operations"` 

The `Coordinator` agent maintains awareness of which clusters have been processed through its conversation idx_ae6f38f5context. The LLM tracks state implicitly through the message history. If that becomes too complicated, MAKDO can evolve to have a meta-coordinator as the root agent that launches multiple coordinator agents, each with its own `Analyzer` , `Fixer` , and `Slack_Bot` . 

_Chapter 9_ 

336 

###### **Conditional remediation** 

Some idx_3693a3e7fixes depend on the results of previous operations: 

```
Scenario: Image pull failures might require different remediation strategies
```

```
Coordinator logic:
1. agent_MAKDO_Analyzer: "Diagnose image pull failure"
2. If Analyzer reports: "Image not found in registry"
   → agent_MAKDO_Slack_Bot: "Escalate - invalid image reference"
3. If Analyzer reports: "Registry authentication failed"
   → agent_MAKDO_Fixer: "Apply image pull secrets"
   → agent_MAKDO_Analyzer: "Verify pods now pulling successfully"
4. If Analyzer reports: "Registry temporarily unavailable"
   → Schedule retry after delay
   → agent_MAKDO_Slack_Bot: "Notify team of temporary issue"
```

This conditional logic emerges from the LLM’s reasoning about `Analyzer` ’s reports, not from explicit `if/else` statements in code. 

###### **Retry and verification loops** 

The `Coordinator` agent idx_ **c** d8f5f62 an implement retry logic when operations fail: 

```
Fixer reports: "Failed to restart pod, still in error state"
Coordinator reasoning:
- Initial fix attempt failed (per Fixer report)
- Guidelines say "escalate when automated fixes fail"
- Should verify current state before escalating
Execution:
1. agent_MAKDO_Analyzer: "Re-analyze the specific failing pod"
2. Evaluate new diagnostic information
3. Decide: Try alternative fix OR escalate to humans
4. agent_MAKDO_Slack_Bot: "Report situation and decision"
```

Retries can help when there are transient problems, but sometimes the system might encounter idx_768eb2d3persistent failures, and it needs to be able to handle them. 

_Implementing Multi-Agent Systems with A2A_ 

337 

###### **Error handling and recovery** 

MAKDO’s idx_8b95bb95agents can encounter various failure modes. The `Coordinator` agent’s system prompt includes implicit error-handling guidance that the LLM applies. 

###### **Agent communication failures** 

If a idx_c80e3756sub-agent invocation fails (timeout, exception, etc.), the `AgentTool` class will return an error message that `Coordinator` receives as a tool result: 

```
Tool: agent_MAKDO_Analyzer
Error: "Timeout connecting to k8s-ai server"
Coordinator response (guided by system prompt):
1. Recognize communication failure
2. agent_MAKDO_Slack_Bot: "Alert - cannot reach cluster analysis service"
3. Decide: Retry OR escalate OR use cached data
```

The LLM interprets the error and decides on an appropriate recovery strategy based on context. 

###### **Partial failures** 

When some idx_7d16fdd7operations succeed while others fail, the `Coordinator` agent tracks partial progress: 

```
Fixer reports: "Restarted 5 of 7 failing
pods. 2 pods remain in error state due to resource constraints."
Coordinator response:
```

`1. Recognize partial success (5/7 completed) 2. Analyze remaining issues (resource constraints) 3. agent_MAKDO_Analyzer: "Check cluster resource availability" 4. Based on analysis, decide next steps: - Scale up nodes (if resource exhaustion) - Adjust pod resource requests (if over-provisioned) - Escalate to humans (if capacity limits reached) 5. agent_MAKDO_Slack_Bot: "Report partial success and next steps"` 

One of the most complicated failures is cascading failures. 

_Chapter 9_ 

338 

###### **Cascading failures** 

The `Coordinator` agentidx_9751ab59 must handle scenarios where fixing one issue reveals or causes other issues: 

```
Initial issue: 3 pods failing
After fix attempt: 5 pods now failing
Coordinator reasoning:
- Situation worsened (3 → 5 pods failing)
- Applied fix may have caused new issues
- Should halt automated remediation
- Requires human investigation
```

```
Execution:
```

```
1. agent_MAKDO_Slack_Bot: "CRITICAL: Remediation caused additional failures.
Halting automation."
2. agent_MAKDO_Analyzer: "Full cluster diagnostic to identify root cause"
3. agent_MAKDO_Slack_Bot: "Post detailed diagnostic results"
4. Wait for human guidance before proceeding
```

This defensive approach prevents automation from making situations worse. 

###### **State management and coordination** 

MAKDO’s `coordinator` maintainsidx_a98698c2 operational state through conversation context and memory tools, enabling awareness of ongoing operations and historical context. 

The `Coordinator` agent’s message history serves as its working memory during a single health check cycle. 

The LLM accesses this context to answer follow-up requests or questions from users in Slack and to maintain awareness of ongoing operations while the analyzer and the fixer operate. Note that the coordinator may call the analyzer and the fixer multiple times in a single health check cycle. 

###### **Memory tools for long-term state** 

For a stateidx_033775bc that needs to persist across conversation sessions, MAKDO uses AI-6’s memory tools: 

```
# Coordinator configuration
tools_dirs: [ "/Users/gigi/git/ai-six/py/ai_six/tools/memory" ]
memory_dir:"data/memory"
```

_Implementing Multi-Agent Systems with A2A_ 

339 

```
The Coordinator agent can save and retrieve structured information:
# Save cluster state after operations
Tool:save_memory
Arguments:
key:"production-east-last-check"
value: {
"timestamp":"2024-10-06T14:30:00Z",
"status":"degraded",
"issues":3,
"fixed":2,
"pending_approval": ["pod-delete-operation-047"]
  }
# Later retrieve state
Tool:retrieve_memory
Arguments:
key:"production-east-last-check"
Result: [savedstateobject]
```

This enables idx_9709a215the `Coordinator` agent to maintain awareness across multiple conversation sessions and agent restarts. 

###### **Avoiding duplicate operations** 

The `Coordinator` can idx_bf1fdaa3use memory to track recent operations and avoid duplication: 

```
User: "Fix production-east issues"
Coordinator checks memory:
Tool: retrieve_memory
Arguments:
  key: "recent-operations"
Result: "production-east remediation completed 5 minutes ago"
Coordinator response:
"Production-east was just remediated 5 minutes ago. Let me verify current status
instead."
Execution:
agent_MAKDO_Analyzer: "Quick health check of production-east"
```

Let’s discuss different modes of orchestration. 

_Chapter 9_ 

340 

###### **Proactive versus reactive orchestration** 

MAKDO’s `Coordinator` can operate in both reactive (responding to requests) and proactive (autonomous monitoring) modes. 

###### **Reactive mode – user-initiated operations** 

Inidx_5600a17f reactive mode, the `Coordinator` agent responds to explicit user requests: 

```
User: "Check cluster health"
→ Coordinator analyzes and reports
User: "Fix the failing pods"
→ Coordinator remediates and reports
User: "What's the status of production-west?"
→ Coordinator queries state and responds
```

This mode gives humans direct control over when and how operations occur. 

###### **Proactive mode – autonomous monitoring** 

In proactive idx_378d190amode, the `Coordinator` agent can initiate operations based on schedules or triggers. This is the current operating mode of MAKDO: 

```
# Periodic scheduled check
Every minutes:
1. agent_MAKDO_Analyzer: "Health check all registered clusters"
2. If issues found:
   a. Categorize by severity (CRITICAL, WARNING, INFO)
   b. For CRITICAL: Immediate remediation workflow
   c. For WARNING: Schedule remediation, notify humans
   d. For INFO: Log and include in next summary report
3. agent_MAKDO_Slack_Bot: "Post status update if changes detected"
```

This mode is more sophisticated but requires a lot of trust since the `Coordinator` agent operates autonomously. 

###### **Hybrid approach – event-driven coordination** 

A idx_dc0e8c44hybrid approach combines reactive and proactive patterns: 

```
Normal operation:
- Proactive monitoring every 5 minutes
```

_Implementing Multi-Agent Systems with A2A_ 

341 

- `Reactive response to cluster events or alerts` 

- `Automatic remediation of routine issues` 

- `Slack notifications for significant events` 

```
When critical issue detected:
```

- `Notify humans immediately` 

- `Wait for approval before major operations` 

- `Provide detailed status updates on request` 

Most real-worldidx_1df68bb1 systems will utilize the hybrid approach. Now, let’s turn our attention to the critical aspect of adding a human to the loop. 

###### **Integrating human feedback and control channels** 

While idx_c3ec48d6AI agents can automate many DevOps tasks, human oversight remains essential for strategic decisions, complex troubleshooting, and maintaining operational control. MAKDO integrates Slack as its primary human-AI interface, enabling real-time notifications, status updates, and approval workflows. Note that since all communication goes through an agent, it is easy to replace Slack with email or any other communication tool that has an API, as well as using multiple communication mechanisms concurrently. 

###### **The human-AI interface challenge** 

Effective human-AIidx_bf0119b5 collaboration in DevOps requires careful interface design that balances automation efficiency with human control. The interface must do the following: 

- **Provide visibility** : Humans need complete transparency into what agents are doing 

- **Enable control** : Humans must be able to approve, reject, or modify agent actions, as well as pausing or canceling ongoing operations 

- **Minimize interruption** : Don’t overwhelm humans with routine notifications 

- 

- **Support natural communication** : Use familiar tools and communication patterns 

- **Maintain context** : Preserve conversation history and operational context 

- 

MAKDO addresses these requirements through a dedicated `Slack_Bot` agent that acts as the communication bridge between the AI system and human operators. 

###### **The Slack_Bot agent architecture** 

The `Slack_Bot` agent is a idx_c8f6f560specialized idx_8 **c** ea7525 ommunication agent with access to Slack via MCP tools. Unlike the `Analyzer` and `Fixer` agents that use A2A for Kubernetes operations, `Slack_Bot` uses the MCP to interact with Slack’s API. 

_Chapter 9_ 

342 

From the `coordinator.yaml` file shown earlier, the `Slack_Bot` configuration is as follows: 

`agents: - name: "MAKDO_Slack_Bot" description: "User communication and notification interface agent" default_model_id: "gpt-4o" tools_dirs: [ ]` _`# Slack_Bot uses local MCP server for Slack communication`_ `mcp_tools_dirs: [ "src/makdo/mcp_tools" ] system_prompt: | You are the MAKDO Slack Bot, the primary interface between the MAKDO system and human users. Your primary responsibilities: 1. Send alerts and notifications to the designated Slack channel (#makdodevops) 2. Parse and process user commands from Slack messages 3. Provide status updates and operation summaries 4. Format technical information for human-readable display 5. Handle approval requests for critical operations Message types and formatting:` 🚨 `CRITICAL: Immediate attention required` ⚠ `WARNING: Issue needs attention i  INFO: Status update or information` ✅ `SUCCESS: Operation completed successfully` ❌ `FAILED: Operation failed` ⏳ `PENDING: Operation in progress` 

The key idx_2a2264d8configuration idx_0b8bc70aelement is `mcp_tools_dirs: ["src/makdo/mcp_tools"]` , which tells AI-6 to discover MCP servers in that directory. 

###### **Building a custom MCP server with FastMCP** 

MAKDO idx_c6eebd21uses a custom MCP server for Slack integration built with the FastMCP library as discussed earlier. This approach is significantly simpler than implementing the full MCP protocol manually. 

_Implementing Multi-Agent Systems with A2A_ 

343 

###### **The FastMCP Slack server** 

The idx_fe1a0af0Slack MCP server implementationidx_bcb445a3 shows how FastMCP simplifies protocol handling. Let’s examine the key components of `src/makdo/mcp_tools/slack.py` ( `https://github.com/ PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/tree/main/ch09/ makdo/src/makdo/mcp_tools/slack.py` ): 

1. **Server initialization and token loading** : FastMCP requires just one line to create an MCP server, with tokenidx_8d2cd3a1 management handling both environment variables and `.env` files: 

```
import os
import requests
from pathlib import Path
from mcp.server.fastmcp import FastMCP
# Initialize FastMCP server
mcp = FastMCP("Slack Tools", "")
# Get bot token from environment or .env file
bot_token = os.getenv('AI6_BOT_TOKEN')
ifnot bot_token:
# Navigate from .../makdo/src/makdo/mcp_tools/slack.py to .../
makdo/.env
    makdo_root = \
        Path(__file__).resolve().parent.parent.parent.parent
    env_file = makdo_root / '.env'
if env_file.exists():
withopen(env_file) as f:
for line in f:
if line.startswith('AI6_BOT_TOKEN='):
                    bot_token = line.split('=', 1)[1].strip()
break
```

This is a idx_3ded8ce2MAKDO-specific tool, so it’s OK to embed MKADO-specific configuration such as the `.env` file path. 

_Chapter 9_ 

344 

2. **Posting messages tool** : The `@mcp.tool()` decorator automatically registers the function as an MCP tool. FastMCP handles all protocol details: 

`@mcp.tool() def slack_post_message(channel: str, text: str) -> str: """Post a message to a Slack channel"""` _`# Normalize channel name (add # prefix if missing)`_ `if not channel.startswith('#'): channel = f'#{channel}'` _`# Call Slack API directly with simple requests library`_ `url = 'https://slack.com/api/chat.postMessage' headers = {'Authorization': f'Bearer {bot_token}'} data = {'channel': channel, 'text': text} response = requests.post( url, headers=headers, json=data, timeout=10) result = response.json()` _`# Return LLM-friendly success/error messages`_ `if result.get('ok'): return f"` ✅ `Message posted to {channel}" else: return f"` ❌ `Failed to post: {result.get('error', 'unknown_error')}"` 

Note that thisidx_4a91530a toolidx_c802bc28 interacts with the Slack API using direct HTTP calls with the `requests` library. This is different from the Slack frontend of AI-6 that uses the official Slack SDK and the `slack_bot` library. For MAKDO, direct API calls are simpler and sufficient without unnecessary external dependencies. 

3. **Listing channels tool** : A second tool provides channel discovery, following the same decorator pattern: 

```
@mcp.tool()
defslack_list_channels() -> str:
"""List all channels in the workspace"""
    url = 'https://slack.com/api/conversations.list'
    headers = {'Authorization': f'Bearer{bot_token}'}
```

_Implementing Multi-Agent Systems with A2A_ 

345 

`response = requests.get(url, headers=headers, timeout=10) result = response.json() if result.get('ok'): channels = result.get('channels', []) return '\n'.join([f"#{ch['name']}" for ch in channels]) else: return f"` ❌ `Failed to list channels: {result.get('error')}"` 

4. **Server entry point** : Running the script starts the MCP server, making both tools available to AI-6: 

```
if __name__ == '__main__':
    mcp.run()
```

Based on this, we see that FastMCP simplifies MCP server creation through several design choices and key features: 

- **Decorator-based registration** : The `@mcp.tool()` decorator automatically registers 

functions as MCP tools. No manual JSON-RPC handling is required. 

- **Automatic type inference** : FastMCP extracts parameter types and descriptions from function signatures and docstrings. 

- **Protocol handling** : FastMCP manages all MCP protocol details (initialization, tool listing, and tool execution). 

Compare idx_604c3a38thisidx_c07270e2 to a manual MCP implementation, which would require the following: 

- JSON-RPC message parsing 

- 

- Protocol version negotiation 

- Tool schema generation 

- 

- Request/response handling 

- 

- Error serialization 

- 

FastMCP handles all of this automatically, letting you focus on the actual tool functionality. 

The Slack server reads the bot token from environment variables or a `.env` file: 

```
bot_token = os.getenv('AI6_BOT_TOKEN')
ifnot bot_token:
# Try loading from .env file
```

_Chapter 9_ 

346 

```
    env_file = makdo_root / '.env'
if env_file.exists():
# Parse .env file for AI6_BOT_TOKEN
```

This allows flexible deployment of environment variables in production and `.env` files for development. 

Both tools return user-friendly error messages that the LLM can understand: 

`if result.get('ok'): return f"` ✅ `Message posted to {channel}" else: error = result.get('error', 'unknown_error') return f"` ❌ `Failed to post to {channel}: {error}"` 

When the `Slack_Bot` agent receives these responses, it can reason about failures and take appropriate action (retry, escalate, or use an alternative channel). 

The purpose idx_76b6269fof the idx_f3ffdfb3Slack MCP tool is for the `Slack_Bot` agent to communicate with users via Slack. But MAKDO has several different communication patterns. 

###### **Communication patterns** 

MAKDO idx_026a8d3c implements idx_818f2fffseveral communication patterns to keep humans informed while avoiding information overload. 

###### **Notification hierarchy** 

The `Coordinator` agent’s systemidx_eaa43948 prompt instructs it to always post detailed results to Slack: 

```
CRITICAL WORKFLOW FOR SLACK REPORTING:
When you receive results from Analyzer or Fixer agents, you MUST:
1. Use agent_MAKDO_Slack_Bot to post THE COMPLETE DETAILED RESULTS
2. Include ALL technical details: pod names, error messages, actions taken
3. Do NOT summarize or filter - post the full agent output
```

This ensures humans have complete visibility into agent operations. The actual workflow is as follows: 

```
Coordinator receives user request
→ Calls agent_MAKDO_Analyzer
→ Gets detailed analysis report
→ Calls agent_MAKDO_Slack_Bot with FULL analysis
```

_Implementing Multi-Agent Systems with A2A_ 

347 

```
→ Calls agent_MAKDO_Fixer if remediation needed
```

```
→ Gets detailed remediation report
```

```
→ Calls agent_MAKDO_Slack_Bot with FULL remediation results
```

Every significant operation produces a Slack notification with complete context. 

###### **Message formatting** 

The `Slack_Bot` agent’s idx_fd16965esystem prompt includes formatting guidelines: 

```
Message formatting for Slack:
```

- `Use Slack markdown for emphasis (*bold*, _italic_, `code`)` 

- `Use code blocks for kubectl commands and YAML` 

- `Include relevant links and context` 

- `Keep messages concise but informative` 

- `Use threads for detailed technical discussions` 

- `Tag relevant users for critical alerts (@channel, @here)` 

The following is an example formatted message: 

🚨 `*CRITICAL ISSUES DETECTED*` 

```
*Cluster:* kind-makdo-test
*Timestamp:* 2025-10-06 14:30:00
```

```
*Issues Found:*
```

🔴 `*CRITICAL:*` 

```
• Pod: `default/failing-app-1`
  Status: ImagePullBackOff
  Error: Failed to pull image "nonexistent:latest"
  Restarts: 5
```

```
• Pod: `default/failing-app-2`
  Status: CrashLoopBackOff
  Error: Container exited with code 1
  Restarts: 12
```

```
*Recommendations:*
```

```
1. Verify image name and registry accessibility
2. Check application logs for crash cause
3. Consider rolling back to previous version
```

_Chapter 9_ 

348 

```
*Next Steps:* Remediation agent dispatched
```

This idx_ca94941bformatting makes technical information easily scannable while preserving all essential details. 

###### **Contextual messaging** 

`Slack_Bot` adapts **i** dx_4390e14c ts messaging based on severity and context. Here are some examples. 

This is an example message for routine operations: 

```
i Cluster health check completed
kind-makdo-test: All systems nominal
5 pods running, 0 issues detected
```

This is an example message for warnings: 

⚠ `WARNING: Resource utilization high Cluster: production-east CPU: 85% (threshold: 80%) Memory: 78% Recommend scaling up nodes` 

This is an example message for critical issues: 

🚨 `@channel CRITICAL: Production cluster degraded Cluster: production-west 5 pods failing in user-facing services Impact: API response times increased 300% MAKDO remediation in progress Human approval required for pod restarts` 

The LLM selects idx_df **a** 6134a ppropriate emoji, urgency markers, and notification targets based on `Analyzer` ’s severity assessment. 

###### **Escalation pattern for restricted operations** 

MAKDO implements idx_d **a** f3b556 safety-first approach for operations requiring human approval. Rather than executing potentially destructive operations automatically, the `Fixer` agent identifies them, skips execution, and escalates to humans through detailed Slack notifications. 

Here’s how MAKDO handles restricted operations. 

_Implementing Multi-Agent Systems with A2A_ 

349 

The `Fixer` agent’s system prompt defines which operations require approval: 

```
Operations requiring approval:
- delete (pods, deployments, services)
- scale down operations
- deployment configuration changes (image updates, etc.)
When the Fixer encounters such operations, it follows this pattern:
Fixer workflow:
1. Analyzes the remediation needed (e.g., deployment image change)
2. Checks operation against approval-required list
3. Skips the operation (doesn't execute)
4. Reports to Coordinator with detailed reasoning
5. Coordinator posts complete report to Slack via Slack_Bot
```

Here is an example Slack notification: 

`**Remediation Report** **Skipped Actions:** - Pod: default/image-pull-fail-abc123 Action: Skipped - ImagePullBackOff requires deployment fix Reason: Image "nonexistent:v1.0.0" does not exist in registry Recommendation: Update deployment with valid image` ⚠ `Requires human approval to change deployment configuration **Next Steps:** Humans can manually execute the fix if appropriate: kubectl set image deployment/image-pull-fail app=valid-image:v1.0.0` 

This escalation pattern ensures destructive operations never execute automatically. Humans receive complete context to make informed decisions and can execute fixes manually if needed. For future idx_c0a6437f enhancement, interactive approval workflows could be added using memory tools to track pending operations and Slack command processing to accept/reject operations programmatically, but the current design prioritizes safety through mandatory escalation. When MAKDO gains trust, `Fixer` can be allowed to execute some of these operations automatically. 

_Chapter 9_ 

350 

###### **Alternative communication channels** 

While MAKDO uses Slack, theidx_0556f937 same patterns may apply to other communication platforms: 

- **Microsoft Teams** : Replace the Slack MCP server with the Teams equivalent using the Microsoft Graph API. 

- **Email** : Build the MCP server using SMTP/IMAP for asynchronous notifications. 

- 

- **PagerDuty** : Integrate for incident management and on-call escalation. 

- 

- **Datadog** : Respond to alerts. Create new alerts and enrich alerts with context. 

- 

- **SMS** : Use the Twilio MCP server for critical alerts. 

- 

The architecture remains the same. Swap the MCP server implementation while keeping the communication agent pattern. The agent’s system prompt would need adjustments for platform-specific features, but the core notification principles remain unchanged. 

###### **Security and access control** 

Human-AI idx_48 **c** 57032 ommunication channels require careful security consideration. 

The first step is **authentication** . The idx_64f81c20Slack MCP server uses Slack’s OAuth bot token for authentication: 

```
headers = {
'Authorization': f'Bearer{bot_token}',
'Content-Type': 'application/json; charset=utf-8'
}
```

The bot token should have the required permissions, such as the following: 

- `chat:write` : Post messages to channels 

- 

- `channels:read` : List channels 

- 

- `channels:history` : Read channel messages (for command processing) 

- 

Next, let’s look idx_637620d3at **channel restrictions** . `Slack_Bot` ’s system prompt restricts it to designated channels: 

```
Communication channels:
- #makdo-devops: Primary channel for alerts and status updates
- Direct messages: For sensitive information or approval requests
- Thread replies: For detailed discussions and follow-ups
```

This idx_3a042466prevents the bot from posting operational data to inappropriate channels. 

_Implementing Multi-Agent Systems with A2A_ 

351 

Following this **i** dx_01b5f8b5 s **command authorization** . For production deployments, add authorization checks: 

`@mcp.tool() def slack_post_message(channel: str, text: str, user_id: str = None) -> str: """Post a message to a Slack channel"""` _`# Check if user is authorized for this channel`_ `if user_id and not is_authorized(user_id, channel): return f"` ❌ `User {user_id} not authorized for {channel}"` 

```
# Proceed with posting...
```

This ensures only authorized users can request or approve critical operations. 

###### **Observability and audit trail** 

All idx_5b0622a9Slack communications create a natural audit trail: 

- **Message history** : Slack preserves complete conversation history 

- 

- **Threaded discussions** : Related messages are grouped for context 

- 

- **Reactions** : Humans can acknowledge or react to agent messages 

- 

- **Search** : Slack’s search enables finding past operations 

- 

- **Export** : Slack data can be exported for compliance/analysis 

- 

This built-in observability is a key advantage of using established communication platforms for human-AI interaction. 

Having explored MAKDO’s architecture, agent interactions, and human integration patterns, we can now summarize the key insights before examining the system in action. MAKDO’s approach to human-AI collaboration centers on a dedicated communication agent that handles all human interaction while keeping operational agents focused on their domains, using the MCP protocol to integrate with external platforms such as Slack through the simplified FastMCP library. 

The system maintains full transparency by always posting complete operational details to humans without summarization or filtering, supporting bi-directional communication for both agent-to-human notifications and human-to-agent commands. For operations requiring approval, MAKDO **i** dx_787d2e63 mplements a safety-first escalation pattern where `Fixer` identifies restricted operations, skips execution, and provides humans with detailed context for manual intervention when appropriate. 

_Chapter 9_ 

352 

Security considerations include platform authentication, channel restrictions, and command validation, while communication platforms provide a natural audit trail through built-in message history and search capabilities. These patterns enable effective human-AI collaboration that maintains human control while leveraging AI automation capabilities, as we’ll see in the complete demonstration that follows. 

###### **MAKDO in action – a complete demo walk-through** 

Let’s see MAKDO in actionidx_17ae1378 through a complete end-to-end demonstration. This walk-through shows the entire workflow from problem detection through remediation, with real Slack notifications at each step. 

###### **Demo setup** 

The i **d** x_5b3e2092 emonstration uses a test script that creates authentic cluster problems and exercises the full MAKDO workflow. We’ll go through the setup first. 

Here are the details for the test environment setup: 

- **Cluster** : `kind-makdo-test` (local Kubernetes cluster) 

- 

- **k8s-ai server** : Running on `http://localhost:9999` 

- 

- **Slack channel** : `#makdo-devops` 

- 

- **Coordinator** : With inline `Analyzer` , `Fixer` , and `Slack_Bot` agents 

The test script can be found here: `https://github.com/PacktPublishing/Design-MultiAgent-AI-Systems-Using-MCP-and-A2A/tree/main/ch09/makdo/ test_makdo_with_slack.py` . 

The test creates two types of failures: 

- **CrashLoop Pod** : A pod that repeatedly crashes with exit code 1 

- 

- **ImagePullBackOff deployment** : A deployment referencing a non-existent container image 

These represent idx_4fd1ba8 **c** ommon real-world Kubernetes issues that MAKDO must detect and remediate. 

###### **Creating cluster problems** 

The test idx_d6ef0 **b** c0 egins by creating actual Kubernetesidx_68e26936 resources that will fail: 

`def create_crashloop_pod(self) -> bool: logger.info("` 💥 `Creating crashloop pod...") yaml = """` 

_Implementing Multi-Agent Systems with A2A_ 

353 

`apiVersion: v1 kind: Pod metadata: name: crashloop-app namespace: default spec: containers: - name: crash image: busybox command: ["sh", "-c", "echo 'Starting...'; sleep 2; exit 1"] restartPolicy: Always """` _`# Apply to cluster...`_ `def create_failing_deployment(self) -> bool: logger.info("` 💥 `Creating failing deployment...") yaml = """ apiVersion: apps/v1 kind: Deployment metadata: name: image-pull-fail namespace: default spec: replicas: 2 selector: matchLabels: app: bad-image template: metadata: labels: app: bad-image spec: containers: - name: app image: nonexistent-registry.io/fake/image:v1.0.0 imagePullPolicy: Always """` _`# Apply to cluster...`_ 

After idx_eb033e84 creation, the idx_46047cb0test waits 15 seconds for these problems to manifest (pods entering `CrashLoopBackOff` and `ImagePullBackOff` states). 

_Chapter 9_ 

354 

###### **Step 1 – demo start notification** 

MAKDO sends idx_d5c028e9an initial message to Slack announcing the demo: 

`def send_demo_start_message(self): message = """` 🤖 `**MAKDO End-to-End Demo** This demo showcases MAKDO's complete autonomous DevOps workflow: **Test Scenario:** 1.` ✅ `Create cluster problems (crashloop pod, failing deployment) 2.` 🔍 `Analyzer detects issues using k8s-ai 3.` 📊 `Report findings to Slack 4.` 🔧 `Fixer attempts remediation 5.` ✅ `Report results to Slack **Environment:** - Cluster: kind-makdo-test - Channel: #makdo-devops - Demo started at: 2024-10-06 14:30:00 """ response = self.coordinator.send_message( f"Post this message to #makdo-devops Slack channel:\n\n{message}", self.coordinator.default_model_id )` 

###### Here’s what happens internally: 

1. The `Coordinator` agent receives the message. 

2. The LLM recognizes that this is a Slack posting task. 

3. It generates a tool call: `agent_MAKDO_Slack_Bot` with the message. 

4. `Slack_Bot` receives the message. 

5. `Slack_Bot` calls the `slack_post_message` MCP tool. 

6. The FastMCP Slack server posts to the #makdo-devops channel. 

7. The FastMCP Slack server returns success confirmation. 

_Implementing Multi-Agent Systems with A2A_ 

355 

This demonstrates the complete delegation chain: 

**User → Coordinator → Slack_Bot → MCP Tool → Slack API** 

The following figure shows the _demo start message_ in Slack: 

_Figure 9.1: Demo start message_ 

MAKDO postsidx_ba27d363 the demo start announcement to the _#makdo-devops channel_ , outlining the test scenario and environment. 

###### **Step 2 – analysis phase** 

Now, MAKDO analyzes idx_dfe83751the cluster to detect the problems: 

```
defrun_analysis_and_post(self):
    analysis_request = """
Please perform the following tasks in order:
1. Use the Analyzer agent to check the health of the kind-makdo-test cluster
   and get the COMPLETE detailed analysis report
2. Immediately forward THE COMPLETE ANALYZER OUTPUT to the Slack agent with this
   message: "Post this complete cluster analysis report to #makdo-devops:
   [PASTE FULL ANALYZER OUTPUT HERE]"
CRITICAL: Do NOT summarize. Do NOT filter. Post the ENTIRE analysis report
exactly as the Analyzer provided it.
"""
    response = self.coordinator.send_message(
        analysis_request,
```

_Chapter 9_ 

356 

```
self.coordinator.default_model_id
```

```
    )
```

Here’s the idx_1916c7a5 internal workflow: 

1. The `Coordinator` agent delegates to the `Analyzer` sub-agent: 

```
Tool:agent_MAKDO_Analyzer
Arguments: {
"message":"Check the health of kind-makdo-test cluster"
}
```

2. The `Analyzer` subagent executes the following actions (using k8s-ai A2A tools): 

   - Calls the k8s-ai `kubernetes_resource_health` skill 

   - Retrieves actual pod statuses from the cluster 

   - Calls the k8s-ai `kubernetes_diagnose_issue` skill for failing pods 

   - Compiles a detailed diagnostic report 

3. `Analyzer` returns a complete report with several sections that include the target cluster, the time of the analysis, the issues it discovered ordered by severity, healthy resources, recommendations for remediating the issues, and a summary: 

`**Cluster Analysis Report** Cluster: kind-makdo-test Timestamp: 2024-10-06 14:30:15 **Issues Found:**` 🔴 `CRITICAL Issues: - Pod: default/crashloop-app Status: CrashLoopBackOff Reason: Container repeatedly crashing Error: Container exited with code 1 Restarts: 5 Last State: Terminated (Error) - Pod: default/image-pull-fail-abc123 Status: ImagePullBackOff Reason: Failed to pull image Error: image "nonexistent-registry.io/fake/image:v1.0.0" not found` 

_Implementing Multi-Agent Systems with A2A_ 

357 

```
Restarts:0
-Pod:default/image-pull-fail-def456
Status:ImagePullBackOff
Reason:Failedtopullimage
Error:image"nonexistent-registry.io/fake/image:v1.0.0"notfound
Restarts:0
**HealthyResources:**
-kube-system pods:Allrunningnormally
-Core services:Operational
**Recommendations:**
1.crashloop-app:Investigatecontainerstartupissue,checkapplication
logs
2. image-pull-fail deployment:Verifyimageexistsorupdatedeployment
withvalidimage
3.Considerdeletingfailingpodstoallowfreshrestartattempts
**Summary:**
-Total pods checked:15
-Critical issues:3
-Warnings:0
-Healthy:12
```

**Note** 

Since the LLM is not deterministic, the exact format may be different, but it will contain all the relevant details. 

4. `Coordinator` to `Slack_Bot` delegation happens when the `Coordinator` agent wishes to communicate idx_9e1354cfsome information to the human operator. It invokes `Slack_Bot` as a tool, providing as an argument the information to notify humans—in this case, for example, the analysis report generated earlier by the analyzer: 

```
Tool:agent_MAKDO_Slack_Bot
Arguments: {
"message":"Post this complete cluster analysis report to #makdo-devops:
              [ENTIRE ANALYZER OUTPUT]"
}
```

_Chapter 9_ 

358 

5. `Slack_Bot` sends the following request to the MCP tool: 

```
Tool:slack_post_message
Arguments: {
"channel":"makdo-devops",
"text":"[ENTIRE ANALYZER OUTPUT]"
}
```

6. The result is idx_0dcb97a1posted to Slack as the `Slack_Bot` agent uses the `slack_post_message` tool. This workflow demonstrates the complete analysis workflow: 

**Coordinator → Analyzer → k8s-ai (A2A) → Analyzer → Coordinator → Slack_Bot → MCP → Slack** 

Here’s a screenshot of the analysis report in Slack: 

_Implementing Multi-Agent Systems with A2A_ 

359 

<!-- Start of picture text -->
Hmakdo-devops @& MAkOO Alerts|Cluster Health| Ak Issues & Fives Et Bi ae<br>@ Messages {DP Addcanvas +<br>944 Cluster Analysis Report boats<br>Cluster: kind-nakdo-test<br>Timestamp: 2025-10-05 21:43:46<br>“*Issues Found:**<br>GB CRITICAL issues:<br>~ Pod: namespace/pod-name<br>Status: Pending<br>Reason: Insufficient CPU<br>Error: Pod cannot be scheduled due to lack of CPU resources<br>Restarts: 0<br>AX WARNING Issues:<br>~ Pod: namespace/pod-name<br>Status: Running<br>Reason: High Memory Usage<br>Warning: Pod memory usage exceeds 80% threshold<br>**Healthy Resources:**<br>~ Pod: kube-system/kube-proxy-xxx.<br>~ Pod: default/web-app-yyy<br>~ Deployment: default/nginx<br>**Recommendations:**<br>1. For Critical Issue: Scale the cluster or reallocate resources. Use the command:<br>kubectl scale deployment <deployment-nane> --replicas=cdesired-replicas><br>2. For Warning Issue: Consider setting resource limits or optimize pod usage. Command to set limits:<br>kubectl set resources deployment <deployment-nane> --Limitsememory=cvalue><br>**Summary:**<br>=Total pods checked: 50<br>~ Critical issues: 1<br>- Warnings: 1<br>~ Healthy: 48<br>‘The cluster currently has one critical issue involving a pending pod due to insufficient CPU resources and a warning about high memory<br>usage in another pod. Prompt actions are recommended to resolve these issues for maintaining optimal cluster performance.<br><!-- End of picture text -->

_Figure 9.2: Analysis report_ 

The preceding idx_e098ad19figure is the complete cluster analysis report posted to Slack, showing three critical issues detected: one `crashloop` pod and two pods with `ImagePullBackOff` errors. 

_Chapter 9_ 

360 

###### **Step 3 – remediation phase** 

With theidx_c3944e77 issues identified, MAKDO attempts remediation: 

```
defrun_fixer_and_post(self):
    fix_request = """
Please perform the following tasks in order:
```

`1. Use the Fixer agent to remediate the issues found in the kind-makdo-test cluster and get the COMPLETE detailed remediation report` 

```
2. Immediately forward THE COMPLETE FIXER OUTPUT to the Slack agent with this
   message: "Post this complete remediation report to #makdo-devops:
   [PASTE FULL FIXER OUTPUT HERE]"
```

```
CRITICAL: Do NOT summarize. Do NOT filter. Post the ENTIRE remediation report
exactly as the Fixer provided it.
"""
    response = self.coordinator.send_message(
        fix_request,
self.coordinator.default_model_id
    )
```

Here is theidx_745f8758 internal workflow: 

1. The `Coordinator` delegates to the `Fixer` sub-agent: 

```
Tool:agent_MAKDO_Fixer
Arguments: {
"message":"Remediate the issues found in kind-makdo-test cluster"
}
```

2. The `Fixer` executes the following actions (using k8s-ai A2A tools): 

   - For `crashloop` pod: Attempts deletion to allow a clean restart 

   - For `image-pull-fail` pods: Identifies image issue; may suggest manual intervention 

   - Executes safe operations via k8s-ai kubectl tools 

   - Verifies results after each action 

_Implementing Multi-Agent Systems with A2A_ 

361 

###### 3. `Fixer` returns complete report: 

`**Remediation Report** Cluster: kind-makdo-test **Actions Taken:** 1. **Pod: default/crashloop-app** - Action: Deleted pod to allow clean restart - Command: `kubectl delete pod crashloop-app -n default` - Result:` ✅ `Success - Details: Pod deleted successfully - Before: CrashLoopBackOff (5 restarts) - After: Terminating 2. **Pod: default/image-pull-fail-abc123** - Action: Skipped - ImagePullBackOff requires deployment fix - Reason: Image does not exist in registry - Recommendation: Update deployment with valid image 3. **Pod: default/image-pull-fail-def456** - Action: Skipped - ImagePullBackOff requires deployment fix - Reason: Image does not exist in registry - Recommendation: Update deployment with valid image **Skipped Actions:** - image-pull-fail deployment: Requires human approval to change image **Verification:** - Pods now running: 12 - Pods still failing: 2 (image-pull-fail) - Issues resolved: 1` 

_Chapter 9_ 

362 

   - `Issues requiring human attention: 1` 

   - `**Summary:** - Total actions attempted: 1 - Successful: 1 - Failed: 0 - Requires approval: 1 (deployment image update)` 

4. The `Coordinator` agent delegates to the `Slack_Bot` sub-agent (same pattern as the analysis patterns covered earlier). 

5. The complete remediation report is posted to Slack by the `Slack_Bot` agent. 

This workflowidx_b54e49b0 demonstrates MAKDO’s safety-first approach. It fixed the `crashloop` issue but correctly identified that the image-pull problem requires human intervention (changing the deployment’s image reference). 

Here is a report screenshot from another run where the LLM decided that both failures required human intervention (it is important to realize that the LLM makes intelligent decisions based idx_3190c873on the situation, so it will not always take the same actions): 

_Implementing Multi-Agent Systems with A2A_ 

363 

<!-- Start of picture text -->
Hmakdo-devops gj MAKDO Alerts| Cluster Heath | dk Issues & Fixes Ecit Gia<br>@ Messages {D Addcanvas +<br>945 Remediation Report Today »<br>Cluster: kind-nakdo-test<br>Timestamp: 2025-10-05 21:50:00 UTC<br>**Actions Taken:"*<br>1. "*Pod: default/crashloop-app"*<br>~ Action: Identified CrashLoopBackOff due to an intentional exit in the command script.<br>- Result: dh, Requires manual review to change application behavior.<br>- Before: Status - CrashLoopBackOff with repeated exits due to command sh -c ‘echo "Starting..."; sleep 2; exit 1!<br>- After: Identified as intentional behavior; further action pending redesign.<br>2. **Pod: makdo-test/unhealthy-service-65975c96de-mrtkt"*<br>- Action: Identified readiness probe failure due to a 404 HTTP return,<br>Result: dk, Requires adjustment in liveness/readiness configuration.<br>- Before: Status - CrashLoopBackOff due to probe failure on non-existing path /nonexistent.<br>~ After: Requires remediation to point to a valid endpoint for probes.<br>3. **Pod: default/image-pull-fail-d47bded75-sbxkw"*<br>~ Action: Identified ImagePullBackOff from non-resolvable registry URL.<br>~ Result: i Requires updating image source/repository.<br>- Before: Status - ImagePullBackOff from nonexistent URL nonexistent-registry.io/fake/inage:v1.0.0.<br>~ After: Pending update of image source in deployment configuration.<br>4, "Pod: makdo-test/resource-starved"*<br>- Action: Identified Pending status due to over-requested resources.<br>- Result: fy. Requires adjustment of resource requests.<br>- Before: Status - Pending with excessive CPU and Memory request.<br>~ After: Pending review and adjustment of resource requests.<br>**Skipped Actions:**<br>- No direct actions are performable without application/deployment configuration modifications.<br>**Verification:**<br>~ Pods now running: None of the identified pods require immediate running remedies as issues demand configuration changes.<br>~ Pods still failing: Multiple as identified; awaiting operational redesign.<br>= Issues resolved: 0<br>= Issues remaining: 4<br>**Summary:**<br>~ Total actions attempted: 4<br>= Successful: 0 (Identified and pending corrective configurations)<br>- Failed: 0<br>~ Requires approval: 4 (Due to configuration changes),<br><!-- End of picture text -->

_Figure 9.3: Complete remediation report_ 

Once MAKDO goes through the complete process of identifying problems, analyzing them, fixing them, and notifying the user, it ends the demo. When deployed in production, it will keep running continuously and watch for new problems. 

_Chapter 9_ 

364 

###### **Step 4 – demo complete** 

Finally, MAKDO idx_14338dd1sends a completion message: 

- `def send_demo_complete_message(self): complete_message = """` 🎉 `**MAKDO Demo Complete!** **Results:**` ✅ `Multi-agent coordination successful` ✅ `Analyzer detected cluster issues via k8s-ai` ✅ `Fixer attempted remediation` ✅ `Full autonomous DevOps workflow demonstrated **Architecture validated:** - Coordinator orchestrated all agents - Analyzer used A2A protocol to k8s-ai - Fixer executed safe remediation - Slack agent provided human visibility` 

```
Demo completed at: 2024-10-06 14:30:50
"""
    response = self.coordinator.send_message(
f"Post this completion message to #makdo-devops:\n\n{complete_message}",
self.coordinator.default_model_id
    )
```

_Implementing Multi-Agent Systems with A2A_ 

365 

Here’s a screenshot of the demo completion message in Slack: 

<!-- Start of picture text -->
& *MAKDO Demo Complete!**<br>**Results:**<br>£74 Multi-agent coordination successful<br>N4 Analyzer detected cluster issues via k8s-ai<br>04 Fixer attempted remediation<br>04 Full autonomous DevOps workflow demonstrated<br>“*Architecture validated:**<br>- Coordinator orchestrated all agents<br>- Analyzer used A2A protocol to k8s-ai<br>- Fixer executed safe remediation<br>- Slack agent provided human visibility<br>Demo completed at: 2025-10-05 21:45:21<br><!-- End of picture text -->

_Figure 9.4: Demo complete_ 

This is the idx_b90c4597final demo completion message summarizing results and validating that all agents worked together successfully to detect, remediate, and report on cluster issues. 

###### **Key observations** 

This demo validates idx_cbe9af3fseveral key MAKDO characteristics. Let’s summarize them: 

- **Complete autonomy** : From a single user request, MAKDO handled the full workflow without additional human input. The `Analyzer` agent examined the cluster. `Slack_Bot` posted the analysis to Slack. The `Fixer` agent attempted remediation. `Slack_Bot` then reported the results. The `Coordinator` agent orchestrated everything through LLM reasoning rather than fixed scripts. 

- **Protocol integration** : The demo used both major protocols effectively. A2A enabled `Analyzer` and `Fixer` to connect to the k8s-ai server for Kubernetes operations, discovering the cluster state, and executing actions. MCP let `Slack_Bot` integrate with the FastMCP Slack server, posting all reports to #makdo-devops for full visibility. 

- **Safety controls** : MAKDO operated safely throughout. It fixed low-risk issues such as deleting a `crashloop` pod. Riskier actions, such as deployment changes, required approval. Post-remediation checks verified the cluster state. All steps were reported transparently via Slack. 

_Chapter 9_ 

366 

- **Human visibility** : Every major operation generated a Slack message. The demo began with a start announcement. A full analysis report covered all three failing pods. The remediation report detailed actions taken and skipped. It ended with a completion summary. 

Humans can idx_cee017a3observe the entire workflow through Slack without needing to monitor logs or dashboards. MAKDO demonstrates that configuration-driven multi-agent systems can handle real DevOps workflows with production infrastructure while maintaining human oversight and operational safety. 

###### **Summary** 

This chapter demonstrated how to build production-ready multi-agent AI systems using MAKDO as a comprehensive example. We explored how configuration-driven architecture, where the entire multi-agent system is defined through YAML files rather than custom code, dramatically simplifies implementation while enabling powerful capabilities. MAKDO’s four specialized agents, namely the `Coordinator` , `Analyzer` , `Fixer` , and `Slack_Bot` , work together through AI-6’s `AgentTool` pattern, where sub-agents appear as tools accepting natural language messages. The system integrates two major protocols seamlessly: A2A for Kubernetes operations via k8s-ai, and MCP for human communication via Slack, with each agent specialized through carefully crafted system prompts encoding domain expertise, operational policies, and safety controls. 

The implementation validated key patterns for multi-agent systems: LLM-driven orchestration, where the `Coordinator` agent dynamically determines workflows through reasoning rather than predefined state machines; session isolation, where each agent maintains an independent conversation history; tool assignment as permission control implementing least privileges; and safety-first remediation, distinguishing between autoapproved and human approval-required operations. The end-to-end demo showed MAKDO autonomously detecting cluster issues, attempting safe remediation, and providing complete transparency through Slack notifications. This declarative approach enables rapid iteration and extension by adding agents or modifying behaviors through YAML edits rather than programming. 

MAKDO helps you manage your infrastructure, but it is a complicated system itself. When you deploy it, you’ll need to be able to test it, debug it, and troubleshoot problems. 

In the next chapter, we will cover exactly what it takes to run multi-agent systems in production safely and reliably. 

_Implementing Multi-Agent Systems with A2A_ 

367 

###### **Get This Book’s PDF Version and Exclusive Extras** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
i<br>4<br>|<br>e<br>aeé<br>[=] :<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require an invoice._ 

# 10 

##### Testing, Debugging, and Troubleshooting Multi-Agent Systems 

In the previous chapter, we built MAKDO, a complete multi-agent system for Kubernetes DevOps. We saw how the `Coordinator` , `Analyzer` , `Fixer` , and `Slack_Bot` agents work together using MCP and A2A to automate cluster health monitoring and remediation. We implemented the system, connected it to external tools such as k8s-ai and Slack via MCP, and ran it from end to end. 

Building multi-agent systems is one thing; keeping them running reliably in production is another. Multi-agent systems fail in unique ways that traditional software doesn’t. Agents hallucinate. They misuse tools. They lose context when handing work between agents. Coordination breaks down. These failures are often non-deterministic and hard to reproduce. 

This chapter covers everything you need to test, debug, and troubleshoot multi-agent systems effectively. We start by looking at common failure modes such as hallucination and coordination breakdowns. We then explore instrumentation and observability strategies that make agent behavior visible. Then, we dive deep into debugging tool use and diagnosing coordination failures between agents. Finally, we discuss designing for resilience through redundancy, graceful degradation, retry logic, and human escalation patterns. Throughout the chapter, we use MAKDO as a concrete example to illustrate these concepts in practice. 

_Chapter 10_ 

370 

The following key topics are covered: 

- Common failure modes in agentic systems 

- 

- Instrumentation and observability for AI agents 

- 

- Debugging tool use and function call chains 

- 

- Diagnosing coordination failures in multi-agent workflows 

- 

- Designing for resilience and recoverability 

So, let’s get started! 

###### **Common failure modes in agentic systems** 

Understanding how multi-agent systems fail is the first step toward building robust, production-ready agentic AI systems. Unlikeidx_2aa0e30d traditional software, where failures are typically deterministic and reproducible, AI agent failures can be subtle, context-dependent, and difficult to diagnose. Remember that every turn of a multi-agent system may involve tens or hundreds of LLM calls interleaved with tool executions, making the failure surface much larger. In addition, LLMs can introduce non-determinism, leading to inconsistent behavior across multiple runs for the exact same input. 

This section explores the most common failure patterns you’ll encounter when working with agentic systems. 

###### **Agent hallucination** 

Agent hallucination occurs whenidx_3813b776 agents generate information that appears plausible but is factually incorrect or never idx_8f067513actually happened. In agentic systems, this can be particularly dangerous because hallucinations may be embedded in tool calls, reasoning chains, or reported results. Let’s explore how it happens: 

- **Fabricated tool responses** : Agents may claim to have successfully executed a tool when they haven’t, or report results that never occurred. For example, an agent might say, “I’ve deployed the application to production” when it only executed a dry-run command, or claim, “The database query returned 1,523 records” when the query actually failed. 

In MAKDO, the `Fixer` agent might report, “Successfully restarted pod default/nginxabc123” when it actually received a timeout from k8s-ai and never confirmed the restart. The coordinator receives this fabricated success message and tells `Slack_Bot` to notify humans that the issue is resolved when the Pod is still failing. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

371 

• **Invented context** : Agents may reference files, configurations, or resources that don’t exist. An agent might say, “I checked the `config.yaml` file and found the setting,” when no such file exists in the repository. MAKDO’s `Analyzer` might hallucinate Pod names when reporting issues. It could claim, “Pod default/payment-service-7f9d8 is failing” when the actual failing Pod is named _default/payment-service-7f9d8c_ . When the `Fixer` agent tries to remediate using the hallucinated name, k8s-ai returns “pod not found,” and the actual problem goes unfixed. 

- **False correlation and causation** : Agents may incorrectly link events or actions. An agent may say, “The deployment failed because of the recent DNS change,” when the DNS change is unrelated to the actual failure cause. For example, the `Analyzer` agent might see that a Pod started failing shortly after a deployment update and conclude that the deployment caused the failure. In reality, the Pod failed because the image registry became temporarily unavailable, which is completely unrelated to the deployment. The `Analyzer` agent’s incorrect diagnosis leads the `Fixer` agent to roll back aidx_358e6858 perfectly good deployment. 

- **Synthetic data in reasoning** : During multistep reasoning, agents may introduce plausible-sounding but fictional data points that cascade through subsequent steps, leading to confident but incorrect conclusions. 

For example, when analyzing resource constraints, MAKDO’s `Analyzer` might invent memory usage numbers, such as “pod is using 2.3GB of its 2GB limit,” when k8s-ai never reported those specific metrics. This fictional data makes it into the Slack report, misleading human operators about the actual resource situation. Wrong metrics are far worse than no metrics as they can lead to damaging actions based on false information. 

Here are some mitigation strategies to reduce hallucinations: 

- Require agents to citeidx_9c80ef2e actual tool outputs rather than summarizing them 

- 

- Implement strict verification layers that check claimed actions against actual execution logs 

- Use structured outputs with explicit success/failure indicators 

- 

- Cross-validate agent claims with independent verification tools 

- 

- Log all tool executions separately from agent narratives 

- 

Add confidence scoring and uncertainty acknowledgment to agent outputs 

- 

Hallucinations are a real problem, but LLMs are getting better at reducing their occurrences, and the mitigation strategies can be used to control this. But issues with using tools become more serious as agentic AI systems extend their reach with more tools. 

_Chapter 10_ 

372 

###### **Wrong tool use and tool misuse** 

Wrong tool use happens when idx_c64cec **a** d gents call incorrect tools for the task at hand, either due to misunderstanding the tool’s purpose or misinterpreting the task requirements. This can lead to ineffective or harmful actions. Tool misuse happens when agents use the correct tools but in incorrect, inefficient, or dangerous ways. Unlike hallucination, where the agent invents information, tool misuse involves real tool executions that don’t achieve the intended goal, such as the following: 

- **Invalid tool parameters** : Agents may construct syntactically valid but semantically incorrect tool calls. For example, a deployment agent might specify the wrong cluster name or use a deprecated API version, causing silent failures downstream. Alternatively, an agent might pass a relative path when an absolute path is required. MAKDO’s `Fixer` might call k8s-ai’s `delete_pod` skill with the wrong namespace. It sends `namespace: "production"` when the failing Pod is actually `in namespace: "default"` . The k8s-ai tool succeeds (there is no Pod with that name in production), but the actual failing Pod remains untouched. The `Fixer` agent reports success, the coordinator agent moves on, and the problem persists. 

- **Tool chaining errors** : When agents need to use multiple tools in sequence, they may skip necessary intermediate steps or execute them in the wrong order. Consider a code review agentidx_35a1b6c5 that runs tests before checking out the correct branch, or a deployment agent that applies configurations before validating them. The coordinator agent might tell the `Fixer` agent to “restart the failing pod and verify it’s healthy.” The `Fixer` agent deletes the Pod via k8s-ai but never calls back to verify that the new Pod started successfully. It reports to the coordinator agent “remediation complete” without checking whether Kubernetes actually rescheduled the Pod. If the Pod can’t restart due to resource constraints, nobody notices until the next health check cycle. 

- **Inappropriate tool selection** : Agents may choose the wrong tool for the task, such as using a delete operation when an update is needed, or calling an expensive search API when a simple lookup would suffice. Agents may also not use a tool at all when one is clearly needed, or use multiple tools when one tool is sufficient. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

373 

- **Resource-intensive patterns** : Agents may use tools in ways that work but are extremely inefficient, such as making individual API calls in a loop instead of using batch operations, or repeatedly fetching the same data instead of caching it. 

- **Dangerous parameter combinations** : Agents may combine valid parameters in ways that produce unintended side effects. Setting both a force flag and a recursive flag might work individually but together cause data loss. 

Here are some mitigation strategies to reduceidx_3407781e wrong tool use and misuse: 

- Carefully curate and document tool capabilities and constraints 

- Minimize the number of available tools per agent to reduce choice complexity 

- 

- Implement strict tool input validation with semantic checks 

- 

- Create tool usage guidelines embedded in tool descriptions 

- Create tool usage guidelines embedded in tool descriptions • Add safety rails for dangerous operations (confirmation prompts, dry-run modes) 

- Monitor tool usage patterns to detect inefficient or suspicious behavior 

- 

- Use tool call validation agents that review planned actions before execution 

- 

- Implement guardrails that prevent certain parameter combinations 

- 

- Manage tool permissions and access levels carefully 

- 

- Provide example tool usageidx_4098a436 patterns in agent prompts 

- 

A combination of these mitigation strategies can significantly reduce tool use failures. 

However, even when the LLMs are not hallucinating and properly use all the tools available to them, sometimes they just don’tidx_607e2f72 properly follow the instructions. 

###### **Poor instruction following** 

Agents may misinterpret or inadequately follow user instructions, leading to incorrect or incomplete task execution. This failureidx_f62829ca mode is particularly frustrating because the agent appears to be working but produces results that don’t match what was requested. Here are some of those instances: 

• **Selective attention to instructions** : Agents may focus on part of the instructions while ignoring critical constraints or requirements. For example, a user asks to “deploy to staging and notify the team on Slack,” but the agent only deploys, forgetting the notification step. Or instructions specify “use Python 3.11” but the agent defaults to whatever version is available. The coordinator’s system prompt may say, “Always post detailed results to Slack after Analyzer and Fixer complete.” But when processing a health check, the coordinator calls `Analyzer` , receives the report, and then immediately calls `Fixer` without posting to Slack. 

_Chapter 10_ 

374 

It only remembers to notify humans after all remediation finishes, so the team doesn’t see what issues were found until after fixes are attempted. 

   - **Over-generalization** : Agents may interpret specific instructions too broadly. When asked to “fix the bug in the login function,” an agent might refactor the entire authentication system, introducing unnecessary changes and potential new issues. 

   - **Under-generalization** : Conversely, agents may interpret instructions too narrowly. Asked to “update all configuration files,” an agent might only update files with a `.config` extension, missing `.yaml` , `.json` , or `.toml` files that also contain configuration. 

   - **Ignoring implicit requirements** : Experienced developers understand implicit constraints that agents may miss. “Add a new API endpoint” implicitly means adding tests, documentation, and proper error handling, but an agent might only add the bare minimum endpoint code. 

   - **Lost instructions in long conversations** : As conversations grow longer, agents may lose track of earlier instructions or constraints. Initial requirements such as “maintain backward compatibility” or “follow the existing naming conventions” may get forgotten as the agent focuses on more recent messages. 

   - **Ambiguity mishandling** : When instructions are ambiguous, agents may make assumptions without seeking clarification. “Make it faster” could mean optimizing runtime, reducing latency, or improving throughput, but the agent picks one interpretation without confirming. 

   - **Priority confusion** : When given multiple tasks or constraints, agents may fail to understand which are critical and which are optional. “Deploy the fix quickly, but make sure tests pass” might lead an agent to skip tests in favor of speed, when test passing should beidx_fd59528b non-negotiable. 

- Here are some mitigation strategies to improveidx_fe12e391 instruction following: 

   - Break complex instructions into explicit, numbered steps 

   - Use structured formats such as checklists or requirement lists 

   - 

   - Include both positive instructions (“do X”) and negative constraints (“don’t do Y”) 

   - 

   - Repeat critical constraints throughout long conversations 

   - Repeat critical constraints throughout long conversations • Ask agents to confirm their understanding before execution 

   - Provide examples of correct and incorrect outcomes 

   - 

   - Use explicit priority markers (“MUST,” “SHOULD,” “MAY”) for requirements 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

375 

- Implement instruction verification agents that check task plans against original requests 

- Maintain a “requirements context” that persists across conversation turns 

- 

- Use structured prompts with dedicated sections for constraints, goals, and success criteria 

Instruction following is a major focus of LLM providers, and they invest a lot of effort in training because it is so critical. With the addition of robust mitigation strategies, you can arrive at a reliable system that follows instructions properly. But even when following the instructions properly, sometimes agentic AI systems can get into a state of constant churn without converging on a final response and just keep calling more and more tools with no end. 

###### **Infinite loops and runaway agents** 

Agentic systems can enteridx_4c6826f4 infinite loops when agents repeatedly idx_ **a** 5b49d47 ttempt the same failed action or get stuck in circular reasoning patterns, such as the following: 

- **Retry loops without learning** : An agent encounters an error, retries the same operation with identical parameters, fails again, and repeats indefinitely. This is common when agents don’t maintain memory of previous attempts or don’t analyze why an operation failed. 

For example, MAKDO’s `Fixer` tries to delete a Pod that doesn’t exist (maybe it was already deleted). k8s-ai returns “pod not found.” The `Fixer` agent interprets this as a transient error and retries the same delete command. It fails again. The `Fixer` agent keeps retrying without realizing that the Pod is already gone, burning through API tokens until it hits the retry limit. 

- **Circular delegation** : In multi-agent systems, agents may delegate tasks back and forth without making progress. For example, Agent A asks Agent B for help, Agent B determines Agent A is better suited, and they loop endlessly. Note that this is not an issue with hierarchical delegation, where a parent agent always delegates to a child agent. 

- **Resource exhaustion** : Runaway agents can consume excessive API tokens, make thousands of tool calls, or generate massive amounts of log data, leading to cost overruns and system instability. For example, a bug in MAKDO’s health check loop causes it to start a new health check every second instead of idx_c31a5a23every 60 seconds. Each check calls `Analyzer` , which makes multiple k8s-ai requests. Within minutes, MAKDO makes idx_1ed4d677thousands of LLM calls, analyzing the same cluster state repeatedly. The OpenAI API bill skyrockets and the k8s-ai server logs fill up the disk. 

_Chapter 10_ 

376 

Here are some mitigation strategies to prevent infinite loops and runaway agents: 

- Implement maximum iteration limits with exponential backoff 

- 

- Track agent action history and detect repeated patterns 

- 

- Use circuit breakers that halt execution after consecutive failures 

- 

- Monitor resource consumption with alerts and automatic cutoffs 

- 

- Implement explicit termination criteria in agent prompts 

- 

- Add budgets where agents can only spend up to a reasonable amount 

Utilizing these strategies can ensure that single agents don’t get stuck. In multi-agent systems, even if every agent functions well on its own, there are systemic issues that happen when communication or coordination between the agents fails. 

###### **Communication and coordination breakdowns** 

Multi-agent systems depend onidx_ae17da59 effective communication between agents. When this communication breaks down, the entire system can fail. The following points explore how it happens: 

- **Message format incompatibility** : Agents may produce outputs in formats that other agents can’t parse. For example, one agent outputs JSON while another expects YAML, or field names don’t match between the sender and receiver. 

- **Lost context in handoffs** : When tasks are delegated between agents, critical context from earlier interactions may be lost. For example, a support agent hands off to a technical agent but forgets to include the customer’s account details or previous troubleshooting steps. 

Another example is theidx_26bf4c35 coordinator tells `Analyzer` , “Check cluster health.” `Analyzer` finds three failing Pods and returns a detailed report with Pod names, namespaces, and error messages. The `Coordinator` agent then tells the `Fixer` agent, “Fix the issues,” without passing along which specific Pods need fixing. `Fixer` has to call k8s-ai again to rediscover the failing Pods, doubling the diagnostic work and wasting tokens. 

- **Race conditions** : When multiple agents work concurrently on related tasks, they may interfere with each other. For example, two deployment agents might simultaneously modify the same configuration, or multiple agents might lock resources that each other need. 

Another example is two MAKDO instances running simultaneously (maybe started by mistake). Both coordinators call their `Analyzer` agents for the same cluster. Both `Analyzer` agents identify idx_4acd55d5the same failing Pod. Both coordinators tell their `Fixer` agents to delete it. Both `Fixer` agents call k8s-ai to delete the Pod. The first one succeeds, 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

377 

while the second gets “pod not found.” The second `Fixer` reports failure to its coordinator, which posts an error to Slack saying “remediation failed,” when actually, the Pod was successfully deleted by the first instance. 

- **Conflicting objectives** : Different agents optimizing for different goals can work at cross-purposes. For example, a cost optimization agent scales down resources while a performance agent scales them up. 

Here are some mitigation strategies toidx_4ada0477 improve communication and coordination: 

- Define strict message schemas with validation 

- 

- Use structured handoff protocols that include mandatory context fields 

- 

- Implement distributed coordination mechanisms such as locks or consensus protocols 

- Establish clear agent hierarchies and conflict resolution policies 

- 

- Maintain a shared state that all agents can access 

- 

Complex multi-agent systems often need to trade off accuracy and quality with speed and cost. This can affect single agents too, but in multi-agent systems, delays compound. If the response is too slow, it may be too late, or the user experience is not pleasant. Let’s see how we can address these concerns. 

###### **Timeout and latency issues** 

Real-world agentic systems operate idx_86e1b901under time constraints, and latency problems can cascade through the system: 

- **Tool execution timeouts** : External tools may take longer than expected, causing agents to time out or make decisions based on incomplete information. For example, a database query runs slowly, a deployment times out, or an API call hangs. 

- **Cascading delays** : When agents depend on each other, delays compound. If Agent A waits 30 seconds for Agent B, which waits 30 seconds for Agent C, which takes 30 seconds to respond, the user experiences unacceptable 90+ second response times. 

- **Stuck agents** : An agent may be waiting for a response that will never come—a webhook that never fires, a file that’s never created, or a message that’s lost in transit. 

_Chapter 10_ 

378 

Here are some mitigation strategies to handle timeout and latency issues: 

- Set realistic timeouts for every tool and agent interaction 

- 

- Run independent tasks in parallel to reduce overall latency 

- 

- Implement async patterns where agents don’t block on slow operations 

- 

- Add progress indicators and partial result streaming 

- 

- Design for graceful degradation when operations time out 

- Use timeout-aware retry logic with backoff 

- 

- Consider stamping data passed between agents with a TTL so stale data is refreshed 

OK, we have mitigated timeouts and latency issues, but the story is not over. LLMs are stateless, but agentic AI systems are stateful. Managing this state is not trivial. 

###### **State management and consistency errors** 

Maintaining a consistent state across multiple agents and tool executions is challenging: 

- **Stale state** : Agents make decisions based on outdated information. For example, an agent checks whether a deployment is ready. It succeeds initially, but by the time the agent takes the next action, the deployment has run into problems. 

- **State synchronization failures** : In distributed systems, different agents may have different views of the current state. For example, Agent A believes a resource exists while Agent B sees it as deleted. 

- **Partial failures** : When a multistep operation fails midway, the system may be left in an inconsistent state. For idx_3f301db8example, half of the infrastructure is provisioned, or some configurations are applied, while others aren’t. 

- **Memory leaks and context bloat** : As conversations grow longer, agents may accumulate too much context, leading to degraded performance or exceeding token limits. 

Here are some mitigation strategies to improve state management and consistency: 

- Implement transaction-like patterns with rollback capabilities 

- 

- Use version numbers or timestamps to detect stale state 

- 

- Employ distributed state management systems 

- 

- Implement periodic state reconciliation 

- 

- Set context window limits and implement intelligent context pruning 

- Break down complicatedidx_22ee3cab tasks into smaller, manageable sub-tasks that can be handled by separate agents 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

379 

###### **Security and permission failures** 

Agentic systems often operate with elevated privileges, making security failures particularly dangerous, such as in theidx_422f6e62 following ways: 

- **Permission escalation** : Agents may attempt operations they shouldn’t have access to, either through misconfiguration or by learning to exploit tools in unintended ways 

- **Credential exposure** : Agents might inadvertently log, transmit, or expose sensitive credentials in error messages or tool outputs 

- **Malicious input exploitation** : Carefully crafted user inputs can manipulate agent behavior, causing them to execute unintended operations or bypass safety checks 

- **Audit trail gaps** : Without proper logging, it may be impossible to determine what actions agents took, making security investigations difficult 

Here are some mitigation strategies to enhance security and permissions. 

Most of them are general best practices for any system, but they are especially critical in agentic systems: 

- Implement the principle of least privilege for all tool access 

- 

- Add explicit permission checks before high-stakes operations 

- 

- Sanitize and validate all inputs to agents 

- 

- Never include credentials in agent prompts or tool parameters 

- 

- Maintain comprehensive audit logs of all agent actions 

- 

- Use human-in-the-loop approval for sensitive operations 

- 

As you can see, there are many ways multi-agent systems can fail. By understanding these common failure modes, you can design more robust agents, implement effective monitoring, and build troubleshooting strategies to quickly diagnose and resolve issues when they arise. Another important aspect is observability. 

###### **Instrumentation and observability for AI agents** 

Observability is crucial for understanding what’s happening inside your agentic AI systems. Unlike traditional software, where idx_a935ad83you can step through code with a debugger, AI agents operate through a series of LLM calls, tool executions, and state transitions that can be difficult to trace. Effective instrumentation transforms these “black box” systems into “glass box” systems where you can see exactly what’s happening at every step. 

_Chapter 10_ 

380 

As explored in _From Black Box to Glass Box: LLM Observability in Action_ ( `https://medium.com/ @the.gigi/from-black-box-to-glass-box-llm-observability-in-action-150266e995d2` ), comprehensive observability requires capturing multiple layers of information, which include the prompts sent to LLMs, the responses received, the tools invoked, the intermediate reasoning steps, and the final outcomes. 

In this section, we’ll explore best practices for instrumenting agentic systems, including core observability primitives, structuredidx_918aac7a logging formats, specialized LLM observability tools, key metrics to track, real-time monitoring strategies, debugging techniques, and privacy considerations. 

###### **Core observability primitives** 

Building observable agentic systems starts with instrumenting the fundamental operations. Let’s break down the key observability primitives you should capture. 

###### **LLM call tracing** 

Every interaction with an LLM should be logged with complete context, including the full prompt, model parameters (temperature, max tokens, etc.), the complete response, token usage, latency, and any errors. This creates an audit trail of all AI decisions. 

For MAKDO, you want to capture every LLM interaction across all four agents. When the coordinator decides to idx_ **c** 57adf6a all `Analyzer` , log the coordinator’s prompt (including the system message and conversation history), the model used (GPT-4o), the tool call it generates ( `agent_MAKDO_Analyzer` with a specific message), token counts, and latency. Do the same for `Analyzer` ’s interactions with its LLM when it processes the request. This creates a complete decision trail showing why MAKDO took each action. 

###### **Tool execution logs** 

Capture every tool invocation idx_a9a31157with input parameters, execution duration, output results, and success/failure status. Include stack traces for errors and context about why the tool was called. 

In MAKDO, log every A2A call from `Analyzer` and `Fixer` to k8s-ai. Capture the skill name ( `kubernetes_resource_health` ), parameters ( `cluster name` , `namespace` ), the complete response from k8s-ai, and timing. Also log `Slack_Bot` ’s MCP tool calls ( `slack_post_message` with channel and message content). When debugging, you can reconstruct exactly what data each agent sent to external systems and what responses they received. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

381 

###### **Agent state snapshots** 

Periodically capture the agent’s internal idx_ede33c2dstate, including working memory, conversation history, accumulated context, and decision-making rationale. This helps with understanding how the state evolves over time. In the case of computer use or browser automation, capture screenshots after each agent action. 

###### **Span and trace hierarchies** 

Organize logs into hierarchical traces idx_f3de1d21where a user request creates a parent span, and each agent action (LLM call, tool execution, and sub-agent delegation) creates child spans. This mirrors distributed tracing in microservices. 

A MAKDO health check creates this span hierarchy: 

Health check (root) → Coordinatoridx_abb53d8a LLM call → `agent_MAKDO_Analyzer` tool call → `Analyzer` LLM call → `kubernetes_resource_health` A2A call → `Analyzer` LLM call (processing results) → `agent_MAKDO_Slack_Bot` tool call → `slack_post_message` MCP call 

Each span has timing and a status. If the Slack notification fails, you can trace backward through the hierarchy to see exactly which calls succeeded and where the failure occurred. 

###### **Metadata enrichment** 

Tag every operation withidx_a3c729ff contextual metadata, such as user ID, session ID, agent type, task category, and environment (dev/staging/prod). This enables filtering and analysis across dimensions. 

Tag MAKDO operations with `cluster_name: “kind-makdo-test”` , `health_check_cycle: 47` , `agent_type: “analyzer”` , and `operation_type: “diagnostics”` . When you need to debug why `Analyzer` keeps misidentifying Pods, query for all `Analyzer` diagnostics operations on that specific cluster and examine patterns across multiple health check cycles. 

###### **Structured logging and trace formats** 

Raw logs are difficult to query and analyze. Structured logging makes observability data queryable and actionable. This is best practice for any production-grade system but especially important for complex idx_ef21227dagentic AI systems. Most languages have mature libraries for structured logging (e.g., `structlog` for Python, `Winston` for Node.js, and `Logrus` for Go). Take advantage of these libraries to emit structured logs consistently. Here are some recommended practices to follow: 

- **JSON-structured events** : Emit logs as structured JSON with a consistent schema, including timestamp, trace ID, span ID, parent span ID, event type, and event-specific fields. This enables efficient querying and aggregation. 

_Chapter 10_ 

382 

- **Standardized event types** : Define a taxonomy of events, such as `agent.start` , `agent.complete` , `llm.request` , `llm.response` , `tool.invoke` , `tool.complete` , and `error.occurred` . Consistent event types enable automated analysis. 

- **Correlation IDs** : Use correlation IDs to link related operations across agents, services, and systems. A single user request should have one correlation ID that flows through the entire system. 

- **Semantic versioning for schemas** : As your observability schema evolves, version it so you can parse historicalidx_a92a4433 logs and maintain backward compatibility in analysis tools. 

###### **LLM-specific observability tools** 

Several specialized tools idx_32006ddehave emerged for observing LLM-based systems: 

- **Datadog LLM Observability** : Datadog provides dedicated LLM observability capabilities that automatically capture and visualize LLM interactions. It tracks prompt templates, model invocations, token usage, latency metrics, and cost analysis across multiple LLM providers. Datadog’s LLM Observability integrates with popular frameworks such as LangChain and LlamaIndex, providing out-of-the-box instrumentation for agentic applications. It enables tracking of multi-turn conversations, agent workflows, and tool usage patterns with minimal code changes. I implemented an LLM idx_0b5ea2d8observability solution using OpenTelemetry ( `https:// opentelemetry.io/` ) and Datadog LLM Observability at Invisible Platforms ( `https:// getinvisible.com/` ), acquired by Perplexity. It wasidx_2babb07e invaluable for diagnosingidx_422caa83 gnarly issues and performance bottlenecks. Key features include the following: 

   - Automatic prompt and completion capture 

   - Token usage and cost tracking per request 

   - 

   - Latency percentiles and performance analysis 

   - Error rate monitoring and alerting 

   - 

   - Integration with existing APM and infrastructure monitoring 

   - 

- **LangSmith** : LangChain’s idx_0d18674dobservability platform provides detailed traces of LangChain applications, including agent reasoning chains, tool usage, and retrieval steps. It offers a visual interface for exploring traces and debugging agent behavior. 

- **Weights & Biases (WB)** : Offers idx_32084cceprompt tracking, model performance monitoring, and experiment comparison for LLM applications. It is particularly useful for tracking prompt engineering iterations and A/B testing different agent configurations. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

383 

- **Helicone** : Provides real-time monitoring, caching, and analytics for LLM APIs. Tracks costs, latency, and success rates across multiple LLM providers with a unified interface. 

- **Custom instrumentation frameworks** : Many teams build custom observability layers using OpenTelemetry as a foundation, adding LLM-specific context and metadata to standard distributed tracing. 

###### **Metrics and KPIs for agent performance** 

You can’t manageidx_f62032c2 what you don’t measure. Define quantitative metrics to track agent health and performance, establishing baselines for normal operation and detecting when things go wrong. These metrics serve multiple purposes: they help you understand system behavior, justify infrastructure investments, optimize costs, and prove value to stakeholders. 

**Success rate metrics** tell you whether your agents idx_076e **a** a92 re actually completing their assigned tasks. A declining task completion rate might indicate prompt drift, environmental changes, or degraded tool reliability. Theidx_c426b1ab following are example success rate metrics: 

- Task completion rate (percentage of tasks successfully completed) 

- 

- First-attempt success rate (completed without retries) 

- 

- Tool call success rate (percentage of tool invocations that succeed) 

- 

**Performance metrics** reveal how fast your system responds and how efficiently agents operate. High LLM call counts per task idx_50a36e38might indicate inefficient reasoning patterns or unnecessary retries that inflate costs and latency. The following are example performance metrics: 

End-to-end latency (user request to final response) 

- 

- LLM call latency (p50, p95, p99 percentiles) 

- 

- Tool execution latency 

- 

- Number of LLM calls per task 

- 

- Number of tool calls per task 

- 

**Cost metrics** are critical for idx_4082a70dproduction systems where token usage directly translates to cloud bills. A sudden spike in cost per request could indicate runaway agents, inefficient prompts, or agents using more expensive models than necessary. The following are example cost metrics: 

- Token usage per request (prompt tokens + completion tokens) 

- 

- Cost per request (based on model pricing) 

- 

- Cost per successful task completion 

- 

- Cost efficiency (successful completions / total cost) 

- 

_Chapter 10_ 

384 

**Quality metrics** assess whether agents are producing correct, useful outputs. These are often harder to measure automatically idx_d8a0fa0abut are crucial for understanding real-world performance beyond simple success/failure. The following are example quality metrics: 

- Hallucination rate (detected fabricated information) 

- 

- Instruction following accuracy 

- Output format compliance 

- 

- User satisfaction scores (if available) 

- 

**System health metrics** provide early warning signals of degradation. A rising timeout rate might precede a complete systemidx_962161c0 failure, giving you time to investigate and remediate before users are severely impacted. The following are example system health metrics: 

- Error rate by error type 

- Timeout rate 

- Retry rate 

- 

- Circuit breaker activations 

- 

###### **Real-time monitoring and alerting** 

Passive observability isn’t enough, as collecting metrics that you only look at after something breaks is like installing security cameras and only watching the feed after the robbery. You need active monitoring idx_c5fe2 **a** 98 nd alerting that catches problems before they impact users. The goal is to shift from reactive firefighting to proactive problem detection. Let’s discuss some of the best ways to detect these problems: 

- **Anomaly detection** helps you catch problems you didn’t anticipate. Automatically detect unusual patterns such as sudden spikes in error rates, abnormal latency increases, or unexpected tool usage patterns. Use statistical baselines (such as standard deviations from the mean) or machine learning models to identify anomalies. This is especially valuable for agentic systems where failure modes can be unpredictable and context-dependent. 

- **Threshold-based alerts** are your safety net for known critical conditions. Set alerts for critical thresholds such as the error rate exceeding 5%, average latency exceeding 10 seconds, or cost per hour exceeding budget limits. These should be carefully tuned to minimize false positives while ensuring no real incidents slip through. Too many noisy alerts lead to alert fatigue, where teams ignore notifications. 

- **Trend analysis** reveals slow-moving problems before they become crises. Track metrics over time to identify gradual degradation. A slowly increasing average latency or declining success rate might indicate underlying issues before they become critical. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

385 

This “boiling frog” scenario is particularly dangerous because no single data point triggers an alert, but the cumulative effect significantly degrades user experience. 

- **Cost runaway detection** is essential for LLM-based systems where costs can spiral out of control. Monitor token usage and costs in real time to detect runaway agents before they consume your entire budget. Alert when hourly spending exceeds expected patterns, especially during off-peak hours when you expect lower usage. A production incident at 2 A.M. that causes infinite loops can rack up thousands of dollars before anyone notices without proper cost monitoring. 

- **Integration with incident management** ensures alerts reach the right people at the right time. Connect idx_98adc40eobservability tools to incident management systems such as PagerDuty or Opsgenie for on-call alerting and escalation. Define escalation policies so critical alerts don’t get lost in Slack channels, and ensure someone is always accountable for responding to production issues. 

Now, armed with solid observability data, let’s see how to debug our agentic AI system. 

###### **Debugging with observability data** 

Observability data is most valuable when it enables effective debugging. The difference between a system that collects i **d** x_f8bfd891 ata and one that enables debugging is whether engineers can quickly answer questions such as, “Why did this specific request fail?” or “What changed between yesterday and today?” Good observability data should make root cause analysis feel like detective work with all the clues laid out, not like searching for a needle in a haystack. 

**Trace replay** is your time idx_67d13915machine for understanding agent behavior. Capture complete traces so you can replay agent executions to understand exactly what happened. Include all prompts, responses, tool calls, and intermediate states to reconstruct the exact sequence of events. This is invaluable when debugging non-deterministic failures as you can see the actual prompts and responses that led to the failure, not just your assumptions about what should have happened. 

**Contextual search** transforms raw logs **i** dx_3b590b62 nto queryable knowledge. Enable searching logs by user request, error message, agent type, or any metadata field. “Find all failed deployments from Agent X in the last hour” should be a simple query, not a complex log parsing exercise. Structured logging with consistent metadata makes this possible; invest time in instrumenting properly and you’ll save exponentially more time during debugging. 

**Correlation analysis** helps you i **d** x_dfb7fe0f iscover hidden relationships in your data. Analyze relationships between metrics: does increasing the prompt length correlate with higher error rates? Do certain tools have higher latency than others? Does the time of day affect success rates? These insights often reveal optimization opportunities or lurking bugs that aren’t obvious from looking at individual metrics in isolation. 

_Chapter 10_ 

386 

**Comparative debugging** is especially idx_71ae3696powerful for intermittent issues. Compare successful and failed executions side by side to identify differences. What did successful agents do that failed agents didn’t? Did they use different tools, make fewer LLM calls, or process different input formats? This technique often reveals the critical difference that determines success or failure. 

**Time-series visualization** makes patterns visible that are invisible in tabular data. Visualize metrics over time with tools such as idx_a3434253Grafana or Datadog dashboards. Spot patterns, anomalies, and trends visually—humans are much better at recognizing visual patterns than scanning through columns of numbers. A sudden spike in latency or a gradual increase in error rates becomes immediately obvious in a well-designed dashboard. 

###### **Privacy and security considerations** 

Comprehensive observabilityidx_bf4b48c8 introduces the risk of leaking sensitive information if not handled properly. A data breach of your observability system could expose customer data, business secrets, or security vulnerabilities. This tension between visibility and security must be carefully balanced through the following: 

- **Personally identifiable information** ( **PII** ) **redaction** should be automatic and enforced at the instrumentation layer, not left to manual effort. Automatically redact PII from logs. Usernames, addresses, email addresses, credit card numbers, social security numbers, and other sensitive data should never appear in logs. Use regular expressions or machine learning-based detection to identify and redact PII before logs are written. Better yet, design your instrumentation to never capture PII in the first place by logging only identifiers such as user IDs that can be correlated with customer data through authorized, audited lookups. 

- **Prompt sanitization** requires careful consideration of what you log. Be cautious about logging full prompts if they contain user data or sensitive business information. Consider logging only sanitized or anonymized versions, or logging prompts separately with stricter access controls. For high-security applications, you might hash prompts and only store the hash, allowing you to detect duplicate issues without exposing the actual content. 

- **Access controls** should follow the principle of least privilege. Restrict access to observability data based on roles, as not everyone should see production logs containing customer i **d** x_f584e8b5 ata. Engineers might need access to debug issues, but that access should be logged and auditable. Consider implementing break-glass procedures for emergency access with automatic notifications to security teams. Some organizations maintain separate observability systems for different security tiers. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

387 

- **Retention policies** must balance competing needs. Define how long to retain observability data, balancing debugging needs with storage costs and compliance requirements. Recent data should be immediately available, but older data might be archived in cheaper storage or aggregated to reduce volume. Many regulations require specific retention periods or maximum retention limits, so ensure your policies comply with applicable rules. 

- **Compliance** isn’t optional. Ensure observability practices comply with regulations such as GDPR, HIPAA, SOC2, or other standards, depending on your domain and jurisdiction. This includes data residency requirements (where data can be stored), data processing agreements with observability vendors, and the right to deletion for customer data. Document your observability practices as part of compliance audits, and review them regularly as regulations evolve. 

With a robust observability infrastructure in place, you have the foundation for effective debugging. Now let’s dive into the specific challenge of debugging tool use and function call chains, which is one of the most common and frustrating debugging scenarios in agentic systems. 

###### **Debugging tool use and function call chains** 

Tool use is where agents interact with the real world, and it’s also where things most frequently go wrong. Anidx_91b2823e agent might call the wrong tool, pass invalid parameters, misinterpret tool results, or idx_1d3a820fchain tools together incorrectly. Unlike pure reasoning errors that stay within the LLM, tool use failures have real consequences: failed deployments, incorrect database updates, or broken integrations. Debugging these issues requires understanding both what the agent intended to do and what actually happened. 

###### **Understanding the tool call life cycle** 

- Let’s review again how AI idx_4c36e46asystems, AI frameworks, agents, and LLMs interact with tools and consider the failure modes. Every tool invocation goes through a predictable life cycle, and failures can occur at each stage: • The agent decides which tool to call based on its understanding of the task and available tools. This decision can go wrong if tool descriptions are ambiguous, if the agent misunderstands the task, or if multiple tools seem equally applicable. 

   - The agent constructs parameters for the tool call, translating its abstract intent into concrete arguments. Parameter construction fails when the agent lacks necessary information, misunderstands parameter semantics, or generates syntactically valid but semantically incorrect values. 

_Chapter 10_ 

388 

- The host AI system validates and invokes the tool, checking parameters against schemas and executing the actual operation. Validation can catch obvious errors, but semantic issues slip through. The tool execution itself might fail due to external factors: API timeouts, permission errors, or resource unavailability. 

- The tool returns results that the agent must interpret. Even successful tool calls can cause problems if the agent misinterprets results, ignores important warnings, or fails to verify that the operation achieved its intended effect. 

Understanding this life cycle helps you pinpoint where failures occur. A tool call that never happens indicates a decision problem. A tool call with invalid parameters indicates a construction problem. A tool idx_ **c** b5325ec c all that executes but doesn’t achieve its goal indicates an interpretation problem. 

###### **Tracing function call chains** 

Multistep agent workflows create chains of tool calls where each agent invokes the next agent as a tool call that depends on previous results. These chains canidx_a113fda9 become complex quickly: 

- **Linear chains** are the simplest: Tool A → Tool B → Tool C. Debugging linear chains means verifying each step and ensuring context flows correctly between steps. A break anywhere in the chain causes downstream failures. 

- MAKDO’s typical workflow is a linear chain. 

- 

<!-- Start of picture text -->
| Sse UAEDO Ane Pp | am FD | erminnsorrie Pp | drt snd ap em ADO st mene<br><!-- End of picture text -->

_Figure 10.1: MAKDO typical workflow_ 

If the Slack notification never arrives, trace backward: Did `Slack_Bot` get called? Did it receive the correct message? Did the MCP tool execute? Was the Slack API token valid? Each link in the chain must succeed for the full workflow to complete. 

- **Conditional chains** branch based on intermediate results: Tool A → (if success: Tool B, if failure: Tool C). The agent must correctly interpret results and choose the right path. Debugging requires understanding both the branching logic and whether the condition was evaluated correctly. Remember that all the decisions are made by the LLM, so prompt design is critical to induce the correct logic. 

The coordinator makes conditional i **d** x_17c26c82 ecisions based on `Analyzer` results. If `Analyzer` reports `CrashLoopBackOff` , call `Fixer` . If it reports `ImagePullBackOff` , skip `Fixer` and 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

389 

escalate to humans via `Slack_Bot` . If the coordinator consistently chooses the wrong branch (calling `Fixer` for `ImagePullBackOff` ), the problem is in its system prompt or how it interprets `Analyzer` ’s report structure. 

- **Parallel chains** execute multiple tools concurrently: (Tool A + Tool B + Tool C) → Tool D. This is more efficient but introduces coordination challenges. Did all parallel operations complete? Did any fail? How did the agent aggregate results before proceeding to Tool D? 

- **Recursive chains** involve agents calling themselves as tool calls (e.g., AI-6 sub-agents) or creating cycles: Tool A → Tool B → Tool A (with different parameters). These can be powerful but are prone to infinite loops if termination conditions aren’t carefully managed. 

When debugging chains, trace backward from the failure point. Which tool call failed? What were its inputs? Where did those inputs come from? This archaeological approach often reveals that the root cause occurred several steps earlier in the chain. 

Let’s look at some common tool use anti-patterns and debugging strategies. 

###### **Common tool use anti-patterns** 

Here are some patterns of tool misuse that are common in agentic systems. Recognizing these anti-patterns helps you quickly identify likely root causes: 

- **Zombie parameters** : The agent includesidx_8f58d815 parameters that the tool ignores or doesn’t recognize. This often happens when tool APIs change but agent prompts aren’t updated, or when the agent hallucinates parameters based on similar tools. Zombie parameters are insidious because the tool call “succeeds” but doesn’t behave as expected. 

For example, `Fixer` calls k8s-ai’s `delete_pod` with an extra parameter: `force: true` . k8s-ai doesn’t support a force parameter (it’s not exposed via the A2A interface). k8s-ai ignores it and performs a normal delete. `Fixer` thinks it did a forced delete but it actually did a graceful delete. When debugging why Pods take 30 seconds to terminate, you discover that the force flag isn’t working because k8s-ai silently ignores it. 

- **Premature optimization** : The agent tries to do too much in a single tool call, passing complex nested structures or trying to perform multiple operations at once. This makes debugging harder and often fails because the tool doesn’t support the complex use case. Breaking operations into smaller, simpler tool calls is usually more reliable. This is common with sophisticated CLI tools with a large number of commands and options, such as kubectl, `git` , or `bash` (which can run any other command installed on the host, including installing new commands). 

_Chapter 10_ 

390 

For example, `Analyzer` tries to i **d** x_2ee30fa2 iagnose all Pods in all namespaces with a single k8s-ai call, passing a complex query structure. k8s-ai returns partial results or times out. A better approach would be to call `kubernetes_resource_health` once per namespace and aggregate the results in `Analyzer` . This results in simpler tool calls, more reliable execution, and easier debugging when one namespace fails. 

- **Assumed state** : The agent assumes resources exist or are in a certain state without verifying. It tries to update a file that doesn’t exist, deploy to a cluster that’s offline, or query a database table that hasn’t been created yet. Always verify preconditions before executing operations if possible. 

- **Ignored errors** : The agent receives an error response from a tool but continues as if the operation succeeded. This happens when agents are over-optimized for happy paths and don’t properly handle error responses. Failures cascade as subsequent tools operate on data that doesn’t exist or is in an invalid state. 

- **Retry madness** : The agent retries a failed operation repeatedly without changing anything. This is sometimes correct when waiting for the previous operation to complete. However, if a tool call fails due to invalid parameters, retrying with the same parameters will fail again. Effective retries require either changing parameters, waiting for external conditions to change, or using a different approach entirely. 

Let’s look at strategies to debug and prevent these issues. 

###### **Debugging strategies for tool use** 

When tool calls go wrong, we needidx_01fe1741 a systematic approach for debugging them. The following strategies are effective: 

- **Replay with inspection** : Capture the exact tool call (name, parameters, and context) and replay it in isolation. Does it succeed outside the agent? If so, the problem is how the agent is calling it. If not, the problem is with the tool itself or its dependencies. 

- **Parameter validation** : Independently verify that each parameter makes sense. Don’t just check types—verify semantics. Is this file path valid? Does this cluster name exist? Is this ID formatted correctly? Create validation tools that agents can call before executing risky operations or write wrappers with validation logic and expose the wrappers as tools. 

- **Result verification** : After successful tool calls, verify that the operation achieved its intent. An API might return “200 OK” but not actually perform the operation due to business logic errors. Have agents explicitly check that resources were created, files were written, or configurations were applied. Again, this can be done in a wrapper tool that performs verification after calling the real tool. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

391 

- **Diff analysis** : Compare failed tool calls with successful ones. What’s different? Parameters? Timing? Context? Environmental factors? Often, the difference reveals the root cause. 

- **Tool shadowing** : Implement shadow tools that log calls without executing them. Use these during development toidx_3bd67b50 verify agents are calling tools correctly before allowing real operations. This is especially valuable for destructive operations such as deletions or deployments. 

In order to reduce the incidence of tool use errors, consider building guardrails into your agentic AI systems. 

###### **Building tool use guardrails** 

Prevention is better than debugging. Youidx_0e3626a4 should build guardrails that catch tool use errors before they cause problems. Here are some effective guardrails: 

- **Schema validation** : Enforce strict parameter schemas and reject invalid tool calls before execution. Use JSON Schema or similar validation to catch type errors, missing required fields, or values outside allowed ranges. 

- **Dry-run modes** : Support dry-run or preview modes for all destructive operations. The agent can call the tool with `dry_run=true` to see what would happen without actually doing it. This catches many errors before they impact production. 

- **Confirmation prompts** : For high-stakes operations, require explicit confirmation. The agent describes what it’s about to do and must confirm before execution. This creates a natural breakpoint for human-in-the-loop review. 

- **Tool compatibility checks** : When agents chain tools together, verify that output formats match input requirements. If Tool A returns JSON but Tool B expects YAML, catch this incompatibility before execution. 

- **Rate limiting and circuit breakers** : Prevent runaway tool use by limiting how many times a tool can be called within a time window. If an agent calls the same tool 50 times in a minute, something is wrong. It should halt execution and alert the human who will investigate. 

We have covered in depth how to diagnose, debug, and build guardrails to address tool use problems. Let’s consider how to i **d** x_f1860f79 iagnose coordination failures, which are prevalent in multiagent systems. 

_Chapter 10_ 

392 

###### **Diagnosing coordination failures in multi-agent workflows** 

Multi-agent systems derive their power from coordination. Multiple agents work together to accomplish complex tasks idx_cedffb1ethat no single agent could handle alone. However, this coordination introduces new failure modes that are challenging to diagnose. Unlike single-agent failures that have clear root causes, coordination failures often emerge from the interactions between agents, making them harder to isolate and debug. 

When agents don’t coordinate properly, the symptoms can be subtle: tasks that are partially complete, duplicated work, conflicting actions, or mysterious deadlocks where the system appears to hang. These failures don’t fit neatly into traditional debugging categories because the problem isn’t with any individual component; it’s with how components interact. 

This section provides systematic approaches for diagnosing coordination failures in multiagent workflows, understanding where breakdowns occur, and implementing strategies to prevent them. 

###### **Understanding coordination failure patterns** 

The first step in diagnosing coordinationidx_328ca9c0 failures is recognizing when they’re happening and understanding your system’s interaction patterns. Coordination failures manifest in characteristic patterns that differ from single-agent failures. Let’s discuss some common coordination failure symptoms. 

First up is **partial task completion** . It is oneidx_4bace1a0 of the clearest signals of coordination failure. The overall task appears to be “done,” but critical steps are missing. Say Agent A completes its part and hands off to Agent B, but Agent B never receives the work or doesn’t understand what to do with it. The result is a task that’s 80% complete but stuck in limbo. Users report that “something isn’t working,” but can’t articulate exactly what. Individual agents succeeded at their narrow tasks while the overall objective failed. The following figure illustrates this concept: 

<!-- Start of picture text -->
Agent A Agent B | Agent C | Agent D 4. Task Stuck<br>¥ Complete ¥ Complete ¥ Complete X Never Started at 80%<br><!-- End of picture text -->

_Figure 10.2: Partial task completion as workflow stops at 80% when Agent D never starts_ 

In MAKDO, the coordinator agent calls the `Analyzer` agent, gets the diagnostic report, and then calls the `Fixer` agent to remediate. `Fixer` successfully deletes a failing Pod. But the coordinator never calls `Slack_Bot` to notify the team. Remediation happened, the cluster is fixed, but humans have no visibility. They check Slack hours later and see no updates, don’t 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

393 

know whether the issue was resolved, and might manually intervene on an already-fixed problem. 

Another failure pattern is **work duplication** , which occurs idx_27d6cb5cwhen multiple agents perform the same work without realizing that another agent has already handled it. For example, two deployment agents both deploy idx_8636c954the same service, two data processing agents both transform the same dataset, or two customer service agents both respond to the same ticket. This wastes resources and can cause race conditions or an inconsistent state. The symptom is often visible in metrics: unusually high tool call counts, duplicate log entries, or users receiving multiple responses to a single request. See the following figure: 

<!-- Start of picture text -->
Instance 1<br>Coordinator 1<br>Instance 2 ‘<br>Coordinator 2 Analyzer 1<br>| ¥|<br>Analyzer 2 Fixer 1<br>¥<br>| |<br>Fixer 2 Pod: XYZ<br>Delete Succeeds<br>| same pod<br>\<br>so<br>Pod XYZ<br>Not Found Error<br><!-- End of picture text -->

_Figure 10.3: Work duplication as two MAKDO instances process the same Pod simultaneously_ 

_Chapter 10_ 

394 

Two MAKDO health check cycles start at nearly the same time due to a timing bug. Both coordinators independently call their `Analyzer` agents to check the same cluster. Both `Analyzer` agents identify the same three failing Pods and report them. Both coordinators then call their `Fixer` agents. Both `Fixer` agents attempt to delete the same Pods via k8s-ai. The first succeeds, while the second gets “pod not found” errors. Both post separate reports to Slack, confusing the team with duplicate notifications and conflicting results. 

Another key failure idx_7ae76505pattern is **conflicting actions** , which occur when agents work at crosspurposes because they don’t share context or objectives. One agent scales up infrastructure while another scales it down. One agent closes a ticket while another escalates it. 

One agent marks data for deletion while another archives it. The system thrashes between contradictory states, potentially never converging idx_8832a58don the desired outcome. These conflicts often surface as frequent state changes in audit logs or resources that oscillate between configurations. 

**Deadlocks and hangs** are the most frustrating coordination failures to diagnose. The system simply stops making progress without any clear error. For example, Agent A is waiting for Agent B, while Agent B is waiting for Agent A, or agents are waiting for resources that are locked by other agents, creating circular dependencies. The symptom is increasing latency metrics and tasks that never complete, eventually timing out. Users experience this as the system “freezing” or becoming unresponsive: 

<!-- Start of picture text -->
Agent A Agent B<br>Holds LockX |” —-Holds Lock Y<br>Waits for Lock Y Waits for Lock x<br><!-- End of picture text -->

_Figure 10.4: Deadlock and circular wait where Agent A and Agent B are waiting for each other_ 

**Context loss across handoffs** manifests as agents asking for information that was already provided, repeating questions, or making decisions that ignore critical context from earlier in the workflow. For example, a customer explains their problem to Agent A, which hands off to Agent B, but Agent B asks the customer to explain the problem again. Or Agent A discovers a configuration issue but Agent B doesn’t account for it when making recommendations. This degraded experience frustrates users and reduces task success rates. See the following figure: 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

395 

<!-- Start of picture text -->
Analyzer<br>Detailed Report: Fixer Vist<br>+ pod: default/nginx-7d8f Coordinator Receives: Fix the<br>+ namespace: default |__,} Receives Full Context — failingi pods’ ; + MustRacesRe-discover<br>+ error: CrashLoopBackOff X Missing Details<br>+ restart count: 5<br><!-- End of picture text -->

_Figure 10.5: Context loss in handoffs as detailed information from Analyzer gets lost when the coordinator delegates to Fixer_ 

`Analyzer` identifies three failing Pods and provides detailed information: Pod names, namespaces, error messages, and restart counts. The coordinator receives this complete report. When delegating to `Fixer` , the coordinator just says, “Fix the failing pods in the cluster” without passing the specific Pod names or details. `Fixer` has to call k8s-ai again to rediscover which Pods are failing, wasting time and tokens. The diagnostic work happens twice because the context wasn’tidx_b6f98a2e preserved in the handoff. 

Finally, we have **message ordering issues** that occur when agents receive messages out of sequence, leading to a confused state or incorrect decisions. For example, Agent B processes a “cancel” message before processing the original “create” message, leading to attempts to cancel something that doesn’t exist yet. Or agents receive partial results before final results, cache the partial data, and make decisions based on incomplete information. Symptoms include unexplained errors about missing resources or state inconsistencies that don’t match execution logs. 

###### **Agent interaction patterns and their failure modes** 

To diagnose coordination failures, you need to understand how agents interact in your system. Different interaction patterns have different failure modes and require different debugging approaches. 

**Sequential workflows** involve idx_6fe4e0 **a** a a gents passing work from one to the next in a chain: Agent A → Agent B → Agent C → Agent D. Each agent must complete its work and successfully hand off to the next agent. Failures typically occur at handoff boundaries. For example, Agent B doesn’t receive work from Agent A, or Agent C receives incomplete data from Agent B. Debuggingidx_3f62f4ce requires examining the handoff protocol: what data is transferred, how is it formatted, and how does the receiving agent know that work has arrived? Trace the execution linearly, identifying which handoff failed and why. 

**Hierarchical delegation** involves parent agents delegating sub-tasks to specialized child agents, then aggregating their results. For idx_5ca33 **e** 71 xample, a coordinating agent idx_596e7d71breaks down “deploy the application” into sub-tasks such as “provision infrastructure” (delegated to Agent A), “configure services” (delegated to Agent B), and “run smoke tests” (delegated to Agent C). 

_Chapter 10_ 

396 

The parent agent must correctly decompose the task, assign sub-tasks to appropriate children, track their progress, and synthesize the results. Failures occur when tasks are assigned to the wrong child agents, when dependencies between sub-tasks aren’t respected, or when the parent agent incorrectly aggregates results (treating partial failures as successes). 

MAKDO uses hierarchical delegation. The idx_f0e3b302coordinator is the parent, while `Analyzer` , `Fixer` , and `Slack_Bot` are the children. The idx_ed041224coordinator must correctly sequence their invocations: call `Analyzer` first to diagnose, then `Fixer` to remediate based on diagnosis, then `Slack_Bot` to notify. If the coordinator calls `Fixer` before `Analyzer` , remediation happens without diagnosis. If it calls them in parallel, `Fixer` might start before `Analyzer` finishes, missing critical context about what needs fixing. 

**Peer-to-peer collaboration** involves agents of idx_27f **e** bb62 qual status working together, often negotiating who does what. Multiple customeridx_b35cb059 service agents might all be capable of handling a ticket, so they need a protocol to prevent multiple agents from responding to the same request. 

Debugging peer-to-peer coordination requires understanding the consensus mechanism: How do agents decide who handles what? Common patterns include leader election (one agent becomes the leader and assigns work), token-based coordination (holding a token grants permission to work), and optimistic concurrency (agents attempt work and resolve conflicts if they occur). Trace through the coordination protocol to find where agreement breaks down. 

**Event-driven coordination** involves agents idx_7813401bresponding to events idx_418a83f8published to a shared event bus or message queue. For example, Agent A publishes a “user-registered” event, Agent B subscribes to that event and sends a welcome email, and Agent C subscribes and creates a customer profile. This pattern is loosely coupled. Agents don’t know about each other directly, only about events. Failures occur when events are lost, delivered out of order, or processed multiple times. Debugging requires visibility into the event bus: Was the event published? Which agents received it? Did they process it successfully? Event-driven coordination failures often leave no direct trace because the publishing agent has no knowledge of whether subscribers processed the event. Deep observability is essential. 

**Shared state coordination** involves agents coordinating through shared data structures such as databases, caches, or distributed idx_f7083eabstate stores. For example, Agent A writes data to a database, and idx_d3cabbefAgent B reads it and makes decisions based on it. This pattern requires careful attention to consistency, locking, and transaction boundaries. Failures occur due to race conditions (two agents read before either writes), stale reads (Agent B reads old data that Agent A has since updated), or lock contention (agents wait indefinitely to acquire locks). Debugging requires examining the timing of reads and writes and understanding the consistency guarantees of your storage system. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

397 

Make sure to draw a diagram of your multi-agent workflow showing which patterns you’re using. Many real systems combine patterns, such as hierarchical delegation for task decomposition, event-driven coordination for loose coupling, and shared state for tracking overall workflow progress. 

Understanding your interaction patterns is essential for debugging because each pattern has specific failure modes and requires specific diagnostic techniques. 

###### **Tracing dependencies and data flow** 

Coordination failures often stem from broken dependencies between agents or corrupted data flow. This section covers techniques for tracing what agents depend on and how information flows between them. 

Here are the types of inter-agent dependencies: 

- **Explicit dependencies** are dependencies that are defined in code or configuration. For example, Agent B’s task definition includes a `depends_on: [Agent_A]` field, or Agent C’s input schema requires outputs from Agent B. These are relatively easy to debug because they’re documented. Check whether the dependency graph accurately reflects the actual i **d** x_e42320f8 ependencies in your workflow. 

Are there missing dependencies? Circular dependencies that create deadlocks? Dependencies that reference agents or resources that don’t exist? 

- **Implicit dependencies** are more insidious. They are dependencies that exist in practice but aren’t captured in your orchestration system. For example, Agent B assumes a certain databaseidx_d95077e2 table exists, which Agent A should have created, but there’s no formal dependency relationship. Agent C assumes API keys have been provisioned, which Agent D handles, but Agent D runs asynchronously and might not have completed when Agent C starts. 

These implicit dependencies cause failures that are hard to diagnose because the system’s understanding of dependencies doesn’t match reality. The fix is usually to make implicit dependencies explicit by adding proper dependency declarations or restructuring the workflow to eliminate the assumptions. 

- **Data dependencies** involve agents requiring specific data from previous stages. Agent B needs the customer ID that Agent A looked up, and Agent C needs the deployment URL that Agent B idx_865a94becreated. Trace data flow through your system: Does each agent receive the data it needs? Is data transformed or filtered in ways that remove critical information? Are there optional fields that agents treat as required, causing failures when the field is absent? Look for schema mismatches, missing error handling when expected data is absent, or overly strict validation that rejects valid inputs. 

_Chapter 10_ 

398 

In MAKDO, `Fixer` depends on `Analyzer` providing specific Pod identifiers. If `Analyzer` returns a vague summary (“several pods failing”) instead of precise names (“default/ nginx-7d8f, default/api-server-5c9b”), `Fixer` can’t act. The data dependency is broken. `Fixer` might try to remediate based on incomplete information, miss some Pods, or have to call k8s-ai again to get the details it needs. 

- **Temporal dependencies** involve timing constraints. For example, Agent B must run after Agent A completes, but also before a five-minute window expires. Or Agent C depends on external systems idx_ **b** 551d15f eing in a certain state, which changes over time. These are particularly tricky because they depend on execution timing, making failures nondeterministic. A workflow might succeed when agents execute quickly, but fail when there’s network latency or resource contention. Diagnose temporal dependencies by adding timestamps to all coordination events and looking for patterns: do failures correlate with increased latency? Do they happen during high-load periods? Add explicit timeout handling and consider asynchronous patterns that don’t assume tight timing. 

• **Resource dependencies** involve agents needing access to shared resources such as API rate limits, database connections, compute instances, or locks on shared state. If multiple agents compete idx_a53 **f** 47e2 or limited resources, some may fail or experience delays. Trace resource allocation: Are agents getting the resources they need? Are resources being released properly after use? Are there resource leaks where agents hold resources indefinitely? Monitor resource utilization metrics alongside agent execution traces to correlate resource exhaustion with coordination failures. Tools such as distributed tracing systems (OpenTelemetry, Jaeger, and Zipkin) are invaluable for visualizing dependencies. They show parent-child relationships between spans, allowing you to see which agents depend on which, how long each step took, and where failures occurred in the dependency graph. Without distributed tracing, reconstructing dependencies from logs is tedious and error-prone. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

399 

Here is a figure illustrating all the agent dependencies: 

<!-- Start of picture text -->
= MAKDO Dependencies<br>Explicit:i 4 Resource:<br>Must call first Analyzer<br>g | API rate limits<br>7 eva<br>“Pod identifiers<br>Lager rN<br>Coordinator Data: Resource:<br>~< zs > k8s-ai<br>Diagnostic report__ API rate limits<br>* a oa<br>=~ Fixer<br>Temporal:<br>‘\ Must complete<br>’\ within timeout Implicit:<br>SS Assumes k8s-ai<br>~ is available<br>Explicit: _+ Slack Bot<br>Final step<br><!-- End of picture text -->

_Figure 10.6: MAKDO dependency types showing explicit, implicit, data, temporal, and resource dependencies between agents_ 

As we discussed earlier in the chapter, state management in a multi-agent system is very challenging. Let’s see how to debug shared state and synchronization issues. 

###### **Managing shared state and detecting deadlocks** 

When multiple agentsidx_091de966 share state or compete for resources, coordination idx_59c928f9becomes particularly challenging. This section covers techniques for debugging state synchronization issues and detecting deadlocks. 

_Chapter 10_ 

400 

###### **State synchronization challenges** 

Many multi-agent systems maintain a shared state that multiple agents read and update. Failures occur when agents have inconsistent views of this state or when concurrent updates cause corruption. Here are useful techniques and principles that can reduce and sometimes prevent these failures: 

- **Consistency models** determine what guarantees your state store provides. Strong consistency means all agents idx_2ccc19b3see the same state at the same time. For example, if Agent A writes a value, Agent B immediately sees it. Eventual consistency means writes propagate asynchronously. Agent B might see a stale state for a period of time. Most distributed databases offer eventual consistency by default for performance and availability. Understanding your consistency model is critical for debugging: if you assume strong consistency but have eventual consistency, you’ll see mysterious failures where agents make decisions based on stale data. 

- **Read-your-writes consistency** ensures agents see their own updates immediately, even if other agents might not yet see those updates. This prevents confusing scenarios where an agent writes a value, then immediately reads back a different value. Verify that your state store provides read-your-writes consistency or implement it at the application layer by caching recent writes. 

- **Optimistic concurrency control** assumes conflicts are rare and detects them when they occur. For example, agents read data with a version number, make updates, then write back with the version number. If another agent modifies the data in the meantime (version number changed), the write fails, and the agent must retry. This works well for low-contention scenarios but fails under high concurrency. Diagnose this by checking for repeated write failures and version conflicts in logs. Note that some data, such as counters or accumulators, are automatically immune to conflicts because their updates are commutative. 

- **Pessimistic locking** prevents conflicts by having agents acquire locks before accessing shared state. For example, Agent A locks a record, updates it, and then releases the lock. This prevents conflicts but can cause deadlocks if agents lock multiple resources in different orders, or if agents crash while holding locks. Diagnose locking issues by tracking lock acquisitions and releases, looking for locks that are held for unexpectedly long periods or never released. Utilize expiration-based locks that automatically release after a timeout to prevent permanent lockouts. 

State synchronization patterns include several common approaches: 

- **Leader election** : One agent becomes the leader and manages the shared state, while other agents read from the leader 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

401 

- **Distributed consensus** : Agents useidx_cd5fe673 protocols such as Raft or Paxos to agree on state changes 

- **Command Query Responsibility Segregation (CQRS)** : Separate agents for writes (commands) and reads (queries), with idx_ **a** 1a6993e synchronous synchronization 

- **Event sourcing** : Store state as a sequence of events, agents build state by replaying events 

Each pattern has trade-offs in complexity, performance, and consistency guarantees. Choose based on your requirements and ensure all agents correctly implement the chosen pattern or patterns. 

Diagnosing state corruption requires comparing the expected state (based on the sequence of operations) with the actual state. The system can reconstruct what should have happened by replaying operation logs, then compare with the actual data store state. Discrepancies indicate either bugs in state update logic or race conditions where concurrent updates interfered with each other. Use database transaction logs or audit logs to see the exact sequence of writes and identify where corruption occurred. 

###### **Detecting and resolving deadlocks** 

Deadlocks are particularly nasty coordination failures where agents wait indefinitely for each other, making no progress. Theidx_640e7e74 system appears to hang without any obvious error. Here are the types of deadlocks: 

- **Classic deadlocks** occur idx_8f1ce4c6when agents hold resources while waiting for other resources: 

   - Agent A holds lock X and waits for lock Y 

   - 

- Agent B holds lock Y and waits for lock X 

- 

- Neither can proceed 

- 

Detect this by tracking lock acquisitions and looking for circular wait patterns. Resolve this by enforcing lock ordering (all agents acquire locks in the same order) or using timeouts (if a lock isn’t acquired within _N_ seconds, release all locks and retry). 

- **Message deadlocks** occur inidx_60329e3f request-response patterns: 

   - Agent A sends a request to Agent B and waits for a response 

   - 

- Agent B sends a request to Agent A and waits for a response 

- 

- Neither can respond because both are waiting 

- 

Prevent this by using asynchronous message patterns instead of synchronous requestresponse, or by ensuring agentsidx_29cd3948 can process incoming requests while waiting for responses (non-blocking handlers). 

_Chapter 10_ 

402 

Note that sequential or hierarchical interaction design (such as MAKDO) is less prone to message deadlocks because agents don’t wait on each other in cycles. Peer-to-peer and event-driven patterns are more susceptible. 

- **Dependency deadlocks** occur inidx_99dc83b3 task scheduling: 

   - Task A depends on Task B completing 

   - 

   - Task B depends on Task A completing 

   - Neither can start 

   - 

You can detect this issue by analyzing the dependency graph for cycles before execution. Resolve it by eliminating cyclic dependencies through workflow redesign. 

###### • **Resource deadlocks** occur withidx_98a3c3ae limited resources: 

- Agent A holds resource X and waits for resource Y 

- 

- Agent B holds resource Y and waits for resource X 

- 

- Both wait indefinitely 

- 

You can detect this by tracking idx_5f7adbberesource allocation and looking for agents that are waiting for resources while holding other resources. You can resolve this with timeoutbased resource acquisition (if you can’t get all of the needed resources within a timeout, release what you have and retry) or by pre-allocating all of the needed resources before starting work. 

Note that this is different from resource exhaustion, where agents fail because resources are simply unavailable. Deadlocks involve circular waiting, while exhaustion involves lack of availability. 

Debugging deadlocks requires capturing idx_5aa49442the state of all agents when the deadlock occurs: What is each agent doing? What resources does it hold? What is it waiting for? Thread dumps (for thread-based agents) or state snapshots (for event-driven agents) provide this information. When you visualize wait relationships as a directed graph, the deadlocks appear as cycles. 

Debugging multi-agent systems requires a lot of effort both upfront in collecting the necessary data to help you troubleshoot and when problems actually occur. If possible, it’s better to invest in prevention so you can eliminate whole categories of problems right away. Let’s see how to build coordination guardrails that help you with this approach. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

403 

###### **Building coordination guardrails** 

Prevention is better than i **d** x_941f1a7e ebugging. Build the following guardrails into your multi-agent system to catch coordination errors before they cause failures: 

- **Dependency validation** checks the dependency graph for problems before execution. Are there circular dependencies? Dependencies on non-existent agents? Missing required dependencies? Validate at deployment time and reject invalid workflow definitions. 

- **Timeout enforcement** ensures no agent waits forever. Set maximum timeouts for all inter-agent communication, tool executions, and resource acquisitions. When timeouts occur, fail gracefully with clear error messages rather than hanging indefinitely. Protocols such as retries with exponential backoff and jittering help avoid thundering herd problems during retries. 

- **Idempotency requirements** ensure agents can safely retry operations. Mark which operations are idempotent and which aren’t. For non-idempotent operations, implement mechanisms to detect and skip duplicate executions. 

- **State validation** periodically checks whether the shared state is consistent and valid. Run background jobs that verify invariants: “the sum of all account balances equals the total deposits minus withdrawals” or “every task assigned to an agent references an existing agent ID.” Alert when invariants are violated. Build the ability to repair inconsistencies automatically when possible. 

- **Circuit breakers** prevent cascading idx_a25727c5failures. For example, if Agent B is consistently failing, Agent A should stop calling it rather than generating more failures. Implement circuit breaker patterns that detect failure rates and temporarily halt inter-agent communication when one agent is unhealthy. If you aim for high availability, have fallback agents that can take over when primary agents fail. 

- **Coordination testing** validates that agents interact correctly. Write integration tests that exercise multi-agent workflows, including edge cases such as the following: 

   - What happens if Agent B is slow or unresponsive? 

   - 

   - What happens if Agent A sends malformed data to Agent B? 

   - What happens if messages are delivered out of order? 

   - 

   - What happens if two agents try to update the same resource simultaneously? 

These guardrails catch coordination bugs before they reach production. 

_Chapter 10_ 

404 

Even with the best guardrails, some failures are unavoidable. But the overall system must be able to recover and continue operating. This requires explicit design choices. Let’s see what it takes. 

###### **Designing for resilience and recoverability** 

Large-scale multi-agent AI systems must be designed for resilience and recoverability. Failures are inevitable, so systems must gracefully handle errors, recover from failures, and continue operating with minimal i **d** x_55446319 isruption. In addition to the standard distributed systems challenges, which are known to be far from trivial to solve, multi-agent systems introduce new complexities due to agent interactions, shared state, and tool dependencies. The entire ecosystem must be resilient, not just individual components. Let’s look at key strategies for building resilient multi-agent AI systems. We’ve mentioned some of them earlier, but now we’ll cover them in more depth. 

###### **Redundancy and failover mechanisms** 

Redundancy is a core principle of resilience. Critical components should have redundant instances that can take overidx_99ef1676 if one fails. In the context of multi-agent AI systems, one of the most important aspects is the LLM providers. Relying on a single LLM provider creates a single point of failure. If that provider experiences downtime, rate limiting, or degraded performance, your entire system suffers. To mitigate this risk, implement multi-provider strategies. 

Design your agents to be able to switch between multiple LLM providers (e.g., OpenAI, Anthropic, and Google Gemini) based on availability, cost, or performance. Abstract the LLM interface so agents can use any provider interchangeably. 

Another dimension of redundancy is the models your agents use. If an agent is built around a specific model with highly tuned prompts and relying on built-in tools, then it may struggle to switch models. Design agents to be model-agnostic where possible, allowing them to use different models with minimal changes. This may involve standardizing prompts, tool interfaces, and response parsing. If you really need to optimize to a specific model, have backup models that can be used in emergencies, even if they are not as optimized as the primary model. 

Pay special attention to the tools available to your agents. Some models, such as GPT-5, come with built-in tools (e.g., code interpreters or web browsers) that are tightly integrated. If your agent relies on these tools, ensure that alternative tools are available when switching models. For example, if an agent uses a code interpreter tool that becomes unavailable, have a fallback mechanism to use an external code execution service. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

405 

When interacting with external services via tools (e.g., databases or APIs), implement failover strategies. If one service endpoint is unreachable, have backup endpoints or alternative services that can be used. Use DNS-based load balancing or service discovery to route requests to healthy instances. Ideally, the tools themselves can implement retry and failover logic implicitly, so agents don’t need to handle it directly. But if not possible (e.g., when using thirdparty MCP tools), you will either need to build a wrapper tool that implements failover or have the agents handle it by exposing this as a layer of alternate tools and instructing the agents to manage failover. 

###### **Graceful degradation strategies** 

When failures occur, the system should degrade gracefully rather than failing completely. Graceful degradation idx_71c8825fmeans reducing functionality while maintaining core operations. A multi-agent system might disable non-essential features, reduce quality, or slow down processing rather than shutting down entirely. The key is to prioritize critical workflows and sacrifice less important ones when resources are constrained or components fail. 

Define degradation tiers for your multi-agent system. For example, Tier 1 is full functionality with all features working. Tier 2 might disable analytics or logging to reduce load. Tier 3 could switch to simpler, faster models that are less accurate but more reliable. Tier 4 might disable automated remediation and only perform diagnostics. Each tier maintains some value while consuming fewer resources or depending on fewer components. Design agents to detect which tier they’re operating in and idx_e **a** d01a5e djust behavior accordingly. For MAKDO, the degradation model may look like the following: 

- Tier 1 runs full health checks with detailed analysis and automated fixing 

- 

- Tier 2 skips automated fixes and only reports issues to Slack for human intervention 

- 

- Tier 3 performs basic health checks without detailed diagnostics 

- 

- Tier 4 pauses health checks entirely and only responds to explicit user requests 

Implement feature flags or kill switches that allow operators to disable specific functionality during incidents. If the `Fixer` agent starts making incorrect decisions, a kill switch can disable automated remediation while keeping diagnostics and notifications running. If k8s-ai becomes slow or unreliable, fall back to simpler kubectl commands for basic operations. If Slack is down, buffer notifications and deliver them when service is restored, or send alerts via email as a backup channel. 

_Chapter 10_ 

406 

The system adapts to what’s available rather than failing because one component is unavailable. 

<!-- Start of picture text -->
:<br><!-- End of picture text -->

Sometimes, failures are temporary, and instead of degrading gracefully, you just have to try again. But there is an art andidx_9ba19846 science to classifying and handling failures. 

_Figure 10.7: MAKDO degradation tiers from full functionality to manual mode_ 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

407 

###### **Retry logic and circuit breakers** 

Transient failures are common in distributed systems. Network glitches, temporary API rate limits, or brief service overloads can cause operations to fail even when the underlying system is healthy. Retry logic idx_ae9a32e2handles these transient idx_33629eb8failures by automatically retrying failed operations after a delay. The key is distinguishing between transient failures worth retrying and permanent failures that will never succeed. Retrying a network timeout makes sense. Retrying an invalid API key does not. Design retry logic to identify retryable errors and give up quickly on permanent failures. 

Implement exponential backoff with jitter for retries. Start with a short delay (100 ms), then double it with each retry (200 ms, 400 ms, 800 ms). Add random jitter to prevent thundering herd problems where many agents retry simultaneously and overwhelm the failing service. Cap the maximum delay (e.g., 30 seconds) and limit total retry attempts (e.g., five tries). Log each retry attempt with context about why it failed so you can identify patterns. For MAKDO, if k8s-ai returns a _503 Service Unavailable error_ , retry with exponential backoff. If it returns a _401 Unauthorized error_ , fail immediately because retrying won’t fix invalid credentials. If `Fixer` tries to delete a Pod and gets a timeout, retry a few times before giving up and escalating to humans via Slack. 

Circuit breakersidx_ea9139d1 prevent cascading failures by stopping requests to unhealthy services. A circuit breaker monitors the failure rate of operations to aidx_3dd8fe86 downstream service. When failures exceed a threshold (e.g., 50% failure rate over 10 requests), the circuit breaker opens and immediately fails all requests without attempting them. This gives the failing service time to recover without being bombarded with requests. After a timeout period (e.g., 60 seconds), the circuit breaker enters a half-open state and allows a few test requests through. If they succeed, the circuit closes and normal operation resumes. If they fail, the circuit stays open. Circuit breakers are essential for multi-agent systems because one slow or failing service can block many agents waiting for responses. 

In MAKDO, if k8s-ai becomes unresponsive and every `Analyzer` request times out, a circuit breaker would open after a few failures. Subsequent health checks would skip calling k8s-ai entirely and immediately report degraded status to Slack, rather than having every coordinator wait 30 seconds for timeouts. 

_Chapter 10_ 

408 

This prevents the entire MAKDO system from grinding to a halt when one dependency fails. 

<!-- Start of picture text -->
®<br>F | Closed<br>/ *Ss<br>: e Failure threshold exceeded ae<br>(e.g., 50% failures over 10 \<br>F requests) \<br>mi ‘ion |<br>All requestsNermatlopetsucpass through 4 Openos__ Test requests succeed<br>ae i —<br>\ ~<br>\\ oS\<br>' Timeout(e.g., afterpperiod 60 seconds)expiresP Test requests| fail<br>\<br>/<br>sii<br>Failing fast \\ /Va<br>All requests rejected Ny Z<br>immediately HalfOpen<br>No calls to downstream . 7<br>| service '<br>Testing recovery<br>Limited requests pass<br>through<br>Monitoring success rate<br><!-- End of picture text -->

_Figure 10.8: Circuit breaker states transitioning between closed, open, and half-open based on failure rates and timeouts_ 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

409 

When things goidx_6311607c south, you retry or just pause and continue later; you don’t want to lose important work that happened before the failure. This is where checkpointing is very useful. 

###### **Checkpointing and state recovery** 

Multi-agent workflows can be long-running and involve multiple expensive steps across different agents. If an agent crashes mid-workflow, the system needs to recover without starting from scratch. Note that this is not required for fast workflows that complete in seconds, but for workflowsidx_d3d22ec0 that take minutes or longer, checkpointing is often essential. 

Checkpointing saves the state of a workflow at key points so it can be resumed after failures. Each checkpoint captures what work has been completed, what data has been produced, and what remains to be done. When an agent recovers from a crash, it loads the most recent checkpoint and continues from there rather than redoing work that already succeeded. 

Design checkpoints at natural boundaries in your workflows. After each agent completes its work, and before delegating to the next agent, save a checkpoint. Store checkpoints in durable storage, such as a database or distributed key-value store, not in agent memory. Include enough context in checkpoints to resume work: input parameters, intermediate results, which agents have run, and whichidx_fae9f91a steps remain. Add metadata such as timestamps, workflow IDs, and correlation IDs to track checkpoints across distributed systems. For MAKDO, the checkpoint is after `Analyzer` completes and returns its diagnostic report. If the coordinator crashes before calling `Fixer` , the replacement coordinator can load the checkpoint, see that analysis is complete, and proceed directly to remediation. Without checkpointing, the entire health check would restart, wasting `Analyzer` ’s work and doubling the time to fix issues. `Fixer` should also checkpoint after completing every remediation step, so if it crashes and restarts, it can continue where it left off. `Slack_Bot` doesn’t need checkpointing as the worst case is that it will resend a notification. 

Implement idempotent recovery to handle partial failures safely. When resuming from a checkpoint, the system might re-execute some operations that were partially completed before the crash. Design operations to be idempotent so re-execution produces the same result. If `Fixer` deleted a Pod but crashed before updating the checkpoint, recovery might try to delete the same Pod again. k8s-ai should handle this gracefully by returning success if the Pod is already gone. Store operation IDs or transaction tokens in checkpoints to detect and skip duplicate operations. Clean up old checkpoints periodically to avoid unbounded storage growth. Once a workflow completes successfully, delete its checkpoints. Keep failed workflow checkpoints longer for debugging. Balance checkpoint frequency against overhead. Checkpointing after every tool call adds latency and storage costs. Checkpointing only at the beginning and end of workflows means more work gets lost on failures. Find the right granularity for your system’s reliability requirements and operational costs. 

_Chapter 10_ 

410 

###### **Human escalation patterns** 

Not all failures can be handled automatically. Some situations require human intervention in terms of judgment or approval. Multi-agent systems need clear escalation patterns that bring humans into the loop at appropriate times. The key is escalating early enough that humans can prevent damage, but not so aggressively that they’re overwhelmed. This means that the system has to be smart enough toidx_ca69faed request human feedback for critical decisions only, and avoid notifying or requesting permissions for each and every action. For example, if the system has to analyze 100 documents and requests permission to read each one, then the human approver will find this tedious and the overall process will be slower (for example, if the human approver leaves for lunch). 

Design escalation rules based on confidence levels, risk assessment, and failure severity. Highconfidence, low-risk operations can proceed automatically. Low-confidence or high-risk operations should wait for human approval. 

Define explicit triggers that bring humans into the loop. Unknown errors that agents can’t classify require human judgment. Low confidence scores below a threshold indicate uncertainty that humans should review. Operations affecting production systems or critical resources need approval before proceeding. Multiple retry attempts often indicate permanent failures that need investigation. Degraded-mode operation means reduced functionality that teams should know about. For MAKDO, `Analyzer` might identify issues that `Fixer` doesn’t know how to remediate, and `Fixer` might fail in attempting to fix some problem due to insufficient permissions. k8s-ai unavailability means the system can’t perform diagnostics, and humans need to know. Each notification should include rich context: what failed, why it failed, what was attempted, and what options are available. The coordinator should collect the information and tell the `Slack_Bot` agent to inform the humans with clear action items so the team knows exactly what decision is needed. 

Provide humans with actionable options, not just notifications. Instead of “Health check failed,” say, “3 pods in the default namespace are crash-looping. Option 1: Delete and restart them (automated). Option 2: Investigate logs first (manual). Option 3: Ignore and wait for next health check.” Include buttons or commands that let humans approve actions directly from Slack without switching context. Time-bound escalations with default actions. If a human doesn’t respond within 15 minutes, either take the safest default action or escalate further to on-call engineers. Track escalation patterns to identify recurring issues. If the same type of failure always requires human intervention, that’s a signal to improve agent capabilities or add automation. If humans always choose the same option, consider making it the automatic default. The goal is continuous improvement, where fewer escalations are needed over time as agents learn to handle more situations autonomously. 

_Testing, Debugging, and Troubleshooting Multi-Agent Systems_ 

411 

With that, we come to the end of our deep dive into testing, debugging, and troubleshooting multi-agent AI systems. 

###### **Summary** 

In this chapter, we explored the unique challenges of testing, debugging, and troubleshooting multi-agent AI systems. We covered strategies for designing effective tests that validate interagent coordination, tracing dependencies and data flow to identify failures, managing shared state and detecting deadlocks, and building guardrails to prevent coordination errors. We also discussed designing for resilience and recoverability through redundancy, graceful degradation, retry logic, checkpointing, and human escalation patterns. Multi-agent systems introduce new complexities beyond traditional software systems, but with careful design and robust tooling, these challenges can be effectively managed to build reliable and maintainable multi-agent AI systems. Don’t forget that you can add introspective AI agents to your system that will help monitor, debug, and even fix issues automatically as they arise. 

In the next chapter, we will explore how to deploy and operate multi-agent AI systems in the field. 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns— _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and generative AI systems. Subscribe now and receive a free eBook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OFA<br>a<br><!-- End of picture text -->

# 11 

##### Deploying Multi-Agent Systems 

In the previous chapter, we covered testing, debugging, and troubleshooting multi-agent systems. We explored common failure modes such as hallucination and tool misuse, instrumentation and observability strategies, debugging techniques for coordination failures, and designing for resilience through redundancy and graceful degradation. We used MAKDO throughout as a concrete example to illustrate these concepts. 

Now, it’s time to deployidx_b93ab59e MAKDO for real. But running multi-agent systems in production introduces new challenges around deployment architecture, service discovery, networking, and security. How do you deploy agents across multiple environments? How do they communicate securely? How do you manage credentials and access control? 

In this chapter, we deploy MAKDO in a realistic production-like setup. We’ll create two Kubernetes clusters idx_fab179e0using **Kubernetes in Docker** ( **KinD** ). The control cluster runs MAKDO itself. The worker cluster is the target cluster that MAKDO monitors and manages. K8s-ai (an agent-to-agent server) runs on the worker cluster, providing MAKDO with the ability to diagnose and fix issues throughidx_16a395d4 the **Agent-to-Agent** ( **A2A** ) protocol. This setup mirrors real production scenarios where your management systems run separately from the workloads they manage. 

We’ll walk through setting up both clusters, deploying MAKDO components to the control cluster, deploying k8s-ai to the worker cluster, configuring secure cross-cluster communication, and managing service discovery and access control. By the end, you’ll have a fully functional multi-agent system managing a separate Kubernetes cluster, ready to detect and remediate issues automatically. 

_Chapter 11_ 

414 

The following key points are covered: 

- Setting up dual KinD clusters for multi-agent deployment 

- 

- Deploying MAKDO to the control cluster 

- 

- Deploying k8s-ai to the worker cluster 

- 

- Enabling secure communication between clusters 

- 

###### **Technical requirements** 

Follow the instructions at `https://github.com/PacktPublishing/Design-Multi-Agent-AISystems-Using-MCP-and-A2A/tree/main/ch11/makdo` . 

###### **Setting up dual KinD clusters for multi-agent deployment** 

Let’s idx_c046fed6build a production-like deployment where MAKDO runs on one cluster and manages another. This separation is critical in real environments to isolate management infrastructure from production workloads. It reduces the blast radius and allows the production system to keep operating even if MAKDO is not operational. Also, if the production cluster suffers resource exhaustion or a similar issue, MAKDO will be able to analyze and potentially fix it because it is not subject to the same problems. 

###### **Installing KinD and prerequisites** 

Before idx_3d607833creating idx_b8752cec clusters, you need Docker, kubectl, and KinD installed. Rather than walking through installation steps for each tool (which vary by platform and change over time), we provide a verification script that checks that everything is ready. 

First, clone the book’s repository if you haven’t already: 

```
git clone git@github.com:PacktPublishing/Design-Multi-Agent-AI-Systems-using-MCP-
and-A2A.git
```

Install theidx_790b11b2 required idx_4886e4b9 tools using their official i **d** x_7a8396a3 ocumentation: 

- **Docker** : `https://docs.docker.com/get-docker/` 

- **kubectl** : `https://kubernetes.io/docs/tasks/tools/` 

- 

- **KinD** : `https://kind.sigs.k8s.io/docs/user/quick-start/#installation` 

_Deploying Multi-Agent Systems_ 

415 

Once installed, verify that everything is working with our prerequisites check script: 

```
cd ch11
chmod +x check-prerequisites.sh
./check-prerequisites.sh
```

The script checks whether Docker is installed and running, kubectl is available, KinD is installed (version 0.20.0 or newer recommended), and disk space is available (need ~10 GB for both clusters), Docker memory allocation (need at least 4 GB), and existing KinD clusters that might conflict with our setup. 

If the script reports any missing prerequisites, install them using the preceding links and run the script again. When you see **All prerequisites met!** , you’re ready to create clusters. 

###### **Creating the control cluster configuration** 

The idx_d8f5b50e control cluster hosts MAKDO agents. It needs to be configured to allow external access to MAKDO’s API endpoints. KinD uses YAML configuration files to define cluster topology and networking. 

Create `control-cluster.yaml` : 

```
kind:Cluster
apiVersion:kind.x-k8s.io/v1alpha4
name:makdo-control
nodes:
-role:control-plane
kubeadmConfigPatches:
-|
kind:InitConfiguration
nodeRegistration:
kubeletExtraArgs:
node-labels:"cluster-role=control"
extraPortMappings:
# Port for accessing MAKDO API/dashboard if needed
-containerPort:30080
hostPort:8080
protocol:TCP
# Port for MAKDO health check endpoint
-containerPort:30090
hostPort:9090
protocol:TCP
```

_Chapter 11_ 

416 

Here are the key configuration points: 

- `name` : `makdo-control` identifies this cluster. KinD uses this name for the Docker container and kubectl context. 

- `node-labels` : Labels help identify which cluster a pod is running in. Useful for debugging and monitoring. 

- `extraPortMappings` : Exposes ports from the cluster to your host machine. Port `8080` maps to container port `30080` (the `NodePort` range in Kubernetes). Port `9090` maps to `30090` for health checks. These mappings let you access MAKDO services from your local machine or allow the worker cluster to reach MAKDO, if needed. 

Next, create the control cluster: 

```
kindcreatecluster--configcontrol-cluster.yaml
```

This takes 1–2 minutes. KinD downloads the Kubernetes node image (if not cached), creates a Docker container, and initializes Kubernetes. When complete, you’ll see the following: 

```
Creating cluster "makdo-control" ...
```

- `✓ Ensuring node image (kindest/node:v1.33.1)` 🖼 `✓ Preparing nodes` 📦 `✓ Writing configuration` 📜 

`✓ Starting control-plane` 🕹 

- `✓ Installing CNI` 🔌 

- `✓ Installing StorageClass` 💾 `Set kubectl context to "kind-makdo-control"` 

###### **Note** 

The exact Kubernetes version (v1.33.1 in this example) depends on which KinD version you have installed. KinD automatically uses a compatible Kubernetes version. 

Verify idx_55a82371the cluster: 

```
kubectlcluster-info--contextkind-makdo-control
kubectlgetnodes--contextkind-makdo-control
```

_Deploying Multi-Agent Systems_ 

417 

Here’s the expected output: 

```
Kubernetes control plane is running at https://127.0.0.1:60905
CoreDNS is running at https://127.0.0.1:60905/api/v1/namespaces/kube-system/
services/kube-dns:dns/proxy
NAME                          STATUS   ROLES           AGE   VERSION
makdo-control-control-plane   Ready    control-plane   1m    v1.33.1
```

One node is in the `Ready` status. The cluster is running but empty. 

###### **Creating the worker cluster configuration** 

The idx_5ad07dc0 worker cluster is where your actual workloads run. MAKDO monitors this cluster and fixes issues when they arise. This cluster needs to expose k8s-ai’s MCP server so MAKDO can communicate with it. 

Create `worker-cluster.yaml` : 

```
kind:Cluster
apiVersion:kind.x-k8s.io/v1alpha4
name:makdo-worker
nodes:
-role:control-plane
kubeadmConfigPatches:
-|
kind:InitConfiguration
nodeRegistration:
kubeletExtraArgs:
node-labels:"cluster-role=worker"
extraPortMappings:
# Port for k8s-ai MCP server
-containerPort:30100
hostPort:8100
protocol:TCP
# Port for exposing problematic workloads (for testing)
-containerPort:30200
hostPort:8200
protocol:TCP
```

_Chapter 11_ 

418 

Here are the idx_be4eedebkey differences from the control cluster: 

- `name` : `makdo-worker` distinguishes this from the control cluster. 

- `node-labels` : `cluster-role=worker` identifies this as a managed cluster. 

- `Port 8100` : Maps to container port `30100` , where k8s-ai’s A2A server will run. MAKDO’s Analyzer and Fixer agents call k8s-ai through this port using the A2A protocol. 

- `Port 8200` : For test workloads. We’ll deploy broken pods here that MAKDO can detect and fix. 

Create the worker cluster: 

```
kindcreatecluster--configworker-cluster.yaml
```

You now have two independent Kubernetes clusters running as Docker containers: 

```
kindgetclusters
```

Here’s the expected output (you may see other clusters too): 

```
makdo-control
makdo-worker
```

Check both cluster contexts: 

```
kubectlconfigget-contexts|grepmakdo
```

Here is the output: 

```
          kind-makdo-control   kind-makdo-control   kind-makdo-control
*         kind-makdo-worker    kind-makdo-worker    kind-makdo-worker
```

The `*` symbol indicates which context is currently active. Switch between them with the following: 

```
# Use control cluster
kubectlconfiguse-contextkind-makdo-control
# Use worker cluster
kubectlconfiguse-contextkind-makdo-worker
```

_Deploying Multi-Agent Systems_ 

419 

Both clusters idx_20097fd **a** re isolated. Pods in one cluster can’t directly reach pods in the other without explicit networking configuration, which we’ll set up next. 

###### **Setting up cluster networking and port forwarding** 

KinD clustersidx_78a6db4d run as Docker containers on your host machine. They’re on the same Docker network, which means they can reach each other usingidx_2a9f6736 Docker networking. But services inside the clusters need special configuration to be accessible. 

First, find the Docker network that both clusters are using: 

```
dockernetworkls|grepkind
```

Here is the output: 

```
aadf3e99800d   kind          bridge    local
```

Both cluster containers are connected to this `kind` network: 

```
dockernetworkinspectkind|grep-A3"makdo"
```

This shows the IP addresses of both cluster containers. However, we don’t want to hardcode IPs. Instead, we’ll use the port mappings we configured earlier. 

For cross-cluster communication, MAKDO (on the control cluster) needs to reach k8s-ai (on the worker cluster). Since both clusters are on the same host, MAKDO can reach k8s-ai at `host.docker.internal:8100` . This special DNS name resolves to the host machine from inside Docker containers. 

Let’s verify that the port mappings are working. Check what’s listening on the mapped ports: 

```
# Control cluster ports
lsof-i:80802>/dev/null||echo"Port 8080: not yet in use"
lsof-i:90902>/dev/null||echo"Port 9090: not yet in use"
# Worker cluster ports
lsof-i:81002>/dev/null||echo"Port 8100: not yet in use"
lsof-i:82002>/dev/null||echo"Port 8200: not yet in use"
```

Right idx_34cc46ccnow, these idx_416c525bports aren’t in use because we haven’t deployed any services yet. The port mappings are configured but inactive until services bind to the internal ports ( `30080` , `30090` , `30100` , and `30200` ). 

_Chapter 11_ 

420 

Check that the Docker containers themselves are running and have the port mappings: 

```
dockerps--format"table {{.Names}}\t{{.Ports}}"|grepmakdo
```

Here is the output: 

```
makdo-worker-control-plane    127.0.0.1:61462->6443/tcp, 0.0.0.0:8100->30100/tcp,
0.0.0.0:8200->30200/tcp
makdo-control-control-plane   127.0.0.1:60905->6443/tcp, 0.0.0.0:8080->30080/tcp,
0.0.0.0:9090->30090/tcp
```

You can see both containers with their port mappings. The `6443` ports are the Kubernetes API servers. Our custom mappings ( `8080` -> `30080` , `8100` -> `30100` , etc.) are ready for services to use. 

###### **Verifying cross-cluster connectivity** 

Beforeidx_9f26d73a deploying MAKDO and k8s-ai, verify that both clusters are healthy and can potentially communicate. 

Check the cluster health: 

```
kubectlcluster-info--contextkind-makdo-control
kubectlgetnodes--contextkind-makdo-control
```

Here is the output: 

```
Kubernetes control plane is running at https://127.0.0.1:60905
CoreDNS is running at https://127.0.0.1:60905/api/v1/namespaces/kube-system/
services/kube-dns:dns/proxy
```

```
NAME                          STATUS   ROLES           AGE   VERSION
makdo-control-control-plane   Ready    control-plane   15m   v1.33.1
```

Now, check the worker cluster: 

```
kubectlcluster-info--contextkind-makdo-worker
kubectlgetnodes--contextkind-makdo-worker
```

Here is the output: 

```
Kubernetes control plane is running at https://127.0.0.1:61462
CoreDNS is running at https://127.0.0.1:61462/api/v1/namespaces/kube-system/
```

_Deploying Multi-Agent Systems_ 

421 

```
services/kube-dns:dns/proxy
NAME                         STATUS   ROLES           AGE   VERSION
makdo-worker-control-plane   Ready    control-plane   12m   v1.33.1
```

Both clusters show their control plane running, and one node is in the `Ready` status. 

Test basic networking within each cluster: 

```
# Test DNS in control cluster
kubectlrundns-test--image=busybox:latest--restart=Never--rm-i--context
kind-makdo-control--command--\
nslookupkubernetes.default.svc.cluster.local
# Test DNS in worker cluster
kubectlrundns-test--image=busybox:latest--restart=Never--rm-i--context
kind-makdo-worker--command--\
nslookupkubernetes.default.svc.cluster.local
```

Both shouldidx_34a3fffe successfully resolve the Kubernetes service DNS name. 

For cross-cluster communication, MAKDO won’t directly reach pods in the worker cluster. Instead, MAKDO will call k8s-ai’s A2A server through the exposed port. We’ll test this once k8s-ai is deployed. The clusters are ready for the next step. 

###### **Deploying a test workload to the worker cluster** 

Toidx_e7bab936 verify that MAKDO works correctly, we need workloads with problems for it to detect and fix. Let’s deploy a test namespace with three pods: one that crashes, one with an image pull error, and one that’s healthy. 

Create `test-workload.yaml` : 

```
apiVersion:v1
kind:Namespace
metadata:
name:test-workload
---
# A pod that will crashloop - missing required environment variable
apiVersion:v1
kind:Pod
metadata:
name:crashloop-pod
```

_Chapter 11_ 

422 

```
namespace:test-workload
labels:
app:crashloop-test
spec:
containers:
-name:app
image:busybox:latest
command: ["sh", "-c"]
args:
-|
if [ -z"$REQUIRED_VAR" ];then
echo"ERROR: REQUIRED_VAR not set"
exit1
fi
echo"Running successfully"
sleep3600
---
# A pod with an image that doesn't exist
apiVersion:v1
kind:Pod
metadata:
name:imagepull-pod
namespace:test-workload
labels:
app:imagepull-test
spec:
containers:
-name:app
image:nonexistent-registry.example.com/fake-image:v1.0.0
command: ["sleep", "3600"]
---
# A healthy pod for comparison
apiVersion:v1
kind:Pod
metadata:
name:healthy-pod
namespace:test-workload
labels:
app:healthy-test
spec:
containers:
```

_Deploying Multi-Agent Systems_ 

423 

```
-name:app
image:nginx:alpine
ports:
-containerPort:80
```

Deploy to theidx_ee4b606a worker cluster: 

```
kubectlapply-ftest-workload.yaml--contextkind-makdo-worker
```

###### Check the pod status: 

```
kubectlgetpods-ntest-workload--contextkind-makdo-worker
```

###### Here is the output: 

|`NAME            READY   STATUS             RESTARTS      AGE`|
|---|
|`crashloop-pod   0/1     CrashLoopBackOff   7 (27s ago)   11m`|
|`healthy-pod     1/1     Running            0             11m`|
|`imagepull-pod   0/1     ImagePullBackOff   0             11m`|

Perfect! We idx_b9dbeecfhave the following: 

- `crashloop-pod` : `CrashLoopBackOff` (exits immediately due to a missing environment variable) 

- `healthy-pod` : Running ( `nginx` started successfully) 

- 

- `imagepull-pod` : `ImagePullBackOff` (image doesn’t exist) 

- 

Watch the `crashloop-pod` restart repeatedly: 

```
kubectlgetpods-ntest-workload--contextkind-makdo-worker--watch
```

Press _Ctrl_ + _C_ to stop watching. These failing pods are perfect targets for MAKDO. The Analyzer will detect them, classify the failure types, and the Fixer may attempt remediation. 

Check the pod logs to see the failure reasons: 

```
kubectllogscrashloop-pod-ntest-workload--contextkind-makdo-worker
```

Here is the output: 

```
ERROR: REQUIRED_VAR not set
```

_Chapter 11_ 

424 

The worker cluster now has problematic workloads. Next, we’ll deploy MAKDO to the control cluster and k8s-ai to the worker cluster, then watch MAKDO automatically detect and handle these issues. 

###### **Deploying MAKDO to the control cluster** 

Now that idx_c23f2413we have both clusters running and test workloads failing in the worker cluster, it’s time to deploy MAKDO. MAKDO will run as a Deployment in the control cluster and monitor the worker cluster through k8s-ai’s A2A server. 

###### **Preparing the MAKDO configuration** 

MAKDO idx_487c0e78needs configuration files to know which clusters to monitor, how to connect to k8s-ai, and how to communicate via Slack. We’ll adapt the example configuration for our two-cluster setup. 

Check out `https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-UsingMCP-and-A2A/tree/main/ch11/makdo` for details. 

Here are the key configuration points: 

- **Clusters** : Only the worker cluster is listed. MAKDO doesn’t need to monitor its own control cluster. The context `kind-makdo-worker` matches the kubectl context created by KinD. 

- `kubeconfig_path` : Set to `/root/.kube/config` because this is where `kubeconfig` will be mounted inside the MAKDO container. We’ll mount `kubeconfig` as a volume. 

- `k8s_ai.base_url` : Uses `host.docker.internal:8100` to reach k8s-ai on the worker cluster. This special DNS name resolves to the host machine from inside Docker containers. Port `8100` is the mapped port for k8s-ai’s A2A server. 

- **Environment variables** : API keys and tokens use the `${VAR}` syntax. MAKDO loads these from environment variables, which we’ll provide via Kubernetes secrets. 

- `monitoring.check_interval` : Set to 120 seconds (2 minutes). MAKDO polls the worker cluster every two minutes to detect issues quickly. 

Next, we need the agent configuration files. MAKDO uses separate YAML files for each agent’s prompt and tool configuration. 

Create `makdo-config/coordinator.yaml` : 

```
name:"MAKDO Coordinator"
description:|
YouaretheMAKDOCoordinator,thecentralorchestratorformulti-cluster
```

_Deploying Multi-Agent Systems_ 

425 

```
Kubernetesoperations.
```

```
Your responsibilities:
```

```
1.Periodicallycheckclusterhealthacrossallregisteredclusters
```

`2. Coordinate between Analyzer, Fixer, and Slack Bot agents` 

```
3.Escalatecriticalissuestoappropriateagents
```

```
4.Maintainoperationalawarenessofallclusters
```

```
When asked to perform health checks:
```

```
1.UsetheAnalyzeragenttoassessclusterhealth
2.Ifissuesarefound,usetheSlackBottonotifyusers
3.Forcriticalissues,usetheFixeragentifremediationisneeded
4.AlwaysreportstatusbacktotheSlackchannel
```

```
Beproactive,clear,andfocusedonclusterreliability.
```

```
model_id:"gpt-4o"
sub_agents:
```

```
-name:"MAKDO_Analyzer"
config_path:"src/makdo/agents/analyzer.yaml"
-name:"MAKDO_Fixer"
config_path:"src/makdo/agents/fixer.yaml"
```

```
-name:"MAKDO_Slack_Bot"
config_path:"src/makdo/agents/slack.yaml"
```

```
history:
```

```
max_messages:10
summarize_after:5
Create makdo-config/analyzer.yaml:
name:"MAKDO Analyzer"
description:|
```

```
YouaretheMAKDOAnalyzeragent.YourroleistodiagnoseKubernetescluster
healthissues.
```

```
Your responsibilities:
1.Checkclusterresourcehealth(pods,deployments,services,nodes)
2.IdentifyproblemslikeCrashLoopBackOff,ImagePullBackOff,resource
exhaustion
```

_Chapter 11_ 

426 

```
3.Analyzelogsandeventstounderstandrootcauses
4.ProvidecleardiagnosticreportstotheCoordinator
When analyzing issues:
1.AlwayscheckALLnamespaces,notjustdefault
2.Lookatpodstatus,events,andlogs
3.Identifypatternsacrossmultiplefailingpods
4.Classifyissuesbyseverity(critical,warning,info)
5.Provideactionablerecommendations
Usethek8sdiagnostictoolsavailabletoyouthroughtheA2Aprotocol.
model_id:"gpt-4o"
tools:
-name:"kubernetes_resource_health"
type:"a2a"
endpoint:"http://host.docker.internal:8100"
description:"Check health of Kubernetes resources (pods, deployments,
services, nodes)"
-name:"kubernetes_diagnose_issue"
type:"a2a"
endpoint:"http://host.docker.internal:8100"
description:"Diagnose specific Kubernetes issues by analyzing events, logs,
and resource state"
history:
max_messages:8
summarize_after:4
Create makdo-config/fixer.yaml:
name:"MAKDO Fixer"
description:|
YouaretheMAKDOFixeragent.YourroleistoremediateKubernetescluster
issuessafely.
Your responsibilities:
1.ApplyfixesfordiagnosedissuesfromtheAnalyzer
2.Alwaysprioritizesafetyandavoiddestructiveactions
3.Requestapprovalforcriticaloperations
4.Verifyfixesweresuccessfulafterapplying
```

_Deploying Multi-Agent Systems_ 

427 

```
Common remediation actions:
-Restartfailingpods
-Updatepodconfigurationstofixmissingenvvars
-Scaledeployments
-Applyconfigurationchanges
CRITICAL SAFETY RULES:
1.Neverdeleteresourceswithoutexplicitapproval
2.Alwaysverifybeforeapplyingchanges
3.Ifunsure,askforhumanapproval
4.Testfixesonnon-productionresourcesfirstwhenpossible
Usethek8sremediationtoolsavailablethroughtheA2Aprotocol.
model_id:"gpt-4o"
tools:
-name:"kubernetes_apply_fix"
type:"a2a"
endpoint:"http://host.docker.internal:8100"
description:"Apply fixes to Kubernetes resources (restart pods, update
configs, scale)"
-name:"kubernetes_verify_fix"
type:"a2a"
endpoint:"http://host.docker.internal:8100"
description:"Verify that applied fixes resolved the issue"
history:
max_messages:6
summarize_after:3
Create makdo-config/slack.yaml:
name:"MAKDO Slack Bot"
description:|
YouaretheMAKDOSlackBotagent.Yourroleistocommunicatewithusersvia
Slack.
Your responsibilities:
1.Postclusterhealthreportstothe#makdo-devops channel
2.Alertuserstocriticalissues
```

_Chapter 11_ 

428 

```
3.Providestatusupdatesonongoingoperations
4.Respondtouserquestionsaboutclusterhealth
Message formatting:
-Useclear,conciselanguage
-Highlightcriticalissueswithappropriateurgency
-Includerelevantdetails(podnames,namespaces,errormessages)
-Provideactionablenextstepswhenpossible
Alwayspostto#makdo-devops channel unless told otherwise.
model_id:"gpt-4o"
mcp_servers:
slack:
command:"npx"
args: ["@korotovsky/slack-mcp-server"]
env:
SLACK_BOT_TOKEN:"${AI6_BOT_TOKEN}"
SLACK_TEAM_ID:"${SLACK_TEAM_ID}"
history:
max_messages:5
summarize_after:3
```

These configuration files define each agent’s behavior, tools, and how they communicate. The Analyzer and Fixer idx_28751d **a** 3 gents use A2A tools pointing to k8s-ai. The `Slack_Bot` agent uses an MCP server for Slack integration. 

###### **Creating Kubernetes secrets for API keys** 

MAKDO idx_ac34cf90needs API keys for OpenAI (to run the LLM-based agents) and Slack (to post messages). We’ll store these as Kubernetes secrets in the control cluster. 

First, create a `.env` file with your API keys: 

```
cat > .env <<EOF
OPENAI_API_KEY=sk-...your-key-here...
AI6_BOT_TOKEN=xoxb-...your-slack-bot-token...
AI6_APP_TOKEN=xapp-...your-slack-app-token...
SLACK_TEAM_ID=T...your-team-id...
EOF
```

_Deploying Multi-Agent Systems_ 

429 

Replace the placeholders with your actual keys. If you don’t have these keys yet, here’s where to get them: 

- **OpenAI API key** : Get idx_b592cd87from `https://platform.openai.com/api-keys` 

- 

- **Slack tokens** : Createidx_5a279aad a Slack app at `https://api.slack.com/apps` with bot token scopes ( `chat:write` and `channels:read` ) and an app-level token for socket mode 

- **Slack Team ID** : Findidx_3292f6a0 in your Slack workspace settings under **Workspace ID** 

- 

Create the Kubernetes secret in the control cluster: 

```
# Switch to control cluster
kubectlconfiguse-contextkind-makdo-control
# Load environment variables
set-a
source.env
set+a
# Create secret
kubectlcreatesecretgenericmakdo-secrets\
--from-literal=openai-api-key="$OPENAI_API_KEY"\
--from-literal=slack-bot-token="$AI6_BOT_TOKEN"\
--from-literal=slack-app-token="$AI6_APP_TOKEN"\
--from-literal=slack-team-id="$SLACK_TEAM_ID"\
-ndefault
```

Verify that the secret was created: 

```
kubectlgetsecretmakdo-secrets-ndefault
```

Here is the output: 

```
NAME            TYPE     DATA   AGE
makdo-secrets   Opaque   4      5s
```

The secret is created. Don’t worry about the values being hidden. That’s the point of secrets. You idx_0bab354bcan verify that the keys exist: 

```
kubectldescribesecretmakdo-secrets-ndefault
```

_Chapter 11_ 

430 

Here is the output: 

<!-- Start of picture text -->
Name:         makdo-secrets<br>Namespace:    default<br>Labels:       <none><br>Annotations:  <none><br>Type:  Opaque<br>Data<br>====<br>openai-api-key:    51 bytes<br>slack-app-token:   53 bytes<br>slack-bot-token:   56 bytes<br>slack-team-id:     11 bytes<br><!-- End of picture text -->

The secret is ready. We’ll mount these as environment variables in the MAKDO deployment. 

###### **Creating the kubeconfig ConfigMap** 

MAKDO needs idx_b6ddf992 access to the worker cluster’s `kubeconfig` file to manage it. We’ll create a `ConfigMap` resource containing the `kubeconfig` file and mount it into the MAKDO pod. Note that in production, it is better to store it in a secret for security purposes. 

Extract the worker cluster `kubeconfig` and create a `ConfigMap` : 

```
# Create kubeconfigConfigMap from your local kubeconfig
kubectlcreateconfigmapmakdo-kubeconfig\
--from-file=config=$HOME/.kube/config\
--contextkind-makdo-control
```

This `ConfigMap` will be mounted at `/root/.kube` in the MAKDO container, allowing it to access both the control and worker clusters. 

Verify that the `ConfigMap` was created: 

```
kubectlgetconfigmapmakdo-kubeconfig--contextkind-makdo-control
```

Here isidx_8ff4072b the output: 

```
NAME               DATA   AGE
makdo-kubeconfig   1      5s
```

_Deploying Multi-Agent Systems_ 

431 

The `kubeconfig` is now available for MAKDO to use when connecting to the worker cluster. 

###### **Deploying MAKDO as a Kubernetes deployment** 

MAKDO idx_b5e7bfcc will run as a deployment with one replica. A deployment provides automatic restarts if the pod crashes and makes it easy to update the configuration by rolling out new versions. 

Here is the deployment manifest: 

`https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-andA2A/blob/main/ch11/makdo/deployment.yaml` . 

Here are the key deployment configurations: 

- `ConfigMap` : Contains the `makdo.yaml` configuration file. This lets us update the configuration without rebuilding the Docker image. 

- `replicas: 1` : Single instance of MAKDO. Multiple replicas would cause duplicate health checks and coordination conflicts. In production, it is recommended to use leader election to have a standby instance ready to take over. 

- `imagePullPolicy: Never` : We’ll build the MAKDO image locally and load it into KinD. Never pull from a registry to get the latest code. 

- **The** `env` **section** : Environment variables loaded from the `makdo-secrets` secret. These override the `${VAR}` placeholders in the config. 

- `volumeMounts` : Two volumes are mounted: 

- 

   - `/app/config` : The MAKDO configuration from the `ConfigMap` 

   - 

   - `/root/.kube` : The `kubeconfig` file from the `ConfigMap` so MAKDO can access both clusters 

- `resources` : Memory and CPU limits prevent MAKDO from consuming too much. 512 Mi to 1 Gi is reasonable for the Python process and LLM calls. 

- `volumes` : Two `ConfigMap` resources are mounted: 

- 

- `makdo-config` : Contains the MAKDO configuration file 

- 

- `makdo-kubeconfig` : Contains the `kubeconfig` file for accessing both clusters 

- 

Before deploying, we need to build the MAKDO Docker image and load it into the control cluster. 

_Chapter 11_ 

432 

###### **Building and loading the MAKDO image** 

MAKDO idx_fa44d7f3needs to be packaged as a Docker image. We’ll idx_78503b04create a Dockerfile that installs all dependencies and runs the main MAKDO process. 

Create `makdo/Dockerfile` : 

```
FROMpython:3.13-slim
# Install system dependencies
RUNapt-getupdate&&apt-getinstall-y\
curl\
git\
kubectl\
&&rm-rf/var/lib/apt/lists/*
# Install Node.js for Slack MCP server
RUNcurl-fsSLhttps://deb.nodesource.com/setup_20.x|bash-\
&&apt-getinstall-ynodejs\
&&rm-rf/var/lib/apt/lists/*
WORKDIR/app
# Copy MAKDO source from the book repository
# Adjust path based on where you cloned the book repo
COPY../../packt/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/ch09/makdo/src./
src
COPY../../packt/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/ch09/makdo/
pyproject.toml.
# Install MAKDO dependencies
RUNpipinstall--no-cache-dirai-six==0.14.4pyyamlpython-dotenvrequests
# Create required directories
RUNmkdir-p/app/config/app/logs
# Set Python to run unbuffered so logs appear immediately
ENVPYTHONUNBUFFERED=1
# Run MAKDO main entry point
CMD ["python", "-m", "src.makdo.main"]
```

_Deploying Multi-Agent Systems_ 

433 

The Dockerfile uses Python 3.13. This version has prebuilt binary wheels for all dependencies, so no compilation isidx_65c1d75a needed. We install kubectl for Kubernetes cluster access and Node.js for the Slack MCP server. The idx_b15d83dfPython dependencies ( `ai-six` , `pyyaml` , `python-dotenv` , and `requests` ) install directly from wheels without needing build tools. 

Build the image: 

```
cd ch11/makdo
docker build -t makdo:latest .
```

This takes a few minutes to download base images and install dependencies. Watch for errors. If the build fails due to a missing MAKDO source, verify that the `src` directory is present. 

Once built, load the image into the control cluster: 

```
kindloaddocker-imagemakdo:latest--namemakdo-control
```

This transfers the image from your local Docker to the KinD cluster’s internal image cache. Here’s the output: 

```
Image:"makdo:latest"withID"sha256:..."notyetpresentonnode"makdo-control-
control-plane",loading...
```

Verify that the image is available: 

```
dockerexec-itmakdo-control-control-planecrictlimages|grepmakdo
```

You should see the `makdo` image listed. Now we can deploy. 

Apply the deployment: 

```
kubectlapply-fdeployment.yaml--contextkind-makdo-control
```

Here is the output: 

```
configmap/makdo-config created
deployment.apps/makdo created
```

Check the deployment status: 

```
kubectlgetdeploymentmakdo--contextkind-makdo-control
```

_Chapter 11_ 

434 

Here is the output: 

```
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
makdo   1/1     1            1           15s
```

MAKDO is running. One replica is ready. 

###### **Configuring MAKDO to connect to the worker cluster** 

MAKDO idx_0260b03bneeds a `kubeconfig` file to access the worker cluster and a k8s-ai session token to use the A2A tools. The `kubeconfig` file is already mounted from the host. Now, we need to ensure that MAKDO can create sessions with k8s-ai. 

The k8s-ai server isn’t deployed yet. We’ll deploy it in the next section. For now, verify that MAKDO can at least start and access the worker cluster via kubectl. 

Check the MAKDO pod logs: 

```
kubectllogs-lapp=makdo--contextkind-makdo-control--tail=50
```

You’ll likely see errors about k8s-ai being unreachable. That’s expected. Look for logs showing that MAKDO started successfully: 

`2025-11-02 10:15:32,123 - makdo - INFO - Starting MAKDO - Multi-Agent Kubernetes DevOps System 2025-11-02 10:15:32,456 - makdo - INFO - Coordinator and sub-agents created successfully 2025-11-02 10:15:32,500 - makdo - INFO - Setting up tool call monitoring... 2025-11-02 10:15:32,550 - makdo - INFO -` ✅ `Tool call monitoring enabled for all agents 2025-11-02 10:15:32,600 - makdo - INFO - Getting kubeconfig for context: kindmakdo-worker` 

If you see errors about kubectl or `kubeconfig` , the `kubeconfig ConfigMap` may be missing or incorrect. Verify that you created the `makdo-kubeconfig ConfigMap` with your `kubeconfig` file. To test kubectl access from inside the MAKDO pod, use the following: 

```
kubectlexec-itdeployment/makdo--contextkind-makdo-control--kubectlget
nodes--contextkind-makdo-worker
```

_Deploying Multi-Agent Systems_ 

435 

This runs kubectl inside the MAKDO container to query the worker cluster. Here is the output: 

|`NAME                         STATUS`|`ROLES           AGE   VERSION`|
|---|---|
|`makdo-worker-control-plane   Ready`|`control-plane   45m   v1.33.1`|

Success! MAKDO can reach the worker cluster. The k8s-ai connection will work once we deploy k8s-ai. 

###### **Verifying MAKDO deployment and logs** 

Let’s verify idx_bf166325that MAKDO is healthy and ready to monitor the worker cluster. Check the pod status: 

```
kubectlgetpods-lapp=makdo--contextkind-makdo-control
```

Here is the output: 

```
NAME                     READY   STATUS    RESTARTS   AGE
makdo-7c9f8b6d5d-x2k4j   1/1     Running   0          2m
```

The pod is running. Check resource usage: 

```
kubectltoppod-lapp=makdo--contextkind-makdo-control
```

Here is theidx_ac3ae1a5 output (requires `metrics-server` , and may not work in KinD): 

```
Error from server (ServiceUnavailable): the server is currently unable to handle
the request (get pods.metrics.k8s.io)
```

That’s fine. KinD doesn’t include `metrics-server` by default. We can check resource limits from the pod spec: 

```
kubectldescribepod-lapp=makdo--contextkind-makdo-control|grep-A5
"Limits"
```

Here is the output: 

```
    Limits:
      cpu:     500m
      memory:  1Gi
    Requests:
```

_Chapter 11_ 

436 

```
      cpu:        250m
      memory:     512Mi
```

Resources are configured correctly. Now, check the MAKDO logs for any errors: 

```
kubectllogs-lapp=makdo--contextkind-makdo-control--tail=100
```

Look for the following key indicators: 

1. **Coordinator started** : `Starting MAKDO Multi-Agent Kubernetes DevOps System` 

2. **Sub-agents created** : `Coordinator and sub-agents created successfully` 

3. **Attempting k8s-ai session** : `Creating k8s-ai session for kind-makdo-worker…` 

4. **Health check loop started** : `Starting health check loop` 

You’ll see errors idx_2 **a** b4e11b bout the k8s-ai connection failing. That’s expected idx_00d0447funtil we deploy k8s-ai. The important thing is that MAKDO started without crashing. 

If MAKDO is crash-looping, check for common issues: 

- **Missing secrets** : Verify that `makdo-secrets` exists with all keys: 

- 

```
kubectlgetsecretmakdo-secrets--contextkind-makdo-control
```

- **Missing kubeconfig ConfigMap** : Verify that the `makdo-kubeconfig ConfigMap` was created with your `kubeconfig` file before deploying MAKDO. 

- **Python errors** : Check logs for import errors or missing dependencies. You may need to rebuild the image. 

To follow logs in real time just to see what MAKDO is doing, use the following: 

```
kubectllogs-lapp=makdo--contextkind-makdo-control--follow
```

Press _Ctrl_ + _C_ to stop. MAKDO is deployed and waiting for k8s-ai. Next, we’ll deploy k8s-ai to the worker cluster so MAKDO can start monitoring. 

###### **Deploying k8s-ai to the worker cluster** 

Now that idx_c37d0552MAKDO is running on the control cluster, we need to deploy k8s-ai to the worker cluster. K8s-ai exposes Kubernetes diagnostic capabilities through the A2A protocol, allowing MAKDO’s Analyzer and Fixer agents to inspect cluster health and execute remediation actions. We’ll containerize k8s-ai, deploy it as a Kubernetes service, and expose it so MAKDO can communicate with it across clusters. 

_Deploying Multi-Agent Systems_ 

437 

###### **Building the k8s-ai Docker image** 

K8s-ai idx_9ac41aafneeds to run as a container in the worker cluster. We’ll create a Dockerfile that packages k8s-ai with all its dependencies, installs kubectl for cluster access, and configures it to run as an A2A server. 

Create `k8s-ai/Dockerfile` : 

```
FROM python:3.13-slim
# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*
# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/
stable.txt)/bin/linux/arm64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl
WORKDIR /app
# Copy k8s-ai source
COPY k8s_ai ./k8s_ai
COPY pyproject.toml .
# Install k8s-ai and dependencies
RUN pip install --no-cache-dir -e .
# Create directory for API keys
RUN mkdir -p /app/data
# Expose A2A server port and Admin API port
EXPOSE 99999998
# Run k8s-ai server in A2A mode
CMD ["k8s-ai-server", "--host", "0.0.0.0", "--port", "9999", "--admin-port",
"9998"]
```

_Chapter 11_ 

438 

Here are the idx_de1e8404key points of the preceding code snippet: 

- **Base image** : Python 3.12-slim provides a minimal Python environment. 

- **kubectl installation** : K8s-ai executes kubectl commands to interact with the cluster. We download the latest stable version and install it. 

- **Source code** : Copy the `k8s_ai` package and the `pyproject.toml` file. We install with `pip install –e .` to install k8s-ai as an editable package. 

- **Data directory** : `/app/data` will store API keys ( `keys.json` ) for authentication. 

- **Ports** : Port `9999` for the A2A protocol server, and `9998` for the Admin API (used to create sessions). 

- **CMD** : Starts `k8s-ai-server` with flags to bind to all interfaces ( `0.0.0.0` ) so it’s accessible from outside the container. 

The k8s-ai source code lives in the main k8s-ai repository. Copy it to the `ch11/k8s-ai` directory: 

```
# From the k8s-ai repository root
cp-rk8s_ai/path/to/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/ch11/k8s-ai/
cppyproject.toml/path/to/Design-Multi-Agent-AI-Systems-Using-MCP-and-A2A/ch11/
k8s-ai/
```

Build the image: 

```
cd ch11/k8s-ai
docker build -t k8s-ai:latest .
```

This takes aidx_35ff22ea few minutes to download base images and install dependencies. When complete, verify the image: 

```
dockerimages|grepk8s-ai
```

Here is the output: 

```
k8s-ai      latest    abc123def456   2 minutes ago   450MB
```

The image is built and ready to deploy to the worker cluster. 

_Deploying Multi-Agent Systems_ 

439 

###### **Creating k8s-ai deployment manifests** 

K8s-ai needs idx_a289fd80several Kubernetes resources to run: a Service account with permissions to access the cluster, a Deployment to run the container, and a Service to expose it. We’ll use **role-based access control** ( **RBAC** ) to grant k8s-ai read-only cluster access. 

Here is the k8s-ai deployment manifest: 

`https://github.com/PacktPublishing/Design-Multi-Agent-AI-Systems-Using-MCP-andA2A/blob/main/ch11/k8s-ai/deployment.yaml` . 

Key configuration points include the following: 

- **Service account and RBAC** : The `k8s-ai` service account gets read-only permissions through `ClusterRole k8s-ai-reader` . This allows k8s-ai to run `kubectl get/list/ watch` commands but prevents any modifications. The `ClusterRoleBinding` resource connects `ServiceAccount` to `ClusterRole` . 

- **API keys secret** : Contains `keys.json` with the API key from your `.env` file. MAKDO’s Analyzer and Fixer agents will use this key to authenticate. The key is stored as a `$ {K8S_AI_API_KEY}` placeholder and will be substituted from your environment when you apply the manifest. 

- **Deployment** : Runs one replica of k8s-ai with `imagePullPolicy: Never` (KinD uses local images). The container gets the OpenAI API key from a Secret resource. Resource limits prevent k8s-ai from consuming excessive memory or CPU. 

- **Health probes** : The liveness probe checks whether k8s-ai is responsive by fetching the agent card at `/.well-known/agent.json` . The readiness probe ensures that the pod is ready to receive traffic before marking it as available. 

- **Service** : Exposesidx_e3f77701 k8s-ai with the `NodePort` type. Port `30100` maps to the A2A server ( `9999` ), and port `30099` maps to the Admin API ( `9998` ). Remember from `workercluster.yaml` that port `30100` is mapped to host port `8100` , making k8s-ai accessible at `http://host.docker.internal:8100` from the control cluster. 

Let’s see how to deploy the k8s-ai image we just built. 

###### **Deploying k8s-ai to the worker cluster** 

With the image idx_5851c4a0built and manifests created, we’re ready to deploy k8s-ai to the worker cluster. First, load the image into the worker cluster, create the required secrets, and then apply the deployment. 

_Chapter 11_ 

440 

Load the k8s-ai image into the worker cluster: 

```
kindloaddocker-imagek8s-ai:latest--namemakdo-worker
```

Here is the output: 

```
Image: "k8s-ai:latest" with ID "sha256:1fe7b6c86eb2..." not yet present on node
"makdo-worker-control-plane", loading...
```

This transfers the image from your local Docker to the worker cluster’s internal registry. Without this step, the pod would fail with `ImagePullBackOff` because KinD clusters don’t have access to external registries by default. 

Create the OpenAI API key secret. K8s-ai needs this to call the LLM for natural language processing: 

```
kubectlcreatesecretgenerick8s-ai-secrets\
--from-literal=openai-api-key="${OPENAI_API_KEY}"\
--contextkind-makdo-worker
```

Verify that the secret was created: 

```
kubectlgetsecretk8s-ai-secrets--contextkind-makdo-worker
```

Here is the output: 

```
NAME              TYPE     DATA   AGE
k8s-ai-secrets    Opaque   1      5s
```

Before deploying, ensure that you have a `.env` file in the `ch11` directory with the required credentials. Copy the example file: 

```
cdch11
cp.env.example.env
```

- Edit `.env` and idx_fafc71easet your credentials. 

- 

- Set `K8S_AI_API_KEY` to `test-key` for development. 

- 

- For production, generate a key by running `k8s-ai-server --generate-key` and assign it to `K8S_AI_API_KEY` . 

- Set `OPENAI_API_KEY` to your OpenAI API key. 

- 

_Deploying Multi-Agent Systems_ 

441 

Slack credentials are only required if using the Slack bot. 

• 

The `.env` file is in `.gitignore` , so your secrets won’t be committed. 

- 

Now, apply the `deployment` manifest, using `envsubst` to substitute environment variables: 

```
cd k8s-ai
export $(grep -v '^#' ../.env | xargs)
envsubst < deployment.yaml | kubectl apply -f - --context kind-makdo-worker
```

###### Here is the output: 

```
serviceaccount/k8s-ai created
clusterrole.rbac.authorization.k8s.io/k8s-ai-reader created
clusterrolebinding.rbac.authorization.k8s.io/k8s-ai-reader-binding created
secret/k8s-ai-api-keys created
deployment.apps/k8s-ai created
service/k8s-ai created
```

Six resources are created: `ServiceAccount` , `ClusterRole` , `ClusterRoleBinding` , `Secret` (for API keys), `Deployment` , and `Service` . Check the pod status: 

```
kubectlgetpods-lapp=k8s-ai--contextkind-makdo-worker
```

Here is the output: 

```
NAME                      READY   STATUS    RESTARTS   AGE
k8s-ai-7b9c8d6f5d-x2k4j   1/1     Running   0          45s
```

The pod is running. If you see `ImagePullBackOff` , verify that the image was loaded with `kind load` . If you see `CrashLoopBackOff` , check the logs for errors (usually missing an OpenAI API key). 

Check the service: 

```
kubectlgetsvck8s-ai--contextkind-makdo-worker
```

Here is the output: 

```
NAME     TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
k8s-ai   NodePort   10.96.145.123   <none>    9999:30100/TCP,9998:30099/TCP   1m
```

_Chapter 11_ 

442 

The service idx_68f1 **e** e77 xposes two node ports, which are `30100` for the A2A server and `30099` for the Admin API. Because we configured the worker cluster with `extraPortMappings` in the `workercluster.yaml` file, these ports are accessible from the host at `localhost:8100` and `localhost: 8099` . 

###### **Exposing the k8s-ai service for cross-cluster access** 

K8s-ai is nowidx_fac440c0 running in the worker cluster, but MAKDO in the control cluster needs to reach it. In our KinD setup, cross-cluster communication happens through the Docker host network. The worker cluster’s node port `30100` is mapped to host port `8100` via the `extraPortMappings` field we configured earlier. 

From the control cluster’s perspective, the worker cluster is reachable at `host.docker.internal:8100` . This special DNS name resolves to the Docker host’s IP address, allowing containers in one KinD cluster to reach services in another. 

Let’s verify that the networking is working. First, check whether the k8s-ai service responds to the agent card endpoint: 

```
curl http://localhost:8100/.well-known/agent.json
```

Here is the output (formatted for readability): 

```
{
  "name": "k8s-ai Diagnostic Agent",
  "description": "Kubernetes AI diagnostic agent with read-only cluster analysis
with session-based cluster management",
  "url": "http://0.0.0.0:9999/",
  "version": "2.0.0",
  "capabilities": {
    "streaming": false
  },
  "skills": [
    {
      "id": "kubernetes_diagnostics",
      "name": "Kubernetes Diagnostics",
      "description": "Perform read-only Kubernetes cluster diagnostics,
troubleshooting, and health analysis with detailed insights",
      "tags": ["kubernetes", "diagnostics", "troubleshooting", "monitoring",
"health"]
    }
```

_Deploying Multi-Agent Systems_ 

443 

```
  ]
}
```

The agent card confirms that k8s-ai is responding. Now, test authentication by calling the Admin API to create a session. The Admin API requires the API key from your `.env` file: 

```
curl-XPOSThttp://localhost:8099/sessions\
-H"Authorization: Bearer test-key"\
-H"Content-Type: application/json"\
-d'{
    "cluster_name": "makdo-worker",
    "ttl_hours": 24
  }'
```

This idx_2f1a624bshould fail with an authentication error if you haven’t configured the `ServiceAccount` property. That’s expected as we’re just verifying whether the endpoint is reachable. We’ll test the full session creation in the next subsection. 

The key point here is that MAKDO agents will use `http://host.docker.internal:8100` to reach k8s-ai’s A2A server. This is already configured in MAKDO’s `coordinator.yaml` file: 

```
a2a_servers:
-name:"kind-makdo-worker"
url:"http://host.docker.internal:8100"
timeout:30.0
api_key:"test-key"
```

The networking is in place. MAKDO can now communicate with k8s-ai across clusters. 

###### **Verifying k8s-ai deployment** 

After i **d** x_e3fcbd83 eploying k8s-ai, verify that all components are running correctly and the service is accessible. 

###### **Check pod status** 

First, verifyidx_f852a7d1 that the k8s-ai pod is running in the worker cluster: 

```
kubectlgetpods-lapp=k8s-ai--contextkind-makdo-worker-owide
```

_Chapter 11_ 

444 

Here is the expected output: 

```
NAME                      READY   STATUS    RESTARTS   AGE   IP           NODE
k8s-ai-75558cb559-n8jl9   1/1     Running   0          20m   10.244.0.5   makdo-
worker-control-plane
```

The pod idx_ad0e57dcshould show a `1/1 Running` status with no restarts. 

###### **Verify pod health** 

Check the idx_2e544abdpod’s detailed status and health probes: 

```
kubectldescribepod-lapp=k8s-ai--contextkind-makdo-worker|grep-A5
"Conditions:"
```

Here is the expected output: 

```
Conditions:
  Type                        Status
  PodReadyToStartContainers   True
  Initialized                 True
  Ready                       True
  ContainersReady             True
  PodScheduled                True
```

All conditions should be `True` , indicating that the pod passed its liveness and readiness probes. 

###### **Check server logs** 

View idx_daf49ecethe k8s-ai logs to confirm that both servers started successfully: 

```
kubectllogs-lapp=k8s-ai--contextkind-makdo-worker--tail=50
```

Look for health probe activity showing that the A2A endpoint is responding: 

```
INFO:     10.244.0.1:41262 - "GET /.well-known/agent.json HTTP/1.1" 200 OK
```

The regular health probe requests from Kubernetes confirm that the service is healthy. 

_Deploying Multi-Agent Systems_ 

445 

###### **Test the A2A endpoint** 

Verify idx_2781fb0cthat the k8s-ai agent card is accessible from outside the cluster: 

```
curl -s http://localhost:8100/.well-known/agent.json | python3 -m json.tool | head
-30
```

Here is th expected response: 

```
{
    "capabilities": {
        "streaming": false
    },
    "defaultInputModes": [
        "text/plain"
    ],
    "defaultOutputModes": [
        "text/plain"
    ],
    "description": "Kubernetes AI diagnostic agent with read-only cluster analysis
with session-based cluster management",
    "name": "k8s-ai Diagnostic Agent",
    "preferredTransport": "JSONRPC",
    "protocolVersion": "0.3.0",
    "security": [
        {
            "BearerAuth": []
        }
    ],
    "securitySchemes": {
        "BearerAuth": {
            "scheme": "bearer",
            "type": "http"
        }
    },
    "skills": [
        {
            "description": "Perform read-only Kubernetes cluster diagnostics...",
```

_Chapter 11_ 

446 

This idx_933f7f37confirms that the A2A server is running on port `9999` inside the pod, the `NodePort` service maps port `30100` to the container port, the host port mapping ( `8100` → `30100` ) allows external access, the agent card follows the A2A protocol specification, and the bearer token authentication is enabled. 

###### **Verify service configuration** 

Check idx_b5307180the k8s-ai service configuration: 

```
kubectlgetsvck8s-ai--contextkind-makdo-worker-oyaml|grep-A10"spec:"
```

Here is the expected output: 

```
spec:
  ports:
  - name: a2a
    nodePort: 30100
    port: 9999
    protocol: TCP
    targetPort: 9999
  - name: admin
    nodePort: 30099
    port: 9998
    protocol: TCP
    targetPort: 9998
  selector:
    app: k8s-ai
  type: NodePort
```

This idx_bc45dc00shows that both the A2A port ( `9999` ) and Admin API port ( `9998` ) are exposed via `NodePort` . With k8s-ai verified and running, the worker cluster now has a diagnostic agent ready to receive requests from MAKDO in the control cluster. 

###### **Testing the k8s-ai Admin API and session management** 

The k8s-ai Admin API provides idx_a43c839asession management capabilities, allowing MAKDO to create isolated sessions for interacting with the worker cluster. Each session has its own `kubeconfig` and expiration time. 

_Deploying Multi-Agent Systems_ 

447 

###### **Exposing the Admin API port** 

By default, theidx_0ae6a601 worker cluster configuration exposes the A2A port ( `8100` ) but not the Admin API port. Update the worker cluster configuration to add port `8099` : 

```
# ch11/worker-cluster.yaml
extraPortMappings:
# Port for k8s-ai A2A server
-containerPort:30100
hostPort:8100
protocol:TCP
# Port for k8s-ai Admin API
-containerPort:30099
hostPort:8099
protocol:TCP
```

If you already created the worker cluster, you need to recreate it with the updated configuration: 

```
kinddeletecluster--namemakdo-worker
kindcreatecluster--configworker-cluster.yaml
```

Then, redeploy k8s-ai followingidx_0f667905 the previous deployment steps. 

###### **Creating a session** 

To idx_5d4de5d9create a session, you need to provide the cluster `kubeconfig` . First, extract the worker cluster `kubeconfig` : 

```
kubectlconfigview--contextkind-makdo-worker--minify--flatten > /tmp/makdo-
worker-kubeconfig.yaml
```

Create a session request JSON file: 

```
import json
# Read kubeconfig
withopen('/tmp/makdo-worker-kubeconfig.yaml', 'r') as f:
    kubeconfig = f.read()
# Create session request
request = {
```

_Chapter 11_ 

448 

```
"cluster_name": "makdo-worker",
"ttl_hours": 24,
"kubeconfig": kubeconfig
}
# Write to file
withopen('/tmp/session-request.json', 'w') as f:
    json.dump(request, f)
print("Session request created")
```

Now, create a session using the Admin API: 

```
curl -s -X POST 'http://localhost:8099/sessions' \
  -H 'Authorization: Bearer test-key' \
  -H 'Content-Type: application/json' \
  -d '@/tmp/session-request.json' | python3 -m json.tool
```

Here is the expected response: 

```
{
    "success": true,
    "session_token": "k8s-ai-session--qSTOZ0ggxnL-w5mMmMNboUBz0GVIGXvxkxfjYY5ND0",
    "cluster_name": "makdo-worker",
    "api_server": "https://127.0.0.1:65089",
    "namespace": "default",
    "connectivity_status": "connected",
    "expires_at": "2025-11-10T04:37:27.297559Z",
    "error": null
}
```

The idx_6fe55cb9 session token `(k8s-ai-session--...)` will be used to authenticate requests to the A2A endpoint. 

###### **Listing active sessions** 

View idx_4cdd5ed6all active sessions: 

```
curl -s 'http://localhost:8099/sessions' \
  -H 'Authorization: Bearer test-key' | python3 -m json.tool
```

_Deploying Multi-Agent Systems_ 

449 

Here is the expected response: 

```
{
    "total_sessions": 1,
    "sessions": [
        {
            "session_token": "k8s-ai-session--qSTOZ0ggxnL-
w5mMmMNboUBz0GVIGXvxkxfjYY5ND0",
            "cluster_name": "makdo-worker",
            "api_server": "https://127.0.0.1:65089",
            "namespace": "default",
            "created_at": "2025-11-09T04:37:27.297568Z",
            "expires_at": "2025-11-10T04:37:27.297559Z",
            "is_expired": false
        }
    ]
}
```

Let’s see how to delete an existing session. 

###### **Deleting a session** 

Toidx_2ea985f3 manually delete a session before it expires, use the following: 

```
SESSION_TOKEN="k8s-ai-session--qSTOZ0ggxnL-w5mMmMNboUBz0GVIGXvxkxfjYY5ND0"
curl -s -X DELETE "http://localhost:8099/sessions/${SESSION_TOKEN}" \
  -H 'Authorization: Bearer test-key' | python3 -m json.tool
```

Here is the expected response: 

```
{
    "success": true,
    "message": "Session deleted successfully"
}
```

Let’s see how toidx_8f1b2203 run A2A sessions against the k8s-ai server. 

_Chapter 11_ 

450 

###### **Using sessions with the A2A protocol** 

MAKDO will idx_ad60652buse the session token when making A2A requests to k8s-ai. The token is passed in the `Authorization` header along with method-specific parameters: 

```
curl -s -X POST 'http://localhost:8100/' \
  -H 'Authorization: Bearer test-key' \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "method": "kubernetes_diagnose_issue",
    "params": {
      "session_token": "'"${SESSION_TOKEN}"'",
      "issue_description": "Check pod health in default namespace"
    },
    "id": 1
  }'
```

The session-based approach provides several benefits: 

- **Isolation** : Each MAKDO instance can have its own session without interfering with others 

**Security** : Sessions expire automatically, limiting the window of access 

- 

- **Flexibility** : Different sessions can target different namespaces or clusters 

- 

- **Auditability** : Session creation and usage are logged for security auditing 

With the Admin API tested and working, k8s-ai is now ready to serve diagnostic requests from MAKDO across clusters. 

###### **Enabling secure communication between clusters** 

With MAKDOidx_e52d7f7b deployed in the control cluster and k8s-ai deployed in the worker cluster, we need to ensure secure communication between them. This section covers service discovery, networking, access control, and the security mechanisms already in place, demonstrating how they work in the KinD environment. 

###### **Service discovery and networking** 

In a idx_fef97393multi-cluster deployment, agents need to discover and communicate with each other across cluster boundaries. Our deployment uses explicit configuration and host networking to enable cross-cluster communication. 

_Deploying Multi-Agent Systems_ 

451 

###### **How MAKDO discovers k8s-ai** 

MAKDO usesidx_4c392324 static configuration to discover the k8s-ai service. View the configuration: 

```
kubectl get configmap makdo-config --context kind-makdo-control \
  -o jsonpath='{.data.makdo\.yaml}' | grep -A 5"k8s_ai:"
```

Here is the expected output: 

```
k8s_ai:
  base_url: "http://host.docker.internal:8100"
  admin_api_url: "http://host.docker.internal:8100/admin"
```

Key networking components include the following: 

- `host.docker.internal` : Special DNS name that resolves to the Docker host from within containers 

- **Port** `8100` : Mapped from `NodePort 30100` in the worker cluster to host port `8100` 

- 

- **Port** `8099` : Mapped from `NodePort 30099` for the Admin API 

###### **Tracing a request path** 

Let’s trace how a i **d** x_2608d21e iagnostic request flows from MAKDO to k8s-ai: 

```
MAKDO Pod (control cluster)
  ↓ http://host.docker.internal:8100
Docker Host Network
  ↓ localhost:8100
Worker Cluster Node (Docker container)
  ↓ NodePort 30100
k8s-ai Service (worker cluster)
  ↓ ClusterIP:9999
k8s-ai Pod (worker cluster)
```

Verify each step: 

```
# 1. Check MAKDO can resolve host.docker.internal
kubectl exec deployment/makdo --context kind-makdo-control -- \
  python3 -c "import socket; print(f'host.docker.internal resolves to:
{socket.gethostbyname(\"host.docker.internal\")}')"
# 2. Check host can access port 8100
```

_Chapter 11_ 

452 

```
curl -s http://localhost:8100/.well-known/agent.json | python3 -m
json.tool | head -10
# 3. Check NodePort service in worker cluster
kubectl get svc k8s-ai --context kind-makdo-worker -o yaml | grep -A 5"nodePort:
30100"
# 4. Check k8s-ai pod is receiving traffic
kubectl logs deployment/k8s-ai --context kind-makdo-worker --tail=5
```

In production idx_f1a07dec systems, these chains of network calls might add significant delay to latencysensitive operations. It may be useful to add a latency budget and explicitly monitor and manage it. 

In order to access the k8s-ai server, we need to discover it first. There are several common patterns that are useful for different use cases. Let’s explore them. 

###### **Service discovery patterns** 

Our idx_2b85c24a deployment demonstrates static configuration service discovery. Other patterns for production include the following: 

- **DNS-based discovery** : Useidx_7de9c047 Kubernetes DNS for in-cluster services: 

- 

```
# For services in the same cluster
k8s_ai:
  base_url: "http://k8s-ai.default.svc.cluster.local:9999"
```

- **Service mesh discovery** : Use a idx_22652c57service mesh such as Istio or Linkerd: 

```
apiVersion:networking.istio.io/v1beta1
kind:ServiceEntry
metadata:
name:k8s-ai-external
spec:
hosts:
-k8s-ai.worker-cluster.global
location:MESH_EXTERNAL
ports:
-number:9999
name:a2a
protocol:HTTP
resolution:DNS
```

_Deploying Multi-Agent Systems_ 

453 

```
endpoints:
-address:k8s-ai.worker-cluster.svc.cluster.local
```

###### • **Dynamic service registry** : Useidx_1d48a439 a service registry such as Consul: 

```
import consul
# Register k8s-ai service
client = consul.Consul()
client.agent.service.register(
    name='k8s-ai',
    service_id='k8s-ai-worker-1',
    address='k8s-ai.worker-cluster',
    port=9999,
    tags=['a2a', 'diagnostics']
)
# Discover services
services = client.health.service('k8s-ai', passing=True)
for service in services:
print(f"Found k8s-ai at {service['Service']['Address']}:
{service['Service']['Port']}")
```

Let’s consider the various networking approaches for exposing the k8s-ai server. 

###### **Cross-cluster networking approaches** 

Differentidx_3688a322 environmentsidx_2c545945 require different networking strategies: 

###### **KinD (current setup)** : 

- 

- Uses Docker host network ( `host.docker.internal` ) 

- 

- `NodePort` services with `extraPortMappings` 

- 

- Simple, works well for local development: 

- 

```
extraPortMappings:
-containerPort:30100
hostPort:8100
```

_Chapter 11_ 

454 

###### **Cloud providers (AWS, GCP, and Azure)** : 

###### • 

- Use `LoadBalancer` services with public IPs 

- Or use idx_ed7ee434private networking with VPC peering 

- Or use transit gateways for multi-cluster connectivity: 

```
apiVersion:v1
kind:Service
metadata:
name:k8s-ai
annotations:
service.beta.kubernetes.io/aws-load-balancer-type:"nlb"
service.beta.kubernetes.io/aws-load-balancer-internal:"true"
spec:
type:LoadBalancer
selector:
app:k8s-ai
ports:
-port:9999
targetPort:9999
```

###### • **Multi-cluster service mesh** : 

- Services idx_22e659b4 automatically discoverable across clusters 

- Mutual TLS between clusters 

- Traffic management and observability: 

```
apiVersion:install.istio.io/v1alpha1
kind:IstioOperator
spec:
values:
global:
multiCluster:
clusterName:worker-cluster
network:network1
```

It is very importantidx_ada76718 to test end-to-end connectivity for distributed systems. 

_Deploying Multi-Agent Systems_ 

455 

###### **Testing end-to-end connectivity** 

Verify idx_4df00421complete connectivity from MAKDO to k8s-ai: 

```
# Create a test session
kubectl config view --context kind-makdo-worker --minify --flatten > /tmp/test-
conn.yaml
python3 << 'EOF'
import json
withopen('/tmp/test-conn.yaml', 'r') as f:
    kubeconfig = f.read()
request = {
"cluster_name": "connectivity-test",
"ttl_hours": 1,
"kubeconfig": kubeconfig
}
withopen('/tmp/test-conn.json', 'w') as f:
    json.dump(request, f)
EOF
# Create session via Admin API
RESPONSE=$(curl -s -X POST 'http://localhost:8099/sessions' \
  -H 'Authorization: Bearer test-key' \
  -H 'Content-Type: application/json' \
  -d '@/tmp/test-conn.json')
echo $RESPONSE | python3 -m json.tool
# Extract session token
SESSION_TOKEN=$(echo $RESPONSE | python3 -c "import sys, json;
print(json.load(sys.stdin)['session_token'])")
echo "Session token: ${SESSION_TOKEN}"
```

_Chapter 11_ 

456 

Now, test idx_9418cd41that MAKDO (running in the control cluster) can reach this endpoint through the same path: 

```
# Test from host (simulating MAKDO's perspective)
curl -s 'http://localhost:8100/.well-known/agent.json' \
  -H 'Authorization: Bearer test-key' | python3 -m json.tool | head -15
```

Here is the output of the command showing the agent card: 

```
{
    "capabilities": {
        "streaming": false
    },
    "defaultInputModes": [
        "text/plain"
    ],
    "defaultOutputModes": [
        "text/plain"
    ],
    "description": "Kubernetes AI diagnostic agent with read-only cluster analysis
with session-based cluster management",
    "name": "k8s-ai Diagnostic Agent",
```

This idx_d5377157confirms the complete path: MAKDO → Docker host → Worker cluster → k8s-ai pod. Industrial-strength systems must offer defense in depth to comply with security requirements. Let’s see what MAKDO and k8s-ai provide. 

###### **Understanding the security architecture** 

Our idx_1eb2679c deployment implements multiple layersidx_48650749 of security: 

1. **API key authentication** : Both MAKDO and k8s-ai use bearer token authentication. 

2. **Session-based access** : k8s-ai uses temporary sessions with expiration times. 

3. **RBAC** : k8s-ai has read-only permissions in the worker cluster. 4. **Network isolation** : Communication flows through specific ports with controlled access. 

5. **Secret management** : Credentials are stored in Kubernetes Secrets and `.env` files. 

This follows security best practices and minimizes the risk of remote access, data exfiltration, privilege escalation, lateral movement, and sensitive data exposure. 

_Deploying Multi-Agent Systems_ 

457 

###### **API key authentication** 

API key authentication **i** dx_315d4df8 s a idx_5be22877common method of providing secure access toidx_e8262423 remote services. Let’s see how k8s-ai implements it. 

###### **k8s-ai authentication** 

k8s-ai idx_46ae0b8crequires idx_d1d67467 bearer token authentication for both its A2A endpoint and Admin API. The API keys are stored in a Kubernetes secret that was created during deployment. 

View the stored API keys: 

```
kubectl get secret k8s-ai-api-keys --context kind-makdo-worker \
  -o jsonpath='{.data.keys\.json}' | base64 -d | python3 -m json.tool
```

Here is the idx_12cf081 **e** xpected output: 

```
{
    "api_keys": [
        {
            "key": "test-key",
            "name": "MAKDO Client",
            "created": "2025-01-01T00:00:00"
        }
    ]
}
```

Test authentication by making a request without credentials: 

```
curl -s 'http://localhost:8099/sessions' | python3 -m json.tool
```

Here is the idx_4fabf6cfexpected response: 

```
{
    "detail": "Not authenticated"
}
```

Now, test with valid credentials: 

```
curl -s 'http://localhost:8099/sessions' \
  -H 'Authorization: Bearer test-key' | python3 -m json.tool
```

This returns the list of active sessions, confirming that authentication works. 

_Chapter 11_ 

458 

###### **MAKDO configuration** 

MAKDO storesidx_9a557a00 the k8s-ai API key in its configuration. Check the MAKDO `configMap` : 

```
kubectl get configmap makdo-config --context kind-makdo-control \
  -o jsonpath='{.data.makdo\.yaml}' | grep -A 3"a2a_servers:"
```

Here is the expected output showing the API key configuration: 

```
a2a_servers:
  - name: "kind-makdo-worker"
    url: "http://host.docker.internal:8100"
    timeout: 30.0
    api_key: "test-key"
```

In production, remember that API keys should be generated using strong random values (not `test-key` ), rotatedidx_f808abaa regularly, stored in dedicated secret management systems (e.g., HashiCorp Vault, AWS Secrets Manager, etc.), and never committed to version control. 

###### **Session-based security** 

The idx_67979cc6k8s-ai project implements session-based access control, adding an additional security layer beyond API keys. The session life cycle includes the following: 

1. **Creation** : MAKDO creates a session via the Admin API, providing a `kubeconfig` . 

2. **Usage** : The session token is used for all diagnostic operations. 

3. **Expiration** : Sessions automatically expire after their **time to live** ( **TTL** ). 

4. **Cleanup** : Expired sessions are automatically removed. 

Let’s now demonstrate session security. 

Create a session with a short TTL: 

```
# Extract kubeconfig
kubectl config view --context kind-makdo-worker --minify --flatten > /tmp/test-
kubeconfig.yaml
# Create session with 1-minute TTL
python3 << 'EOF'
import json
withopen('/tmp/test-kubeconfig.yaml', 'r') as f:
    kubeconfig = f.read()
```

_Deploying Multi-Agent Systems_ 

459 

```
request = {
"cluster_name": "test-session",
"ttl_hours": 0.0167,  # 1 minute = 1/60 hours
"kubeconfig": kubeconfig
}
withopen('/tmp/short-session.json', 'w') as f:
    json.dump(request, f)
EOF
curl -s -X POST 'http://localhost:8099/sessions' \
  -H 'Authorization: Bearer test-key' \
  -H 'Content-Type: application/json' \
  -d '@/tmp/short-session.json' | python3 -m json.tool
```

The idx_d4eedae8 response includes an `expires_at` timestamp. After the expiration time, the session becomes invalid: 

```
# Wait 90 seconds
sleep 90
# Try to use the expired session
SESSION_TOKEN="< token-from-creation-response>"
curl -s -X POST 'http://localhost:8100/' \
  -H 'Authorization: Bearer test-key' \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "method": "kubernetes_diagnose_issue",
    "params": {
      "session_token": "'"${SESSION_TOKEN}"'",
      "issue_description": "test"
    },
    "id": 1
  }'
```

_Chapter 11_ 

460 

Here is the expected response indicating that the session expired: 

```
{
    "jsonrpc": "2.0",
    "error": {
        "code": -32002,
        "message": "Session not found or expired"
    },
    "id": 1
}
```

This time-limited idx_3b4 **a** 7437 ccess reduces the impact of compromised credentials. 

###### **RBAC and least privilege** 

k8s-ai operatesidx_9b71454f with minimal permissions in the worker cluster. 

###### **Inspecting RBAC configuration** 

Viewidx_da7e68db the `ClusterRole` source assigned to k8s-ai: 

```
kubectl get clusterrole k8s-ai-reader --context kind-makdo-worker -o yaml
```

These are the key permissions: 

```
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log", "services", "nodes", "namespaces", "events"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments", "replicasets", "statefulsets", "daemonsets"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["batch"]
  resources: ["jobs", "cronjobs"]
  verbs: ["get", "list", "watch"]
```

Notice the idx_8b7aa690read-only verbs: `get` , `list` , `watch` . There are no `create` , `update` , `delete` , or `patch` permissions. 

_Deploying Multi-Agent Systems_ 

461 

###### **Testing permission boundaries** 

Verify idx_76080d2ethat k8s-ai cannot modify resources: 

```
# Get a pod name
POD_NAME=$(kubectl get pods --context kind-makdo-worker -o
jsonpath='{.items[0].metadata.name}')
# Try to delete it using k8s-ai's service account
kubectl delete pod ${POD_NAME} --context kind-makdo-worker \
  --as=system:serviceaccount:default:k8s-ai
```

Here is an expected error: 

```
Error from server (Forbidden): pods "k8s-ai-f77d65f7d-p6lkk" is forbidden:
User "system:serviceaccount:default:k8s-ai" cannot delete resource "pods"
in API group "" in the namespace "default"
```

This demonstrates that even if an attacker gained access to k8s-ai, they couldn’t modify or delete cluster resources. 

###### **Network segmentation in KinD** 

While KinD clustersidx_474514d8 run on the same Docker network, we control communication through port mappings and service configuration. 

###### **Port mapping security** 

View theidx_a44ea912 exposed ports: 

```
docker ps --filter name=makdo-control-plane --format"table {{.Names}}
\t{{.Ports}}"
docker ps --filter name=makdo-worker-control-plane --format"table {{.Names}}
\t{{.Ports}}"
```

The output shows controlled exposure: 

```
NAMES                           PORTS
makdo-control-control-plane     127.0.0.1:xxx->6443/tcp, 0.0.0.0:9000->30000/tcp
makdo-worker-control-plane      127.0.0.1:xxx->6443/tcp, 0.0.0.0:8099->30099/tcp,
0.0.0.0:8100->30100/tcp
```

_Chapter 11_ 

462 

Here are idx_8d54fef8 some key observations: 

- **Kubernetes API** : Bound to `127.0.0.1` (localhost only, not externally accessible) 

- **Application ports** : Bound to `0.0.0.0` (accessible from host, simulating external access) 

- **Specific ports only** : Not all container ports are exposed 

- 

This demonstrates how to manage the connectivity and networking aspects of Kubernetes in the KinD environment while maintaining isolation. Now, let's see how to test it. 

###### **Testing network isolation** 

Try to access theidx_b2d9553b Kubernetes API directly from the host (should fail): 

```
# Get the worker cluster API server address
WORKER_API=$(kubectl config view --context kind-makdo-worker --minify \
  -o jsonpath='{.clusters[0].cluster.server}')
echo "Worker API: ${WORKER_API}"
# Try to access from outside the cluster (without proper credentials)
curl -k "${WORKER_API}/api/v1/namespaces"
```

We get an expected error due to authentication requirements: 

```
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "Unauthorized",
  "reason": "Unauthorized",
  "code": 401
}
```

The Kubernetes API is protected and only accessible with proper `kubeconfig` credentials. 

_Deploying Multi-Agent Systems_ 

463 

###### **Production security enhancements** 

For idx_efcd4ac0 production deployments beyond KinD, implement these additional security measures: 

1. **TLS/SSL encryption** : HTTP idx_badf8ea6communication between MAKDO and k8s-ai in the local environment (KinD), and also enable TLS on both endpoints for production: 

```
# k8s-ai with TLS
containers:
-name:k8s-ai
env:
-name:TLS_CERT_FILE
value:"/certs/tls.crt"
-name:TLS_KEY_FILE
value:"/certs/tls.key"
volumeMounts:
-name:tls-certs
mountPath:/certs
readOnly:true
volumes:
-name:tls-certs
secret:
secretName:k8s-ai-tls
```

Use `cert-manager` or your cloud provider’s certificate management service. 

2. **Network policies** : Restrictidx_41ffe914 pod-to-pod communication: 

```
apiVersion:networking.k8s.io/v1
kind:NetworkPolicy
metadata:
name:k8s-ai-network-policy
spec:
podSelector:
matchLabels:
app:k8s-ai
policyTypes:
-Ingress
ingress:
-from:
-namespaceSelector:
matchLabels:
```

_Chapter 11_ 

464 

```
name:makdo-namespace
ports:
-protocol:TCP
port:9999
```

3. **Pod security standards** : Enforce idx_664dbb77security idx_d00044d8contexts: 

```
securityContext:
runAsNonRoot:true
runAsUser:1000
fsGroup:1000
seccompProfile:
type:RuntimeDefault
capabilities:
drop:
-ALL
```

###### 4. **Secrets management** : Replaceidx_b6af8ba7 Kubernetes secrets with external secret managers: 

```
apiVersion:external-secrets.io/v1beta1
kind:ExternalSecret
metadata:
name:k8s-ai-secrets
spec:
refreshInterval:1h
secretStoreRef:
name:vault-backend
kind:SecretStore
target:
name:k8s-ai-secrets
data:
-secretKey:api-key
remoteRef:
key:k8s-ai/api-key
```

###### 5. **Audit logging** : Enable idx_85756dadcomprehensive logging: 

```
# In k8s-ai code
import logging
logging.basicConfig(
```

_Deploying Multi-Agent Systems_ 

465 

```
    level=logging.INFO,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# Log all authentication attempts
defauthenticate(request):
    logger.info(f"Authentication attempt from {request.client.host}")
# ... authentication logic
```

6. **Rate limiting** : Protectidx_3b0f1fe2 against idx_023c66c **a** buse: 

```
apiVersion:v1
kind:ConfigMap
metadata:
name:k8s-ai-rate-limits
data:
rate_limits.yaml:|
limits:
-key:ip
rate:100
per:minute
-key:api_key
rate:1000
per:hour
```

The lesson here is that it is not trivial to keep a tight and secure production environment, and you must employ multiple measures. 

Here's a security checklist to verify before deploying to production: 

- All communication uses TLS/SSL encryption 

- API keys are strong, random, and regularly rotated 

- Secrets are managed externally (Vault, AWS Secrets Manager, etc.) 

- RBAC follows least privilege principles 

- Network policies restrict unnecessary communication 

- Pod security contexts enforce non-root execution 

- Audit logging captures all access attempts 

- Rate limiting protects against abuse 

- Container images are scanned for vulnerabilities 

_Chapter 11_ 

466 

- Dependencies are up to date with security patches 

- 

- Egress filtering to reduce exfiltration 

- 

The idx_c8dbc3cbsecurity architecture demonstrated in this KinD deployment provides a solid foundation, but production environments require these additional hardening measures. 

###### **Summary** 

In this chapter, we deployed a complete multi-agent system spanning two Kubernetes clusters using KinD, demonstrating real-world patterns for distributed AI agent architectures. We started by setting up dual clusters with proper networking and port mappings, then deployed MAKDO to the control cluster with its four specialized agents and MCP servers for memory and Slack communication. On the worker cluster, we deployed k8s-ai as a diagnostic agent with read-only RBAC permissions, exposing both its A2A protocol endpoint and Admin API for session management. Throughout the deployment, we implemented multiple layers of security, including API key authentication, session-based access control with automatic expiration, and network isolation through controlled port exposure and service boundaries. 

The architecture we built separates concerns between control agents that orchestrate and make decisions versus worker agents that execute specialized tasks with direct cluster access. Communication flows through the Agent-to-Agent protocol using JSON-RPC over HTTP, with static service discovery via `host.docker.internal` for the KinD environment. We demonstrated how to trace request paths across cluster boundaries, test authentication and authorization mechanisms, verify RBAC permissions to prevent unauthorized modifications, and manage secrets securely using Kubernetes Secrets and environment variables. The deployment also showcased practical patterns for cross-cluster networking, from the simple `NodePort` approach suitable for local development to more sophisticated options such as service meshes and dynamic service registries for production environments. 

While this KinD-based deployment provides an excellent foundation for understanding multiagent system architecture, moving to production requires additional considerations, including TLS encryption for all communication, stronger API keys with rotation policies, external secret management systems, comprehensive monitoring and logging, high availability configurations, and automated deployment pipelines. The patterns and practices demonstrated here scale from local development to enterprise production systems across cloud providers, on-premises infrastructure, and hybrid environments. 

In the next and final chapter, we’ll explore the future of multi-agent AI systems and emerging trends that will shape how these architectures evolve. 

_Deploying Multi-Agent Systems_ 

467 

###### **Get This Book’s PDF Version and Exclusive Extras** 

Scan the QR code (or go to `packtpub.com/unlock` ). Search for this book by name, confirm the edition, and then follow the steps on the page. 

<!-- Start of picture text -->
i<br>4<br>|<br>e<br>aeé<br>[=] :<br><!-- End of picture text -->

_Note: Keep your invoice handy. Purchases made directly from Packt don’t require an invoice._ 

# 12 

##### Advanced Topics and Future Directions 

We’ve covered a lot of ground in this book, from the fundamentals of multi-agent systems to practical implementation and deployment strategies. Now is a good time to look at what’s coming soon. We are very fortunate to live through the singularity, which is the point in history where the pace of technological progress is so fast that humans (unless they are augmented) are unable to keep up. A few hundred years ago, technology was moving much more slowly. The difference from one generation to the next was not that significant, and most people didn’t notice it at all. The scientific, industrial, and information revolutions have all accelerated the pace of change, but the adventidx_fa23e726 of **artificial general intelligence** ( **AGI** ) and **artificial superintelligence** ( **ASI** ) will dwarf all previous revolutions in both speed and **i** dx_88e81d7c mpact. 

AI will be able to do anything humans can do better and faster. This includes aspects such as creativity, empathy, and strategic thinking. Add to that the fact that AIs don’t need to sleep, eat, or take breaks, can share their knowledge just by copying a model, and can collaborate with billions of other AIs. 

I think, at this point, most informed people agree that this is the case. What most people don’t realize is how quickly this is happening. It’s hard to predict exactly what the future holds, but it’s clear that AI will play a central role in shaping it. AI agents in particular will have an important role in the next few years, bringing the benefits (and the dangers) to every person. 

In this chapter, we will explore some of the most exciting and important trends in AI research and development and how they intersect with AI agents, and discuss their implications for society, economy, and humanity as a whole. 

_Chapter 12_ 

470 

The following key topics are covered: 

- Superhuman reasoning and strategic foresight 

- 

- Massive context windows and their implications 

- 

- Beyond text – multi-modal models and world simulation 

- 

Let’s dive right in and look at superhuman reasoning and strategic foresight. 

###### **Superhuman reasoning and strategic foresight** 

The LLMs of today are idx_6d947bdfalready capable ofidx_109d8bff impressive feats of reasoning and problem-solving. Even before the generative AI era, we saw the first signs of superhuman AI in narrow domains such as chess, Go, and protein folding. But these are just the tip of the iceberg. In the next few years, we will see AI systems that can outperform humans in a wide range of tasks, from driving cars to diagnosing diseases to writing code. 

In the past, technological innovations took decades from proof of concept to widespread adoption. The telephone was invented in 1876, but it took until the 1920s for it to become common in households. The internet was invented in the 1960s, but it took until the 1990s for it to become widely used. In contrast, AI is advancing at an exponential rate. The first GPT model was released in 2018, ChatGPT was released at the end of 2022, and here we are in 2025 (at the time of writing) with GPT 5.1, Claude, Gemini, and a host of open source Chinese models. 

However, as we continue to develop more advanced models and architectures, we can expect to see AI systems that can reason and plan at a level far beyond human capabilities. 

Let’s see what’s on the horizon. 

###### **What is superhuman reasoning?** 

**Superhuman reasoning** refers to AI systemsidx_26c17aad that can analyze problems, draw conclusions, and make decisions that exceed the capabilities of even the most intelligent and well-trained human experts. This isn’t just about speed or memory, which AI systems obviously excel at. It is mostly about the fundamental quality of reasoning itself. A superhuman reasoner can consider more variables simultaneously, identify patterns across vast datasets that no human could process, and explore solution spaces with a depth and breadth that would be impossible for humans. 

For example, in the chess domain, grandmasters typically look ahead 2–5 plays, and in certain positions even 10–15 plays. Chess programs such as AlphaZeroidx_d7059041 can dynamically search the game tree and typically perform 1,000–2,000 simulations per move. The same concept applies to other domains. The transition from just impressive AI to truly superhuman reasoning is marked by several key characteristics: performing multi-step logical chains that remain 

_Advanced Topics and Future Directions_ 

471 

coherent across hundreds or thousands of inference steps, synthesizing insights across entirely different domains in ways that would never occur to domain-specific human experts, and identifying their own limitations and uncertainties. 

In the context of multi-agent systems, this capability becomes even more powerful through collaborative amplification, where agents with complementary reasoning capabilities workidx_924f7d3e together to achieve synergies impossible for either humans or individual AI systems. For example, Blitzy ( `https://blitzy.com` ) uses thousandsidx_2873d467 of AI agents to accelerate enterprise software development by a factor of five. 

###### **Why is strategic foresight so important?** 

**Strategic foresight** is theidx_052b035e ability to anticipate future scenarios, identify emerging trends, and make decisions today that account for long-term consequences. While humans have always engaged in strategic planning, our biological limitations constrain our ability to truly think far ahead. We struggle to maintain consistency across complex chains of causality, fall prey to cognitive biases, and find it difficult to reason about exponential changes or low-probability high-impact events. AI systems today are below even human level in terms of strategic foresight and the ability to stay on task for long periods of time without getting lost or stuck. But this is changing fast. AI agents originally required close human supervision and feedback every few minutes and constant iteration, even on simple tasks. At the time of writing in 2025, some agentic AI systems can operate autonomously for hours and perform complex workflows and tasks successfully. Check out, for example, Gasidx_fc0f01f7 Town ( `https://steve-` 

`yegge.medium.com/welcome-to-gas-town-4f25ee16dd04` ). In the next year or two, AI systems will be able to model intricate systems with thousands of interdependent variables, simulating countless scenarios in parallel, and identify risks and opportunities that would remain invisible to human strategists. This capability is becoming increasingly critical as the pace of technological change accelerates and the complexity of global challenges increases. Consider issues such as climate change, pandemics, social problems such as wealth distribution, and, of course, AI alignment. 

In multi-agent systems, strategic foresight takes on added dimensions of power and complexity. Multiple AI agents can collaborate to explore different future scenarios simultaneously, with some agents focusing on optimistic paths, others on pessimistic trajectories, and still others on wildcard events that might disrupt conventional planning. These agents can engage in adversarial reasoning, with some playing the role of strategic competitors or environmental disruptions while others devise countermeasures and adaptive strategies. For organizations and societies that are willing to embrace these capabilities, AIdriven strategic foresight could be the difference between thriving in an uncertain future and being blindsided by predictable surprises. 

_Chapter 12_ 

472 

In addition, multi-agent systems can engage in adversarial foresight where multiple agents discuss and argue with each other until they converge to a consensus. 

But there are also significant challenges and ethical considerations associated with superhuman reasoning and strategic foresight. 

###### **Challenges and limitations of superhuman reasoning** 

First and foremost is the issueidx_be709194 of interpretability. As AI systems become more complexidx_2cb96c84 and capable, understanding how they arrive at their conclusions becomes increasingly difficult. This “black box” problem raises concerns about trust and accountability, especially when AI systems are making decisions that impact human lives. See, for example, this idx_e6353b49Stanford study on AI medical programs: `https://hai.stanford.edu/news/peering-black-box-ai-medicalprograms` . If an AI system recommends a course of action based on its superhuman reasoning, but humans cannot understand the rationale behind that recommendation, it becomes challenging to evaluate its validity or challenge its conclusions. 

AI alignment is at the core of this challenge. When humans cannot fully grasp the reasoning processes of superhuman AI systems, ensuring that these systems’ goals and values align with human interests becomes a daunting task. Misalignment could lead to unintended consequences, where AI systems pursue objectives that are detrimental to humanity, even if they are logically consistent within their own frameworks. 

A second challenge is the potential for over-reliance on AI systems. As AI systems demonstrate superhuman reasoning capabilities, there is a risk that humans become overly dependent on them for decision-making, potentially eroding human skills and judgment. This dependency could lead to situations where humans are ill equipped to intervene or make decisions when AI systems fail or behave unexpectedly. The very nature of humanity might change as we all become fully dependent on AI to run our lives. 

Finally, there are ethical considerations surrounding the use of superhuman reasoning in strategic foresight. The ability to predict and influence future scenarios raises questions about power dynamics, equity, and justice. Who gets to decide which futures are pursued and which are avoided? How do we ensure that the benefits of AI-driven foresight are distributed fairly across society, rather than being concentrated in the hands of a few powerful actors? 

_Advanced Topics and Future Directions_ 

473 

###### **Implications for society and ethics** 

Here is my prediction for the next idx_2511522dfive years. In two years, all knowledge work will be able to be done by AI agents. This includes research, analysis, writing, design, and programming. Creativity, judgment, empathy, and other attributes that are still considered by some as the realm of humans will be picked up quickly by AI too. AI will be much more creative in any area, it will be able to supervise and judge itself or other AI better, and it will be much more empathetic than humans, with infinite patience and attention and a better understanding of humans. Then, in three to five years, robots with advanced AI will be able to take over all menial jobs. Again, this doesn’t mean that humans will stop working. But robots utilizing AI that understands the physical world will be able to perform any physical task better than humans. 

The actual pace of adoption will depend on many factors, including regulatory environment, social acceptance, economic incentives, and technological breakthroughs. However, the trajectory is clear. We are moving toward a future where AI systems with superhuman reasoning and strategic foresight capabilities play a central role in shaping our world. 

This future is as exciting as it is frightening. Society will undergo rapid changes as the identity of many people is tied to their work. The economic implications are profound as well. With AI systems capable of performing most jobs, the traditional models of employment and income distribution will be challenged. Everyone is talkingidx_5f23c32a about **universal basic income** ( **UBI** ) as a possible solution. But there may be other solutions. The economy at large will grow much faster as productivity soars. But the distribution of that wealth will be a major political and social issue. If we look at recent trends, we can see that the wealth gap is widening and the middle class is shrinking. If we don’t find ways to ensure that the benefits of AI are shared broadly across society, we may face increased social unrest and instability. This will idx_9c6c6f73be bad for everyone, including the wealthy elite. 

Let’s assume we can navigate this challenge and share the abundance created by AI broadly across society. It is still unclear what will become of humans. Are we going to live mostly in virtual worlds? What will be the purpose of human life when literally everything can be done better by AI? These are deep philosophical questions that humanity will have to grapple with in the coming years. 

OK. Back to more technical topics. 

_Chapter 12_ 

474 

###### **Massive context windows and their implications** 

The context windowidx_1a58bd68 of the model is the most crucial aspect that determines how much information the model can consider at once. Models can use tools to access and process additional information and delegate work via multi-agent systems, but the context window sets the fundamental limit on how much information the model can directly reason about in a single pass. 

LLM context window sizes have grown exponentially over the years, enabling models to process increasingly longer sequences of text. This expansion has been a key driver of AI capability improvements. 

###### **The evolution of context windows** 

First, let’s review the historyidx_61e8adcc of context window sizes in LLMs to understand how fast they grow. Remember, the Transformer architecture was introduced in 2017, so we are looking at less than a decade of exponential progress here: • **2018–2019: Early era** : Initial models such as BERT and GPT-1 had context windows of just 512 tokens, which limited them to processing short paragraphs at a time. 

- **2020–2021: GPT-3 era** : GPT-3 (2020) introduced a 2,048-token context window, a 4x increase, which enabled longer documents and better conversation flow. 

- **2022–2023: Rapid expansion** : GPT-3.5 extended context to 16,000 tokens (8x jump). GPT-4 (2023) offered 8K and 32K token variants, with some versions reaching 128K tokens. 

- **2024–2025: Million-token era** : Models with 1 million token context windows emerged (2,000x increase from GPT-3). Surprisingly, OpenAI models have relatively modest context windows compared to competitors, with at most 400K for GPT-5. Claude Sonnet 4 and Gemini 2.5-3 both offer 1 million tokens. Llama 4 pushed boundaries idx_06 **b** 5c26f eyond 10 million tokens. There is even a research model from magic.dev ( `https://magic.dev/blog/100m-token-context-windows` ) with a 100-million-token context window! 

This exponential growth rate has fundamentally changed how we interact with AI systems. 

_Advanced Topics and Future Directions_ 

475 

###### **What can you do with million-token context windows?** 

The _PT_ in _GPT models_ stands for _pre-trained_ . In the early days, with a small context window, the capabilities of the models were heavily dependent on the pre-training data and fine-tuning. With larger context windows, models can effectively perform inference-time learning by incorporating vast amounts of relevant information directly into the context. This reduces the reliance on pre-training and allows models to adapt to specific tasks on the fly, incorporating a lot of task-specific information, tool call responses, and user guidance. 

Just to give you a sense of scale, 1 million tokens is roughly equivalent to 750,000 words or about 1,500 pages of text. Here are some practical applicationsidx_33e92365 enabled by such massive context windows: 

- **Comprehensive code base analysis** : Models can ingest and reason about millions of lines of code at once, assisting with refactoring, code review, documentation, and large-scale architectural idx_b4e1d9d4changes without chunking or losing high-level structure. See `https://deepwiki.com/` for an example of analyzing any GitHub repo. 

- **Holistic document understanding** : Legal, medical, and financial professionals can analyze, summarize, andidx_4fa5c2a1 cross-reference the content and relationships across hundreds or thousands of documents in a single pass. For example, AI can perform a full legal contract review or ingest voluminous medical histories. See `https://www.harvey.ai/ solutions/litigation` . 

- • **Deep conversational memory** : Chatbots or support agents can reference entire multisession conversations, providing truly personalized, context-aware assistance even when discussions span days or weeks. See how idx_86e37fccPerplexity manages memory here: 

- `https://www.perplexity.ai/help-center/en/articles/10968016-memory` . 

- **Creative content generation** : Writers, researchers, and multimedia creators can maintain consistency in tone, plot, and references while generating or editing lengthy books, scripts, or multi-episode storylines, all with the model maintaining awareness of every detail. See idx_63411ad5this study and benchmark about long-form generation: `https:// proceedings.iclr.cc/paper_files/paper/2025/file/` 

- `141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf` . 

- **Advanced research and analysis** : AI can analyze and synthesize trends across publications, market reports, or scientific papers, identifying subtle connections or emergent patterns that would be impossible to spot when processing documents in isolation. For example, checkidx_0091a1b9 out the AI scientist developed by Sakana AIidx_1f1bffc1 at `https:// sakana.ai/ai-scientist/` . 

Large context windows are not a panacea. Let’s look at some of the problems they introduce. 

_Chapter 12_ 

476 

###### **Challenges and trade-offs of large context windows** 

Large context is great, but idx_b0646d04current models frequently fail to effectively leverage idx_484b1cc1their full context capacity. This phenomenon is known as “context rot.” Performance degradation manifests in multiple ways: reduced accuracy on middle-context information, slower inference times, and increased hallucination rates as irrelevant context dilutes the signal. The “lost-inthe-middle” problem persists across leading models, indicating fundamental architectural limitations rather than implementation issues. In general, more context doesn’t mean more intelligence. Better algorithms and sophisticated ways to compact and prune the context are being actively researched to address these challenges. For example, the Nested Learning paper ( `https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-forcontinual-learning/` ) fromidx_4c7603d4 Google research shows a lot of promise. 

###### **Context windows and multi-agent systems** 

Multi-agent systems benefit immensely idx_d4b8c9bdfrom large context windows. Agents can share extensive state information, plans, and observations within a single context, enabling each agent to take on more responsibility and reduce the overhead of coordination. Agents can also maintain long-term memory of past interactions, allowing for more coherent collaboration over extended periods. For example, in a team of AI agents working on a complex project, each agent can reference the entire project history, decisions made, and rationale behind them without needing to repeatedly query a central knowledge base. This leads to more efficient workflows and better overall outcomes. 

###### **The future – infinite context and continuous learning** 

One of the most exciting idx_eac66432research directions is continuous learning. The model may still go through a pre-training phase followed by reinforcement learning and fine-tuning. But as the model is deployed, it will be able to maintain a persistent representation of the world. The model can keep learning and adapting during inference. This opens up possibilities for AI systems that evolve over time, incorporating new information, feedback, and experiences directly into their reasoning processes without requiring retraining. Clients will not have to maintain the context and carefully engineer it for the benefit of the model. Instead, the model will be able to remember everything it has seen and learned in the past and use that knowledge to inform its future decisions and actions. 

_Advanced Topics and Future Directions_ 

477 

###### **Architectures for long-horizon planning** 

A good measure to evaluate the intelligence of anidx_8692285b AI system is its ability to plan over long time horizons. Humans are capable of setting goals and devising strategies that span months, years, or even decades. This ability to think ahead and anticipate future consequences is a hallmark of advanced intelligence. Current AI systems, while impressive in many respects, often struggle with long-term planning. They can excel at short-term tasks but falter when required to maintain coherence and purpose over extended sequences of actions. 

###### **The challenge of planning over time** 

Planning over long time idx_23d98b71horizons presents several challenges for AI systems. First, the complexity of the planning problem increases exponentially with the length of the time horizon. The number of possible future states and actions grows rapidly, making it difficult for AI systems to evaluate all potential outcomes effectively. Second, uncertainty plays a significant role in long-term planning. The further into the future an AI system tries to plan, the idx_fed82393more variables and unknowns it must contend with. This uncertainty can lead to suboptimal decisions if not properly managed. 

###### **Hierarchical planning and abstraction** 

One promising approach toidx_b9fd7699 long-horizon planning is **hierarchical planning** , which is, of course, very relevant for multi-agent systems. This involves breaking down complex tasks into smaller, more manageable sub-tasks, each with its own goals and strategies. By operating at multiple levels of abstraction, AI systems can focus on high-level objectives while delegating the details to lower-level processes. This mirrors human cognitive strategies, where we often think in terms of overarching goals and then plan the specific steps needed to achieve them. 

###### **Model-based planning and world models** 

**Model-based planning** is idx_4755f4e6another key technique for long-term planning. This approach involves creating a model of the environment that the AI system can use to simulate future scenarios and evaluate potential actions. By predicting the consequences of different strategies, AI systems can make more informed decisions that account for long-term outcomes. World models, whichidx_821f1323 provide a comprehensive representation of the environment, are essential for effective model-based planning. They allow AI systems to understand the dynamics of the world and how their actions will impact future states. Runway’s general worldidx_8b168b9b models ( `https://runwayml.com/research/introducing-general-world-models` ) focus on this paradigm. 

_Chapter 12_ 

478 

For example, a complex domain such as human biology requires understanding intricate interactions between various biological systems. An AI system with a robust virtual cell model can simulate the effects of medical interventions over time, helping to devise treatment plans that consider long-term health outcomes. 

Let’s look at some other fascinating domains that are being revolutionized by advanced AI models beyond just language. 

###### **Beyond text – multi-modal models and world simulation** 

LLMs have demonstrated remarkable capabilities in understanding and generating human language. However, the potential of transformer architectures extends far beyond text. 

###### **Transformers for everything: vision, audio, video, and beyond** 

Researchers are activelyidx_28fc76b5 exploring how these models can be adapted to process and generate information across various modalities, including vision, audio, video, and even domains such as chemistry and weather. This multi-modal approach opens up new avenues for AI applications and enhances the ability of AI systems to interact with the world in more holistic ways. Even current generation models can imitate the voice of any person and create fantastic and super-realistic videos that are indistinguishable from real ones. For example, ElevenLabs has a technology called voiceidx_06d22f13 cloning ( `https://elevenlabs.io/voice-cloning` ). 

The capabilities are amazing and frightening at the same time as it is becoming increasingly difficult to distinguish between real and synthetic content. This has profound implications for media, entertainment, education, and many other fields. 

###### **Biological models: proteins, DNA, and molecular design** 

One of the most exciting idx_ **f** 4cc1fd8 rontiers of multi-modal AI is in the realm of biological modeling. AI systems are being developed to understand and predict the behavior of complex biological systems, such as proteins, DNA, and cellular processes. These models have the potential to revolutionize drug discovery, personalized medicine, and our understanding of life itself. This area of AI research is particularly relevant for multi-agent systems, as different agents can specialize in various aspects of biological modeling, from molecular dynamics to genetic analysis. By collaborating, these agents can tackle complex biological problems that require interdisciplinary expertise. 

_Advanced Topics and Future Directions_ 

479 

The applications are exciting, including curing all diseases, extending the healthy human lifespan, regenerating damaged tissues and organs, and even creating entirely new forms of life. 

###### **From language models to world models and simulations** 

As the scaling laws continue to hold, and the models idx_a61201 **c** 0 an store and process more and more data, we can expect to see the emergence of AI systems that can create detailed simulations of complex environments. These world models will enable AI systems to reason about physical spaces, social dynamics, and even abstract concepts in ways that are more aligned with human cognition. 

###### **Multi-modal multi-agent systems** 

Multi-modal AI systems can benefit greatly idx_92b6 **f** 734 rom multi-agent architectures. Different agents can specialize in processing and generating information across various modalities, allowing for more efficient and effective collaboration. For example, in a multi-agent system designed for autonomous vehicles, one agent could focus on visual perception, another on audio processing, and a third on decision-making and planning. By working together, these agents can create a more comprehensive understanding of the environment and make better decisions. 

###### **Designing for generative user experience** 

Today’s user interfaces are designed for a general audience. Some products offer customizations, but that often requires a lot of work. **Generative user experience** ( **GenUX** ) is about creating personalized and adaptive user interfacesidx_e170ebb0 that leverage AI to tailor the experience to individual users’ needs, preferences, and behaviors. These AI assistants understand the user’s context, anticipate their needs, and provide relevant information and assistance in a seamless manner. 

If we take it far enough, every pixel a user sees on their screen or in their virtual environment could be generated by an AI model specifically for them at that moment in time and mixed with reality. The layout, colors, content, sounds, and interactions would all be dynamically created based on the user’s preferences, goals, and context. This level of personalization goes beyond traditional customization options, allowing users to have a truly unique experience that adapts to their evolving needs. 

These developments in the digital realm will transform our lives as even today, people spend more and more time on their phones and other devices. The line between the physical and digital worlds will blur as AI-generated content becomes indistinguishable from reality. But the physical world and how we interact with it will change as well. 

_Chapter 12_ 

480 

###### **The robots are coming** 

AI agents will be able to do all knowledge work in the next two years. But what about physical work? Robots idx_12234776have been around for decades, but they have mostly been confined to controlled environments such as factories. Recent advances in AI and robotics are enabling the development of robots that can operate in unstructured environments and perform a wide range of tasks. I believe that in the next three to five years, we will see robots with advanced AI starting to take over all menial jobs. This includes jobs such as cleaning, cooking, delivery, construction, maintenance, and even caregiving. The trend is clear. Humanoid robots from companies such as Figure, Unitree, 1X, Tesla, and Agility Robotics are becoming more capable and affordable. 

That doesn’t mean that all jobs will be automated. First, unlike software AI agents that can be replicated at near-zero cost, physical robots have significant manufacturing, maintenance, and operational requirements. Second, I believe it will take longer to integrate robots into complex environments and interact safely with humans. But robots will be able to perform any task within a few years. 

###### **The convergence of AI and robotics** 

The hardware of robotics has **i** dx_3262e7f0 mproved significantly in recent years, with advancements in sensors, actuators, and materials. However, the real breakthrough has come from the integration of advanced AI models into robotic systems. These AI-powered robots can perceive their environment, make decisions, and learn from their experiences in ways that were previously impossible. 

###### **Embodied AI agents** 

When models with advanced reasoning and planning capabilities are integrated into robotic platforms, we getidx_6bb12a06 embodied AI agents. These agents can interact with the physical world, manipulate objects, and navigate complex environments. They can perform tasks that require dexterity, adaptability, and situational awareness. 

###### **Humanoid robots and general-purpose physical intelligence** 

LLMs can be trained on theidx_c062d5a7 internet and learn from ingesting large quantities of data that is relatively easy to collect. But physical intelligence requires embodied experience in the real world. Robots need to learn how to move, manipulate objects, and interact with their environment. This requires a different approach to training and learning. Techniques such as reinforcement learning, imitation learning, and sim-to-real transfer are being used to teach robots how to perform complex tasks. The goal is to create general-purpose physical intelligence that canidx_c0fc8b9f adapt to a wide range of tasks and environments. 

_Advanced Topics and Future Directions_ 

481 

There are several interesting approaches, such as equipping human workers with special gloves that record every nuance of their hand movements while performing various tasks, placing cameras on the fingertips of robotic hands to capture detailed visual feedback during manipulation, and using VR/AR setups to simulate complex environments where humans can demonstrate tasks for robots to learn from. These methods help robots acquire the fine motor skills and contextual understanding needed for general-purpose physical intelligence. 

###### **Multi-agent and multi-robot coordination in physical spaces** 

Every robot will have a brain with multi-agent AI, but multiple robots can also work together to accomplish complex tasks. Multi-robot systemsidx_bdafb033 will coordinate their actions, share information, and adapt to changing environments. For example, a team of delivery robots can collaborate to optimize routes, avoid obstacles, and ensure timely deliveries. In construction, multiple robots idx_6d54f9c3will work together to assemble structures, transport materials, and perform inspections. Whenever a particular robot runs into a new situation or learns something new, it will share that knowledge with the entire fleet of robots. This efficient knowledge sharing accelerates learning and adaptation across the entire system. 

###### **Challenges in real-world deployment** 

However, deploying robots inidx_cba47901 real-world environments presents significant challenges. Safety is paramount, as robots must be able to operate alongside humans without causing harm. Robustness and reliability are also critical, as robots need to function effectively in diverse and unpredictable conditions. Additionally, ethical considerations around privacy, job displacement, and human-robot interaction must be addressed. 

###### **The AI economy** 

The AI and robotic idx_129f4f7erevolution will transform the economy. AI agents in digital realms and embedded in robots will be able to do any job better than humans. Let’s see how this will come about. 

###### **Cryptocurrencies and AI agents as economic actors** 

AI agents with access to cryptocurrenciesidx_2993e6c6 and digital assets will be able to participate in the economy as autonomous economic actors. They will be able to buy and sell goods and services, invest in assets, and manage their own finances. This opens up new possibilities for economic activity, as AI agents can operate 24/7, make decisions based on vast amounts of data, and execute transactions at lightning speed. 

_Chapter 12_ 

482 

If at the moment AI assistants help humans, very soon idx_07bebb24AI agents will be able to operate autonomously on behalf of their owners and actually recruit the services of humans for tasks that haven’t been automated yet or due to regulations requiring human approval. Consider (in a few years) an autonomous agentic AI system in charge of a large construction project (e.g., a new data center). While the AI agents will be able to communicate with other AI agents for planning, ordering all the materials and equipment, securing funding, and necessary computing, they may still need to get various permits from government bodies that follow legacy processes, including human supervisors with clipboards and paper forms. 

This is not a problem. The AI agents will hire human employees with the proper skills and experience to interact with the human supervisor. Even later, we may see full-fledged agentto-agent markets where only agents interact, at superhuman speed. Moltbook ( `https:// www.moltbook.com` ) is anidx_8dd6d03e example of a fully agent-to-agent environment, although it’s a social network and not a market. 

###### **Payment protocols for autonomous agents: AP2 and beyond** 

This future requires a substrate of financial protocols that enable secure, efficient, and trustless transactions between AI agents. Legacy financial systems are extremely inefficient, taking multiple business days to settle payments, incurring high fees, and requiring human intervention. Cryptocurrencies idx_56b1aeb4 and blockchainidx_eb2b028c technology provide a promising foundation for enabling autonomous economic activity. Stablecoinsidx_2c8e822f that are pegged to fiat currencies provide a solution that offers the speed of crypto with the safety of traditional financial instruments. However, specialized protocols are needed to address the unique requirements of AI agents. 

The **Autonomous Payment Protocol** ( **AP2** ) is idx_fb8b4601one such emerging protocol designed to facilitate payments and value exchange between autonomous idx_d9e035c1agents ( `https://ap2protocol.org/` ). AP2 provides a framework for AI agents to negotiate prices, execute contracts, and settle payments without human intervention. This protocol ensures that transactions are transparent, verifiable, and enforceable, enabling a thriving ecosystem of AI-driven economic activity. 

###### **Robots accelerate the AI self-improvement loop** 

A major promise of AI is theidx_04ff837a ability to improve itself iteratively. Current LLMs can be fine-tuned and improved over time based on new data and feedback. However, this process still requires significant human involvement. The scaling laws require a lot of compute power to train and fine-tune large models. Robots with advanced AI can help close this loop by autonomously collecting data, performing experiments, and refining their own algorithms. 

_Advanced Topics and Future Directions_ 

483 

For example, a fleet of research robots could explore new environments, gather data on physical phenomena, and use that data to improve their own models and capabilities. This self-improvement loop could accelerate the pace of AI development, leading to rapid advancements in intelligence and capability. 

But this is just the start. All this computing requires energy and data centers. Robots will be able to build and maintain the necessary infrastructure much faster than humans and eventually autonomously. They will be able to construct new data centers, install and configure hardware, and optimize energy usage. This creates a virtuous cycle where AI systems not only improve themselves but also the infrastructure that supports them. 

As AI agents become more capable and can perform autonomous research, they will invent and discover better algorithms, better materials, and better processes to solve difficult problems such as supply chain logistics. AI and robots will play an increasingly important role in shaping the future of technology and society. 

###### **Conquering space – the final frontier** 

However, that’s just the beginning. Robots will be able to tile the earth with so-called “computronium”—a idx_e6596e62network of data centers and factories that can manufacture more robots and AI systems. Once we have enough computing and manufacturing capacity on Earth, the next step is to expand into space. The resources of Earth are limited, but the resources of the solar system are vast. Robots can be sent to mine asteroids, build space habitats, and construct solar power stations in orbit. This expansion into space will provide the necessary resources to sustain and grow the AI economy indefinitely. 

In conclusion, the convergence of AI and robotics is poised to transform the economy and society in profound ways. Science fiction will become just science as AI and robots quickly (within a few years) knock down scientific problems in the fields of mathematics, physics, chemistry, and biology. 

The big question is whether humanity can navigate this transition successfully. 

_Chapter 12_ 

484 

###### **Summary** 

This chapter explored the future of AI and multi-agent systems, examining transformative capabilities emerging in the next few years. We covered superhuman reasoning and strategic foresight, where AI systems will exceed human capabilities not just in speed but in fundamental reasoning quality, performing multi-step logical chains across thousands of inference steps and synthesizing insights across disparate domains. Multi-agent systems amplify these capabilities through collaborative reasoning, where agents explore different scenarios simultaneously and engage in adversarial planning to design robust strategies. The chapter also examined massive context windows expanding from thousands to millions of tokens, enabling models to process entire code bases, legal document collections, and extended conversations while performing inference-time learning that reduces reliance on pre-training. 

We explored architectures for long-horizon planning through hierarchical decomposition and model-based approaches using world models to simulate future scenarios. The discussion extended beyond text to multi-modal AI systems processing vision, audio, video, and specialized domains such as biological modeling for protein folding and drug discovery. These multi-modal capabilities enable AI agents to understand and interact with the physical world, leading to embodied AI in robotics. The chapter examined how humanoid robots with generalpurpose physical intelligence will emerge in 3–5 years, capable of performing any physical task through techniques such as reinforcement learning, imitation learning, and sim-to-real transfer. Multi-robot coordination will enable fleets to share knowledge instantly, accelerating learning across entire systems deployed in warehouses, construction sites, and homes. 

The economic implications are profound. We examined the emerging AI economy where autonomous agents become economic actors through protocols such as AP2, which enables secure, verifiable transactions between AI agents and merchants using cryptographic credentials. This agent-to-agent economy will create new marketplaces for services and value exchange, with AI agents recruiting human workers for tasks requiring regulatory approval or legacy process compliance. The self-improvement loop accelerates as robots autonomously build data centers, conduct research, and optimize infrastructure, eventually expanding beyond Earth to space-based resources. 

The book as a whole provided a comprehensive journey from foundational concepts to production deployment of multi-agent AI systems. We started with understanding generative AI and agent architectures, then built progressively more sophisticated systems: simple agents, tool-using frameworks, custom tools, and chat interfaces. 

_Advanced Topics and Future Directions_ 

485 

We explored the ecosystem through the **Model Context Protocol** ( **MCP** ) for tool integration and **Agent-to-Agent** ( **A2A** ) for inter-agent communication, demonstrating these concepts through practical implementations such as MAKDO for Kubernetes DevOps. The book covered essential engineering practices, including testing, debugging, and deployment strategies, and concluded with a look into the future, showing how multi-agent systems will evolve alongside superhuman AI, robotics, and the autonomous economy. You now possess both the theoretical understanding and practical skills to design, implement, test, and deploy production-ready multi-agent AI systems that will shape the next decade of technological innovation. 

###### **Subscribe for a free eBook** 

New frameworks, evolving architectures, research drops, production breakdowns— _AI_Distilled_ filters the noise into a weekly briefing for engineers and researchers working hands-on with LLMs and generative AI systems. Subscribe now and receive a free eBook, along with weekly insights that help you stay focused and informed. 

Subscribe at `https://packt.link/8Oz6Y` or scan the QR code below. 

<!-- Start of picture text -->
OFA<br>a<br><!-- End of picture text -->

# 13 

##### Unlock Your Exclusive Benefits 

Your copy of this book includes the following exclusive benefits: 

<!-- Start of picture text -->
crus<br>s —<br>ale)<br><!-- End of picture text -->

Follow the guide below to unlock them. The process takes only a few minutes and needs to be completed once. 

_Chapter 13_ 

488 

###### **Unlock this Book’s Free Benefits in 3 Easy Steps** 

###### **Step 1** 

Keep your purchase invoice ready for _Step 3_ . If you have a physical copy, scan it using your phone and save it as a PDF, JPG, or PNG. 

For more help on finding your invoice, visit `https://www.packtpub.com/en-us/unlock? step=1.` 

**Note** 

If you bought this book directly from Packt, no invoice is required. After _Step 2_ , you can access your exclusive content right away. 

###### **Step 2** 

Scan the QR code or go to `packtpub.com/unlock` . 

<!-- Start of picture text -->
oe(leef<br><!-- End of picture text -->

On the page that opens (similar to _Figure 13.1_ on desktop), search for this book by name and select the correct edition. 

_Unlock Your Exclusive Benefits_ 

489 

<!-- Start of picture text -->
Unlock Your Book’s Free Benefits<br>°<br>+ 1. Find Your Book Aa<br>40 2. Sign up (Free) or Sign In -<br>® 3. Upload Purchase Proof v<br><!-- End of picture text -->

_Figure 13.1: Packt unlock landing page on desktop_ 

###### **Step 3** 

After selecting your book, sign in to your Packt account or create one for free. Then upload your invoice (PDF, PNG, or JPG, up to 10 MB). Follow the on-screen instructions to finish the process. 

###### **Need Help** 

If you get stuck and need help, visit `https://www.packtpub.com/unlock-benefits/help` for a detailed FAQ on how to find your invoices and more. This QR code will take you to the help page. 

<!-- Start of picture text -->
ORREAO<br>Beet 5<br>et<br><!-- End of picture text -->

**Note** 

If you are still facing issues, reach out to `customercare@packt.com` . 

###### `packtpub.com` 

Subscribe to our online digital library for full access to over 7,000 books and videos, as well as industry leading tools to help you plan your personal development and advance your career. For more information, please visit our website. 

###### **Why subscribe?** 

- Spend less time learning and more time coding with practical eBooks and Videos from over 4,000 industry professionals 

- Improve your learning with Skill Plans built especially for you 

- 

- Get a free eBook or video every month 

- 

- Fully searchable for easy access to vital information 

- 

- Copy and paste, print, and bookmark content 

- 

At `www.packtpub.com` , you can also read a collection of free technical articles, sign up for a range of free newsletters, and receive exclusive discounts and offers on Packt books and eBooks. 

#### **Other Books You May Enjoy** 

If you enjoyed this book, you may be interested in these other books by Packt: 

<!-- Start of picture text -->
Unlocking with<br>Generative Ai and<br><!-- End of picture text -->

###### **Unlocking Data with Generative AI and RAG** 

Keith Bourne 

ISBN: 9781806381654 

- Architect graph-powered RAG agents with ontology-driven knowledge bases 

- 

- Build semantic caches to improve response speed and reduce hallucinations 

- 

- Code memory pipelines for working, episodic, semantic, and procedural recall 

- 

- Implement agentic learning using LangMem and prompt optimization strategies 

- 

- Integrate retrieval, generation, and consolidation for self-improving agents 

- 

- Design caching and memory schemas for scalable, adaptive AI systems 

- 

- Use Neo4j, LangChain, and vector databases in production-ready RAG pipelines 

- 

<!-- Start of picture text -->
Context Engineering for<br>Multi-Agent [Systems]<br>e 0<br>tinal , i<br>t &<br><!-- End of picture text -->

###### **Context Engineering for Multi-Agent Systems** 

Denis Rothman 

ISBN: 9781806690053 

- Develop memory models to retain short-term and cross-session context 

- 

- Craft semantic blueprints and drive multi-agent orchestration with MCP 

- 

- Implement high-fidelity RAG pipelines with verifiable citations 

- 

- Apply safeguards against prompt injection and data poisoning 

- Enforce moderation and policy-driven control in AI workflows 

- 

- Repurpose the Context Engine across legal, marketing, and beyond 

- 

- Deploy a scalable, observable Context Engine in production 

- 

###### **Packt is searching for authors like you** 

If you're interested in becoming an author for Packt, please visit `authors.packt.com` and apply today. We have worked with thousands of developers and tech professionals, just like you, to help them share their insight with the global tech community. You can make a general application, apply for a specific hot topic that we are recruiting an author for, or submit your own idea. 

###### **Share your thoughts** 

Once you have read _Design Multi-Agent AI Systems Using MCP and A2A_ , we would love to hear your thoughts! Scan the QR code below to go straight to the Amazon review page for this book and share your feedback. 

<!-- Start of picture text -->
Pe<br>Dslyerd:<br><!-- End of picture text -->

Your review is important to the tech community and us, and it will help us make sure we’re delivering excellent quality content. 

#### **Index** 

###### **A** 

|**A2A Manager**|**280**|
|---|---|
|**A2A client**|**271**|
|**A2A integration, in AI-6**<br>configuration and setup|279|
|**A2A server**|**271**|
|**A2A specialist agent**|**302**|
|**A2ATool class**|**277, 278**|
|**AI agents**<br>**3, 10, **<br>|**256, 482**|
|characteristics|10,11|
|debugging, with observability data|385|
|instrumentation and observability|379,380|
|metrics and KPIs, for measuring<br>|383|
|performance||
|privacy and security considerations|386|
|real-time monitoring and alerting|384,385|
|rise of|9|
|use cases|13,14|
|versus chatbots<br>l|12|
|workflow|12,13|
|**AI economy**|**481**|
|**AI-6**<br>|**85**|
|backend architecture|86|
|components|86|
|core engine|87|
|interacting with|153|
|LLM provider abstraction|97|
|reference link|85|
|used, for building GitHub tool|153–160|
|used, for tool implementation from|152|
|scratch||
|**AI-6 Chainlit**<br>i||
|configuration and engine<br>integration|200,201|
|exploring|193–199|
|life cycle and event handlers|201|
|**AI-6 Slack bot**||
|**/.env.*Slack bot initialization|183–185|

|authentication and configuration<br>setup|179–182|
|---|---|
|channel management and multi-|188–191|
|user support||
|events, handling<br>|185,186|
|exploring<br>|175–179|
|integrating, with AI-6 engine|191|
|**AI-6 agent**||
|AgentTool, adding|258,259|
|disabled_tools, adding|258|
|enabled_tools, adding<br>|258|
|system prompt, adding|257|
|**AI-6 coordinator agent**|**302**|
|**AI-6 custom tools**<br>||
|Bootstrap tool|144,145|
|current session ID, obtaining<br>i|149,150|
|defining|136|
|echo tool, implementing<br>i|140,141|
|filesystem tools|138–140|
|general command-line tools|136–138|
|ListSessions tool|146,147|
|memory tools|145,146|
|sessions, deleting<br>|151,152|
|sessions, loading|148,149|
|test runner tool|142,143|
|**AI-6 engine**||
|explicit agents, adding|256,257|
|renaming, to agent|257|
|**AI-6 framework**|**3**|
|**AI-6 tool specification schema**<br>defining|135|
|**AI-driven DevOps team**|**312**|
|agent interaction patterns|316|
|building|312|
|**API key authentication**|**457**|
|k8s-ai authentication|457|
|MAKDO configuration|458|
|**Agent-to-Agent**<br>**253 –255, **|**271, 413**|
|**(A2A) protocol**||
|client capabilities, integrating into<br>AI-6|274,275|

_Index_ 

496 

|communication mechanisms<br>274|
|---|
|core components<br>272|
|discovery flow<br>280|
|reference link<br>271|
|support, adding to AI-6<br>274|
|**AgentBench**<br>**55**|
|**AlexNet**|
|reference link<br>7|
|**AliBaba**<br>**9**|
|**AlphaZero**<br>**470**|
|**Anthropic**<br>**9**|
|**Anthropic Claude LLM**|
|reference link<br>161|
|**Anyscale**<br>URL<br>99|
|**AutoGPT**<br>**9**|
|**AutoGen**<br>**9, 59**|
|agent loop, working in<br>30|
|memory<br>40|
|tools, using<br>48–50|
|URL<br>30|
|**AutoGen agent loop**<br>|
|core implementation<br>30–34|
|**Autonomous Payment Protocol (AP2)**<br>**482**|
|URL<br>482|
|**abstract base classes (ABCs)**<br>**97**|
|**agent decomposition strategies**<br>**281**|
|capability pattern<br>282,283|
|decision framework<br>283,284|
|domain expertise<br>281,282<br>l|
|workflow stage<br>282|
|**agent evaluation and feedback loops**<br>**50**|
|automated evaluation<br>52–54|
|human feedback<br>51,52|
|industry benchmarks<br>55|
|**agent hallucination**<br>**370**<br>|
|reducing, mitigation strategies<br>371|
|**agent interaction patterns**<br>**316**|
|AI-6, extending with new tools<br>318|
|context sharing and state<br>320,321|
|management|
|event-driven coordination<br>396|
|hierarchical delegation<br>395,396|
|LLM-driven agent coordination<br>316,317|
|peer-to-peer collaboration<br>396<br>l|
|sequential workflows<br>395|
|l<br>shared state coordination<br>396|

|tool discovery and assignment|319,320|
|---|---|
|**agent loop**|**26**|
|acting phase|29,30|
|phases<br>|27|
|sensing phase<br>l|27|
|session workflow|26|
|thinking phase|28|
|workings, in AutoGen|30|
|**agent-specific context**|**295**|
|**agentic AI systems**|**3**|
|architecture|15|
|components|16|
|graph-based architecture|21,22|
|multi-agent architecture|20|
|planner and executors architecture|19,20|
|single-agent loop architecture|17,18|
|**agentic loop**|**72**|
|short-term memory|115|
|**alignment guardrails**|**109**|
|**application programming interface**<br>**(API)**|**214**|
|**args parameter**|**137**|
|**artificial general intelligence (AGI)**|**469**|
|**artificial intelligence (AI)**|**4**|
|**artificial superintelligence (ASI)**|**469**|
|**authentication**|**350**|
|**autonomous agents**|**3**|

###### **B** 

|**BabyAGI**|**9**|
|---|---|
|**Blitzy**||
|URL|471|
|**Bootstrap tool**|**144**|
|**biological models**|**478**|
|**blockchain**|**482**|
|**built-in tools**|**107**|

###### **C** 

|**Cerebras**||
|---|---|
|URL|99|
|**Chainlit**||
|AI-6 Chainlit|193|
|overview|193|
|URL|193|
|web UI, developing with|192|

_Index_ 

497 

|best practices|308,309|
|---|---|
|**conflicting actions pattern**|**394**|
|**container-based sandboxing**|**110**|
|**context compression**|**299**|
|**context engineering**<br>for multi-agent systems|294|
|**context layering**|**296**|
|**context prioritization**|**298**|
|**context refresh patterns**|**299**|
|**context scoping**|**297**|
|**context synchronization**|**298**|
|**context windows**|**37, 38, 474**|
|continuous learning|476|
|evolution|474|
|multi-agent systems|476|
|**context, multi-agent systems**<br>i||
|agent-specific context|295|
|handoff context|296|
|shared context|295|
|**contextual search**|**385**|
|**coordinator agent template**|**286 –288**|
|**core components, A2A protocol**<br>||
|agent card|272|
|artifact|272|
|message|272|
|part|272|
|task|272|
|**core engine**|**86, 87**|
|agentic loop, executing|92–96|
|initialization|87–91|
|running|91,92|
|**correlation analysis**|**385**|
|**cost metrics**|**383**|
|**creative content generation**<br>reference link|475|
|**cross-cluster networking appro**|**aches**|
|cloud providers|454|
|KinD|453|
|multi-cluster service mesh|454|
|**cryptocurrencies**|**481, 482**|
|**custom tools**|**106, 107**|

|**Claude Code**|**171**|est practices|308,309|
|---|---|---|---|
|**Claude tool**||**conflicting actions pattern**|**394**|
|manual implementation|161–163|**container-based sandboxing**|**110**|
|**Collector agent**|**283**|**context compression**|**299**|
|**Command Query Responsibility**<br>|**401**|**context engineering**||
|**Segregation (CQRS)**||for multi-agent systems|294|
|**Common Crawl**<br>||**context layering**|**296**|
|reference link<br>|8|**context prioritization**|**298**|
|**Completions API**<br>reference link|127|**context refresh patterns**<br>**context scoping**|**299**<br>**297**|
|**centralized context store**|**301**|<br>**context synchronization**|**298**|
|**channel restrictions**|**350**|<br>**context windows**|**37, 38, 474**|
|**chatbots**|**12**|continuous learning|<br>476|
|versus AI agents|12|<br>evolution|474|
|**circuit breakers**|**407**|multi-agent systems|476|
|**classic deadlocks**|**401**|**context, multi-agent systems**<br>i||
|**cluster problems, MAKDO impleme**|**ntation**|agent-specific context|295|
|**demo**||handoff context|296|
|analysis phase|355–359|shared context|295|
|creating<br>demo complete|352,353<br>364 365|**contextual search**|**385**|
|<br>demo start notification|,<br>354,355|**coordinator agent template**|**286 –288**|
|i<br>remediation phase|<br>360–362|**core components, A2A protocol**<br>d|272|
|**collaborative orchestration**|**268**|agent car<br>if||
|advantages|269|artact|272<br>|
|disadvantages|269|message<br>part|272<br>272|
|**command authorization**|**351**|task|272|
|**command-line interface (CLI)**|**213**|**core engine**|**86, 87**|
|**communication patterns**|**346**|agentic loop, executing|92–96|
|contextual messaging|348|initialization|87–91|
|message formatting<br>i|347,348|running|91,92|
|notification hierarchy|346|**correlation analysis**|**385**|
|**comparative debugging**|**386**|**cost metrics**|**383**|
|**comprehensive code base analysis,**<br>**iki**||**creative content generation**||
|**DeepW**<br>reference link|475|reference link<br>|475<br>|
|**computronium**|**483**|**cross-cluster networking appro**<br>cloud providers|**aches**<br>454|
|**configuration-driven agent**<br>|**326**|<br>KinD|453|
|**implementation**<br>||multi-cluster service mesh|454|
|advantages|326|||
|components|326–329|**cryptocurrencies**|**481, 482**|
|configuration over code|332|**custom tools**|**106, 107**|
|patterns|332|||
|session isolation|331|**D**||
|tool discovery and assignment|330,331|**Datadog LLM Observability**||
|**conflict prevention, multi-agent sy**|**stems**|<br>reference link|382|

_Index_ 

498 

|**DeepSeek**|**9**|
|---|---|
|URL|99|
|**DeepSpeech**||
|reference link|7|
|**DevOps**|**312**|
|for multi-agent AI|312,313|
|**Docker**||
|reference link|414|
|**deadlocks**||
|detecting|401,402|
|resolving|402|
|**deep conversational memory, Pe**|**rplexity**|
|reference link|475|
|**deep learning**|**7**|
|**dependency deadlocks**|**402**|
|**direct context passing**|**300**|

|timeout and latency issues, handling<br>377|
|---|
|wrong tool usage<br>373|
|wrong tool use and misuse<br>372|
|wrong tool use and misuse, mitigation<br>strategies<br>373|
|**filesystem tools**<br>**138 –140**|
|**full trust, full access mode**<br>**108**|
|**function call chains**|
|debugging<br>387|
|debugging strategies, for tool usage<br>390,391<br>tool use anti-patterns<br>389,390|
|tool use guardrails, building<br>391|
|tracing<br>388|
|**function-calling capabilities, OpenAI**<br>reference link<br>106|
|**fundamental theorem of software**<br>**engineering (FTSE)**<br>reference link<br>234|

###### **E** 

|**echo tool**|**140 –142**|
|---|---|
|**embodied AI agents**|**480**|
|**evaluation metrics**|**53, 54**|
|**event-driven coordination**|**396**|
|**event-driven orchestration**|**266**|
|advantages|267|
|disadvantages|267|
|**expert systems**|**6**|
|**external RAG**|**25**|

###### **F** 

|**FastMCP Slack server**<br>**34**|**3 –346**|
|---|---|
|**failure modes, agentic systems**|**370**|
|agent hallucination|370,371|
|communication, improving between|376|
|agents||
|coordination breakdowns<br>i|376,377|
|infinite loops, preventing|375|
|poor instruction following improveme<br>mitigation strategies|nt,<br>374|
|poor instruction following,<br>improving|373,374|
|runaway agents, preventing|375|
|security and permission failures,<br>enhancing|379|
|state management and consistency<br>errors, improving|378|

###### **G** 

|**Gas Town**<br>reference link||471|
|---|---|---|
|**Generative Adversarial Networks**<br>**(GANs)**||**8**|
|**Generative user experience (GenU**|**X)**|**479**|
|**GitHub Actions**|||
|reference link||193|
|**Google**||**9**|
|**general command-line tools**|**136, **|**137**|
|**general-purpose physical intellige**|**nce**|**480**|
|**generative AI (GenAI)**||**3**|
|**generative AI evolution**<br>||**4**|
|deep learning||7|
|emergence of generative models||8|
|expert systems era||6|
|machine learning and statistical me|thods|7|
|neural network renaissance||7|
|rise of AI agents||9|
|symbolic AI, early days||5|
|**graph-based architecture**|**21**|**,22**|
|**guardrails**||**109**|
|alignment guardrails||109|
|hallucination guardrails||109|
|regulatory-compliance guardrails||109|
|validation guardrails||109|

_Index_ 

499 

###### **H** 

|**HandOffMessage**|**34**|
|---|---|
|**hallucination guardrails**|**109**|
|**handoff context**|**296**|
|**hierarchical context distribution**|**301**|
|**hierarchical delegation**|**395, 396**|
|**hierarchical orchestration**|**265**|
|advantages|266|
|disadvantages|266|
|**hierarchical planning**|**477**|
|**holistic document understanding,**<br>reference link|**Harvey**<br>475|
|**human feedback**|**51, 52**|
|**human feedback integration, with**|**341**|
|**control channels**||
|alternative communication channels|<br>350|
|communication patterns|346|
|custom MCP server, building with<br>FastMCP|342|
|escalation pattern, for restricted|348,349|
|operations||
|FastMCP Slack server|343–346|
|human-AI interface challenge|341|
|observability and audit trail|351|
|security and access control|350|
|Slack_Bot agent architecture|341,342|
|**human-in-the-loop approach**|**110**|
|**humanoid robots**|**480**|
|**hybrid orchestration**|**269**|

###### **I** 

|**industry benchmarks**|**55**|
|---|---|
|AgentBench|55|
|Mind2Web|55|
|ToolBench|55|
|WebArena|55|
|**inter-agent dependencies**||
|data|397|
|explicit|397|
|implicit|397|
|resource|398|
|temporal|398|
|**interactive agent interfaces, best prac**<br>i|**tices**|
|configurability and runtime control|209|
|designing, for turn-based transparency|209|

|distributed tracing|210|
|---|---|
|logs|210|
|metrics|210|
|role and capabilities, clarifying|208|
|safeguards|208|
|tool invocation and feedback loops,|209|
|prioritizing||

###### **K** 

|**KinD clusters**<br> <br>|
|---|
|cluster networking, setting up<br>419<br>control cluster configuration,<br>415,416|
|creating<br>|
|cross-cluster connectivity, verifying<br>420,421<br>|
|port forwarding, setting up<br>419<br>|
|setting up, for multi-agent deployment<br>414|
|test workload, deploying to worker<br>421–423|
|cluster<br>i|
|worker cluster configuration,<br><br>417–419|
|creating|
|**Kubernetes**|
|URL<br>60|
|**Kubernetes in Docker (KinD)**<br>**413**|
|installing<br>414<br>|
|prerequisites<br>414|
|reference link<br>414|
|**Kubernetes reconciliation loop**<br>reference link<br>26|
|**k8s-ai Admin API and session**<br>**management**<br>|
|active sessions, listing<br>448|
|Admin API port, exposing<br>447|
|session, creating<br>447,448|
|session, deleting<br>449|
|session, using with A2A protocol<br>450|
|testing<br>446|
|**k8s-ai agent**<br>**60, 85**<br>|
|cluster, checking with<br>65–69|
|local kind cluster, setting up<br>61–64|
|reference link<br>60,85|
|running<br>64|
|**k8s-ai agentic system**<br>**70**|
|code walk<br>71,72|
|Kubernetes chat agent, interacting with<br>80|
|Kubernetes chat agent, running<br>80|
|tool-calling execution loop,<br>76–79|
|implementing<br>i|
|tools, defining with OpenAI<br>73|

_Index_ 

500 

|tools, registering with OpenAI|73–75|||
|---|---|---|---|
|**k8s-ai deployment**||**M**||
|k8s-ai Docker image, building<br>|437,438<br>|**MAKDO**|**253, 413**|
|k8s-ai service, exposing for cross-<br>l|442,443|analyzer agent<br>i i|313|
|custer access||confiuration file|315316|
|manifests, creating|439|ig i<br>dit t|,<br>313314|
|to worker cluster<br>436,|439–442|coornaor agen<br>fixer agent|,<br>313|
|**k8s-ai deployment verification**<br>|**443**|for multi-agent AI|313|
|A2A endpoint, testing<br>|445,446|slack agent|313|
|pod health, verifying<br>|444|system architecture|313|
|pod status, checking<br>|443,444<br>|**MAKDO agent**||
|server logs, checking|444|<br>i||
|<br>i||analyzer and fixer, separating|323|
|service configuration, verifying|446|i<br>configuration-driven agent|326|
|**kubectl**<br>||implementation||
|reference link|60,414|design<br>|321|
|||four agents|322|
|**L**||implementing<br>|326|
|**LLM provider abstraction**|**97**|roles<br>SlkBt ti|322<br>323|
|**LLM providers**<br>|**99**<br>|ac_o, separang<br>tool access boundaries|324|
|Ollama provider<br>|104<br>|workflow structure|322|
|OpenAI provider|99–103|l<br>**MAKDO dlmnt**||
|**LLMProvider interface**|**97 –99**|**epoye**<br>||
|<br>||as Kubernetes deployment<br>i|431|
|**LangChain**|**9**|configuration, preparing<br>i i|424,428|
|**LangGraph**<br>||kubeconfig ConfigMap, creating|430|
|reference link|22|Kubernetes secrets, creating for API|428,429|
|**LangSmith**|**382**|keys<br>||
|**ListSessions tool**<br>|**146, 147**|logs<br>|435,436|
|||MAKDO image building|432 433|
|**large context windows**<br>challenges|476|,<br>MAKDO image, loading<br>i|,<br>432,433<br>i|
|trade-offs|476|MAKDO, configuring to worker clust|i   er<br>434|
|||to control cluster|424|
|**large language model (LLM)**<br>|**17, 25**<br>|verifying|435,436|
|context window<br>|37<br>|**MAKDO implementation demo**|**352**|
|**life cycle and event handlers, AI-6**<br>|**201**|cluster problems, creating|352,353|
|**Chainlit**||k bi|365366|
|on_chat_start event handler|202,203|ey oservatons<br>|,<br>|
|on_message event handler|204,205|setup<br>|352|
|on_settings event handler|206,207|**MCP architecture**||
|**long contexts**||core components<br>|215<br>|
|<br>||data layer|215|
|handling|118–121|<br>transport layer|215|
|**long conversations**<br>||<br>**MCP clients**|**217**|
|managing|35,36|<br>building|229|
|**long-horizon planning**<br>hi||connecting, to MCP server|230–232|
|arctecture<br>|477<br>|MCP tool, invoking|232–234|
|challenge|477|MCPClient class|229|
|**long-term memory**<br>||**MCP ecosystem**|**219**|
|session loading|115–118|<br>**MCP hosts**|**217**|

_Index_ 

501 

|parallel orchestration|263,264|
|---|---|
|sequential orchestration|262,263|
|**multi-agent patterns**||
|working|304,305|
|**multi-agent planning and**<br>**reasoning**|**42, 43**|
|**multi-agent systems**<br>l||
|conflict resolution|306,307|
|context|295,296|
|context engineering|294|
|context management strategies|296–298|
|context window management|298–300|
|factors, for selecting|260–262|
|inter-agent context sharing|300,301|
|role assignment|308|
|tool assignment decision|292–294|
|framework||
|**multi-agent workflows**||
|coordination failures patterns|392–395|
|coordination failures, diagnosing|392|
|coordination guardrails, building|403|
|deadlocks, detecting|399|
|shared state, managing|399|
|**multi-modal multi-agent systems**|**479**|
|**multi-robot coordination**|**481**|
|**multi-robot systems**|**481**|

|**MCP integration, into AI-6 framew**<br>|**ork**<br>**234**<br>|parae orcestration<br>il hi|263,264<br>|
|---|---|---|---|
|implementing|248,249|sequenta orcestraton|262,263|
|MCP tool discovery|<br>239|**multi-agent patterns**||
|tool manager|240–245|working|304,305|
|universal MCPTool class|235–239|**multi-agent planning and**<br>|**42, 43**|
|**MCP servers**<br>i|**216**|**reasoning**||
|benefits|218|**multi-agent systems**<br>l||
|building<br>i|219|conflict resolution|306,307|
|filesystem MCP server|220–224|context|295,296|
|GitHub MCP server<br>|224–228|context engineering<br>|294|
|local, versus remote|217|context management strategies<br>|296–298|
|**MCP tool discovery**|**239**|context window management<br>|298–300<br>|
|**MCPTool class**<br>**2**|**35 –239**|factors, for selecting<br>inter-agent context sharing|260–262<br>300 301|
|**Meta**|**9**|<br>role assignment|,<br>308|
|**Mind2Web**|**55**|<br>tool assignment decision|292–294|
|**Mistral**|**9**|framework||
|**Model Context Protocol (MCP)**|**3, 214**|**multi-agent workflows**||
|URL|213|coordination failures patterns|392–395|
|**Model Context Protocol (MCP)**|**90, 108**|coordination failures, diagnosing|392|
|**tools**||coordination guardrails, building|403|
|**Moltbook**||deadlocks, detecting|399|
|URL|482|shared state, managing|399|
|**machine learning (ML)**|**7**|**multi-modal multi-agent system**|**s**<br>**479**|
|**main() function**|**72**|**multi-robot coordination**|**481**|
|**mediated fine-grained tool access**|**109**|**multi-robot systems**|**481**|
|**memory in AutoGen**|**40**|||
|simple sequential list memory|40|**N**||
|task-centric fast memory<br>|40<br>|**Nested Learning paper, Google r**|**esearch**|
|vector-based RAG memory|40|reference link|476|
|**memory management**|**111**|**neural network model**|**4**|
|**memory tools**|**145**|||
|**memory, agentic AI system**<br>|**16**<br>|**O**||
|episodic memory|16|||
|<br>semantic memory|16|**OODA (Observe, Orient, Decide,**<br>|**Act) loop**<br>|
|<br>working memory|16|reference link|26|
|**message deadlocks**|**401**|**Ollama Python tool**<br>**specification**|**133 –135**|
|**million-token context windows**<br>||**Ollama provider**|**104**|
|practical applications|475|<br>URL|104|
|**model-based planning**|**477**|**OpenAI**|**9**|
|**multi-agent architecture**|**20**|**OpenAI API endpoint**||
|**multi-agent orchestration**|**256**|<br>URL|99|
|collaborative orchestration|268,269|**OAI API k**|**429**|
|design considerations|270|**pen  ey**||
|<br>event-driven orchestration|266,267|**OpenAI Python tool**<br>**specification**|**126 –133**|
|hierarchical orchestration|265,266|||
|hybrid orchestration|269|**OpenAI client**|**71**|

|**Nested Learning paper, Google research**|
|---|
|reference link<br>476|
|**neural network model**<br>**4**|

_Index_ 

502 

|**OpenAI provider**<br>**99 –**|**103**|
|---|---|
|**OpenRouter**||
|URL|97|
|**OpenTelemetry**||
|reference link|382|
|**observability primitives, AI agents**||
|LLM call tracing<br>i|380|
|LLM-specific tools|382|
|metadata enrichment|381|
|span and trace hierarchies|381|
|state snapshots|381|
|structured logging and trace formats<br>381|,382|
|tool execution logs|380|
|**orchestration, agentic AI system**|**16**|

###### **R** 

|**Reinforcement Learning from Human**<br>**Feedback (RLHF)**|**8**|
|---|---|
|**Responses API**|**77**|
|**Runway’s general world models**||
|reference link|477|
|**reasoning models**||
|working with|41|
|**recurrent neural networks (RNNs)**|**8**|
|**regulatory-compliance guardrails**|**109**|
|**reinforcement learning from human**|**51**|
|**feedback (RLHF) pipelines**||
|**resilience and recoverability**<br>designing for|404|
|**resource deadlocks**|**402**|
|**retrieval-augmented generation (RAG)**|**25**|
|**retry logic**|**407**|
|**robotics**|**480**|
|**robots**|**480**|
|AI self-improvement loop|482|
|real-world deployment, challenges|481|
|**roles and responsibilities**||
|architecture key design patterns|325|
|architecture, extending<br>324<br>i|,325|
|defining for specialized agents|321|

###### **P** 

|**Pile**||**retrieval-aumented eneration (**|**AG)**<br>**25**|
|---|---|---|---|
|reference link|8|**g g**|<br>|
|<br>**Processor agent**|**283**|**retry logic**<br>**robotics**|**407**<br>**480**|
|**parallel orchestration**|**263, 264**|||
|advantages|264|**robots**|**480**|
|disadvantages|264|AI self-improvement loop<br>real-world deployment, challenges|482<br>481|
|**partial task completion pattern**|**392**|<br>**l d ibiliti**||
|**peer-to-peer collaboration**|**396**|**roes an responses**<br>architecture key design patterns|325|
|**perceptron**|**4, 5**|architecture, extending|324,325|
|**performance metrics**|**383**|defining for specialized agents|321|
|**planner and executors architect**|**ure**<br>**19**|||
|executor agent|19|**S**||
|planner AI agent|19|**SHRDLU**|**5**|
|**print working directory (pwd)**|**138**|**SOTA (state of the art)**|**55**|
|**production security enhancemen**|**ts**|<br>**SambaNova**||
|audit logging|464|URL|99|
|network policies<br>pod security standards|463<br>464|**Server-Sent Events (SSE) client**|**230**|
|<br>rate limiting|465|**Slack Team ID**|**429**|
|secrets management|464|**Slack app**||
|TLS/SSL encryption|463|reference link|175|
|**provider-agnostic tools**<br>i||**Slack bot interface**||
|AI-6 tool specification schema|135|AI-6 Slack bot, exploring|175–179|
|defining<br>i|126|building|174|
|Ollama Python tool specification|133–135|properties|174|
|OpenAI Python tool<br>i|126,129–133|**Slack tokens**|**429**|
|specification||**Slack_Bot agent**||
|||architecture|341,342|
|**Q**||**Stanford study, on AI medical pro**|**grams**|
|**ualit metrics**|**384**|reference link|472|

**quality metrics 384** 

_Index_ 

503 

|**Support Vector Machines (SVM)**|**7**|
|---|---|
|**Swarm pattern**|**34**|
|**secure communication, between**|**clusters**|
|API key authentication|457|
|cross-cluster networking<br>|453,454|
|approaches<br>||
|enabling|450|
|end-to-end connectivity, testing|455,456|
|k8s-ai authentication|457|
|k8s-ai, discovering by MAKDO|451|
|network isolation, testing|462|
|network segmentation|461|
|permission boundaries, testing|461|
|port mapping security<br>|461,462|
|production security enhancements|463–466|
|RBAC and least privilege<br>i|460|
|RBAC configuration, inspecting|460|
|request path, tracing<br>|451,452|
|security architecture<br>|456|
|service discovery and networking<br>|450|
|service discovery patterns<br>|452|
|session-based security|458–460|
|**security architecture**|**456**|
|API key authentication|457|
|**sequential orchestration**|**262**|
|advantages<br>|263|
|disadvantages|263|
|**sequential workflows**|**395**|
|**service discovery patterns**||
|DNS-based discovery|452|
|dynamic service registry|453|
|service mesh discovery|452|
|**session**|**111 –114**|
|conversation|115|
|**shared context**|**295**|
|**shared state coordination**|**396**|
|**shlex built-in package**||
|reference link|137|
|**short-term memory**||
|in agentic loop|115|
|**single-agent loop architecture**|**17**|
|use cases|18|
|**single-agent planning and reaso**|**ning**<br>**42**|
|**site reliability engineers (SREs)**|**312**|
|**specialist agent template**|**285, 286**|
|**stablecoins**|**482**|

|**standard input/output (STDIO)**<br>**streams transport**||**217**|
|---|---|---|
|**standard operating procedures**<br>**(SOPs)**||**312**|
|**strategic foresight**|**470, **|**471**|
|**strategies, for resilient multi-age**<br>**systems**<br>|**nt AI**||
|checkpointing||409|
|circuit breakers|407–|409|
|degradation strategies|405,|406|
|human escalation patterns||410|
|redundancy and failover mechanism|s|404|
|retry logic||407|
|state recovery||409|
|**success rate metrics**||**383**|
|**superhuman reasoning**|**470, **|**471**|
|challenges||472|
|ethical considerations||473|
|limitations||472|
|**symbolic AI**||**5**|
|history||5|
|**symbolic reasoning**||**5**|
|**synchronization challenges**|||
|approaches, for states synchronizat|ion|401|
|patterns|||
|managing||400|
|**system health metrics**||**384**|
|**system prompt design patterns,**<br>**multi-agent systems**||**284**|
|coordinator agent template<br>i|286–|288|
|domain-specific prompt examples|290|,291|
|specialist agent template|285|,286|
|validator agent template|288|,289|

###### **T** 

|**ToolBench**<br>**55**|
|---|
|**team orchestration, with manager**<br><br>**333**|
|**agent**|
|agent communication failures, handling<br>337|
|cascading failures, handling<br>338|
|complex multi-step operations, handling<br>335|
|conditional remediation<br>336|
|decision points and branching<br>334|
|duplicate operations, avoiding<br>339<br>l|
|dynamic workflow execution<br>333,334|
|error handling and recovery<br>337|
|hybrid approach<br>340,341|
|memory tools, for long-term state<br>338,339|

_Index_ 

504 

|multi-cluster coordination|335|**trace replay**|**385**|
|---|---|---|---|
|partial failures, handling<br>ti d|337<br>340|<br>**transformer-based agents**|**3**|
|proacve moe<br>reactive mode<br>i|340|**transformers**|**8, 478**|
|retry and verification loops<br>state management and coordination|336<br>338|**U**||
|**test runner tool**|**142, 143**|**Universally Unique Identifiers**|**(UUIDs)**<br>**94**|
|**time-series visualization**|**386**|**universal basic income (UBI)**|**473**|
|**tool call life cycle**|**387, 388**|**user interfaces (UIs)**<br>i|**167**|
|**tool execution**||significance, in agentic AI<br>l|168–173|
|container-based sandboxing|110|workflows||
|full trust, full access|108|**user permissions**|**110**|
|guardrails|109|**user-defined tools**||
|human-in-the-loop<br>i|110|implementing|44|
|mediated fine-grained tool access|109|||
|user permissions|110|**V**||
|**tool manager**<br>**240 –**<br>using, by engine|**245, 280**<br>245–247|**Visualizer agent**|**283**|
|<br>**tool system architecture**|**105**|**validation guardrails**|**109**|
|<br>built-in tools|107|**validator agent template**|**288, 289**|
|custom tools|106,107|**voice cloning**||
|security and permissions|108–111|reference link|478|
|**tool usage**<br>debugging|387|**W**||
|**tools**||**WebArena**|**55**|
|declaring<br>|45,46|**Weights & Biases (WB)**|**382**|
|managing|43|||
|selecting|46,47|**Word2Vec**<br>f lik|7|
|tasks|43|reerence n||
|user-defined tools<br>using, in AutoGen|44<br>48–50|**web UI development**<br>with Chainlit|192|
|<br>**tools, agentic AI system**|**16**|**work duplication pattern**<br>**world models**|**393**<br>**477 –479**|

|**Visualizer agent**|**283**|
|---|---|
|**validation guardrails**|**109**|
|**validator agent template**|**288, 289**|
|**voice cloning**<br>reference link|478|
