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

### Example Output

```
What is the weather in Tokyo?
The weather in Tokyo is sunny.
```

## Project Structure

```
langgraph-dev/
├── simple_agent.py       # Example agent implementation
├── pyproject.toml        # Project configuration and dependencies
├── uv.lock              # Locked dependencies
├── langgraph.json       # LangGraph Studio configuration
├── .env                 # Environment variables (not tracked)
├── .python-version      # Python version specification
└── README.md           # This file
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
    input = {"messages": [{"role": "human", "content": "Your query"}]}
    async for chunk in agent.astream(input, stream_mode="values"):
        print(chunk)
```

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
