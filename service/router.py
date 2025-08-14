from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from src.agentic_bootcamp.tools import TOOLS
from src.agentic_bootcamp.planning import react_loop

router = APIRouter()

class ChatIn(BaseModel):
    message: str

@router.post("/chat")
def chat(in_: ChatIn) -> Dict[str, str]:
    reply = react_loop(in_.message, TOOLS)
    return {"reply": reply}
