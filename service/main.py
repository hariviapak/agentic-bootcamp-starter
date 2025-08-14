from fastapi import FastAPI
from .router import router

app = FastAPI(title="Agentic Bootcamp Service")
app.include_router(router)

# Run with: uvicorn service.main:app --reload
