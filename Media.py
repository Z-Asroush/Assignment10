import pytube
from Actor import Actor

class Media():
    def __init__(self,ID,NAME,CATEGORY,DIRECTOR,IMDB , URL ,INFO,CAST ):
        self.id=ID
        self.category=CATEGORY
        self.name= NAME
        self.director= DIRECTOR
        self.imdb=IMDB 
        self.url = URL
        self.info=INFO
        self.cast =CAST

    def show(self):
        print('ID: {self.id} ,NAME:{self.name} , CATEGORY:{self.category} , DIRECTOR:{self.director} ,IMDB:{self.imdb} , URL:{self.url} ,INFO:{self.info},CAST:{self.cast} ')
    
    def show_info(self):
        print(self.info)

    def show_casts(self):
        casts= self.cast.split('-')  
        for actor in casts:
            Actor(actor).show() 

    def download(self):
        link=input('enter link:')
        first_stream=pytube.YouTube(link).streams.first() 
        first_stream.downloud(output_path='./',filename='mediaa.mp4')                  
          