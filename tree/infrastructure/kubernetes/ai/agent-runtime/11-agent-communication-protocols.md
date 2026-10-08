---
title: Agent Communication Protocols
description: 'MCP/A2A/ACP Protocol Deep Dive: Transport/Tool/Resource Models, Agent-to-Agent Collaboration, Protocol Selection and Integration Practices'
summary: 'MCP/A2A/ACP Protocol Deep Dive: Transport/Tool/Resource Models, Agent-to-Agent Collaboration, Protocol Selection and Integration Practices'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- mcp
- a2a
- acp
- protocol
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Platform Engineers
- Architects
estimated_read_time: 20min
intent_queries:
- What is Agent Communication Protocol
- MCP protocol explained
- A2A protocol explained
- Agent protocol selection comparison
trigger_keywords:
- mcp
- a2a
- acp
- agent-protocol
prerequisites:
- llm-basics
- kubernetes-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/11-agent-communication-protocols.md
---
# Agent Communication Protocols

## Overview

As AI Agents evolve from monolithic applications into distributed multi-agent systems, the communication protocols between agents become a critical component of the infrastructure layer. This document provides an in-depth analysis of three mainstream agent communication protocols: MCP (Model Context Protocol), A2A (Agent-to-Agent), and ACP (Agent Communication Protocol), along with a protocol selection guide and integration practices.

```
Protocol Positioning:

MCP (Model Context Protocol):
  - Open protocol led by Anthropic
  - Defines standardized interfaces between LLMs and external tools/resources
  - Analogy: USB-C for AI — a unified tool integration standard

A2A (Agent-to-Agent Protocol):
  - Open protocol led by Google
  - Defines discovery, collaboration, and communication mechanisms between agents
  - Analogy: HTTP for Agents — the inter-agent communication standard

ACP (Agent Communication Protocol):
  - Open protocol led by IBM
  - Message-based agent communication middleware
  - Analogy: AMQP for Agents — message-queue-style communication
```

## MCP (Model Context Protocol) Deep Dive

### Protocol Architecture

MCP adopts a client-server architecture that defines standardized communication between LLM applications and external resources:

```
+-------------------+     +-------------------+
|   MCP Host        |     |   MCP Server      |
| (LLM Application) |<--->| (Tool/Resource    |
|                   |     |  Provider)        |
+-------------------+     +-------------------+
        |                         |
        v                         v
+-------------------+     +-------------------+
|   MCP Client      |     |   External        |
| (Protocol Layer)  |     |   Resources       |
+-------------------+     +-------------------+

Transport layer: stdio / SSE / Streamable HTTP
Protocol layer: JSON-RPC 2.0
Semantic layer: Tool / Resource / Prompt / Sampling
```

### Transport Layer

```python
# MCP supports three Transport methods

# 1. stdio - Standard input/output (local process)
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("my-tools")

@server.tool()
async def search_database(query: str) -> str:
    """Search the database"""
    results = await db.search(query)
    return json.dumps(results)

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)


# 2. SSE - Server-Sent Events (HTTP long connection)
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route

transport = SseServerTransport("/messages")

async def handle_sse(request):
    async with transport.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        await server.run(streams[0], streams[1])

app = Starlette(routes=[
    Route("/sse", endpoint=handle_sse),
    Route("/messages", endpoint=transport.handle_post_message,
          methods=["POST"]),
])


# 3. Streamable HTTP (recommended new approach)
from mcp.server.streamable_http import StreamableHTTPServerTransport

transport = StreamableHTTPServerTransport("/mcp")

app = Starlette(routes=[
    Route("/mcp", endpoint=transport.handle_request),
])
```

### Tool Definition and Implementation

```python
from mcp.types import Tool, TextContent
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(description="Search query")
    max_results: int = Field(default=10, description="Maximum number of results")

@server.tool()
async def web_search(input: SearchInput) -> list[TextContent]:
    """Search the internet for the latest information"""
    results = await search_engine.search(
        query=input.query,
        limit=input.max_results,
    )

    formatted = "\n".join(
        f"- {r.title}: {r.snippet}" for r in results
    )
    return [TextContent(type="text", text=formatted)]


@server.tool()
async def execute_sql(
    database: str,
    query: str,
) -> list[TextContent]:
    """Execute an SQL query (read-only)"""
    # Safety check
    if any(keyword in query.upper() for keyword in
           ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER"]):
        return [TextContent(
            type="text",
            text="Error: Only SELECT queries are allowed",
        )]

    try:
        result = await db.execute(database, query)
        return [TextContent(
            type="text",
            text=json.dumps(result, ensure_ascii=False),
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Query error: {str(e)}",
        )]
```

### Resource Exposure

```python
@server.resource("file:///{path}")
async def read_file(path: str) -> str:
    """Read file contents"""
    full_path = validate_path(path)
    with open(full_path, "r") as f:
        return f.read()


@server.resource("db:///{table}")
async def get_table_schema(table: str) -> str:
    """Get database table schema"""
    schema = await db.get_schema(table)
    return json.dumps(schema)


@server.resource("config:///{key}")
async def get_config(key: str) -> str:
    """Get configuration information"""
    value = config.get(key)
    return json.dumps(value)
```

### Prompt Templates

```python
@server.prompt()
async def code_review(
    code: str,
    language: str = "python",
) -> str:
    """Code review prompt template"""
    return f"""Please review the following {language} code, focusing on:
1. Potential bugs and errors
2. Performance issues
3. Security vulnerabilities
4. Code style and best practices

```{language}
{code}
```

Please provide a detailed review report."""


@server.prompt()
async def sql_generator(
    schema: str,
    requirement: str,
) -> str:
    """SQL generation prompt template"""
    return f"""Based on the following database schema:
{schema}

Generate an SQL query that satisfies the following requirement:
{requirement}

Requirements:
1. Generate only SELECT queries
2. Add appropriate comments
3. Consider query performance
"""
```

### Client Integration

```python
from mcp.client import ClientSession
from mcp.client.sse import sse_client

async def use_mcp_server():
    """Connect to an MCP server and use its tools"""
    async with sse_client("http://localhost:8080/sse") as (
        read_stream, write_stream
    ):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")

            # List available resources
            resources = await session.list_resources()
            print(f"Available resources: {[r.uri for r in resources.resources]}")

            # Call a tool
            result = await session.call_tool(
                "web_search",
                arguments={
                    "query": "kubernetes best practices",
                    "max_results": 5,
                },
            )
            print(f"Search results: {result.content}")

            # Read a resource
            resource = await session.read_resource("file:///README.md")
            print(f"File contents: {resource.contents}")
```
## A2A (Agent-to-Agent) Protocol

### Protocol Overview

The A2A protocol defines a standardized communication method between Agents, enabling Agents built with different frameworks to discover and collaborate with each other:

```
A2A Core Concepts:

Agent Card:
  - Self-describing document for an Agent
  - Contains capabilities, endpoints, and authentication information
  - Similar to an OpenAPI specification for APIs

Task:
  - Unit of work between Agents
  - Contains a state machine (submitted → working → completed)
  - Supports long-running operations

Artifact:
  - Output produced by a Task
  - Supports multiple content types
  - Can be files, data, or streaming content

Message:
  - Communication message between Agents
  - Supports text, structured data, and files
  - Contains role and context information
```

### Agent Card Definition

```json
{
  "name": "Research Agent",
  "description": "An Agent that performs deep research and generates reports",
  "url": "https://research-agent.example.com",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": true,
    "stateTransitionHistory": true
  },
  "authentication": {
    "schemes": ["bearer"],
    "credentials": "Bearer token required"
  },
  "defaultInputModes": ["text/plain", "application/json"],
  "defaultOutputModes": ["text/plain", "text/markdown"],
  "skills": [
    {
      "id": "web-research",
      "name": "Web Research",
      "description": "Search the internet and extract information",
      "tags": ["research", "search", "information"],
      "examples": [
        "Research Kubernetes best practices",
        "Find the latest AI papers"
      ]
    },
    {
      "id": "report-generation",
      "name": "Report Generation",
      "description": "Generate structured research reports",
      "tags": ["writing", "report", "analysis"]
    }
  ]
}
```

### Task Lifecycle

```python
from a2a.types import Task, TaskState, Message, Artifact
from a2a.server import A2AServer

class ResearchAgentServer(A2AServer):
    """Research Agent implementing the A2A protocol"""

    async def handle_task(
        self,
        task: Task,
    ) -> Task:
        """Handle an Agent task"""
        # Update task state to working
        task.status.state = TaskState.WORKING
        await self.notify_status_change(task)

        try:
            # Extract user message
            user_message = task.message
            query = user_message.parts[0].text

            # Conduct research
            research_result = await self.conduct_research(query)

            # Create output artifact
            artifact = Artifact(
                name="research-report",
                parts=[
                    {
                        "type": "text",
                        "text": research_result.report,
                    },
                    {
                        "type": "file",
                        "file": {
                            "name": "sources.json",
                            "mime_type": "application/json",
                            "data": base64.b64encode(
                                json.dumps(research_result.sources).encode()
                            ).decode(),
                        },
                    },
                ],
            )

            # Update task state to completed
            task.status.state = TaskState.COMPLETED
            task.artifacts = [artifact]

        except Exception as e:
            task.status.state = TaskState.FAILED
            task.status.message = str(e)

        return task

    async def conduct_research(self, query: str) -> ResearchResult:
        """Execute a research task"""
        # Search for relevant information
        search_results = await self.web_search(query)

        # Analyze and synthesize
        analysis = await self.analyze(search_results)

        # Generate report
        report = await self.generate_report(analysis)

        return ResearchResult(
            report=report,
            sources=search_results,
        )
```

### Agent-to-Agent Collaboration

```python
from a2a.client import A2AClient

async def multi_agent_research(topic: str):
    """Multi-Agent collaborative research"""

    # 1. Discover available Agents
    research_agent = await A2AClient.discover(
        "https://research-agent.example.com"
    )
    writing_agent = await A2AClient.discover(
        "https://writing-agent.example.com"
    )
    review_agent = await A2AClient.discover(
        "https://review-agent.example.com"
    )

    # 2. Create a research task
    research_task = await research_agent.create_task(
        message=Message(
            role="user",
            parts=[{"type": "text", "text": f"Deep research: {topic}"}],
        ),
    )

    # 3. Wait for research to complete
    research_result = await research_agent.wait_for_completion(
        research_task.id,
    )

    # 4. Send research results to the writing Agent
    writing_task = await writing_agent.create_task(
        message=Message(
            role="user",
            parts=[{
                "type": "text",
                "text": f"Write a report based on the following research results:\n{research_result.artifacts[0].parts[0].text}",
            }],
        ),
    )

    # 5. Wait for writing to complete
    writing_result = await writing_agent.wait_for_completion(
        writing_task.id,
    )

    # 6. Send to the review Agent
    review_task = await review_agent.create_task(
        message=Message(
            role="user",
            parts=[{
                "type": "text",
                "text": f"Review the following report:\n{writing_result.artifacts[0].parts[0].text}",
            }],
        ),
    )

    # 7. Get the final result
    review_result = await review_agent.wait_for_completion(
        review_task.id,
    )

    return {
        "report": writing_result.artifacts[0].parts[0].text,
        "review": review_result.artifacts[0].parts[0].text,
    }
```
## ACP (Agent Communication Protocol)

### Protocol Overview

ACP is based on a message queue pattern, providing asynchronous, reliable Agent communication:

```
ACP Architecture Features:

Message-Driven:
  - Asynchronous communication based on message queues
  - Supports publish/subscribe pattern
  - Message persistence and reliable delivery

Loose Coupling:
  - Agents do not need to know each other's addresses
  - Indirect communication via message broker
  - Supports dynamic scaling

Reliability:
  - Message acknowledgment mechanism
  - Dead-letter queue for handling failed messages
  - Supports message retry
```

### ACP Implementation

```python
from acp import ACPAgent, Message, MessageType

class ResearchACPAgent(ACPAgent):
    """Research Agent based on ACP"""

    def __init__(self, agent_id: str, broker_url: str):
        super().__init__(agent_id, broker_url)
        self.register_handler(
            MessageType.REQUEST,
            self.handle_research_request,
        )

    async def handle_research_request(self, message: Message):
        """Handle research request"""
        query = message.payload["query"]

        # Execute research
        result = await self.conduct_research(query)

        # Send response
        response = Message(
            type=MessageType.RESPONSE,
            sender=self.agent_id,
            recipient=message.sender,
            correlation_id=message.id,
            payload={
                "result": result.report,
                "sources": result.sources,
            },
        )

        await self.send(response)

    async def conduct_research(self, query: str):
        """Execute research logic"""
        # Publish search request to Search Agent
        search_response = await self.request(
            recipient="search-agent",
            payload={"query": query, "type": "web_search"},
            timeout=30,
        )

        # Publish analysis request to Analysis Agent
        analysis_response = await self.request(
            recipient="analysis-agent",
            payload={
                "data": search_response.payload["results"],
                "type": "text_analysis",
            },
            timeout=60,
        )

        return ResearchResult(
            report=analysis_response.payload["report"],
            sources=search_response.payload["results"],
        )


# Usage example
async def main():
    # Start Agent
    agent = ResearchACPAgent(
        agent_id="research-agent-001",
        broker_url="amqp://localhost:5672",
    )

    # Subscribe to topic
    await agent.subscribe("research.requests")

    # Start processing messages
    await agent.start()
```

### Message Routing

```python
class ACPRouter:
    """ACP message router"""

    def __init__(self, broker_url: str):
        self.broker = MessageBroker(broker_url)
        self.routes = {}

    def register_route(
        self,
        pattern: str,
        handler: ACPAgent,
    ):
        """Register message route"""
        self.routes[pattern] = handler

    async def route_message(self, message: Message):
        """Route message to target Agent"""
        # Route based on message type
        if message.type == MessageType.REQUEST:
            # Find target Agent
            recipient = message.recipient
            if recipient in self.routes:
                await self.routes[recipient].receive(message)
            else:
                # Broadcast to subscribers
                await self.broker.publish(
                    topic=f"requests.{recipient}",
                    message=message,
                )

        elif message.type == MessageType.PUBLISH:
            # Publish/subscribe pattern
            topic = message.payload.get("topic", "default")
            await self.broker.publish(
                topic=topic,
                message=message,
            )
```

## OpenAI Agents SDK

### SDK Overview

The OpenAI Agents SDK provides native multi-Agent collaboration capabilities:

```python
from openai.agents import Agent, Runner

# Define Agents
research_agent = Agent(
    name="Research Agent",
    instructions="""You are a research assistant.
    Search the internet for information and provide accurate, up-to-date answers.""",
    model="gpt-4o",
    tools=[
        WebSearchTool(),
        FileSearchTool(),
    ],
)

writing_agent = Agent(
    name="Writing Agent",
    instructions="""You are a writing expert.
    Write clear, structured reports based on the provided materials.""",
    model="gpt-4o",
)

review_agent = Agent(
    name="Review Agent",
    instructions="""You are a review expert.
    Review content for accuracy, completeness, and quality.""",
    model="gpt-4o",
    tools=[CodeInterpreterTool()],
)

# Collaboration between Agents
async def research_and_write(topic: str):
    # 1. Research phase
    research_result = await Runner.run(
        starting_agent=research_agent,
        input=f"Conduct in-depth research on the following topic: {topic}",
    )

    # 2. Writing phase
    writing_result = await Runner.run(
        starting_agent=writing_agent,
        input=f"Write a report based on the following research:\n{research_result.final_output}",
    )

    # 3. Review phase
    review_result = await Runner.run(
        starting_agent=review_agent,
        input=f"Review the following report:\n{writing_result.final_output}",
    )

    return {
        "research": research_result.final_output,
        "report": writing_result.final_output,
        "review": review_result.final_output,
    }
```

### Handoff Mechanism

```python
from openai.agents import Agent, handoff

# Define Agent with Handoffs
triage_agent = Agent(
    name="Triage Agent",
    instructions="""You are a task dispatch Agent.
    Based on the type of user request, hand off the task to the appropriate Agent:
    - Research requests → Research Agent
    - Writing requests → Writing Agent
    - Code requests → Code Agent""",
    model="gpt-4o",
    handoffs=[
        handoff(
            agent=research_agent,
            description="Handle research and information gathering requests",
        ),
        handoff(
            agent=writing_agent,
            description="Handle writing and content generation requests",
        ),
        handoff(
            agent=code_agent,
            description="Handle programming and code-related requests",
        ),
    ],
)

# Usage
result = await Runner.run(
    starting_agent=triage_agent,
    input="Research best practices for Kubernetes network policies",
)
```
## Protocol Selection Comparison

### Feature Comparison

```
Feature Comparison Table:

                MCP          A2A          ACP          OpenAI SDK
─────────────────────────────────────────────────────────────────
Role         Tool Access   Agent Collab  Messaging     SDK Integration
Comm Mode    Req/Response  Task-Driven   Async Msg     Function Call
Discovery    Static Config Agent Card    Topic Sub     Code-Defined
State Mgmt   Stateless     Task FSM      Msg State     Runner Mgmt
Streaming    SSE/HTTP      SSE           Msg Stream    Streaming API
Security     OAuth/API Key mTLS/JWT      SASL/TLS     API Key
Use Case     Tool Integ    Cross-Org     Enterprise    Rapid Proto
Maturity     High(GA)      Mid(Preview)  Mid          High(GA)
```

### Selection Guide

```
Selection Decision Tree:

Need to integrate external tools/APIs?
  └── Yes → MCP
       Unified tool integration standard
       Wide ecosystem support

Need cross-organization Agent collaboration?
  └── Yes → A2A
       Standardized Agent discovery
       Supports heterogeneous Agents

Need highly reliable async communication?
  └── Yes → ACP
       Message queue guarantees reliable delivery
       Supports complex routing

Rapid prototyping or OpenAI ecosystem?
  └── Yes → OpenAI Agents SDK
       Out-of-the-box multi-Agent support
       Deep integration with OpenAI services

Combined usage:
  MCP + A2A: Tool integration + Agent collaboration
  MCP + ACP: Tool integration + Async communication
  A2A + ACP: Agent collaboration + Message reliability
```

### Integration Architecture

```python
# Hybrid Agent architecture combining MCP + A2A
class HybridAgent:
    """Hybrid Agent supporting both MCP and A2A"""

    def __init__(self):
        # MCP: expose tools as a Server
        self.mcp_server = Server("hybrid-agent")

        # A2A: participate in collaboration as an Agent
        self.a2a_server = A2AServer(
            agent_card=self._build_agent_card(),
        )

        # Register MCP tools
        self._register_mcp_tools()

        # Register A2A handlers
        self._register_a2a_handlers()

    def _register_mcp_tools(self):
        @self.mcp_server.tool()
        async def search(query: str) -> str:
            """Search tool"""
            return await self.search(query)

        @self.mcp_server.tool()
        async def analyze(data: str) -> str:
            """Analysis tool"""
            return await self.analyze(data)

    def _register_a2a_handlers(self):
        @self.a2a_server.task_handler()
        async def handle_research(task: Task) -> Task:
            """Handle research tasks"""
            query = task.message.parts[0].text

            # Use MCP tools to perform research
            search_result = await self.mcp_client.call_tool(
                "search", {"query": query}
            )
            analysis = await self.mcp_client.call_tool(
                "analyze", {"data": search_result}
            )

            task.status.state = TaskState.COMPLETED
            task.artifacts = [Artifact(
                parts=[{"type": "text", "text": analysis}]
            )]
            return task

    async def start(self):
        """Start Agent services"""
        await asyncio.gather(
            self.mcp_server.run(),
            self.a2a_server.run(),
        )
```

---

*The three major protocols — MCP, A2A, and ACP — address tool integration, Agent collaboration, and message communication respectively. Used in combination, they can build a complete Agent communication infrastructure.*
