
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.services.tool_service import get_tools
from app.storage.memory import chat_memory

router = APIRouter(prefix="/api", tags=["Chat"])

service = ChatService()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    
   return StreamingResponse(
       service.stream_chat(request.message),
       media_type="text/plain"
   )

@router.get("/memory/{session_id}")
async def memory(session_id: str):
    return chat_memory.get(session_id, []) 

@router.get("/tool")
async def tool():
    data = await get_tools() 
    return data