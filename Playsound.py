from playsound import playsound
import os

audio_file = "success.mp3"

if os.path.exists(audio_file):
    playsound(audio_file)
else:
    print(f"File not found: {audio_file}")
