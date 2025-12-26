from __future__ import annotations

from typing import Optional

from supabase import Client, create_client

from app.config import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY

_supabase: Optional[Client] = None


def get_supabase() -> Client:
    global _supabase
    if _supabase is None:
        if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
            raise RuntimeError(
                "Supabase env vars missing. Check SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY."
            )
        _supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    return _supabase


def create_conversation() -> str:
    sb = get_supabase()
    result = sb.table("conversations").insert({}).execute()
    return result.data[0]["id"]


def save_message(
    conversation_id: str,
    role: str,
    content: str,
    model: Optional[str] = None,
    env: Optional[str] = None,
    request_id: Optional[str] = None,
) -> None:
    sb = get_supabase()
    sb.table("messages").insert(
        {
            "conversation_id": conversation_id,
            "role": role,
            "content": content,
            "model": model,
            "env": env,
            "request_id": request_id,
        }
    ).execute()