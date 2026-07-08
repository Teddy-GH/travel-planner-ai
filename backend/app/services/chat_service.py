from google import genai

from app.config import GOOGLE_API_KEY
from app.storage.memory import chat_memory
from app.providers.gemini_provider import GeminiProvider
from app.services.prompt_service import PromptService
from app.services.memory_service import MemoryService



class ChatService:
    
    def __init__(self):
        self.provider = GeminiProvider()
        self.prompt = PromptService()
        self.memory = MemoryService()
    
    async def stream_chat(self, message: str):
        
        async for chunk in self.provider.stream(message):
            yield chunk
                
        
    
    
        
    async def chat(self, session_id:  str, message: str) -> str:
            history = self.memory.get_history(session_id)
            
            # User history
            self.memory.add_user_message(
                session_id,
                message
            )
        
            
            reply = await self.provider.generate(
                self.prompt
            )
           
        
            self.memory.add_assistant_message(
                session_id,
                message
            )
            
            return reply