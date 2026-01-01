from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import handle_chat
from typing import List
from fastapi import APIRouter
from app.models.chat import ConversationSummary, MessageItem
from app.services.db import list_conversations, get_messages


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    """
    HTTP endpoint that delegates to the chat service.
    Keeps the route thin and reusable for other interfaces.
    """
    return handle_chat(payload)

@router.get("/api/conversations", response_model=List[ConversationSummary])
def api_list_conversations():
    return list_conversations(limit=30)

@router.get("/api/conversations/{conversation_id}/messages", response_model=List[MessageItem])
def api_get_conversation_messages(conversation_id: str):
    return get_messages(conversation_id, limit=300)