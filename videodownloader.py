from pytube import  YouTube
link = input('Enter the link : ')
video = YouTube(link)
stream = video.streams.get_audio_only()
stream.download()