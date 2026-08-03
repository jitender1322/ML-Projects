from fastapi import FastAPI # type: ignore
from app.routes.speech_routes import router as speech_router
from fastapi.middleware.cors import CORSMiddleware # type: ignore

app = FastAPI(
    title="FluentFlow AI",
    description="AI English Speaking & Grammar Correction API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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