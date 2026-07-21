from app.providers.gemini_provider import GeminiProvider
from app.services.prompt_service import PromptService
from app.services.memory_service import MemoryService
from langchain_core.messages import(
    HumanMessage,
    AIMessage
)

from app.tools import tool_registry
from app.tools.router import ToolRouter



class ChatService:
    
    def __init__(self):
        self.provider = GeminiProvider()
        self.prompt = PromptService()
        self.memory = MemoryService()
        self.tool_router = ToolRouter()
        

    
    async def stream_chat(self, message: str):
        
        async for chunk in self.provider.stream(message):
            yield chunk
                
        
    
        
    async def chat(self, session_id:  str, message: str) -> str:
            
            # Save user message
            self.memory.add_message(
                session_id,
                HumanMessage(content=message),
            )
            
            # store history after user conversation
            history = self.memory.get_history(session_id)
        
            # route to matching tool
            tool = self.tool_router.route(message)
            
            # Build prompt
            if tool:
                
                parameters = self.extractor.extract(
                    tool,
                    message,
                )
                
                print(parameters)
                
                tool_result = await tool.execute(
                    **parameters
                )
            
                prompt = await self.prompt.build_prompt(
                    history=history,
                    user_input=message,
                    tool_result=tool_result,
                    
                )
            
            else:
              
                prompt = self.prompt.build_prompt(
                        history=history,
                        user_input=message
                    )
            
            #  Generate AI response
            reply = await self.provider.generate(prompt)
            
           #  Save assistant reply
            self.memory.add_message(
                session_id,
                AIMessage(content=reply),
            )
            
            return reply
        
        
      


    async def get_tools():
        tool = tool_registry.get("weather")

        result = await tool.execute(
            city="Dubai"
        )

        print(result)