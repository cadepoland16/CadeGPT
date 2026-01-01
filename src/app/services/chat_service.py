from datetime import datetime
import uuid

from app.config import APP_ENV
from app.models.chat import ChatRequest, ChatResponse
from app.services.llm import simple_chat
from app.services.db import create_conversation, add_message


def handle_chat(request: ChatRequest) -> ChatResponse:
    # 1) Use existing conversation if provided, else create one
    conversation_id = request.conversation_id or create_conversation()

    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow()

    # 2) Save user message
    add_message(
        conversation_id=conversation_id,
        role="user",
        content=request.message,
        model=None,
        env=APP_ENV,
        request_id=request_id,
    )

    # 3) Get model response
    reply_text, model_used = simple_chat(request.message)

    # 4) Save assistant message
    add_message(
        conversation_id=conversation_id,
        role="assistant",
        content=reply_text,
        model=model_used,
        env=APP_ENV,
        request_id=request_id,
    )

    # 5) Return structured API response
    return ChatResponse(
        reply=reply_text,
        model=model_used,
        env=APP_ENV,
        timestamp=timestamp,
        request_id=request_id,
        conversation_id=conversation_id,
    )