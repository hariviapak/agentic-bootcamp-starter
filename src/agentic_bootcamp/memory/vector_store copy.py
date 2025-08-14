from __future__ import annotations
from typing import List, Dict, Tuple
import math

class VectorStore:
    """Minimal, dependency-free vector store.
    Uses a simple bag-of-words vector to illustrate retrieval. Replace with Chroma/FAISS later.
    """
    def __init__(self):
        self._docs: List[Dict] = []  # each: {text, metadata, _vec}

    def _embed(self, text: str) -> Dict[str, int]:
        vec: Dict[str, int] = {}
        for tok in text.lower().split():
            vec[tok] = vec.get(tok, 0) + 1
        return vec

    def _cosine(self, a: Dict[str, int], b: Dict[str, int]) -> float:
        dot = sum(va * b.get(k, 0) for k, va in a.items())
        na = math.sqrt(sum(v*v for v in a.values()))
        nb = math.sqrt(sum(v*v for v in b.values()))
        if na == 0 or nb == 0:
            return 0.0
        return dot / (na * nb)

    def add(self, text: str, metadata: Dict | None = None):
        item = {"text": text, "metadata": metadata or {}}
        item["_vec"] = self._embed(text)
        self._docs.append(item)

    def search(self, query: str, k: int = 3) -> List[Dict]:
        if not self._docs:
            return []
        qv = self._embed(query)
        scored = [(self._cosine(qv, d["_vec"]), d) for d in self._docs]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [d for _, d in scored[:k]]
