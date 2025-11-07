"""Utility functions to inspect LangGraph object structures."""

from pprint import pprint
import json
from typing import Any


def inspect_chunk(chunk: Any, show_methods: bool = False):
    """Inspect the structure of a LangGraph chunk.

    Args:
        chunk: The chunk object to inspect
        show_methods: If True, also show available methods
    """
    print("=" * 80)
    print("CHUNK TYPE:", type(chunk))
    print("=" * 80)

    # If it's a dict, pretty print it
    if isinstance(chunk, dict):
        print("\nDICTIONARY KEYS:")
        pprint(list(chunk.keys()))

        print("\nFULL STRUCTURE:")
        pprint(chunk, depth=3, width=120)
    else:
        # For objects, show attributes
        print("\nOBJECT ATTRIBUTES:")
        attrs = {k: v for k, v in vars(chunk).items() if not k.startswith('_')}
        pprint(attrs, depth=3, width=120)

        if show_methods:
            print("\nAVAILABLE METHODS:")
            methods = [m for m in dir(chunk) if not m.startswith('_') and callable(getattr(chunk, m))]
            pprint(methods)

    print("=" * 80)


def inspect_messages(chunk: dict):
    """Inspect the messages array in a chunk."""
    if "messages" not in chunk:
        print("No messages in chunk")
        return

    messages = chunk["messages"]
    print(f"\nFOUND {len(messages)} MESSAGES:")
    print("=" * 80)

    for i, msg in enumerate(messages):
        print(f"\n[{i}] Message Type: {type(msg).__name__}")

        # Show key attributes
        if hasattr(msg, "type"):
            print(f"    type: {msg.type}")
        if hasattr(msg, "content"):
            content = str(msg.content)[:100]  # Truncate long content
            print(f"    content: {content}...")
        if hasattr(msg, "name"):
            print(f"    name: {msg.name}")
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"    tool_calls: {len(msg.tool_calls)} calls")

        # Show all non-private attributes
        print(f"    All attributes: {[k for k in vars(msg).keys() if not k.startswith('_')]}")

    print("=" * 80)


def to_json_serializable(chunk: Any) -> dict:
    """Convert chunk to JSON-serializable dict for inspection.

    Useful for saving to file or detailed inspection.
    """
    if isinstance(chunk, dict):
        result = {}
        for key, value in chunk.items():
            if key == "messages":
                # Convert messages to dicts
                result[key] = [
                    {
                        "type": type(msg).__name__,
                        "attributes": {k: str(v)[:200] for k, v in vars(msg).items() if not k.startswith('_')}
                    }
                    for msg in value
                ]
            else:
                result[key] = str(value)[:200]  # Truncate long values
        return result
    else:
        return {
            "type": type(chunk).__name__,
            "attributes": {k: str(v)[:200] for k, v in vars(chunk).items() if not k.startswith('_')}
        }


# Example usage
if __name__ == "__main__":
    print("""
Usage examples:

1. Inspect full chunk structure:
   inspect_chunk(chunk)

2. Inspect just the messages:
   inspect_messages(chunk)

3. Show available methods:
   inspect_chunk(chunk, show_methods=True)

4. Save to JSON file:
   data = to_json_serializable(chunk)
   with open('chunk_structure.json', 'w') as f:
       json.dump(data, f, indent=2)
""")
