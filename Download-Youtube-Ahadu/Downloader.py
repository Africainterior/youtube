#!bin/env python
# Coded by Ahadu Eyasu, Ethiopia.

from pytube import YouTube
import os, sys
re="\033[1;31m"
gr="\033[1;31m"
cy="\033[1;36m"

def banner():
    print(gr+"              Made By Ahadu Eyasu, Ethiopia        ")
    print(cy+"             --------------------------------      ")
banner()
print(gr+"Installng Useful Data...")
os.system('python3 -m pip install pytube')
os.system('pip3 install pytube')
banner()

link = input(gr+"[-] Enter the url of the video: "+cy)
yt = YouTube(link)

print("Title of the video: ",yt.title)
print("Views of the video: ",yt.views)
print("Length of the video: ",yt.length)
print("Rating of the video: ",yt.rating)

print(yt.streams.filter(progressive=True))

ys = yt.streams.get_highest_resolution()

print(gr+"Downloading the video...(speed depends on your Internet/wifi connection)")
ys.download()
print(gr+"Download completed please subscribe to my channel https://www.youtube.com/channel/UCDAA-BPoq6ZjzhAnBt3kCrA")
