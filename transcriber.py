import whisper

def transcribe_audio(audio_path):
    """Transcribes speech to text."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]