from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY
from app.services.prompt_service import PromptService
from langchain_core.output_parsers import StrOutputParser

client = genai.Client(api_key=GOOGLE_API_KEY)


class GeminiProvider:

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key= GOOGLE_API_KEY,
            temperature=0.7,
        )

        self.parser = StrOutputParser()

        self.chain = self.model | self.parser
        
    
    async def generate(self, prompt: str) -> str:
        """pass prompt to langchain parse it respond"""
        messages = PromptService.build_prompt()
        
        return await self.chain.ainvoke(messages)
    


    async def stream(self, messages):
        
        for chunk in self.chain.astream(messages):
                yield chunk.text