"""Example: Using inspection utilities to understand LangGraph structures."""

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
import asyncio
from inspect_structure import inspect_chunk, inspect_messages

load_dotenv()


@tool
def get_current_weather(city: str) -> str:
    """Get the current weather for a given city."""
    return f"The weather in {city} is sunny."


agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_current_weather],
    debug=False,
    system_prompt="You are a helpful assistant.",
)


async def inspect_stream():
    """Inspect the structure of streaming chunks."""
    input_msg = {"messages": [{"role": "human", "content": "What is the weather in Tokyo?"}]}

    chunk_count = 0
    async for chunk in agent.astream(input_msg, stream_mode="values"):
        chunk_count += 1
        print(f"\n{'#' * 80}")
        print(f"CHUNK {chunk_count}")
        print(f"{'#' * 80}")

        # Option 1: Full inspection
        # inspect_chunk(chunk)

        # Option 2: Just inspect messages (cleaner)
        inspect_messages(chunk)

        # Option 3: Quick type check
        if "messages" in chunk and chunk["messages"]:
            last_msg = chunk["messages"][-1]
            print(f"\nLast message type: {type(last_msg).__name__}")
            print(f"Has 'type' attr: {hasattr(last_msg, 'type')}")
            if hasattr(last_msg, 'type'):
                print(f"Message type value: {last_msg.type}")


if __name__ == "__main__":
    asyncio.run(inspect_stream())
