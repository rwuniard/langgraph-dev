"""Quick one-liner inspection methods for LangGraph objects."""

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
import asyncio
from pprint import pprint
import json

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


async def quick_inspection_methods():
    """Demonstrate quick inspection one-liners."""
    input_msg = {"messages": [{"role": "human", "content": "What is the weather in Tokyo?"}]}

    async for chunk in agent.astream(input_msg, stream_mode="values"):
        if "messages" in chunk and chunk["messages"]:
            last_msg = chunk["messages"][-1]

            # ============================================================
            # METHOD 1: pprint (Pretty Print) - Most Readable
            # ============================================================
            print("\n" + "=" * 80)
            print("METHOD 1: pprint - Best for quick inspection")
            print("=" * 80)
            pprint(vars(last_msg), width=120, depth=2)

            # ============================================================
            # METHOD 2: dir() - See all available attributes/methods
            # ============================================================
            print("\n" + "=" * 80)
            print("METHOD 2: dir() - See what you can access")
            print("=" * 80)
            print("Attributes:", [x for x in dir(last_msg) if not x.startswith('_')])

            # ============================================================
            # METHOD 3: vars() or __dict__ - Object attributes as dict
            # ============================================================
            print("\n" + "=" * 80)
            print("METHOD 3: vars() - Raw attribute dictionary")
            print("=" * 80)
            print("Keys:", list(vars(last_msg).keys()))

            # ============================================================
            # METHOD 4: type() - Understand what you're dealing with
            # ============================================================
            print("\n" + "=" * 80)
            print("METHOD 4: type() - Identify the object class")
            print("=" * 80)
            print(f"Type: {type(last_msg)}")
            print(f"Type name: {type(last_msg).__name__}")
            print(f"Module: {type(last_msg).__module__}")

            # ============================================================
            # METHOD 5: JSON dump (for LangChain messages)
            # ============================================================
            print("\n" + "=" * 80)
            print("METHOD 5: JSON serialization")
            print("=" * 80)
            # LangChain messages often have .dict() or model_dump() methods
            if hasattr(last_msg, 'model_dump'):
                print(json.dumps(last_msg.model_dump(), indent=2, default=str))
            elif hasattr(last_msg, 'dict'):
                print(json.dumps(last_msg.dict(), indent=2, default=str))

            # ============================================================
            # METHOD 6: Custom format - Just what you need
            # ============================================================
            print("\n" + "=" * 80)
            print("METHOD 6: Custom inspection - Only relevant fields")
            print("=" * 80)
            info = {
                "class": type(last_msg).__name__,
                "type": getattr(last_msg, 'type', None),
                "content": getattr(last_msg, 'content', None),
                "has_tool_calls": hasattr(last_msg, 'tool_calls') and bool(last_msg.tool_calls),
            }
            pprint(info)

            # Only inspect first chunk to avoid clutter
            break


if __name__ == "__main__":
    print("""
================================================================================
QUICK INSPECTION METHODS FOR LANGGRAPH OBJECTS
================================================================================

This script demonstrates 6 different ways to inspect object structures:

1. pprint(vars(obj))           - Pretty printed attributes (MOST USEFUL)
2. dir(obj)                    - All available attributes and methods
3. vars(obj) or obj.__dict__   - Raw attribute dictionary
4. type(obj)                   - Object class information
5. obj.model_dump() or .dict() - JSON serialization (for Pydantic models)
6. Custom format               - Extract only what you need

Press Enter to run...
""")
    input()
    asyncio.run(quick_inspection_methods())
