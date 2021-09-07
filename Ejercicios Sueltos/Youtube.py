from pytube import YouTube
link = input("URL del video: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()