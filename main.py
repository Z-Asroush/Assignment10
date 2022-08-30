from Media import Media
from Clip import Clip
from Film import Film
from Series import Series
from Documentary import Documentary

class main():
    def __init__(self):
        try:
            f=open('data.txt','r')
        except:
            print('error')
            exit()

        text=f.read()
        detail=text.split('\n')
        self.medias=[]
        i=0

        while i<len(detail):
            info= detail[i].split(',')
            if info[1]=='film':
                self.medias.append(Film(info))
            elif info[1]=='documentary':
                self.medias.append(Documentary(info))
            elif info[1]=='series':
                self.medias.append(Series(info))
            elif info[1]=='clip':
                self.medias.append(Clip(info))
            i+=1
        self.show_menu()        

    def show_menu(self):
        print('1_ add media')
        print('2_ edit media info')
        print('3_ delete media')
        print('4_ search')
        print('5_ show list')
        print('6_ download')
        print('7_ show info')
        print('8_ duration search')
        print('9_ show actors')
        print('10_save and exit') 
        choice=input('enter option:')

        if choice=='1':
            self.Add_media=choice
        elif choice=='2':
            self.edit_media_info=choice                
        elif choice=='3':
            self.delete_media=choice 
        elif choice=='4':
            self.search=choice 
        elif choice=='5':
            self.show_list=choice 
        elif choice=='6':
            self.download=choice 
        elif choice=='7':
            self.show_info=choice
        elif choice=='8':
            self.duration_search=choice
        elif choice=='9':
            self.show_actors=choice 
        elif choice=='10':
            self.save_exit=choice 


    def Add_media(self):
        category=input('enter category(film or clip or series or documentary):')
        id=input('enter id:')
        name=input('enter name:')
        director=input('enter director:')
        IMDB=input('enter IMDB:' )
        duration=input('enter duration:')
        url=input('enter url:')
        info=input('enter media info:')
        casts=input('enter casts:')
        episode=input('enter episode:')
        
        
        media_info=[id,category,name,director,IMDB,duration,url,info,casts,episode]

        if category=='film':
            self.medias.append(Film(media_info))
        elif category=='series':
            self.medias.append(Series(media_info))    
        elif category=='clip':
            self.medias.append(Clip(media_info))  
        elif category=='documentary':
            self.medias.append(Documentary(media_info))

        self.show_menu()      

    def edit_media_info(self):
        entrance=input('enter name of media:')
        for media in self.medias:
            if media.name==entrance:
                if media.category=='film':
                    media=media.edit_film()
                    break
                elif media.category=='series':
                    media=media.edit_series()
                    break
                elif media.category=='clip':
                    media=media.edit_clip()
                    break
                elif media.category=='documentary':
                    media=media.edit_documentary()
                    break 
        self.show_menu()            


    def delete_media(self):
        entrance=input('enter name of media:')
        for media in self.medias:
            if entrance==media.name:
                self.medias.remove(media)
                break
        self.show_menu()    

    def search(self):
        entrance=input('enter name of media:')
        for media in self.medias:
            if media.name==entrance:
                media.show()
                break
        self.show_menu()

    def show_list(self):
        for media in self.medias:
            media.show()
        self.show_menu()

    def download(self):
        entrance=input('enter name of media:')
        for media in self.medias:
            if media.name==entrance:
                media.download()
                break
        self.show_menu()    

    def show_info(self):
        entrance=input('enter name of media:')
        for media in self.medias:
            if media.name==entrance:
                media.show_info()
                break
        self.show_menu() 


    def show_actors(self):
        entrance=input('enter name of media:')
        for media in self.medias:
            if media.name==entrance:
                media.show_casts()
                break
        self.show_menu()  

    def save_exit(self):
        out=open('data.txt','w')
        for media in self.medias:
            out.write(media.id +','+ media.category +','+media.name+','+media.year+','+media.director+','+media.imdb+','+media.duration+','+media.url+','+media.info+','+media.cast+','+media.genre+','+media.episode+','+media.subject+','+media.company)
            if media!=self.medias[-1]:
                out.write('\n')
        out.close()
        exit()        

if __name__ == "__main__":
    widget = main()