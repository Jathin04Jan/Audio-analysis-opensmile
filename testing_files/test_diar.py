from pyannote.audio import Pipeline
import os

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=os.getenv("PYANNOTE_AUTH_TOKEN")
)

diarization = pipeline("converted_audio-rec.wav")
print(diarization)