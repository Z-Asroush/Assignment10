import pytube
from Actor import Actor

class media():
    def __init__(self,NAME,FORMAT,DIRECTOR , URL , DURATION,CAST ):
        self.name= NAME
        self.format=FORMAT
        self.director= DIRECTOR 
        self.url = URL
        self.duration = DURATION
        self.cast =CAST

    def show(self):
        for i in range (len(media_list)):
            print(media_list[i])

    def show_cast(self):
        casts= self.cast.split('-')  
        for actor in casts:
            Actor(actor).show() 

    def download(self):
        link=input('enter link:')
        first_stream=pytube.YouTube(link).streams.first() 
        first_stream.downloud(output_path='./',filename='media.mp4')                  

media_list=[]            