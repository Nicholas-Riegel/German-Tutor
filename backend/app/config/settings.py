from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Provider selection
    llm_provider: str = "ollama"   # "ollama" or "openai"
    stt_provider: str = "local"    # "local" or "openai"
    tts_provider: str = "edge"     # "edge" or "openai"

    # Ollama settings
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    # OpenAI settings (only needed when using openai providers)
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"


settings = Settings()