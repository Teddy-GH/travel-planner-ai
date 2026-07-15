from app.providers.gemini_provider import GeminiProvider
from app.services.prompt_service import PromptService
from app.services.memory_service import MemoryService
from langchain_core.messages import(
    HumanMessage,
    AIMessage
)



class ChatService:
    
    def __init__(self):
        self.provider = GeminiProvider()
        self.prompt = PromptService()
        self.memory = MemoryService()
    
    async def stream_chat(self, message: str):
        
        async for chunk in self.provider.stream(message):
            yield chunk
                
        
    
        
    async def chat(self, session_id:  str, message: str) -> str:
            
            # User history
            self.memory.add_message(
                session_id,
                HumanMessage(content=message),
            )
            # store history after user conversation
            history = self.memory.get_history(session_id)
        
            
            prompt = await self.provider.generate(
                self.prompt.build_prompt(history)
            )
            
            reply = await self.provider.generate(prompt)
        
            self.memory.add_message(
                session_id,
                AIMessage(content=reply),
            )
            
            return reply