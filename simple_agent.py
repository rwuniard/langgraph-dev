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
    input = {"messages": [{"role": "human", "content": "What is the weather in Tokyo?"}]}
    async for chunk in agent.astream(input, stream_mode="values"):
        print(chunk)
        print()
    print()

asyncio.run(stream_agent())