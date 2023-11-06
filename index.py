import openai
from pytube import YouTube

# yt = YouTube("https://www.youtube.com/watch?v=hTU3-M54tvs")

# print("Title: ", yt.title)
# # print("Streams: ", yt.streams.filter(only_audio=True,file_extension='mp4'))

# audio = yt.streams.filter(only_audio=True,file_extension='mp4').first()

# print("Downloading...")
# audio.download()

# openai.api_key = ""

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# audio_file= open("C:\\Users\\nouma\\OneDrive\\Desktop\\ChatWithYtVideo\\audio\\test.mp4", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)

# # save the transcript to a file
# with open("C:\\Users\\nouma\\OneDrive\\Desktop\\ChatWithYtVideo\\audio\\transcript.txt", "w") as f:
#     f.write(transcript.text)
