from pytube import YouTube
import os


def downloadVideo(link: str, path: str) -> str:
    video = YouTube(link)

    if not os.path.exists(path):
        os.makedirs(path)

    stream = video.streams.get_highest_resolution()

    stream.download(path)
    return "ok"


def downloadMp3(link: str, path: str) -> str:
    video = YouTube(link)

    if not os.path.exists(path):
        os.makedirs(path)

    stream = video.streams.filter(
        only_audio=True).first()

    out_file = stream.download(path)

    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    return "ok"


print(downloadMp3(
    "https://music.youtube.com/watch?v=KY_6FYsX6wo&list=RDAMVMKY_6FYsX6wo",
    "../../Área de Trabalho/"))
