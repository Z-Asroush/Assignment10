from media import media

class   documentary(media):
    def __init__(self,media): 
        media.__init__(self,media[0],media[1],media[2],media[3],media[4] )
        self.format =media[1]
        self.name=media[2]
        self.director=media[3]
        self.duration=media[4]  