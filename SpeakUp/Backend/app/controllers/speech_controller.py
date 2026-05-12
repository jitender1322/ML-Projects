import os
from fastapi import UploadFile
from app.services.whisper_service import transcribe_audio
from app.services.grammar_service import analyze_grammar

UPLOAD_DIR = "uploads"

def test_speech():
    return {
        "message": "Speech route working successfully"
    }

async def upload_audio_controller(audio: UploadFile):

    # Validate WAV file
    if not audio.filename.endswith(".wav"):
        return {
            "error": "Only WAV files are allowed"
        }

    # Create uploads folder
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # File path
    file_path = os.path.join(UPLOAD_DIR, audio.filename)

    # Save uploaded audio
    with open(file_path, "wb") as buffer:
        content = await audio.read()
        buffer.write(content)

    # Whisper transcription
    transcription = transcribe_audio(file_path)

    # Gemini grammar analysis
    grammar_result = analyze_grammar(transcription)

    # Delete audio file
    os.remove(file_path)

    return {
        "message": "Analysis successful",
        "ai_result": grammar_result
    }