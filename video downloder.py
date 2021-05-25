import pytube
url=input('enter the url')
youtube = pytube. YouTube(url)
streams = youtube.streams.all()
j=1
for i in streams:
 print(str(j)+"  "+str(i))
 j+=1   

stream_number = int(input("enter the number \t"))
video = streams[stream_number-1]  
video.download('F:\myy ash\Tempy')    
print("downloading completed!!!!!!!!!!!!!!!!!!!!!")
