"""A minimal LLM client wrapper.
- Default shows OpenAI-style function calling, but we keep it provider-agnostic.
- For Week 1, we simulate tool-calling by *deciding in Python* rather than relying on the provider to call tools.
"""
from __future__ import annotations
from typing import Any, Dict

class LLMClient:
    def __init__(self, model_name: str, temperature: float = 0.3, api_key: str | None = None):
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = api_key

    def chat(self, messages: list[dict[str, str]]) -> Dict[str, Any]:
        """Placeholder for an LLM chat call.
        Replace with a real provider's SDK call (OpenAI/Groq/Anthropic) later.
        For now, returns a dumb echo with tiny heuristic.
        """
        last = messages[-1]["content"]
        if "weather" in last.lower():
            return {"role": "assistant", "content": "I can check the weather if you give me a city."}
        return {"role": "assistant", "content": f"You said: {last}"}
