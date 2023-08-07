from pytube import Playlist

link = 'https://www.youtube.com/playlist?list=PLq_SHLFD-pSD_LeiV2dyAHgED7PDF48Jq'
p_list = Playlist(link)

print("*****Playlist Name*****")
print(f'Downloading : {p_list.title}')

for video in p_list.videos:
    video.streams.first().download()   #first() downloads the video in the least resolution possible