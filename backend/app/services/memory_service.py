from collections import defaultdict

class MemoryService:
    
    def __init__(self):
        self.memory = defaultdict(list)
    
    def get_history(self, session_id: str):
        return self.memory[session_id]
    
    def add_user_message(
        self,
        session_id: str,
        message: str
    ): 
        self.memory[session_id].append({
            "role": "user",
            "content": message
        }) 
        
    def add_assistant_message(
        self, 
        session_id: str, 
        message: str,
        ):
          self.memory[session_id].append({
              "role": "assistant",
              "content": message
          })
            