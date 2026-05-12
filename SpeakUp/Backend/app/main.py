from fastapi import FastAPI
from app.routes.speech_routes import router as speech_router

app = FastAPI(
    title="FluentFlow AI",
    description="AI English Speaking & Grammar Correction API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "FluentFlow AI Backend Running"
    }

app.include_router(
    speech_router,
    prefix="/api/speech",
    tags=["Speech"]
)