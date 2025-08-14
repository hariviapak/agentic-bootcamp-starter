"""Week 2+: simple router + ReAct-ish loop scaffolding.
Fill in prompt templates and connect to your LLM provider.
"""
from __future__ import annotations
from typing import Callable, Dict, Any
from pydantic import BaseModel

class ToolSpec(BaseModel):
    name: str
    schema: type[BaseModel]
    fn: Callable[[BaseModel], str]

def simple_router(user_input: str, tools: dict[str, dict]) -> str | None:
    t = user_input.lower()
    if any(k in t for k in ["calc", "math", "+", "-", "*", "/"]):
        return "math_eval"
    if "weather" in t:
        return "get_weather"
    if "read" in t and ("file" in t or ".txt" in t or ".md" in t):
        return "read_text_file"
    if "convert" in t:
        return "unit_converter"
    return None

def react_loop(user_input: str, tools: dict[str, dict]) -> str:
    tool_name = simple_router(user_input, tools)
    if not tool_name:
        return "No tool selected. Replying with plain LLM answer."
    spec = tools[tool_name]
    schema = spec["schema"]
    fn = spec["fn"]
    # naive arg extraction for Week 1/2; replace with JSON-structured calls later
    if tool_name == "math_eval":
        args = schema(expression=user_input.replace("calc", "").strip())
    elif tool_name == "get_weather":
        # Expect: "weather in City"
        city = user_input.split("in")[-1].strip() if "in" in user_input else user_input
        args = schema(city=city)
    elif tool_name == "unit_converter":
        # Expect: "convert 100 km to miles"
        parts = user_input.split()
        value = float(parts[1])
        from_unit = parts[2]
        to_unit = parts[4]
        args = schema(value=value, from_unit=from_unit, to_unit=to_unit)
    elif tool_name == "read_text_file":
        # Expect: "read file path/to/file.txt"
        parts = user_input.split()
        path = parts[-1]
        args = schema(path=path)
    else:
        return "Tool routing matched but arg parsing not implemented."
    return fn(args)
