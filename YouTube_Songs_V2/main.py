import os

from pytube import YouTube

links = [
'https://www.youtube.com/watch?v=LdFBROw1xVw&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=114',
'https://www.youtube.com/watch?v=HHDCn5UOOus&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=113',
'https://www.youtube.com/watch?v=ZXM96rj6oWo&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=112',
'https://www.youtube.com/watch?v=htCH7X4DF_o&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=111',
'https://www.youtube.com/watch?v=ggn8i3pN1Qg&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=110',
'https://www.youtube.com/watch?v=3pynO8bfGKM&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=109',
'https://www.youtube.com/watch?v=0bjhBIVFEO0&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=108',
'https://www.youtube.com/watch?v=pDdWZVsZCpA&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=107',
'https://www.youtube.com/watch?v=lYOREZ5TcHU&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=106',
'https://www.youtube.com/watch?v=DoBVa94v3pI&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=105',
'https://www.youtube.com/watch?v=GT8bbhYqNP4&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=104',
'https://www.youtube.com/watch?v=20XZitzVotU&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=103',
'https://www.youtube.com/watch?v=7wGx9bMW0IQ&list=PL2hoGhz2jBSrEk4tA0nS72lZjifPPCd8r&index=102']
for x,y in enumerate(links):

    yt = YouTube(y)

    title=yt.title

    print(f"{x+1}){title}")

    image = yt.thumbnail_url

    stream = yt.streams.get_by_itag(140)

    stream.download()

    otitle=title+".mp4"
    ntitle=title+".mp3"
    
    try:
        os.rename(otitle,ntitle)

        print("Audio Downloaded")
    except:
        print("Error")

print("BYE")


