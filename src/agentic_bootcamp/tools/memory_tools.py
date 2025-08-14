from pydantic import BaseModel, Field
from typing import Optional

class RememberFactInput(BaseModel):
    """Store a short, self-contained fact in long-term memory."""
    fact: str = Field(..., description="A concise fact, e.g., 'My GST number is 12345'.")
    namespace: Optional[str] = Field(default="default", description="Optional namespace group.")

def remember_fact(x: RememberFactInput, vector_store) -> str:
    vector_store.add(x.fact, metadata={"namespace": x.namespace})
    return f"Saved: {x.fact}"
