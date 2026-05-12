from fastapi import APIRouter, UploadFile, File
from app.controllers.speech_controller import (
    test_speech,
    upload_audio_controller
)

router = APIRouter()

@router.get("/test")
def speech_test():
    return test_speech()

@router.post("/upload")
async def upload_audio(audio: UploadFile = File(...)):
    return await upload_audio_controller(audio)