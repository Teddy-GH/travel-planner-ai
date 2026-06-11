from openai import OpenAI

from app.core.config import settings
from app.storage.memory import (
    get_history,
    add_message,
)

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

class ChatService:
    
    def chat(
        self,
        session_id: str,
        message: str
    ) -> str:
        
        add_message(
            session_id,
            "user",
            message
        )
        
        history = get_history(session_id)
        
        messages = [
            {
                "role": "system",
                "content":(
                    "You are a professional "
                    "travel planning assistant."
                )
            }
        ]
        
        messages.extend(history)
        
        response = client.responses.create(
            model=settings.MODEL_NAME,
            input=messages
        )
        
        answer = response.output_text
        
        add_message(
            session_id,
            "assistant",
            answer
        )
        
        return answer