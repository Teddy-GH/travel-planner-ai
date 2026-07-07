
from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/api", tags=["Chat"])

service = ChatService()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    
    reply = await service.chat(
        request.session_id,
        request.message,
    )
    
    return ChatResponse(
        session_id = request.session_id,
        reply=reply
    )