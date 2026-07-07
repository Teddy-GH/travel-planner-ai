from google import genai

from app.config import GOOGLE_API_KEY
from app.storage.memory import chat_memory

client = genai.Client(api_key=GOOGLE_API_KEY)


class GeminiService:

    def generate(self, prompt: str):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    
class ChatService:
    async def chat(self, session_id:  str, message: str) -> str:
            history = chat_memory[session_id]
            
            history.append(f"User: {message}")
            
            # Temporarly reply
            reply = f"I remember {len(history)} message(s). You said: {message}"
            
            history.append(f"Assistant: {reply}")
            
            return reply