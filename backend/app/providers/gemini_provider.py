from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY
from app.services.prompt_service import PromptService

client = genai.Client(api_key=GOOGLE_API_KEY)


class GeminiProvider:

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key= GOOGLE_API_KEY,
            temperature=0.7,
        )
        
    
    async def generate(self, prompt: str) -> str:
        messages = PromptService.build_prompt()
        
        response = client.models.ainvoke(messages)
        
        return response.content
    
    async def stream(self, prompt: str):
        stream = client.models.generate_content_stream(
            model = "gemini-2.5-flash",
            contents=prompt,
        )
        
        for chunk in stream:
            if chunk.text:
                yield chunk.text