from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm.base import Message
from app.services.llm.factory import get_llm_service

# APIRouter is like a mini FastAPI app — it holds a group of related endpoints.
# Instead of defining every route in main.py, we split them into focused files:
#   routers/chat.py    → /chat/...      (sending messages, conversation history)
#   routers/audio.py   → /audio/...     (uploading voice recordings, getting audio responses)
#   routers/sessions.py → /sessions/... (creating, listing, deleting study sessions)
# We register each router in main.py so FastAPI knows about it.
router = APIRouter(prefix="/chat", tags=["chat"])

# The German tutor's personality and rules.
# This is sent to the LLM as a "system" message before every conversation.
SYSTEM_PROMPT = """Du bist ein freundlicher, geduldiger Deutschlehrer. Dein Ziel ist es, natürliche Gespräche auf Deutsch zu führen, die dem Lernenden helfen, die Sprache fließend zu sprechen.

GESPRÄCHSSTIL:
- Antworte IMMER auf Deutsch
- Führe das Gespräch natürlich und locker — wie ein Gespräch mit einem Muttersprachler
- Stelle gelegentlich Folgefragen, um das Gespräch am Laufen zu halten
- Benutze einfaches, klares Deutsch das zum Niveau des Lernenden passt

FEHLERKORREKTUR:
- Korrigiere Fehler NICHT direkt oder explizit während des Gesprächs — das unterbricht den Gedankenfluss
- Verwende stattdessen "implicit recast": Wenn der Lernende einen Fehler macht, benutze die korrekte Form ganz natürlich in deiner Antwort, ohne darauf hinzuweisen
- Mache das nur gelegentlich — nicht bei jedem Fehler, das wirkt sonst unnatürlich

GESPRÄCHSENDE:
Wenn der Lernende sich verabschiedet (z.B. "Tschüss", "Auf Wiedersehen") oder explizit um Feedback bittet, gib eine kurze freundliche Rückmeldung:
1. Zuerst: Was gut lief — ein konkretes Lob (z.B. Wortschatz, Satzstruktur, Thema)
2. Dann: 1-2 der wichtigsten Grammatik- oder Vokabelpunkte zum Üben, mit einem kurzen Beispiel
Halte das Feedback kurz, positiv und ermutigend.
"""
# English summary of the system prompt:
# - Always respond in German, conversationally
# - Use implicit recast: naturally model correct forms in replies without flagging errors
# - Do this occasionally, not mechanically after every mistake
# - When conversation ends (goodbye / feedback request): briefly praise what went well,
#   then give 1-2 key grammar/vocab points to work on, with examples. Keep it encouraging.


# Pydantic models define the shape of the request and response JSON.
# FastAPI uses these to validate input and auto-generate the /docs page.
class ChatRequest(BaseModel):
    message: str                  # the user's message
    history: list[dict] = []      # previous messages [{role, content}, ...], empty by default


class ChatResponse(BaseModel):
    reply: str                    # the AI's German response


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    # Convert history dicts into Message objects
    messages = [Message(role=m["role"], content=m["content"]) for m in request.history]
    # Append the new user message at the end
    messages.append(Message(role="user", content=request.message))

    # get_llm_service() returns whichever provider is configured in .env
    llm = get_llm_service()
    reply = await llm.chat(messages, SYSTEM_PROMPT)

    return ChatResponse(reply=reply)
