from openai import AsyncOpenAI

from app.services.llm.base import LLMService, Message


class OpenAIProvider(LLMService):
    """Implements LLMService using the OpenAI API (e.g. GPT-4o)."""

    def __init__(self, api_key: str, model: str) -> None:
        # AsyncOpenAI is the async version of the OpenAI client.
        # Passing the api_key here means we never hardcode it — it comes from .env via settings.
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def chat(self, messages: list[Message], system_prompt: str) -> str:
        # OpenAI expects the same {"role": ..., "content": ...} format as Ollama.
        # The system prompt is passed as a "system" role message, same pattern.
        openai_messages = [{"role": "system", "content": system_prompt}]
        openai_messages += [{"role": m.role, "content": m.content} for m in messages]

        # The OpenAI library handles the HTTP call for us — no manual httpx needed.
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=openai_messages,
        )

        # OpenAI's response structure: response.choices[0].message.content
        # choices[0] — the first (and usually only) response candidate
        # message.content — the actual text reply
        return response.choices[0].message.content
