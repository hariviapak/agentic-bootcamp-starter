from __future__ import annotations
from typing import Dict, Any, Tuple, Optional, List
import json

from .llm_client import LLMClient

def _build_tool_manifest(TOOLS: dict) -> list[dict]:
    manifest = []
    for name, spec in TOOLS.items():
        schema = spec["schema"]
        manifest.append({
            "name": name,
            "description": schema.__doc__ or f"Tool {name}",
            "parameters": schema.model_json_schema()
        })
    return manifest

def _keyword_router(user_input: str, TOOLS: dict) -> Optional[str]:
    t = user_input.lower()
    if any(k in t for k in ["calc", "math", "+", "-", "*", "/"]):
        return "math_eval" if "math_eval" in TOOLS else None
    if "weather" in t:
        return "get_weather" if "get_weather" in TOOLS else None
    if "read" in t and ("file" in t or ".txt" in t or ".md" in t or ".log" in t):
        return "read_text_file" if "read_text_file" in TOOLS else None
    return None

def ai_select_tool(user_input: str, TOOLS: dict, client: LLMClient) -> Tuple[Optional[str], Dict[str, Any], float, str]:
    manifest = _build_tool_manifest(TOOLS)
    system = {
        "role": "system",
        "content": (
            "You are a tool router. Read the user's request and pick the BEST tool.\n"
            "Return ONLY a strict JSON object with keys: tool (string|null), args (object), confidence (0..1), thoughts (string).\n"
            "If no suitable tool, set tool=null and confidence=0.\n"
            "Use the provided JSON Schemas for each tool when constructing args."
        )
    }
    tools_desc = json.dumps(manifest, ensure_ascii=False)
    user = {
        "role": "user",
        "content": f"TOOLS: {tools_desc}\n\nUSER REQUEST: {user_input}\nRespond with JSON only."
    }
    resp = client.chat([system, user], json_mode=True)
    content = resp.get("content", "{}")
    try:
        data = json.loads(content)
        tool = data.get("tool")
        args = data.get("args") or {}
        conf = float(data.get("confidence", 0.0))
        thoughts = data.get("thoughts", "")
        if tool and tool in TOOLS:
            schema = TOOLS[tool]["schema"]
            try:
                schema(**args)
            except Exception as e:
                thoughts += f" | arg_validation_error: {e}"
                tool, args, conf = None, {}, 0.0
        else:
            tool = None
        return tool, args, conf, thoughts
    except Exception as e:
        return None, {}, 0.0, f"parse_error: {e}"

def react_loop(user_input: str, TOOLS: dict, client: Optional[LLMClient] = None) -> str:
    if client is None or client.api_key is None:
        print("No client provided")
        tool_name = _keyword_router(user_input, TOOLS)
        if not tool_name:
            if client:
                return client.chat([{"role": "user", "content": user_input}])["content"]
            return f"(stub) You said: {user_input}"
        spec = TOOLS[tool_name]
        args = _naive_arg_parse(tool_name, user_input, spec["schema"])
        return spec["fn"](args)

    tool_name, args, conf, thoughts = ai_select_tool(user_input, TOOLS, client)
    print(tool_name, args, conf, thoughts)
    if not tool_name or conf < 0.35:
        return client.chat([{"role": "user", "content": user_input}])["content"]

    schema = TOOLS[tool_name]["schema"]
    fn = TOOLS[tool_name]["fn"]
    result = fn(schema(**args))

    messages = [
        {"role": "system", "content": "You are an assistant that explains tool results clearly and briefly."},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": f"(took action) tool={tool_name} args={json.dumps(args)}"},
        {"role": "assistant", "content": f"(observation) {result}"},
        {"role": "user", "content": "Summarize the result for me in one short helpful answer."}
    ]
    final = client.chat(messages)
    return final.get("content", str(result))

def _naive_arg_parse(tool_name: str, user_input: str, schema):
    if tool_name == "math_eval":
        return schema(expression=user_input.replace("calc", "").strip())
    if tool_name == "get_weather":
        city = user_input.split("in")[-1].strip() if "in" in user_input else user_input
        return schema(city=city)
    if tool_name == "read_text_file":
        parts = user_input.split()
        path = parts[-1]
        return schema(path=path)
    return schema()
