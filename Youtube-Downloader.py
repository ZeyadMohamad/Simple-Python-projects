from pytube import YouTube

# def Download_video(link):

#     yt = YouTube(link)
#     yt = yt.streams.get_highest_resolution()

#     try:
#         yt.download()
#     except:
#         print("An error occurred")

#     print("The video has been downloaded successfully")

# link = ""
# Download_video(link)

#---------------------------------------------------------

# def Download_audio(link_2):

#     yt_object = YouTube(link_2)
#     yt_object = yt_object.streams.get_audio_only()

#     try:
#         yt_object.download()
#     except:
#         print("an error has occurred")

#     print("The audio has been downloaded successfully")

# link_2 = "https://www.youtube.com/watch?v=XDPV0d-YdU4"
# Download_audio(link_2)

yt = YouTube("https://www.youtube.com/watch?v=XDPV0d-YdU4")

vids= yt.streams.all()
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Enter vid num: "))
vids[vnum].download(r"D:\python")
print('done')
# When using any of the functions, comment the other
# to avoid an error