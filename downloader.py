from pytube import YouTube


link = input("Link to YouTube video: ")
folder = input("Path to desired directory: ")
yt = YouTube(link)

print(yt.title)

yd = yt.streams.get_highest_resolution()
yd.download(folder)
