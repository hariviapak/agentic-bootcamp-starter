"""Week 1 runnable CLI:
- Chat loop that routes to tools when confident, otherwise falls back to LLM echo.
- Replace LLMClient.chat() with a real SDK call when ready.
"""
from __future__ import annotations
from typing import List, Dict
from .config import settings
from .llm_client import LLMClient
from .tools import TOOLS
from .planning import react_loop

BANNER = """
==============================
 Agentic AI Bootcamp — Week 1
==============================
Type 'exit' to quit.
Try:
 - weather in Delhi
 - calc 2+2*5
 - read file ./README.md
"""

def main():
    print(BANNER)
    print(settings.openai_api_key)
    client = LLMClient(model_name=settings.model_name, temperature=settings.temperature, api_key=settings.openai_api_key)
    print(client.model_name)
    history: List[Dict[str, str]] = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        user = input("You: ").strip()
        if user.lower() in {"exit", "quit"}:
            print("Bye!")
            break
        # Try tool-first ReAct stub
        tool_answer = react_loop(user, TOOLS,client=client)
        if "No tool selected" in tool_answer:
            history.append({"role": "user", "content": user})
            resp = client.chat(history)
            print("Agent:", resp["content"])
            history.append({"role": "assistant", "content": resp["content"]})
        else:
            print("Agent (tool):", tool_answer)

if __name__ == "__main__":
    main()
