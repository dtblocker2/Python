from pytube import YouTube

def download_audio(youtube_url, output_path):
    # Create a YouTube object
    yt = YouTube(youtube_url)

    # Get the audio-only stream
    stream = yt.streams.filter(only_audio=True).first()

    # Download the audio
    stream.download(output_path)

    print(f"Downloaded audio: {yt.title}")

# Example usage
youtube_url = "https://www.youtube.com/watch?v=31SGauVu1JU"
output_path = "path/to/save/audio"
download_audio(youtube_url, output_path)
