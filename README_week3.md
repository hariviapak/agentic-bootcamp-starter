# Week 3 — Memory & Persistence (Upgrade)

This upgrade adds:
- **Short-term memory** (conversation buffer with trimming)
- **Long-term memory** (vector store with simple in-memory fallback)
- A new tool: **remember_fact** to store key facts on demand
- Agent loop now injects relevant memory into prompts and stores new info

## Install
```bash
# in your project root
pip install -r requirements.txt
cp .env.example .env  # if not done already
```

> chromadb is optional in this minimal upgrade (we keep an in-memory vector fallback). 
> You can add Chroma later if you like.

## Files changed / added
- `src/agentic_bootcamp/memory/conversation_memory.py` (NEW)
- `src/agentic_bootcamp/memory/vector_store.py` (UPDATED: simple vector fallback)
- `src/agentic_bootcamp/tools/memory_tools.py` (NEW: remember_fact tool)
- `src/agentic_bootcamp/planning.py` (UPDATED: memory-aware loop, backwards compatible)
- `src/agentic_bootcamp/app.py` (UPDATED: wires memory into the loop)

## Run
```bash
python -m src.agentic_bootcamp.app
```
Try:
- "remember my GST number is 12345"
- "what's my GST number?"
- "I live in Mohali. remember this."
- "what did I tell you about where I live?"

## How it works
- Short-term: last N turns are kept and trimmed.
- Long-term: we index short text facts; retrieval grabs the top-k to insert into the LLM context.
- The loop uses memory first, then tools, then general LLM responses.
