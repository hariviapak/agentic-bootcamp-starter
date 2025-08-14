from __future__ import annotations
from typing import List, Dict

from .config import settings
from .llm_client import LLMClient
from .tools import TOOLS as BASE_TOOLS
from .planning import react_loop
from .memory.conversation_memory import ConversationMemory
from .memory.vector_store import VectorStore
from .tools.memory_tools import remember_fact, RememberFactInput

TOOLS = dict(BASE_TOOLS)
TOOLS["remember_fact"] = {"fn": remember_fact, "schema": RememberFactInput}

BANNER = """
==============================
 Agentic AI Bootcamp — Week 3
 Memory & Persistence enabled
==============================
Type 'exit' to quit.
Try:
 - remember my GST number is 12345
 - what's my GST number?
 - weather in Delhi
 - calc 2+2*5
"""

def main():
    print(BANNER)
    client = LLMClient(model_name=settings.model_name, temperature=settings.temperature, api_key=settings.openai_api_key)
    convo = ConversationMemory(max_turns=12)
    vectors = VectorStore()

    while True:
        user = input("You: ").strip()
        if user.lower() in {"exit", "quit"}:
            print("Bye!")
            break
        convo.add("user", user)

        reply = react_loop(
            user_input=user,
            TOOLS=TOOLS,
            client=client,
            short_memory=convo.as_list(),
            vector_store=vectors,
        )

        print("Agent:", reply)
        convo.add("assistant", reply)

if __name__ == "__main__":
    main()
