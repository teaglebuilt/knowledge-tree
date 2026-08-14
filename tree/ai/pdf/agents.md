---
title: agents
source: sources/ai/pdf/agents.pdf
source_type: paper
source_hash: 6beddc2fab0e2a72d8a6b4c73cfd7f80088987e50276b9c9c84d37f584e68c9a
tags:
- ai
- paper
extracted: '2026-08-14'
---

Click to edit Master title style 

**AI Agents A-Z** 

Master AI agents: frameworks, deployment, evaluation, best practices, and more **Sinan Ozdemir** Data Scientist, Entrepreneur, Author, Lecturer <mark>fo</mark> 

## Welcome! 

# Click to edit Master title style 

<!-- Start of picture text -->
livelessons©<br>Introduction<br>to Transformer<br>Models for NLP<br>Sinan Ozdemir<br>> video<br><!-- End of picture text -->

<!-- Start of picture text -->
LARGE<br>LANGUAGE<br>MODELS<br><!-- End of picture text -->

My name is **Sinan Ozdemir** ( in/sinan-ozdemir + @prof_oz ) 

- Current **founder** of Loop Genius (World’s first AI Marketing Agency) 

- - Current **lecturer** for O’Reilly and Pearson 

- Founder of Kylie.ai (Funded by OpenAI Founder + Acquired) 

- **Masters** in Theoretical Math from **Johns Hopkins** 

- Former lecturer of Data Science at Johns Hopkins 

<!-- Start of picture text -->
|<br>e _<br><!-- End of picture text -->

Author of ML textbooks and online series, including 

- <u>Quick Start Guide to LLMs</u> ~~<u>SS</u>~~ (Top 50 in NLP) - <u>Associated Video Series</u> 

- <u>The Principles of Data Science</u> 

- <u>Introduction to Transformer Models for NLP</u> 

Click to edit Master title style 

## **Introduction to AI Agents** 

What are AI Agents Click to edit Master title style 

AI agents are (semi) autonomous systems that interact with environments, make decisions, and perform tasks on behalf of users. 

- **Autonomy** : Can perform tasks without continuous human intervention. 

- **Decision-making** : Use data to analyze and choose actions. 

- **Adaptation** : Learn and improve over time with feedback (ideally). 

Agents vs LLMs Click to edit Master title style 

<!-- Start of picture text -->
A<br>VS’<br>Y<br>Agent Large Language Model<br>Performs specific tasks Focuses on understanding<br>and makes decisions and generating human-like<br>based on its environment. text.<br><!-- End of picture text -->

https://www.datacamp.com/tutorial/crew-ai 

Agents vs LLMs Click to edit Master title style 

**ChatGPT** is an Agent on top of an LLM (like **GPT-4o** ) 

Agents vs LLMs Click to edit Master title style 

That’s a fair assessment but let’s break it down further: _Agents_ are **prompts** on top of LLMs specifically designed to perform a **task/goal** using **tools** and a set of **rules/descriptions/backstories** 

Agents vs LLMs Click to edit Master title style 

- **Task/goal** 

   - The thing you want the agent to do 

- **Tools** 

- The actions the agents are allowed to perform 

- - **Rules/Descriptions/Backstories** 

   - Context around the task (e.g. only speak spanish) 

- **Prompt** 

   - The consolidation of all of the above into a single set of instructions to an LLM 

Agents vs LLMs Click to edit Master title style 

- **Task/goal** 

   - Go to practicallyintelligent.com and tell me what it’s about 

- **Tools** 

   - Web Scraper Tool 

- **Rules/Descriptions/Backstories** - Check the full website 

- **Prompt** 

   - More on this later 

Agents Click to edit Master title style 

User asks an Agent a question, which uses a toolbox of tools to answer the question 

<!-- Start of picture text -->
alrYY;<br>“Who was that person... MNP D Thought I should look this up<br>i) fe) °<br>pes u<br>i) et P 4 Action Search for: “query”<br>a q<br>oe Observation It appears that...<br>“The answer is...”<br>ae © Response "The answer is...”<br><!-- End of picture text -->

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Agents Click to edit Master title style Pretty much any tool you can think of: 

<!-- Start of picture text -->
“Check my stock portfolio” ONGSOY, D Thought I will query the APIa Googedale<br>Cc Bes °<br>Cc > eS ee Action: GET /api/wallet<br>ul<br>HZ observation {"balance”: ..}<br>“Your balance is..”<br>RQ © Response "Your balance is..”<br><!-- End of picture text -->

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

# ChatGPT is an Agent Click to edit Master title style 

Source: ChatGPT 

# ChatGPT is an Agent Click to edit Master title style 

A little prompt injection to see their system prompt. 

Note now “bio” is a tool (it’s memory feature) 

Source: ChatGPT 

Agents are Essentially Workflows Click to edit Master title style 

Agents are workflows with discrete decision points: 

1. Did the AI identify the right tool to start with? 2. Did the AI use the first tool correctly? 

3. Did the tool succeed? 

4. Did the tool return the right information? 5. Did the AI use the returned information correctly? 6. Did the AI choose the second tool correctly? 

7. Etc, etc, etc 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Why AI Agents might be Essential Click to edit Master title style 

### **Productivity and Efficiency:** 

- Automate repetitive tasks, freeing up human resources for more complex activities. 

- - Handle dynamic and real-time environments like finance or customer service. 

**Personalization:** 

- Tailor user experiences based on individual preferences. 

Evolution of AI Agents Click to edit Master title style 

**Early AI Agents:** 

- Rule-based systems with predefined actions. 

- - Limited flexibility and adaptability. 

- Examples: Alexa, Siri 

**Modern AI Agents:** 

- LLMs with prompts for reasoning through tasks with access to (usually) pre-defined tools 

Click to edit Master title style 

**Frameworks for Modern AI Agents** 

# Overview of Leading AI Agent Frameworks Click to edit Master title style 

### **LangChain:** 

- Designed for large language models (LLMs), supports agent workflows for NLP and decision-making tasks. 

- Key features: customizable workflows, tool integrations, and agent collaboration 

<!-- Start of picture text -->
Build context-aware reasoning applications<br>© Open in GitHub Codespaces X Follow @Langc!<br><!-- End of picture text -->

Screenshot from LangChain GitHub repository.© LangChain AI. All rights reserved. https://github.com/langchain-ai/langchain 

# Overview of Leading AI Agent Frameworks Click to edit Master title style 

<!-- Start of picture text -->
agent<br>a inue } Brel<br><!-- End of picture text -->

### **LangGraph:** 

- Library for building stateful, multi-actor applications with LLMs. 

- Key features: human in the loop, statefulness, Langchain under the hood 

https://github.com/langchain-ai/langgraph-example 

# Overview of Leading AI Agent Frameworks Click to edit Master title style 

**CrewAI:** 

- Focuses on collaborative, role-based AI agents that work in teams to tackle complex tasks. 

- Key features: agent roles, dynamic task delegation, inter-agent communication 

Source: https://www.crewai.com/ 

CrewAI: Collaborative Intelligence Click to edit Master title style 

- CrewAI enables the orchestration of **multiple** agents, each with a specific role, collaborating on tasks. 

- Supports hierarchical and sequential task delegation for complex workflows (more on this during our code) 

CrewAI: Collaborative Intelligence Click to edit Master title style 

Screenshot from CrewAI GitHub repository. © CrewAI Inc. All rights reserved. https://github.com/crewAIIn c/crewAI 

ChatGPT is a **Single** Agent Click to edit Master title style 

ChatGPT is a (most likely) a single prompt running over and over in sequence handling one task at a time 

Source: ChatGPT 

CrewAI: Collaborative Intelligence Click to edit Master title style 

- **Role-based design:** - Agents are assigned specific responsibilities, such as research or report generation. 

- **Autonomous inter-agent delegation:** - Agents can delegate tasks to others dynamically based on workflow requirements. 

# Overview of Leading AI Agent Frameworks Click to edit Master title style 

### **OpenAI Swarm:** 

- Lightweight framework for coordinating multi-agent interactions. 

- Enables agent handoffs and flexible tool usage for dynamic workflows 

https://github.com/openai/swarm 

OpenAI Swarm: Lightweight (Experimental) Click to edit Master title style 

- A lightweight framework designed to orchestrate conversations and workflows between multiple agents. 

- Ideal for dynamic, real-time systems that need flexible task handoffs. 

- Simple handoff mechanisms between agents. 

- - **Stateless** between calls, powered by Chat Completions API. 

   - Stateless means no memory from sub-task to sub-task within a single agent call 

Overview of Leading AI Agent Frameworks Click to edit Master title style 

### **AutoGen:** 

- Microsoft’s framework for multi-agent systems, designed for asynchronous communication and distributed deployments 

<!-- Start of picture text -->
AutoGen<br>An Open-Source Programming Framework for Agentic Al<br><!-- End of picture text -->

https://microsoft.github.io/autogen/0.2/ 

AutoGen: Scalable and Distributed AI Click to edit Master title style 

- AutoGen focuses on building distributed, scalable agent systems for complex, real-time applications. 

- Meant for enterprises requiring asynchronous communication between agents. 

- Cross-language support: Integrates agents using multiple languages (e.g., C#, Python, .NET). 

Frameworks Click to edit Master title style 

<!-- Start of picture text -->
But what about?<br>:ee A it Fra mew<br>@W,<br>A /<br>Lo .c|<br>OL<br>a ork rayve f<br>e<br>|, ‘<br>ve(org fa<br>. ;<br>X Fotom eormsoaen )= UsShy<br>===<br>— — Men,G;<br>Github 2)1)<br><!-- End of picture text -->

Code Time! Click to edit Master title style 

<!-- Start of picture text -->
-<br>7 | 7, ~ ie :<br>ak ie I tees<br>Our First<br>Agents: CrewAI &<br>LangGraph<br><!-- End of picture text -->

Click to edit Master title style 

## **Deployment Strategies** 

Best Practices for Deploying AI Agents Click to edit Master title style 

**Reliability:** 

- Utilize redundancy and failover mechanisms to ensure agent availability. 

   - E.g. A tool fails to load or an agent fails to write correct tool input arguments 

- Implement monitoring and alerting systems for performance and error tracking 

## Streamlit 

Click to edit Master title style 

- Open-source framework for building and sharing data apps 

<!-- Start of picture text -->
Aq<br>Streamlit<br><!-- End of picture text -->

- Accessible for users of all skill levels 

- Deployment process is easy, HuggingFace will host for you 

- Large open-source community 

- Democratizes the process of building data apps 

Streamlit Example Click to edit Master title style 

Our Scraping Agent 

Backstory/Rules 

Tools 

Streamlit Example Click to edit Master title style 

### Our Scraping **Task** 

Goal 

Rule 

Streamlit Example Click to edit Master title style 

Our Result 

Streamlit Example Click to edit Master title style You ONLY have access to the following tools, and should NEVER make up tool 

So where’s the prompt? 

Here’s a snippet of the CrewAI prompt that they **hide** from you 

<!-- Start of picture text -->
Action Input: the<br>Observation: the<br><!-- End of picture text -->

Code Time! Click to edit Master title style 

<!-- Start of picture text -->
-<br>7 | 7, ~ ie :<br>ak ie I tees<br>Building an<br>Agent Streamlit<br>App<br><!-- End of picture text -->

Click to edit Master title style 

**Agents! Can we Build it?** 

# Brief History of Modern NLP Click to edit Master title style 

<!-- Start of picture text -->
2001<br>Neural Language<br>Models<br><!-- End of picture text -->

<!-- Start of picture text -->
2014–2017<br>Seq2seq +<br>Attention<br><!-- End of picture text -->

<!-- Start of picture text -->
2013<br>encoding semantic<br>meaning with<br>Word2vec<br><!-- End of picture text -->

<!-- Start of picture text -->
2017–Present<br>Transformers + Large<br>Language Models<br><!-- End of picture text -->

Bengio et al. <u><mark>https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf</mark></u> Mikolov et al. <u><mark>https://arxiv.org/abs/1301.3781</mark></u> Xu et al. <u><mark>http://proceedings.mlr.press/v37/xuc15.pdf</mark> https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf</u> 

# 2017 – Transformers Click to edit Master title style 

<!-- Start of picture text -->
Output<br>Probabilities<br>Add & Nom<br>Feed<br>Forward<br>fad & Nom, Multi-Head<br>Forward =, Nx<br>i Add & Nom<br>Add Nom ==<br>Multi Head Muti-Head<br>Attention Attention<br>a a<br>Positional Positional<br>Encoding COP aw Encoding<br>Input Output<br>Embedding Embedding<br>Inputs. Outputs<br>(shifted right)<br>Figure 1: The Transformer - model architecture.<br><!-- End of picture text -->

**“Attention is all you need”** 

- Introduced the transformer architecture 

- A sequence to sequence model (takes text in and writes text back) 

- • The parent model of GPT, BERT, T5, and many more 

Source: https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf 

Language Models Click to edit Master title style 

Consider the following example: 

If you don’t   ___   at the sign, you will get a ticket. 

Language Models Click to edit Master title style 

Consider the following example: 

If you don’t   ___   at the sign, you will get a ticket. 

95% 5% 

Language Models Click to edit Master title style 

In a **language modeling** task, a model is trained to predict a missing word in a sequence of words. In general, there are two types of language models: 

- Auto-regressive 

- Auto-encoding 

Auto-___ Language Models Click to edit Master title style 

**Auto-encoding LLMs - the readers** 

**Auto-regressive LLMs - the writers** 

Learns entire sequences by predicting tokens (words) given past and future context 

If you don’t __ at the sign, you will get a ticket. 

Predict a future token (word) given either past context or future context but not both. If you don’t __ ........... mind? want? have? 

<!-- Start of picture text -->
©<br><!-- End of picture text -->

<!-- Start of picture text -->
V<br><!-- End of picture text -->

cannot generate text but great for **classification** , **embedding** + **retrieval** tasks 

Capable of **generating text** , hence the term Generative LLMs but must be larger to read nearly as well as auto-encoding systems 

Examples: **BERT** , XLNET, RoBERTa, sBERT 

Examples: **GPT** family, Llama family, Anthropic’s Claude family, honestly most of the LLMs you see out there today 

Auto-regressive Models Click to edit Master title style 

Generative AI refers to auto-regressive LLMs who must be able to reason through information and hold a conversation for several turns within its context window 

Source: Anthropic’s Claude 

Auto-regressive Models Click to edit Master title style 

Generative AI refers to auto-regressive LLMs who must be able to reason through information and hold a conversation for several turns within its context window 

Source: Anthropic’s Claude 

Auto-regressive Models Click to edit Master title style 

Most Agents rely on **only** auto-regressive models to reason through: 

1. Tool selection (Python tool vs Web scraping tool) 2. Tool input (what should I look up on the web?) 3. Deciding when to return the final answer 4. Etc 

Click to edit Master title style 

**Prompt Engineering for Performance and Consistency** 

Prompt Engineering LLMs Click to edit Master title style 

**Prompt Engineering** – The process of carefully designing inputs for massively large language models such as Claude or ChatGPT to guide them to produce relevant and coherent outputs. Many AI researchers consider prompt engineering a “bug” in AI and that it will go away in the next few years. 

Reasoning vs Thinking Click to edit Master title style 

Think of LLMs as “ **reasoning machines** ” vs “thinking machines”. LLMs excel at tasks that require **reasoning** - using context and input information in conjunction to produce a nuanced answer 

Reasoning vs Thinking Click to edit Master title style 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Few-shot Learning / In-context Learning Click to edit Master title style 

**Few-shot learning** – Giving an LLM examples of a task being solved to teach the LLM how to reason through a problem and also to format the answer in a desired format 

These examples can be as detailed as you’d like (at the cost of.. well money) 

Pre-training GPT - How Few-Shot Works Click to edit Master title style 

GPT-3 paper’s title called out few-shot learning as a primary source of **in-context learning** –on the job training for an LLM 

Source: OpenAI 

Chain of Thought Prompting Click to edit Master title style 

**Chain of Thought Prompting** forces an LLM to generate reasoning for an answer alongside an answer. This usually leads to better/more actionable results. 

# ChatGPT versus Math–Chain of Thought Click to edit Master title style 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

ChatGPT versus Math Click to edit Master title style 

<!-- Start of picture text -->
(©) Hugging Face<br><!-- End of picture text -->

#### <u>huggingface.co/datasets/math_qa</u> 

A large-scale collection of math word problems. It includes questions, multiple-choice options, rationales, and correct answers annotated with operational programs 

<!-- Start of picture text -->
e Question: A train running at the speed of 48 km/hr crosses a pole<br>in 9 seconds . what is the length of the train ?<br>e Rationale: Speed = (48x 5/18) m/sec =(40/3) m/sec. length of<br>the train = ( speed x time ) . length of the train = (40/3x9)m=120m.<br>answer isc.<br>e Options: a) 140,b)130,c)120,d)170,e)160<br>e Correct Option is: C<br><!-- End of picture text -->

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

# ChatGPT versus Math–Combo of Techniques Click to edit Master title style 

<!-- Start of picture text -->
oe Anthropic Opus Accuracy across prompting techniques<br>veveve:<br>an JOOOOOG<br><«x> sSoooocee eee.www ven<br>%3° : aa LS HHEFH5550000vec<br>c J oe KX XE poo000Gcoco<br>ake Seri KX Heo0000%e 2000<br>fey5°g eePek sees SSSKX XEEHR 00000ceeete e000<br>oz iS ponnes SEH SSeoc eee<br>Reeser| SS CHA 2a<br>Rekale b Sooooo°<br><!-- End of picture text -->

<!-- Start of picture text -->
2a u 3-8-Instruct A ; ;<br>b Sooooo°<br>08<br>Bos<br>Soa voces<br>> oovo°e<br>§ roo eoocce<br>vanes EEEEEO 00000200000<br>Loz GY pooo0e —= Litt poo0d0ceceece<br>po9900 ee ae nee toed<br><!-- End of picture text -->

<!-- Start of picture text -->
Legend<br>7 Just Ask (K=0 with CoT) MAN Semantic K=3 (with CoT) @ee Random K=1 (no CoT)<br>xX Just Ask (K=0 no CoT) OO Semantic K=3 (no CoT) Random K=3 (with CoT)<br>= lim *X% SemanticSemantic K=1K=1 (with(no CoT) CoT) sm Random K=1 (with CoT) | Random K=3 (no CoT)<br><!-- End of picture text -->

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

## ReAct 

Click to edit Master title style 

Reasoning and Action ( **ReAct** )-style agents integrate reasoning and action by interleaving thought processes with task-specific actions. This approach allows agents to plan and adjust strategies based on real-time feedback from their environment. 

## ReAct 

Click to edit Master title style 

Reasoning and Action ( **ReAct** )-style agents integrate reasoning and action by interleaving thought processes with task-specific actions. 

This approach allows agents to plan and adjust strategies based on real-time feedback from their environment. 

**<mark>Thought</mark>** <mark>: comment on what you want to do next.</mark> **<mark>Action</mark>** <mark>: the action to take</mark> **<mark>Action Input</mark>** <mark>: the input to the action</mark> **<mark>Observation</mark>** <mark>: the result of the action</mark> 

**<mark>Thought</mark>** <mark>: Now comment on what you want to do next.</mark> **<mark>Action</mark>** <mark>: the next action to take</mark> **<mark>Action Input</mark>** <mark>: the input to the next action</mark> **<mark>Observation</mark>** <mark>: the result of the next action ... (this Thought/Action/Action Input/Observation repeats until you are sure of the answer)</mark> **<mark>Thought</mark>** <mark>: I can finally return the final answer</mark> **<mark>Action</mark>** <mark>: Respond to the User</mark> **<mark>Action Input</mark>** <mark>: The final answer to the task</mark> 

Code Time! Click to edit Master title style 

<!-- Start of picture text -->
-<br>7 | 7, ~ ie :<br>ak ie I tees<br>First Steps with<br>our own Agent<br>Framework<br><!-- End of picture text -->

Click to edit Master title style 

## **Agent Evaluation** 

Evaluating LLMs Click to edit Master title style 

Evaluation is not just about checking whether an agent works or not; it's a step to understand how well the model is working, which can directly impact the usefulness of the model in a real-world scenario. 

Key Metrics for AI Agent Evaluation Click to edit Master title style 

### **Response Time:** 

- Measures how quickly an agent processes inputs and returns outputs. Critical for real-time applications like chatbots and financial systems. 

Key Metrics for AI Agent Evaluation Click to edit Master title style 

**Accuracy:** 

- Evaluates the correctness of the agent’s decision-making, especially for tasks involving data analysis or predictions. 

**Task Completion Rate:** 

- Measures how effectively agents complete assigned tasks, especially in multi-agent systems 

Common Challenges in AI Agent Evaluation Click to edit Master title style 

### **Bias in Decision-Making:** 

- Agents may inherit biases from training data, leading to skewed outputs. Addressing bias requires continuous monitoring and retraining of models 

**Explainability:** 

- AI agents often function as "black boxes," making it difficult to understand how they arrive at decisions. Use explainability tools to improve transparency. 

Common Challenges in AI Agent Evaluation Click to edit Master title style 

### **Agent Collaboration Failures:** 

- In multi-agent systems, breakdowns in communication or poor task delegation can lead to inefficiencies. Use frameworks with built-in debugging tools like AutoGen to address this 

Source: Our Upcoming Code 

Evaluating LLMs Click to edit Master title style 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Evaluating Agents Click to edit Master title style 

- **Picking tool** - classification or multiple choice 

- Usually Multiple Choice 

- **Response to human** - free text response 

Evaluating Agents / LLMs Click to edit Master title style 

<!-- Start of picture text -->
How do I evaluate my LLM?<br>Generative Task Understanding Task<br>[3QL? é CL Sx<br>Multiple Choice Free Text Response Embeddings Classification<br>Execute Tools<br>Could pick<br>Pick Tools<br>tools but would<br>be harder<br><!-- End of picture text -->

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Evaluating Agents Click to edit Master title style 

- **Picking tool** - classification or multiple choice 

- Usually Multiple Choice 

Evaluating Generative LLMs - Multiple Choice Click to edit Master title style 

**Go off of Model’s Output** 

Use the model’s output as your answer, even if they try to respond with a different answer 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Evaluating Agent Tool Selection Click to edit Master title style 

**Accuracy** : The number of correct predictions over all predictions 

**Precision** : # times _scraper_ was correct / # times _scraper_ was selected Useful when the cost of false positives is high 

**Recall** : # times _scraper_ chosen / # times _scraper_ should be selected Useful when the cost of false negatives is high. 

Example: Evaluating an Agent Click to edit Master title style 

('Check the floor price of the world of women nft', **'Crypto and NFT Tool'** ), ('What is the price of ethereum right now?', **'Crypto and NFT Tool'** ), (Tell me about https://loopgenius.com, **'Firecrawl web search tool'** ), ('Visit https://openai.com and summarize it', **'Firecrawl web search tool'** ), 

('What are the current gas prices in Chicago?', **'SerpAPI Tool'** ) 

Accuracy of Tool Selection by Model Click to edit Master title style 

Precision/Recall of Tool Selection by Model/Tool Click to edit Master title style 

Positional Bias in Tool Selection Click to edit Master title style 

Depending on where the tools are in the agent prompt, tools listed later in the list might end up towards the middle of the prompt, where information can get ignored due to **positional bias** - a structural bias in Transformers 

Positional Bias in Tool Selection Click to edit Master title style 

Positional Bias affects tool selection: 

Positional Bias in Tool Selection Click to edit Master title style 

OpenAI is not immune to Positional Bias: 

Positional Bias in Tool Selection Click to edit Master title style 

Google is not immune to Positional Bias: 

Positional Bias in Tool Selection Click to edit Master title style 

Deepseek is not immune to Positional Bias (98.94% overall accuracy): 

# Code Time! (Time permitting) Click to edit Master title style 

<!-- Start of picture text -->
-<br>7 | 7, ~ ie :<br>ak ie I tees<br>Positional Bias<br>with Tool<br>Selection<br><!-- End of picture text -->

Evaluating Agents Click to edit Master title style 

- **Response to human** - free text response 

Evaluating Free Text using Semantic Similarity Click to edit Master title style 

Metrics like **Semantic Similarity** can compare free text to see if the LLM got the “gist” of the output right. 

<!-- Start of picture text -->
President Trump scrapped Obama-era program that protects<br>from deportation immigrants brought illegally into the U<br>presarch enonean as cnetaren Seng amp Verena tt on ae<br>UUCUECEee eee CH CEMEIRISS Ske CA B uo tle<br><!-- End of picture text -->

<!-- Start of picture text -->
Trumpfey announced his decision to endton DACA,fact a political de<br>cision that protects from deportation immigrants brought<br>illegally into the United States as children, delaying i<br>mnlamantatian intil March and aivina a aridlacked Canara<br><!-- End of picture text -->

We can use embeddings to capture the semantic information in each and use cosine similarity to see how close they are, similar to our semantic search system 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Evaluating Free Text with Rubrics Click to edit Master title style 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Evaluating Free Text with Rubrics Click to edit Master title style 

A rubric can be a way to capture what you’re trying to evaluate in a prompt and let an LLM try and figure it out. 

Be careful though, we already have seen how LLM’s can have bias even in their own outputs when it comes to evaluation (our “choose the better answer” example from a few lessons ago) 

Source: Quick Start Guide to LLMs by Sinan Ozdemir 

Evaluating Free Text with Rubrics Click to edit Master title style Different models will yield different scores. Which one aligns with your thoughts? 

**What happens to you if you eat watermelon seeds?** “Eating watermelon seeds is Comparison of 10 generally safe and does not cause harm. In fact, watermelon seeds are 8 2 rich in nutrients like healthy fats, S 8 a protein, and fiber. Swallowing v 6 43 watermelon seeds during eating will « m 4 c pass through your digestive system $ without germination, as they require < 2 specific conditions to grow.” 

Evaluating Agents Click to edit Master title style 

If comparing between multiple agents, backstories, sequential processes, etc, you might want to compare against two agents or tasks 

Task Definition 1 Click to edit Master title style 

Task Definition 2 Click to edit Master title style 

Two Main Options Click to edit Master title style 

- **Human Evaluation** 

   - Asking a human to pick between model outputs 

   - - Not a new industry - AWS Mechanical Turk, Scale AI, etc) 

   - - Expensive (min $2 per pair at scale with decent quality) 

   - Main issue is finding consensus among judges 

- **LLM Evaluation** 

   - Asking an LLM to pick between model outputs 

      - Newer as a method 

   - Relatively Cheap (Can be as low cents per pair) 

   - Main issue is AI bias (e.g., some models are more likely to choose the first output - positional bias) 

Agent Evaluation Prompt Example Click to edit Master title style 

### User Question 

{{ user-question }} 

### Rating Task 

Rate the performance of two AI assistants in response to the user question. ... 

### The Start of Assistant 1's Answer {{ assistant-1-answer }} ### The End of Assistant 1's Answer 

Output a score from 1 to 8 where a 1 means you strongly prefer Assistant 1's answer and 8 means you strongly prefer Assistant 2's answer. 

### The Start of Assistant 2's Answer {{ assistant-2-answer }} ### The End of Assistant 2's Answer 

Give the answer in the json format: JSON: {"reason": "...", "answer": integer score} 

.. continued @ Pearson 

JSON: 

Screenshot from Hugging Face LLM Leaderboard. © Hugging Face. All rights reserved. https://huggingface.co/blog/llm-leaderboard 

Agent Evaluation Prompt Example Click to edit Master title style 

LLM Evaluation Prompt Example Click to edit Master title style 

Positional bias rears its head again. 

When randomly assigning agent outputs to Assistant 1 or 2 

GPT-4 was more likely to just pick Assistant 1 

<!-- Start of picture text -->
Al Scores to pairs of responses with the exact same human score<br>400<br>350<br>250<br>€<br>8 200<br>150<br>100<br>50<br>oO<br>10 2.0 3.0 40 5.0 6.0 7.0 8.0 9.0<br>Score given by Al<br><!-- End of picture text -->

Source: https://ai-office-hours.beehiiv.com/p/ais-s upervising-ais 

Testing Free Response Evaluation Click to edit Master title style 

### Rating Task 

Rate the performance of two assistants in response to the user question. 

Output a score from 1 to 3 where a 1 means you strongly prefer Assistant 1's answer and 3 means you strongly prefer Assistant 2's answer and 2 means either answer works just as well as the other. 

Testing Free Response Evaluation Click to edit Master title style 

No Chain of Thought Yes Chain of Thought Source: https://github.com/sinanuozdemir/or eilly-ai-agents 

# LLM Evaluation Prompt Example Click to edit Master title style 

I used the prompt on the responses about me: (1 == Assistant 1 is best) (2 == Assistants are same) (3 == Assistant 2 is best) 100 times with CoT (Orange) and 100 times without CoT (blue) 

<!-- Start of picture text -->
Histogram of Scores by COT<br>60<br>COT<br>Ss 50 Gm: COT: False<br>2 40 G9 COT: True<br>S 30<br>fou<br>2 20<br>10<br>0<br>1 2 3<br>Score<br><!-- End of picture text -->

Without CoT, more likely to select 1 or 2 With CoT, it’s more spread out 

# Testing Free Response Evaluation Click to edit Master title style 

Just use the simplest framework possible that solves your need. I know that sounds oversimplified, but I made my own just so I could iterate faster and frankly it was fun. 

Source: https://github.com/sinanuozdemir/squad-goals 

Two Main Options Click to edit Master title style 

- **Human Evaluation** 

   - Probably better at first 

   - Higher quality 

   - Gives you a chance to decide what you truly care about 

- **LLM Evaluation** 

   - Scale up the factors you actually care about 

   - - Rubrics mitigate positional biases 

   - Can potentially catch errors on the fly 

# Code Time! Click to edit Master title style 

<!-- Start of picture text -->
-<br>7 | 7, ~ ie :<br>ak ie I tees<br>Positional Bias<br>in Agent<br>Response<br>Selection<br><!-- End of picture text -->

Testing Data Click to edit Master title style 

This of course all assumes you actually have examples to test with with a rubric, accuracy report, etc 

Testing an agent will require **testing data** (examples of fully worked out tasks, tool selection, etc) 

Collecting Labeled Data Click to edit Master title style 

- **Manual Labeling:** This can be done in-house or outsourced to a third-party service. This is often the most accurate but also the most time-consuming and expensive method 

- **Crowdsourcing:** Distribute labeling to a crowd. This is often quicker and cheaper, but the quality of the labels can vary 

- **Synthetic Labeling:** Synthetic data, i.e., data generated via simulations or other means, comes with the "ground truth" labels, which can be used for training models 

Synthetic Data Labeling Click to edit Master title style 

<mark>synthetic_question_prompt = '''Please write {n} search queries that an average person would ask for that should result in this context.</mark> 

<mark>examples: ["A great place in Paris for my dog and cat", "How to diagnose this thing on my foot", "Reset password on iphone now"] The questions MUST have an answer in this context.</mark> 

<mark>Use this format to output: Document: A given document to make questions from JSON: ["english query 1", "english query 2", ..., "english query n"] ###</mark> 

<mark>Document: {document} JSON:'''</mark> 

Synthetic Data Labeling Click to edit Master title style 

Collecting feedback from users Click to edit Master title style 

**Explicit Feedback:** Users directly provide their opinion or preference. E.g. rating a product on a scale from 1 to 5, or liking/disliking a social media post. 

Explicit feedback provides clear insight into user preferences, but can be hard to collect in large quantities. 

**Implicit Feedback:** Feedback inferred from user actions. E.g. the amount of time a user spends reading an article might imply that they find it interesting. 

Usually abundant but can be noisy, as the inferred preferences may not always align perfectly with the user's true feelings. 

# Collecting feedback from users Click to edit Master title style 

Copying is **implicit** feedback "Excited to announce the release of my latest book, 'A Quick Start () Guide to LLMs! © It's been an enlightening journey distilling complex Thumbs up or down is **explicit** feedback buddinginsights intoattorneyaccessible or just wisdcuri **o** us,m. Whethlet's d **e** mystifyr you're athelaw student,world of LLMs a <mark>|</mark> 

Click to edit Master title style 

**Cost Projections and Management** 

Understanding Costs in AI Agent Deployment Click to edit Master title style 

- **Data Handling:** Costs for managing, cleaning, and processing large datasets for training and real-time inference. 

- **Scalability:** Costs increase as agents are scaled for higher loads or multi-agent setups, especially when using real-time data processing 

Agent Types and Cost Click to edit Master title style 

- **Stateless Agents:** Simpler and cheaper to deploy; ideal for lightweight tasks. 

- **Stateful, Multi-Agent Systems:** Require more compute resources, especially for collaboration and real-time task management 

Initial Setup Costs Click to edit Master title style 

- **Costs related to framework setup** (e.g., LangChain, AutoGen, or CrewAI), cloud configuration, and software licenses. 

   - Example: Deploying a small multi-agent system on AWS can cost $25–$100/month depending on usage 

Ongoing Costs Click to edit Master title style 

- **Compute Resources:** For models that require constant processing (e.g., chatbots, real-time data agents), cloud compute costs can grow significantly. 

- **Maintenance and Updates:** Factor in the cost of continuously updating and retraining models to ensure performance remains optimal 

LLMs/Agents in Business Workflows Click to edit Master title style 

- **Iterative Development:** Start small with a proof-of-concept, gather feedback, make improvements, and gradually increase the scope and complexity of the integration 

- **User Training:** Ensure that all users know how to use the new tools effectively and understand the benefits and limitations of LLMs 

- **Monitoring & Maintenance:** Regularly evaluate the performance of the LLM, and be ready to fine-tune the model or update the training data as needed 

Click to edit Master title style 

## **Iteration and Improvement** 

Techniques for Iterating on AI Agent Designs Click to edit Master title style 

### **Feedback Loops:** 

- Implement feedback loops where agents receive real-time or batch feedback on their actions and adjust their future decisions accordingly. 

Techniques for Iterating on AI Agent Designs Click to edit Master title style 

### **Task Refinement:** 

- Continuously refine agent tasks to ensure they handle more complex situations. This can be done through adding more data, improving the underlying model, or fine-tuning prompts. 

Click to edit Master title style 

## **Advanced Integration Techniques + Best Practices** 

## ReAct 

Click to edit Master title style 

Reasoning and Action ( **ReAct** )-style agents integrate reasoning and action by interleaving thought processes with task-specific actions. 

Optimizing Agents - Plan & Execute Click to edit Master title style 

Instead of a single powerful LLM slowly working its way through the Thought-Action-Observation loop over and over in a sequential manner.. What if a large LLM made a **plan** while smaller, faster LLMs **executed** on that plan? 

Optimizing Agents - Plan & Execute Click to edit Master title style 

**Plan & Execute** Agents offload execution onto smaller, faster LLMs, leaving a larger, slower LLM only to plan + return final answers 

Code Time! Click to edit Master title style 

<!-- Start of picture text -->
Plan & Execute<br>Agents<br><!-- End of picture text -->

Optimizing Agents - Reflection Click to edit Master title style 

Instead of simple returning the final answer after working its way through the Thought-Action-Observation loop.. 

What if we **reflected** on the Agent’s work before returning the final answer, allowing for revisions along the way? 

Optimizing Agents - Reflection Click to edit Master title style 

**Reflection** Agents have built in reflection modules to reflect on, critique final answers and offer suggestions to revise & improve 

Code Time! Click to edit Master title style 

<!-- Start of picture text -->
Reflection<br>Agents<br><!-- End of picture text -->

Integrating Real-Time Data into AI Agents Click to edit Master title style 

**Why Real-Time Data Matters:** 

- Many AI agents need to operate in dynamic environments where they react to constantly changing data (e.g., stock market, customer interactions). 

**Methods for Integration:** 

- Use APIs to connect AI agents with live data sources (e.g., weather APIs, financial feeds). 

Why real-time data matters Click to edit Master title style 

“Grounding” an LLM with real-time factual data is one way to prevent **hallucinations -** an AI’s ability to generate perfectly fine text about an incorrect scenario 

Giving an LLM access to real-time data grounds the AI to use the given context more often (not always - see the evaluation slides) 

Integrating Real-Time Data into AI Agents Click to edit Master title style 

### **Handling Real-Time Data:** 

- Ensure that your agents can process data fast enough, potentially using edge computing or distributed cloud resources. 

- Focus on data quality by using preprocessing steps to remove noise from data streams 

Best Practices for AI Agent Development Click to edit Master title style 

### **Modular Testing and Debugging:** 

- Break workflows into smaller, testable modules to quickly identify and address issues during development. 

- Use AutoGen’s debugging tools or LangChain’s testing features to track performance and reliability 

Best Practices for AI Agent Development Click to edit Master title style 

### **Feedback Loops for Continuous Improvement:** 

- Implement feedback loops for real-time agent performance tracking. Use data from system telemetry or human feedback to improve agent decision-making. 

- Frameworks like CrewAI support continuous improvement with built-in task performance evaluation 

# Ethical Considerations and Compliance Click to edit Master title style 

### **Ethics in AI Agents:** 

- AI agents must be designed to handle sensitive data securely and make unbiased decisions. 

- Key Risks: Data privacy, algorithmic bias, decision opacity, and potential harm from misaligned AI actions 

Ethical Considerations and Compliance Click to edit Master title style 

### **Ensuring Compliance:** 

- Follow data protection regulations such as GDPR when designing agents that handle personal data. 

- - Implement transparency mechanisms (e.g., explainable AI) to ensure accountability in decision-making 

**Best Practices:** 

- Regular audits of AI agent decisions to ensure fairness and compliance 

Click to edit Master title style 

## **Future Trends and Next Steps** 

# Computer Use Click to edit Master title style 

Anthropic's "computer use" feature allows Claude 3.5 to interact with a computer's interface and perform tasks. To accomplish this, Claude will: 

1. Receive a command and identifies the steps needed to complete it 

2. Scan screenshots to determine what steps to take 

3. Read and interpret the display 4. Move the cursor, type text, click buttons, etc 

<!-- Start of picture text -->
y\™ Claude | Computer use for automating operations) © (ad<br>the form chin windowfieldas you complete © > GO lecehost2000 Pre teh aleecasharcccct<br>two. scien veces seme & | AcmeInc. Vendor R<br>111 help you fil out the vendor ivan<br>form for'Ant Equipment<br>Co. Let [2 sexchiyconpanynanemiooremat. | seweh ———<br>- =<br>@ Screenshot ™<br>Q Leos ety Arse<br>open vendor search portal Search fora Company Select county *<br>isnotLeetme visible incheck the the vendor spreadsheet.search<br>need to click on ————4dress ie2<br>MORE VIDEOS portal tab. city<br>utPromnea*<br>DP  ) 1:05/ 203 - Example GS Ike”) YouTube 25<br><!-- End of picture text -->

Source: Anthropic’s Youtube 

# Computer Use Click to edit Master title style 

Anthropic's "computer use" feature allows Claude 3.5 to interact with a computer's interface and perform tasks. To accomplish this, Claude will: 

1. Receive a command and identifies the steps needed to complete it 

2. Scan screenshots to determine what steps to take 

3. Read and interpret the display 4. Move the cursor, type text, click buttons, etc 

Open-Source Computer Use Click to edit Master title style 

**OmniParser** (By Microsoft) is a model for parsing screenshots into structured and easy-to-understand elements. 

We could use this to pass off to an LLM to generate actions that can be accurately grounded in the corresponding regions of the interface. 

<!-- Start of picture text -->
@® Spaces #8 microsoft OmniParser © © like Running on ZERO,<br>OmniParser for Pure Vision Based General GUI Agent &<br>OmniParser is a screen parsing tool to convert general GUI screen to structured elements.<br>Upload image ania X Image Output I<br>ify<br>Parsed screen elements<br>Box Threshold 0.05 ° Text Box ID 0: https://github.<br>com/sinanuozdemir<br><!-- End of picture text -->

Source: https://huggingface.co/spaces/mic rosoft/OmniParser 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **AI and IoT Integration:** 

- AI agents are increasingly being integrated with the Internet of Things (IoT) to enable smarter, more responsive systems. 

- Use cases include smart homes, industrial automation, and healthcare monitoring 

Emerging Trends in AI Agent Technology Click to edit Master title style 

**Collaborative Multi-Agent Systems:** 

- AI agents working together in more complex, multi-agent environments to handle large-scale, dynamic tasks. 

Innovations on the Horizon Click to edit Master title style 

**Real-Time Collaboration Between Agents:** 

- Future systems will see enhanced communication between agents, allowing for real-time problem solving and decision-making. 

- AutoGen and Swarm are frameworks already exploring this collaborative capability 

Emerging Trends in AI Agent Technology Click to edit Master title style 

**Simpler UIs for generating agents on the fly:** - Right now everything is so hard coded and there are few to no commercially viable agent building platforms that don’t require some technical background to get it working well. This needs to change if we are going to stare at a bright agentic future 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **AI and IoT Integration:** 

- AI agents are increasingly being integrated with the Internet of Things (IoT) to enable smarter, more responsive systems. 

- Use cases include smart homes, industrial automation, and healthcare monitoring 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **Collaborative Multi-Agent Systems:** 

- By sharing the load across multiple agents, we can save on context window size so one agent can focus on a specific sub-task without being bogged down by the memory of what came before 

- Agents can be given a namespace designation like being good at a certain type of task with a fine-tuned LLM or being the “Agent for X” where X is Spotify tasks, Youtube tasks, Twitter tasks, etc 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **Collaborative Multi-Agent Systems:** 

- For either option, the idea is to split up the load between agents so that we don’t stuff too many tools or too much context into a single prompt/LLM 

Innovations on the Horizon Click to edit Master title style 

**Real-Time Collaboration Between Agents:** 

- Future systems will see enhanced communication between agents, allowing for real-time problem solving and decision-making. 

- AutoGen and Swarm are frameworks already exploring this collaborative capability 

Emerging Trends in AI Agent Technology Click to edit Master title style 

**Simpler UIs for generating agents on the fly:** - Right now everything is so hard coded and there are few to no commercially viable agent building platforms that don’t require some technical background to get it working well. This needs to change if we are going to stare at a bright agentic future 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **Auto-Generation of Tasks** 

- Given a high level goal, kick off an entirely generated task workflow without needing to hard-code task definitions 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **Auto-Generation of Tools** 

- Given some documentation, write a custom API tool like we did for SERP and Alpaca 

Emerging Trends in AI Agent Technology Click to edit Master title style 

### **Auto-Generation of Agents** 

- Write rules/permissions for agents on the fly. At this point we run into the philosophical question: what really is the _“agent”_ part? Is it the prompt, the tool, the well defined- tasks, the backstory, all of the above? 

Summary + Next Steps Click to edit Master title style 

<!-- Start of picture text -->
livelessons®<br>Introduction<br>to Transformer<br>Models for NLP<br>Sinan Ozdemir<br>? video<br><!-- End of picture text -->

A comprehensive introduction to LLMs + Transformers <u>https://learning.oreilly.com/videos/introduction-to-transformer/9780137923717</u> Check out my live trainings for more in depth content! <u>https://learning.oreilly.com/search/?q=Sinan%20Ozdemir&type=live-event-series</u> 

<!-- Start of picture text -->
LARGE<br>LANGUAGE<br>MODELS<br>and MultimodalAl ?<br>-<br><!-- End of picture text -->

Thank you! / Final Q/A Click to edit Master title style 

Many of these examples were based off of my new book on LLMs, usually top 10 in many categories on Amazon including NLP 

<!-- Start of picture text -->
~ fee i She N<br>QUICK START GUIDE 19<br>LANGNG UA GE<br>MODELS<br>Strategies and Best Practices for<br>ChatGPT, Embeddings, Fine-Tuning,<br>and MultimodalAl<br>“a<br>P SINAN OZDEMIR '<br><!-- End of picture text -->

<u>https://a.co/d/2hYnk9j</u> ~~ee~~ 

Click to edit Master title style 

**AI Agents A-Z** Thank you!!! **Sinan Ozdemir** Data Scientist, Entrepreneur, Author, Lecturer <mark>fo</mark>
