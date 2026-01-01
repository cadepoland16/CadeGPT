from typing import Optional, Tuple

import requests
from openai import OpenAI

from app.config import (
    APP_ENV,
    OPENAI_API_KEY,
    LLM_PROVIDER,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)

# Lazily created OpenAI client
_openai_client: Optional[OpenAI] = None


def _get_openai_client() -> OpenAI:
    global _openai_client

    if _openai_client is None:
        if not OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
        _openai_client = OpenAI(api_key=OPENAI_API_KEY)

    return _openai_client


def simple_chat(message: str) -> Tuple[str, str]:
    """
    Core LLM dispatch function.

    ALWAYS returns:
        (reply_text, model_used)
    """

    provider = (LLM_PROVIDER or "mock").lower()

    # Always respect mock first
    if provider == "mock" or APP_ENV == "mock":
        return f"[MOCK REPLY] You said: {message}", "mock"

    if provider == "ollama":
        reply = _ollama_chat(message)
        return reply, OLLAMA_MODEL

    if provider == "openai":
        reply = _openai_chat(message)
        return reply, "gpt-4o-mini"

    raise RuntimeError(f"Unknown LLM_PROVIDER: {provider}")


def _ollama_chat(message: str) -> str:
    """
    Call a local Ollama model via its HTTP /api/chat endpoint.
    """
    url = f"{OLLAMA_BASE_URL.rstrip('/')}/api/chat"

    payload = {
        "model": OLLAMA_MODEL,
        "stream": False,
        "messages": [
            {"role": "user", "content": message}
        ],
    }

    response = requests.post(url, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()

    message_obj = data.get("message") or {}
    content = message_obj.get("content")

    if not content:
        raise RuntimeError(f"Ollama response missing message.content: {data}")

    return content


def _openai_chat(message: str) -> str:
    """
    Call OpenAI chat completions.
    """
    client = _get_openai_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful, concise assistant."},
            {"role": "user", "content": message},
        ],
    )

    return response.choices[0].message.content or ""