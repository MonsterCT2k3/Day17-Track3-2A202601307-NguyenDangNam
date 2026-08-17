"""Thin LLM wrapper for the demo UI chat reply supporting Gemini and Groq.

This is the ONLY place the lab calls a generative LLM. Benchmark scoring never
uses an LLM (see LAB.md): retrieval evidence is graded deterministically. Here
the LLM only turns retrieved memory context into a grounded assistant reply so
the mini-product feels real.

Supported backends:
- Gemini (gemini-2.0-flash by default)
- Groq (llama-3.3-70b-versatile by default)
"""

from __future__ import annotations

import json
from typing import Any

import requests

from .config import settings

SYSTEM_INSTRUCTION = (
    "You are the assistant of a personal memory agent for VinUni Lab 17. "
    "Answer the user grounded ONLY in the retrieved memory context provided. "
    "If the context does not contain the answer, say so plainly instead of "
    "inventing facts. Be concise and cite the concrete markers/ids you used. "
    "You may reply in the user's language (Vietnamese or English)."
)


def gemini_available() -> bool:
    """True when a key is configured. UI uses this to show status."""
    return bool(settings.gemini_api_key or settings.groq_api_key)


def _to_contents(history: list[dict[str, str]]) -> list[dict[str, Any]]:
    """Map chat history to google-genai `contents` turns.

    Roles: user -> "user", everything else (assistant/model) -> "model".
    """
    contents: list[dict[str, Any]] = []
    for msg in history:
        role = "user" if msg.get("role") == "user" else "model"
        text = msg.get("content", "")
        if not text:
            continue
        contents.append({"role": role, "parts": [{"text": text}]})
    return contents


def _call_groq(
    memory_context: str,
    history: list[dict[str, str]],
    user_message: str,
    *,
    model: str | None = None,
) -> str:
    """Generate reply using Groq OpenAI-compatible API."""
    model_name = model or settings.groq_model or "llama-3.3-70b-versatile"
    grounding = (
        "Retrieved memory context for this turn:\n"
        "-------------------------------------\n"
        f"{memory_context.strip() or '(no memory retrieved)'}\n"
        "-------------------------------------\n\n"
        f"User message: {user_message}"
    )

    messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
    for msg in history:
        r = "assistant" if msg.get("role") in ("assistant", "model") else "user"
        txt = msg.get("content", "")
        if txt:
            messages.append({"role": r, "content": txt})
    messages.append({"role": "user", "content": grounding})

    headers = {
        "Authorization": f"Bearer {settings.groq_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model_name,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 800,
    }

    resp = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=30,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Groq API error ({resp.status_code}): {resp.text}")
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()


def _call_gemini(
    memory_context: str,
    history: list[dict[str, str]],
    user_message: str,
    *,
    model: str | None = None,
) -> str:
    """Generate reply using Google GenAI SDK with fallback model names."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.gemini_api_key)
    candidate_models = [
        model or settings.gemini_model,
        "gemini-2.0-flash",
        "gemini-1.5-flash",
    ]
    # Remove duplicates while preserving order
    seen = set()
    model_list = [m for m in candidate_models if m and not (m in seen or seen.add(m))]

    grounding = (
        "Retrieved memory context for this turn:\n"
        "-------------------------------------\n"
        f"{memory_context.strip() or '(no memory retrieved)'}\n"
        "-------------------------------------\n\n"
        f"User message: {user_message}"
    )

    contents = _to_contents(history)
    contents.append({"role": "user", "parts": [{"text": grounding}]})

    last_exc = None
    for m in model_list:
        try:
            response = client.models.generate_content(
                model=m,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.3,
                    max_output_tokens=800,
                ),
            )
            return (getattr(response, "text", "") or "").strip()
        except Exception as exc:
            last_exc = exc
            continue

    if last_exc:
        raise last_exc
    raise RuntimeError("No valid Gemini model found.")


def generate_reply(
    memory_context: str,
    history: list[dict[str, str]],
    user_message: str,
    *,
    model: str | None = None,
) -> str:
    """Generate a grounded assistant reply with Gemini or Groq."""
    if not (settings.gemini_api_key or settings.groq_api_key):
        raise RuntimeError(
            "Neither GEMINI_API_KEY nor GROQ_API_KEY is configured. "
            "Please add an API key to .env to enable chat replies."
        )

    # 1. Try Gemini first if key exists
    if settings.gemini_api_key:
        try:
            return _call_gemini(memory_context, history, user_message, model=model)
        except Exception as gemini_err:
            # Fallback to Groq if available
            if settings.groq_api_key:
                return _call_groq(memory_context, history, user_message, model=model)
            raise gemini_err

    # 2. Otherwise use Groq
    return _call_groq(memory_context, history, user_message, model=model)
