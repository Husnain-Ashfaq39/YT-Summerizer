import yt_dlp

def download_audio(video_url, output_path="audio.mp3"):
    """Download audio from a YouTube video."""
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_path,
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return output_path, None
    except Exception as e:
        return None, f"An error occurred while downloading audio: {str(e)}" 