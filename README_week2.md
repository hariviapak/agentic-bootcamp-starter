# Week 2 — Multi-Tool Agents & AI Routing (Upgrade)

This upgrade lets an LLM **choose the right tool and fill arguments** from natural language.
It falls back to the plain LLM answer if confidence is low or no tool fits.

## Install
```bash
# in your project root
pip install -r requirements.txt
cp .env.example .env
# set OPENAI_API_KEY=sk-...
```

## Run
```bash
python -m src.agentic_bootcamp.app
```
Now the router is **AI-powered**. Try:
- "convert 10 km to miles"
- "what's the weather in Delhi?"
- "read file ./README.md"
- "calculate 12*(4+5)"

## Notes
- If `OPENAI_API_KEY` is missing, the app falls back to a **keyword router** and stub LLM.
- Tool schemas are validated via Pydantic. If the LLM proposes bad args, we reject and ask it again.
- The loop uses a mini **ReAct**: select tool → run → provide observation → ask LLM to draft the final answer.
