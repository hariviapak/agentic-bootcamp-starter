"""Week 3+: glue layer for a vector DB (Chroma/FAISS/Pinecone).
This module exposes a tiny interface you can keep regardless of the backend.
"""
from typing import List, Dict

class VectorStore:
    def __init__(self):
        self._docs: List[Dict] = []

    def add(self, text: str, metadata: Dict | None = None):
        self._docs.append({"text": text, "metadata": metadata or {}})

    def search(self, query: str, k: int = 3) -> list[Dict]:
        # Dummy: return most recent k. Replace with real vector similarity.
        return self._docs[-k:][::-1]
