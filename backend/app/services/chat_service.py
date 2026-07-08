from google import genai

from app.config import GOOGLE_API_KEY
from app.storage.memory import chat_memory
from app.providers.gemini_provider import GeminiProvider



class ChatService:
    
    def __init__(self):
        self.provider = GeminiProvider()
    
    async def stream_chat(self, message: str):
        
        async for chunk in self.provider.stream(message):
            yield chunk
                
        
    
    def build_prompt(
        self,
        history,
    ):
        conversation = ""
        
        for item in history:
            
            conversation += (
                f"{item['role']}: "
                f"{item['content']}\n"
            )    
        return conversation
        
    async def chat(self, session_id:  str, message: str) -> str:
            history = chat_memory[session_id]
            # User history
            history.append({
                "role": "user",
                "content": message
            })
            
            SYSTEM_PROMPT = """
            You are an expert travel planner.add()
            
            Always:
            
            - Recommend destinations.
            - Estimate costs.
            - Suggest hotels.
            - Give daily itinerary.
            
            
            
            Keep answers concise.
            """
            conversation = self.build_prompt(history)
            
            prompt = f"""
            {SYSTEM_PROMPT}
            
            Conversation:
            
            {conversation}
            
            """
            
            
            
            reply = await self.provider.generate(
                prompt
            )
           
            
            history.append(
               {
                   "role": "assistant",
                   "content": reply
               }
            )
            
            return reply