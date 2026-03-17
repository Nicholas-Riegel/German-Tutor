from app.config.settings import settings
from app.services.llm.base import LLMService
from app.services.llm.ollama import OllamaProvider
from app.services.llm.openai import OpenAIProvider


def get_llm_service() -> LLMService:
    """Read the LLM_PROVIDER setting and return the appropriate provider.

    This is the single place in the codebase that decides which LLM to use.
    Everything else just calls get_llm_service() and doesn't care which one it gets.
    To switch providers, change LLM_PROVIDER in your .env file — no code changes needed.
    """
    if settings.llm_provider == "openai":
        return OpenAIProvider(
            api_key=settings.openai_api_key,
            model=settings.openai_model,
        )

    # Default to Ollama (local) for any other value, including "ollama"
    return OllamaProvider(
        url=settings.ollama_url,
        model=settings.ollama_model,
    )
