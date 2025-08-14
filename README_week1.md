# Agentic AI Bootcamp — Starter Repo

A clean, extendable starter for learning and building **agentic AI systems** over 4 weeks.
Use it as-is or grow it week-by-week following the included roadmap.

## Quickstart
```bash
# 1) Create a virtual environment (recommended)
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Set your environment
cp .env.example .env
# Edit .env and set OPENAI_API_KEY (or another provider if you swap later)

# 4) Run the Week 1 CLI demo (single/multi-tool agent)
python -m src.agentic_bootcamp.app
```

## What's Inside
- **Week 1:** LLM basics, function/tool calling, structured outputs (this repo runs now).
- **Week 2:** Multi-tool routing & ReAct loop (scaffolded).
- **Week 3:** Memory & Retrieval (Chroma/FAISS hooks provided).
- **Week 4:** Multi-agent orchestration + FastAPI service (skeleton included).

## Notes
- This is provider-agnostic. The default shows OpenAI-style function calling, but you can adapt to any SDK with JSON tool-calling.
- Tool stubs are Python functions with Pydantic schemas for validation.
- Tests: `pytest -q`

## Directory Tree
```
agentic-bootcamp-starter/
├─ README.md
├─ requirements.txt
├─ .env.example
├─ pyproject.toml
├─ Makefile
├─ src/
│  └─ agentic_bootcamp/
│     ├─ app.py
│     ├─ config.py
│     ├─ llm_client.py
│     ├─ planning.py
│     ├─ memory/
│     │  ├─ __init__.py
│     │  └─ vector_store.py
│     ├─ tools/
│     │  ├─ __init__.py
│     │  ├─ math_tool.py
│     │  ├─ weather_tool.py
│     │  └─ file_reader_tool.py
│     └─ web/
│        ├─ __init__.py
│        └─ search_tool.py
├─ service/
│  ├─ main.py
│  └─ router.py
└─ tests/
   └─ test_basic.py
```

## Roadmap Mapping
- **W1**: `src/agentic_bootcamp/app.py`, `tools/*`, `llm_client.py`
- **W2**: `planning.py` (routing + ReAct), `web/search_tool.py`
- **W3**: `memory/vector_store.py` (plug in Chroma/FAISS), hook into app
- **W4**: `service/` FastAPI + Docker (add Dockerfile later)
