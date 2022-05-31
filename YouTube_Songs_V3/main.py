import os

from pytube import YouTube
file = open("Links.txt",'r')
reading = file.readlines()

errors=["/",":","*","?","<",">","|","'",'"',"."]

for x, y in enumerate(reading):

    yt = YouTube(y)

    title = yt.title

    print(f"{x + 1}){title}")

    for z,k in enumerate(errors):
        if title.find(k)>=0:
            #print(k)
            title=title.replace(k,"")
            #print(title)
            print("Solving the error...")



    image = yt.thumbnail_url

    stream = yt.streams.get_by_itag(140)

    stream.download()

    otitle = title + ".mp4"
    ntitle = title + ".mp3"


    try:
        os.rename(otitle, ntitle)

        print("Audio Downloaded")
    except:
        print("Error")

        # songName = input("Please write a correct name: ")
        # songName=songName+".mp3"
        # print(songName)
        #os.rename(otitle, songName)

file.close()
print("BYE")
