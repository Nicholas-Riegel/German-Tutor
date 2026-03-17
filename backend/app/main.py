from fastapi import FastAPI
from app.config.settings import settings
from app.routers import chat

app = FastAPI(
    title="German Tutor API",
    description="AI-powered German conversation tutor",
    version="0.1.0",
)

# Register the chat router — this adds all routes defined in routers/chat.py to the app
app.include_router(chat.router)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "llm_provider": settings.llm_provider,
        "stt_provider": settings.stt_provider,
        "tts_provider": settings.tts_provider,
    }