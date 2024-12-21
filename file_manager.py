def save_transcription(transcription, output_file="transcription.txt"):
    """Save transcription to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(transcription)
        return True
    except Exception as e:
        print(f"Error saving transcription: {str(e)}")
        return False 