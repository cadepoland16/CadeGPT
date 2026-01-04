from fastapi import APIRouter
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import handle_chat

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    return handle_chat(payload)