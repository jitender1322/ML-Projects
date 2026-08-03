from fastapi import APIRouter, UploadFile, File

from app.controllers.speech_controller import (
    test_speech,
    upload_audio_controller
)

from app.schemas.response_schema import APIResponse

router = APIRouter()


@router.get(
    "/test",
    response_model=APIResponse
)
def speech_test():
    return test_speech()


@router.post(
    "/upload",
    response_model=APIResponse
)
async def upload_audio(audio: UploadFile = File(...)):
    return await upload_audio_controller(audio)