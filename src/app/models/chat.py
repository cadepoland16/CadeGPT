from datetime import datetime
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    """
    Outgoing response from the API for a single chat turn.
    """
    reply: str                 # what the assistant says
    model: str                 # which model/provider generated it (or mock)
    env: str                   # current environment, e.g. "mock", "dev", "prod"
    timestamp: datetime        # when the response was generated (UTC)
    request_id: str            # unique id for this request/response
    conversation_id: str       # id of the Supabase conversation row

class ConversationSummary(BaseModel):
    id: str
    created_at: datetime


class MessageItem(BaseModel):
    id: str
    conversation_id: str
    role: str
    content: str
    model: str | None = None
    env: str | None = None
    request_id: str | None = None
    created_at: datetime