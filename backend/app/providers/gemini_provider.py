from google import genai
from app.config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)


class GeminiProvider:
    
    async def generate(self, prompt: str) -> str:
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        
        return response.text
    
    async def stream(self, prompt: str):
        stream = client.models.generate_content_stream(
            model = "gemini-2.5-flash",
            contents=prompt,
        )
        
        for chunk in stream:
            if chunk.text:
                yield chunk.text