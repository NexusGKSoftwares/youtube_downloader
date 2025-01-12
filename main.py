from pytube import YouTube
import os

def download_youtube_audio(url, output_dir="downloads"):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Initialize YouTube object
        yt = YouTube(url)
        
        # Extract audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        if not audio_stream:
            print("No audio stream available for this video.")
            return
        
        # Download the audio
        print(f"Downloading audio: {yt.title}")
        audio_stream.download(output_dir)
        print(f"Download complete! File saved in {output_dir}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    download_directory = input("Enter the download directory (default: 'downloads'): ") or "downloads"
    
    download_youtube_audio(video_url, download_directory)
