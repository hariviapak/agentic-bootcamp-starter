from pydantic import BaseModel, Field

class WebSearchInput(BaseModel):
    query: str = Field(..., description="Web query")

def web_search(x: WebSearchInput) -> str:
    # Stub. Replace with a real web.run or search API in your environment.
    return f"[stub] Would search the web for: {x.query}"
