from pytube import YouTube

import moviepy.editor

import time

links = ['https://www.youtube.com/watch?v=be12BC5pQLE',
         'https://www.youtube.com/watch?v=Y_V4ExWIdQk',
         'https://www.youtube.com/watch?v=ncyVV9bwmdU']

for x,y in enumerate(links):

    yt = YouTube(y)

    title=yt.title

    print(title)

    image = yt.thumbnail_url

    print(image)

    stream = yt.streams.get_by_itag(18)

    print(stream)

    stream.download()

    print("Video Downloaded")

    print(f"{title}.mp4")
    try:
        video = moviepy.editor.VideoFileClip(f"{title}.mp4")

        audio = video.audio

        audio.write_audiofile(f"{title}.mp3")

        print("Song Downloaded")
    except:
        print("The problem in the title of the song")

print("BYE")
