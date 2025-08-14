from pydantic import BaseModel, Field
from pathlib import Path

class FileReadInput(BaseModel):
    path: str = Field(..., description="Path to a local text file")

def read_text_file(x: FileReadInput) -> str:
    p = Path(x.path)
    if not p.exists():
        return f"File not found: {x.path}"
    if p.suffix not in {".txt", ".md", ".log"}:
        return f"Unsupported file type: {p.suffix}"
    return p.read_text(encoding="utf-8")[:4000]
