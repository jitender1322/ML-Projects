import os
from fastapi import UploadFile, HTTPException # type: ignore

from app.services.whisper_service import transcribe_audio
from app.services.grammar_service import analyze_grammar

UPLOAD_DIR = "uploads"


def test_speech():
    return {
        "success": True,
        "message": "Speech route working successfully",
        "data": None
    }


async def upload_audio_controller(audio: UploadFile):

    try:

        # Validate file
        if not (audio.filename.endswith(".wav") or audio.filename.endswith(".webm")):
            raise HTTPException(
                status_code=400,
                detail="Only WAV files are allowed"
            )

        # Create uploads folder
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # File path
        file_path = os.path.join(UPLOAD_DIR, audio.filename)

        # Save audio
        with open(file_path, "wb") as buffer:
            content = await audio.read()
            buffer.write(content)

        # Whisper transcription
        transcription = transcribe_audio(file_path)

        # Grammar analysis
        grammar_result = analyze_grammar(transcription)

        # Delete file
        os.remove(file_path)

        return {
            "success": True,
            "message": "Analysis successful",
            "data": grammar_result
        }

    except HTTPException as http_error:
        raise http_error

    except Exception as e:

        return {
            "success": False,
            "message": "Internal server error",
            "data": str(e)
        }