from collections import defaultdict

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    BaseMessage
)

class MemoryService:
    
    def __init__(self):
        self.memory: dict[str, list[BaseMessage]] = defaultdict(list)
    
    def get_history(self, session_id: str) -> list[BaseMessage]:
        return self.memory[session_id]
    

    def add_message(
        self,
        session_id: str,
        message: str,
    ):
        self.memory[session_id].append(message)      
            