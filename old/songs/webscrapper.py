import os
import sys
from pytube import YouTube
from pytube.cli import on_progress

PATH_SAVE = "D:\\Downloads"

yt = YouTube("https://www.youtube.com/watch?v=0pWsCiBvLOk", on_progress_callback=on_progress)
#Download mp3
audio_file = yt.streams.filter(only_audio=True).first().download(PATH_SAVE)
base, ext = os.path.splitext(audio_file)
new_file = base + '.mp3'
os.rename(audio_file, new_file)

#Download Video
ys = yt.streams.filter(res="1080p").first()
ys.download(PATH_SAVE)