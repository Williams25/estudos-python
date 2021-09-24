messagePython = "curso de python"
print(messagePython)

from pytube import YouTube

def downloadVideo (link: str) -> str:
  video = YouTube(link)
  stream = video.streams.get_highest_resolution()
  stream.download()
  return "ok"

print(downloadVideo("https://www.youtube.com/watch?v=SoCp5k2yZ1U"))
