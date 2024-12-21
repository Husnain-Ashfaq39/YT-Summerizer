import os
from audio_downloader import download_audio
from transcriber import transcribe_and_translate
from text_cleaner import remove_fillers
from file_manager import save_transcription
from summarizer import summarize_text

def main():
    video_url = input("Enter YouTube video URL: ")
    print("\nDownloading audio...")
    audio_path, error = download_audio(video_url)

    if audio_path:
        print("\nAudio downloaded. Transcribing and translating...")
        transcription, error = transcribe_and_translate(audio_path)

        if transcription:
            print("\nTranscription and Translation:")
            print(transcription)
            
            # Clean the transcription
            cleaned_transcription = remove_fillers(transcription)
            print("\nCleaned Transcription:")
            print(cleaned_transcription)
            
            # Summarize the cleaned transcription
            summary = summarize_text(cleaned_transcription)
            print("\nSummary:")
            print(summary)
            
            # Save summary to file
            if save_transcription(summary, output_file="summary.txt"):
                print("\nSummary saved to summary.txt")
            else:
                print("\nFailed to save summary to file")
        else:
            print("\nError:", error)

        # Clean up downloaded audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)
    else:
        print("\nError:", error)

if __name__ == "__main__":
    main()
