from __future__ import annotations
from typing import List, Dict

class ConversationMemory:
    """A simple short-term memory buffer with a max token-ish length by message count."""
    def __init__(self, max_turns: int = 12):
        self.max_turns = max_turns
        self.messages: List[Dict[str, str]] = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        self._trim()

    def _trim(self):
        max_msgs = max(2, self.max_turns * 2)
        if len(self.messages) > max_msgs:
            self.messages = self.messages[-max_msgs:]

    def as_list(self) -> List[Dict[str, str]]:
        return list(self.messages)
