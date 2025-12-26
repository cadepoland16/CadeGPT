from datetime import datetime
import uuid

from app.config import APP_ENV, LLM_PROVIDER, OLLAMA_MODEL
from app.models.chat import ChatRequest, ChatResponse
from app.services.llm import simple_chat
from app.services.db import create_conversation, save_message


def handle_chat(request: ChatRequest) -> ChatResponse:
    # 1) Conversation + ids
    conversation_id = create_conversation()
    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow()

    # 2) Save user message
    save_message(
        conversation_id=conversation_id,
        role="user",
        content=request.message,
        model=None,
        env=APP_ENV,
        request_id=request_id,
    )

    # 3) Get reply from LLM layer
    reply_text = simple_chat(request.message)

    # 4) Model label
    provider = (LLM_PROVIDER or "mock").lower()
    if APP_ENV == "mock" or provider == "mock":
        model_name = "mock-model"
    elif provider == "ollama":
        model_name = f"ollama:{OLLAMA_MODEL}"
    elif provider == "openai":
        model_name = "gpt-4o-mini"
    else:
        model_name = f"unknown-provider:{provider}"

    # 5) Save assistant message
    save_message(
        conversation_id=conversation_id,
        role="assistant",
        content=reply_text,
        model=model_name,
        env=APP_ENV,
        request_id=request_id,
    )

    # 6) Return response
    return ChatResponse(
        reply=reply_text,
        model=model_name,
        env=APP_ENV,
        timestamp=timestamp,
        request_id=request_id,
        conversation_id=conversation_id,
    )