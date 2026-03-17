import httpx

from app.services.llm.base import LLMService, Message


class OllamaProvider(LLMService):
    """Implements LLMService using a locally running Ollama server."""

    def __init__(self, url: str, model: str) -> None:
        # url  — Ollama's local server address, e.g. "http://localhost:11434"
        # model — which model to use, e.g. "llama3.2"
        self.url = url
        self.model = model

    async def chat(self, messages: list[Message], system_prompt: str) -> str:
        # Ollama expects messages as a list of {"role": ..., "content": ...} dicts.
        # We prepend the system prompt as a "system" role message — this is how
        # you give the model its personality and instructions before the conversation.
        ollama_messages = [{"role": "system", "content": system_prompt}]
        ollama_messages += [{"role": m.role, "content": m.content} for m in messages]

        # httpx.AsyncClient is like the requests library but async-friendly.
        # The `async with` block ensures the connection is properly closed when done.
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self.url}/api/chat",
                json={
                    "model": self.model,
                    "messages": ollama_messages,
                    "stream": False,  # get the full response at once, not word-by-word
                },
            )
            response.raise_for_status()  # raise an error if Ollama returned a non-200 status

        # Ollama's response JSON looks like: {"message": {"role": "assistant", "content": "..."}}
        return response.json()["message"]["content"]
