from __future__ import annotations
from typing import Any, Dict, List, Optional
import json

class LLMClient:
    """
    LLM client with graceful fallback:
    - If OPENAI_API_KEY is set and 'openai' is installed, use OpenAI Chat Completions.
    - Else, fall back to a stub that returns simple echoes.
    Supports JSON responses via response_format={"type":"json_object"} when requested.
    """
    def __init__(self, model_name: str, temperature: float = 0.3, api_key: Optional[str] = None):
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = api_key
        self._client = None
        print("api_key", api_key)
        if api_key:
            try:
                from openai import OpenAI
                self._client = OpenAI(api_key=api_key)
            except Exception:
                self._client = None  # fallback to stub

    def _call_openai(self, messages: List[Dict[str, str]], json_mode: bool = False) -> Dict[str, Any]:
        if not self._client:
            return {"role": "assistant", "content": self._stub(messages, json_mode=json_mode)}

        kwargs = dict(
            model=self.model_name,
            messages=messages,
            temperature=self.temperature,
        )
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}

        resp = self._client.chat.completions.create(**kwargs)
        msg = resp.choices[0].message
        content = msg.content or ""
        return {"role": "assistant", "content": content}

    def _stub(self, messages: List[Dict[str, str]], json_mode: bool = False) -> str:
        last = messages[-1]["content"]
        if json_mode:
            return json.dumps({"tool": None, "args": {}, "confidence": 0.0, "thoughts": "stub: no API key"})
        if "weather" in last.lower():
            return "I can check the weather if you give me a city."
        return f"You said: {last}"

    def chat(self, messages: List[Dict[str, str]], json_mode: bool = False) -> Dict[str, Any]:
        if self._client:
            return self._call_openai(messages, json_mode=json_mode)
        return {"role": "assistant", "content": self._stub(messages, json_mode=json_mode)}
