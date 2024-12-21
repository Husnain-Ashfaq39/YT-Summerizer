import whisper

def transcribe_and_translate(audio_path, target_language="en"):
    """Transcribe and translate audio using Whisper."""
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path, task="translate", language=target_language)
        return result["text"], None
    except Exception as e:
        return None, f"An error occurred while transcribing: {str(e)}" 