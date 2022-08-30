from Media import Media

class Film(Media):
    def __init__(self,media ):
        media.__init__(self,media[0],media[1],media[2],media[3],media[4], media[5],media[6],media[7],media[8] )
        self.media=media
        self.duration=media[5]
        self.episode='episode'

    def edit_film(self):
        print('which item? \n 1-name  2-director  3-IMDB  4-duration  5-url  6-info  7-category ')    
        item=input('enter number:')
        changed=input('enter changed item:')
        if item=='1':
            self.name=changed
        elif item=='2':
            self.director=changed
        elif item=='3':
            self.imdb=changed        
        elif item=='4':
            self.duration=changed        
        elif item=='5':
            self.url=changed       
        elif item=='6':
            self.info=changed        
        elif item=='7':
            self.category=changed        
        return self.media   