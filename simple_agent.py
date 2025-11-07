from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
import asyncio


load_dotenv()


@tool
def get_current_weather(city: str) -> str:
    """Get the current weather for a given city.
    Args:
        city: The city to get the weather for.
    Returns:
        The current weather for the city.
    """
    return f"The weather in {city} is sunny."

agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_current_weather],
    debug=False,
    system_prompt="You are a helpful assistant that can answer questions and help with tasks.",
)


async def stream_agent():
    """Stream agent responses using pretty_print() for clean formatting."""
    input = {"messages": [{"role": "human", "content": "What is the weather in Tokyo?"}]}
    async for chunk in agent.astream(input, stream_mode="values"):
        chunk.pretty_print()
        print("*" * 100)
        if "messages" in chunk and chunk["messages"]:
            last_message = chunk["messages"][-1]
            # Use built-in pretty_print() method for clean output
            if hasattr(last_message, "type") and last_message.type == "ai":
                if last_message.content:
                    last_message.pretty_print()
    print()

asyncio.run(stream_agent())