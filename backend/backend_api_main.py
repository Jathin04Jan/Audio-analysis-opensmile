# app/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import uuid
import os

# import your transcription + analysis functions here
from diarized_transcribe import runTranscribe
from main import runAnalysis

app = FastAPI()

@app.post("/api/upload")
async def upload_call(file: UploadFile = File(...)):
    call_id = str(uuid.uuid4())
    audio_path = f"/tmp/{call_id}.wav"
    with open(audio_path, "wb") as out:
        shutil.copyfileobj(file.file, out)
    # 1. transcribe → transcript_json
    transcript = runTranscribe(audio_path)
    # 2. LLM analysis → summary_str
    summary = runAnalysis(audio_path, transcript)
    return JSONResponse({
        "call_id": call_id,
        "transcript": transcript,
        "summary": summary
    })