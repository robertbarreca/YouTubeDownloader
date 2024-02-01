from pytube import YouTube
import sys


link = sys.argv[1]
folder = sys.argv[2]
yt = YouTube(link)

print("Started download")
yd = yt.streams.get_highest_resolution()
try:
    yd.download(folder)
except:
    print("Something went wrong please try again")
print("Succesfully downloaded video!")
