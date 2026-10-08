---
title: Semantic Kernel Enterprise-Grade Agent Deep Guide
description: 'Comprehensive analysis of Semantic Kernel Kernel/Plugin/Function three-layer architecture, covering Planner automatic planning, multi-language support, Azure OpenAI integration, and AutoGen interoperability'
summary: 'Comprehensive analysis of Semantic Kernel Kernel/Plugin/Function three-layer architecture'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- semantic-kernel
- microsoft
- enterprise
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
- What is Semantic Kernel
- How to use Semantic Kernel
- Semantic Kernel Planner automatic planning
trigger_keywords:
- semantic-kernel
- kernel
- plugin
- planner
- azure-openai
prerequisites:
- llm-basics
- python-basics
- kubectl-basics
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/06-semantic-kernel-enterprise.md
---
> **Production Environment Security Notice**
>
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (will modify cluster state, but is generally reversible), 🟢 Low Risk/Read-Only (information gathering, no side effects).


# Semantic Kernel Enterprise-Grade Agent In-Depth Guide

## 1. Core Architecture

### 1.1 Design Positioning

Semantic Kernel (SK) is Microsoft's open-source AI orchestration SDK, designed specifically for enterprise applications. Core advantages:
- **Native .NET / C# support**: Suitable for enterprise .NET technology stacks
- **Deep Azure integration**: Native support for Azure OpenAI and Azure AI Search
- **Plugin-based architecture**: Standardized Plugin/Function abstractions
- **Multi-language support**: C#, Python, Java

```
┌─────────────────────────────────────────────────┐
│           Semantic Kernel Architecture            │
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │              Application                  │    │
│  └──────────────────┬───────────────────────┘    │
│                     │                            │
│  ┌──────────────────┴───────────────────────┐    │
│  │           Kernel (Core Runtime)           │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐  │    │
│  │  │ AI       │ │ Plugin   │ │ Service  │  │    │
│  │  │ Services │ │ Manager  │ │ Selector │  │    │
│  │  └──────────┘ └──────────┘ └──────────┘  │    │
│  └──────────────────┬───────────────────────┘    │
│                     │                            │
│  ┌──────────────────┴───────────────────────┐    │
│  │              Plugins                       │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐  │    │
│  │  │ Native   │ │ OpenAPI  │ │ Memory   │  │    │
│  │  │ Functions│ │ Plugins  │ │ Plugins  │  │    │
│  │  └──────────┘ └──────────┘ └──────────┘  │    │
│  └──────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

### 1.2 Kernel Initialization (C#)

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

// Create Kernel
var builder = Kernel.CreateBuilder();

// Add AI services
builder.AddAzureOpenAIChatCompletion(
    deploymentName: "gpt-4o",
    endpoint: "https://my-resource.openai.azure.com/",
    apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")
);

// Add plugins
builder.Plugins.AddFromType<K8sPlugin>();
builder.Plugins.AddFromType<LogAnalysisPlugin>();

var kernel = builder.Build();
```

### 1.3 Kernel Initialization (Python)

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions import KernelPlugin

# Create Kernel
kernel = sk.Kernel()

# Add AI services
kernel.add_service(
    AzureChatCompletion(
        service_id="default",
        deployment_name="gpt-4o",
        endpoint="https://my-resource.openai.azure.com/",
        api_key=os.environ["AZURE_OPENAI_KEY"],
    )
)

# Add plugins
kernel.add_plugin(K8sPlugin(), "k8s")
kernel.add_plugin(LogPlugin(), "logs")
```

---

## 2. Plugin / Function Architecture

### 2.1 Native Plugin (C#)

```csharp
using Microsoft.SemanticKernel;
using System.ComponentModel;

public class K8sPlugin
{
    [KernelFunction("get_pod_status")]
    [Description("Query the running status of a Kubernetes Pod")]
    public async Task<string> GetPodStatus(
        [Description("Namespace")] string namespace = "default",
        [Description("Pod name")] string podName = "")
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "kubectl",
                Arguments = $"get pods -n {namespace} -o wide",
                RedirectStandardOutput = true,
                UseShellExecute = false,
            }
        };
        process.Start();
        return await process.StandardOutput.ReadToEndAsync();
    }

    [KernelFunction("describe_pod")]
    [Description("Get detailed description information for a Pod")]
    public async Task<string> DescribePod(
        [Description("Namespace")] string @namespace,
        [Description("Pod name")] string podName)
    {
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = "kubectl",
                Arguments = $"describe pod {podName} -n {@namespace}",
                RedirectStandardOutput = true,
                UseShellExecute = false,
            }
        };
        process.Start();
        return await process.StandardOutput.ReadToEndAsync();
    }
}
```

### 2.2 Native Plugin (Python)

```python
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel_pydantic import KernelBaseModel

class K8sPlugin(KernelBaseModel):
    """Kubernetes cluster management plugin."""

    @kernel_function(
        description="Query the running status of a Kubernetes Pod",
        name="get_pod_status",
    )
    def get_pod_status(
        self, namespace: str = "default", pod_name: str = ""
    ) -> str:
        import subprocess
        cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "wide"]
        if pod_name:
            cmd = ["kubectl", "get", "pod", pod_name, "-n", namespace, "-o", "yaml"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.stdout

    @kernel_function(
        description="Get detailed description information for a Pod",
        name="describe_pod",
    )
    def describe_pod(self, namespace: str, pod_name: str) -> str:
        import subprocess
        result = subprocess.run(
            ["kubectl", "describe", "pod", pod_name, "-n", namespace],
            capture_output=True, text=True, timeout=30
        )
        return result.stdout
```

### 2.3 OpenAPI Plugin

```python
# Import plugin from OpenAPI Schema
from semantic_kernel.functions import KernelPluginFromOpenAPI

# Load OpenAPI Spec
plugin = kernel.add_plugin_from_openapi(
    plugin_name="k8s_api",
    openapi_document_path="./k8s-openapi.json",
    execution_settings=sk_openapi.OpenAPIFunctionExecutionParameters(
        enable_payload_namespacing=True,
    ),
)
```

### 2.4 Memory Plugin

```python
from semantic_kernel.memory import SemanticTextMemory

# Configure memory storage
kernel.add_plugin(
    TextMemoryPlugin(
        memory=SemanticTextMemory(
            storage=VolatileMemoryStore(),
            embeddings=AzureTextEmbedding(
                deployment_name="text-embedding-3-small",
                endpoint="https://my-resource.openai.azure.com/",
            ),
        )
    ),
    "memory",
)

# Store knowledge
await kernel.memory.save_information(
    collection="k8s_docs",
    id="doc-001",
    text="Pod OOMKilled is usually caused by container memory usage exceeding the limits configuration",
)

# Semantic search
results = await kernel.memory.search(
    collection="k8s_docs",
    query="insufficient container memory",
    limit=5,
)
```

---
## 3. Planner Automatic Planning

### 3.1 Function Calling Planner (Recommended)

```python
from semantic_kernel.connectors.ai.open_ai import OpenAIPromptExecutionSettings
from semantic_kernel.planners import FunctionCallingStepwisePlanner

# Create Planner
planner = FunctionCallingStepwisePlanner(
    service_id="default",
    max_iterations=10,
)

# Execute planning
result = await planner.invoke(
    kernel=kernel,
    question="Check why the nginx Pod in the default namespace keeps restarting and provide remediation suggestions",
)

print(f"Final answer: {result.final_answer}")
print(f"Steps executed: {len(result.steps)}")
for step in result.steps:
    print(f"  [{step.plugin_name}.{step.function_name}] → {step.output[:100]}")
```

### 3.2 AgentChat (Multi-Agent Collaboration)

```python
from semantic_kernel.agents import (
    ChatCompletionAgent,
    AgentGroupChat,
    AgentTerminationStrategy,
)

# Define Agents
diagnostician = ChatCompletionAgent(
    service_id="default",
    kernel=kernel,
    name="diagnostician",
    instructions="You are a K8s diagnostics expert responsible for analyzing root causes.",
)

fixer = ChatCompletionAgent(
    service_id="default",
    kernel=kernel,
    name="fixer",
    instructions="You are a K8s remediation engineer responsible for executing fix operations.",
)

# Termination strategy
class K8sTerminationStrategy(AgentTerminationStrategy):
    async def should_agent_terminate(self, agent, history):
        return "TERMINATE" in history[-1].content

# Create Agent group chat
group_chat = AgentGroupChat(
    agents=[diagnostician, fixer],
    termination_strategy=K8sTerminationStrategy(),
)

# Execute conversation
result = await group_chat.invoke(
    message="Pod nginx-abc123 encountered CrashLoopBackOff",
)
```

### 3.3 Stepwise Planner (Step-by-Step Planning)

```python
from semantic_kernel.planners import FunctionCallingStepwisePlanner

# Step-by-step planning, each step can be manually reviewed
planner = FunctionCallingStepwisePlanner(
    service_id="default",
    max_iterations=15,
)

# Get planning steps (without executing)
plan = await planner.create_plan(
    kernel=kernel,
    question="Analyze all Pods in Pending state across the cluster and provide scheduling recommendations",
)

# Execute step by step
for step in plan.steps:
    print(f"Executing: {step.plugin_name}.{step.function_name}")
    # Manual approval logic can be added here
    result = await step.invoke(kernel=kernel)
    print(f"Result: {result}")
```

---

## 4. Multi-Language Support

### 4.1 C# / .NET

```csharp
// .NET 8 + Semantic Kernel
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddKernel()
    .AddAzureOpenAIChatCompletion("gpt-4o", endpoint, apiKey)
    .Plugins.AddFromType<K8sPlugin>();

var app = builder.Build();

app.MapPost("/diagnose", async (Kernel kernel, DiagnosisRequest request) =>
{
    var result = await kernel.InvokePromptAsync(
        $"Diagnose the anomaly of {request.PodName} in the {request.Namespace} namespace",
        new KernelArguments
        {
            ["namespace"] = request.Namespace,
            ["pod_name"] = request.PodName,
        }
    );
    return Results.Ok(new { diagnosis = result.ToString() });
});

app.Run();
```

### 4.2 Python

```python
from fastapi import FastAPI
import semantic_kernel as sk

app = FastAPI()

@app.post("/diagnose")
async def diagnose(namespace: str, pod_name: str):
    kernel = sk.Kernel()
    kernel.add_service(AzureChatCompletion(...))
    kernel.add_plugin(K8sPlugin(), "k8s")

    result = await kernel.invoke_prompt(
        f"Diagnose the anomaly of {pod_name} in the {namespace} namespace",
        namespace=namespace,
        pod_name=pod_name,
    )
    return {"diagnosis": str(result)}
```

### 4.3 Java

```java
import com.microsoft.semantickernel.Kernel;
import com.microsoft.semantickernel.aiservices.openai.chatcompletion.OpenAIChatCompletion;

var kernel = Kernel.builder()
    .withAIService(OpenAIChatCompletion.builder()
        .withModelId("gpt-4o")
        .withEndpoint(endpoint)
        .withApiKey(apiKey)
        .build())
    .withPlugin(new K8sPlugin())
    .build();

var result = kernel.invokePromptAsync(
    "Diagnose the anomaly of the nginx Pod in the default namespace"
).block();
```

---

## 5. Azure OpenAI Integration

### 5.1 Connection Configuration

```python
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# Basic configuration
kernel.add_service(
    AzureChatCompletion(
        service_id="default",
        deployment_name="gpt-4o",
        endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_KEY"],
        api_version="2024-08-01-preview",
    )
)

# Using Managed Identity (recommended for production environments)
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
kernel.add_service(
    AzureChatCompletion(
        service_id="default",
        deployment_name="gpt-4o",
        endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        ad_token_provider=credential.get_token(
            "https://cognitiveservices.azure.com/.default"
        ),
    )
)
```

### 5.2 Azure AI Search Integration

```python
from semantic_kernel.connectors.memory.azure import AzureAISearchMemoryStore

# Configure Azure AI Search
kernel.add_plugin(
    TextMemoryPlugin(
        memory=SemanticTextMemory(
            storage=AzureAISearchMemoryStore(
                endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
                api_key=os.environ["AZURE_SEARCH_KEY"],
            ),
            embeddings=AzureTextEmbedding(
                deployment_name="text-embedding-3-small",
            ),
        )
    ),
    "memory",
)
```

---
## 6. Interoperability with AutoGen

### 6.1 SK Agent in AutoGen Group Chat

```python
from autogen import GroupChat, GroupChatManager, AssistantAgent
from semantic_kernel.agents import ChatCompletionAgent

# SK Agent
sk_agent = ChatCompletionAgent(
    service_id="default",
    kernel=kernel,
    name="sk_expert",
    instructions="You are a K8s expert who uses SK plugins to query the cluster.",
)

# AutoGen Agent
autogen_agent = AssistantAgent(
    name="analyst",
    system_message="You are an analysis expert.",
    llm_config=llm_config,
)

# Bridge layer
class SKAutoGenBridge:
    """Wraps an SK Agent as an AutoGen-compatible Agent."""

    def __init__(self, sk_agent: ChatCompletionAgent):
        self.sk_agent = sk_agent

    async def generate_reply(self, messages):
        last_msg = messages[-1]["content"]
        result = await self.sk_agent.invoke(last_msg)
        return str(result[0].content)
```

### 6.2 Unified Orchestration

```python
# Using SK as the tool layer and AutoGen as the conversation layer
class HybridOrchestrator:
    def __init__(self):
        self.kernel = sk.Kernel()
        self.kernel.add_plugin(K8sPlugin(), "k8s")

    async def run(self, task: str):
        # SK executes tool calls
        tool_result = await self.kernel.invoke(
            plugin_name="k8s",
            function_name="get_pod_status",
            namespace="default",
        )

        # AutoGen handles the conversation
        autogen_result = user_proxy.initiate_chat(
            assistant,
            message=f"Analyze the following Pod status:\n{tool_result}\n\nTask: {task}",
            max_turns=5,
        )

        return autogen_result.summary
```

---

## 7. Production Best Practices

### 7.1 Dependency Injection

```csharp
// C# dependency injection
builder.Services.AddSingleton<IK8sService, K8sService>();
builder.Services.AddKernel()
    .AddAzureOpenAIChatCompletion("gpt-4o", endpoint, key)
    .Plugins.AddFromType<K8sPlugin>(sp =>
        new K8sPlugin(sp.GetRequiredService<IK8sService>()));
```

### 7.2 Observability

```python
# OpenTelemetry integration
from opentelemetry import trace
from semantic_kernel.functions import KernelPlugin

# SK built-in tracing
kernel = sk.Kernel()
# Automatically records all function calls
```

### 7.3 Error Handling

```python
from semantic_kernel.exceptions import KernelException

try:
    result = await kernel.invoke(
        plugin_name="k8s",
        function_name="get_pod_status",
    )
except KernelException as e:
    logger.error(f"SK function call failed: {e}")
    # Fallback handling
```

### 7.4 Security Configuration

```yaml
# Azure RBAC
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: sk-agent-reader
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "events"]
    verbs: ["get", "list", "watch"]
```

---

## Related

- [[domain-14-ai-ml-infra/03-agent-runtime/04-autogen-microsoft-agent|Microsoft AutoGen]]
- [[domain-14-ai-ml-infra/03-agent-runtime/07-agent-framework-selection-guide|Agent Framework Selection Decision Tree]]

## See Also

- [[domain-14-ai-ml-infra/03-agent-runtime/01-langchain-langgraph-deep-dive|LangChain/LangGraph Deep Dive Guide]]
- [[domain-14-ai-ml-infra/03-agent-runtime/05-dify-agent-platform|Dify Agent Platform]]


<!-- risk-assessed -->
