import os
from supabase import create_client, Client


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Missing SUPABASE_URL and/or SUPABASE_*_KEY in environment (.env)")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def create_conversation() -> str:
    """
    Inserts a new conversation row and returns its UUID string.
    """
    resp = supabase.table("conversations").insert({}).execute()
    # resp.data should be a list like [{"id": "...", ...}]
    return resp.data[0]["id"]


def add_message(
    conversation_id: str,
    role: str,
    content: str,
    model: str | None = None,
    env: str | None = None,
    request_id: str | None = None,
):
    """
    Inserts a message row.
    """
    return (
        supabase.table("messages")
        .insert(
            {
                "conversation_id": conversation_id,
                "role": role,
                "content": content,
                "model": model,
                "env": env,
                "request_id": request_id,
            }
        )
        .execute()
    )


# Backwards-compatible alias (older code imports save_message)
def save_message(
    conversation_id: str,
    role: str,
    content: str,
    model: str | None = None,
    env: str | None = None,
    request_id: str | None = None,
):
    return add_message(
        conversation_id=conversation_id,
        role=role,
        content=content,
        model=model,
        env=env,
        request_id=request_id,
    )


def list_conversations(limit: int = 50):
    """
    Returns conversation rows (newest first).
    """
    resp = (
        supabase.table("conversations")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return resp.data


def get_messages(conversation_id: str, limit: int = 200):
    """
    Returns messages (oldest -> newest) for a conversation.
    """
    resp = (
        supabase.table("messages")
        .select("*")
        .eq("conversation_id", conversation_id)
        .order("created_at", desc=False)
        .limit(limit)
        .execute()
    )
    return resp.data