from pytube import YouTube

link = 'https://www.youtube.com/watch?v=sNrLlmOIn-c&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&index=9&ab_channel=CodeHelp-byBabbar'
my_video = YouTube(link)
print("********VIDEO TITLE********")
print(my_video.title)

print("*****THE THUMBNAIL OF THE YOUTUBE VIDEO*****")
print(my_video.thumbnail_url)

print("*****Download Youtube Video*****")
videos = my_video.streams.all()                                # stream function gives us all the available formats ie vid and audio
# videos = my_video.streams.filter(only_audio = True)            #this stream function gives us only the audio format to download
vid= list(enumerate(videos))                                     #streaming resolutions or formats are converted to a list 
for i in vid:
    print(i)                                                     #we'll get the list of stream resolutions

strm = int(input("Enter the resolution of your choice: "))
videos[strm].download()
print("Video downloaded successfully")