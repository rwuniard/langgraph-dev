# LangGraph Development

A development environment for building and testing LangGraph AI agents with LangChain integration.

## Overview

This project provides a foundation for developing AI agents using LangGraph and LangChain. It includes examples of agent creation, tool integration, and streaming responses.

## Features

- **Agent Creation**: Build AI agents with custom tools and system prompts
- **Tool Integration**: Define and integrate custom tools using LangChain's `@tool` decorator
- **Streaming Support**: Asynchronous streaming of agent responses
- **OpenAI Integration**: Powered by OpenAI models (GPT-4o-mini)
- **LangGraph Studio**: Visual debugging and interaction with agent graphs
- **Inspection Utilities**: Built-in tools to inspect and understand LangGraph object structures

## Prerequisites

- Python 3.12 or higher
- OpenAI API key

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. Clone the repository:
```bash
git clone <repository-url>
cd langgraph-dev
```

2. Install dependencies:
```bash
# Note: Use quotes around "langgraph-cli[inmem]" for zsh shell compatibility
uv add "langgraph-cli[inmem]" langchain langchain-openai
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Configuration

Create a `.env` file in the project root with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the Simple Agent

The project includes a simple weather agent example in [simple_agent.py](simple_agent.py):

```bash
uv run python simple_agent.py
```

This example demonstrates:
- Creating an agent with the `create_agent` function
- Defining a custom tool (`get_current_weather`)
- Streaming agent responses asynchronously

### Using LangGraph Studio

LangGraph Studio provides a visual interface to interact with and debug your agents.

1. Generate the `langgraph.json` configuration file (required for LangGraph Studio)

2. Activate the virtual environment:
```bash
source .venv/bin/activate
```

3. Start LangGraph development server:
```bash
langgraph dev
```

4. The command will:
   - Launch your default browser automatically
   - Connect to your local network
   - Allow the web application to communicate with your Python environment

5. In LangGraph Studio, you can:
   - Visualize your agent's graph structure
   - Interact with the agent in real-time
   - Debug and understand the execution flow
   - Step through agent decision-making processes

### Debugging and Inspection

The project includes utilities to inspect LangGraph object structures for easier debugging.

#### Using Pretty Print

LangChain messages have a built-in `pretty_print()` method for clean output:

```python
async for chunk in agent.astream(input, stream_mode="values"):
    if "messages" in chunk and chunk["messages"]:
        last_message = chunk["messages"][-1]
        last_message.pretty_print()  # Clean, formatted output
```

#### Inspection Tools

The `inspector_tools/` directory contains utilities for detailed object inspection:

**Quick Inspection** - See all available inspection methods:
```bash
uv run python inspector_tools/quick_inspect.py
```

**Detailed Example** - Inspect streaming chunks in real-time:
```bash
uv run python inspector_tools/inspect_example.py
```

**Using Utilities in Your Code**:
```python
from inspector_tools.inspect_structure import inspect_chunk, inspect_messages
from pprint import pprint

# Inspect full chunk structure
inspect_chunk(chunk)

# Inspect just messages
inspect_messages(chunk)

# Quick inspection with pprint
pprint(vars(message), depth=2, width=120)
```

**Available Inspection Methods**:
1. `inspect_chunk(chunk)` - Full chunk structure with type information
2. `inspect_messages(chunk)` - Detailed message array inspection
3. `to_json_serializable(chunk)` - Convert to JSON for file export
4. `pprint(vars(obj))` - Quick pretty-printed attribute view

### Example Output

```
What is the weather in Tokyo?
The weather in Tokyo is sunny.
```

## Project Structure

```
langgraph-dev/
├── simple_agent.py              # Example agent implementation
├── inspector_tools/             # Debugging and inspection utilities
│   ├── inspect_structure.py     # Reusable inspection functions
│   ├── inspect_example.py       # Working example with agent
│   └── quick_inspect.py         # Quick inspection methods demo
├── pyproject.toml               # Project configuration and dependencies
├── uv.lock                      # Locked dependencies
├── langgraph.json               # LangGraph Studio configuration
├── .env                         # Environment variables (not tracked)
├── .python-version              # Python version specification
└── README.md                    # This file
```

## Dependencies

- **langchain** (>=1.0.4): Core LangChain framework
- **langchain-openai** (>=1.0.2): OpenAI integration for LangChain
- **langgraph-cli[inmem]** (>=0.4.7): LangGraph CLI with in-memory support

## Development

### Creating Custom Tools

Define custom tools using the `@tool` decorator:

```python
from langchain.tools import tool

@tool
def your_custom_tool(param: str) -> str:
    """Tool description for the agent.

    Args:
        param: Parameter description.

    Returns:
        Result description.
    """
    # Your tool implementation
    return "result"
```

### Creating Agents

Use the `create_agent` function to build agents:

```python
from langchain.agents import create_agent

agent = create_agent(
    model="gpt-4o-mini",
    tools=[your_custom_tool],
    debug=False,
    system_prompt="Your system prompt here"
)
```

### Streaming Responses

Implement asynchronous streaming for real-time responses:

```python
async def stream_agent():
    """Stream agent responses with clean formatting."""
    input = {"messages": [{"role": "human", "content": "Your query"}]}
    async for chunk in agent.astream(input, stream_mode="values"):
        if "messages" in chunk and chunk["messages"]:
            last_message = chunk["messages"][-1]
            # Use built-in pretty_print() for clean output
            if hasattr(last_message, "type") and last_message.type == "ai":
                if last_message.content:
                    last_message.pretty_print()
```

**Token-by-Token Streaming** (for real-time typing effect):

```python
async def stream_tokens():
    """Stream AI response token by token."""
    input = {"messages": [{"role": "human", "content": "Your query"}]}
    async for message_chunk, metadata in agent.astream(input, stream_mode="messages"):
        if message_chunk.content:
            print(message_chunk.content, end="", flush=True)
    print()
```

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
