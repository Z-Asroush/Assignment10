from film import Film
from series import Series
from actor import Actor
from clip import Clip
from documentary import Documentary
import pytube

class media:
    def __init__(self,n,f,di , u , du,c ):
        self.name= n 
        self.director= di 
        self.url = u 
        self.duration = du
        self.format=f
        self.cast =c        
    def show_info():
        pass 

    def download(self):
        link=input('enter link:')
        first_stream=pytube.YouTube(link).streams.first() 
        first_stream.downloud(output_path='./',filename='media.mp4')  

    def loud(self):
        print('louding...')    
        self.myfile=self.open('D:\py-class\OOP\media\data.txt','r')
        self.data=self.myfile.read().split('\n')
        for i in range (len(self.data)):
            self.detail_list=self.data[i].split(',')
            if self.detail_list[1]=='film':
                self.media_list.append({'id':self.detail_list[0], 'format':self.detail_list[1] ,'name':self.detail_list[2], 'director':self.detail_list[3] , 'IMDB':self.detail_list[4],'duration':self.detail_list[5]})
            elif self.detail_list[1]=='series':
                self.media_list.append({'id':self.detail_list[0], 'format':self.detail_list[1] ,'name':self.detail_list[2], 'director':self.detail_list[3]  ,'episod':self.detail_list[4],'duration':self.detail_list[5]}) 
            elif   self.detail_list[1]=='documentary':
                self.media_list.append({'id':self.detail_list[0], 'format':self.detail_list[1] ,'name':self.detail_list[2], 'director':self.detail_list[3],'duration':self.detail_list[4]})
            elif   self.detail_list[1]=='clip':
                self.media_list.append({'id':self.detail_list[0], 'format':self.detail_list[1] ,'name':self.detail_list[2], 'director':self.detail_list[3],'duration':self.detail_list[4]})      
        self.myfile.close()

    def Add_media(self):
        id=input('enter id:')
        name=input('enter name:')
        director=input('enter director:')
        duration=input('enter duration:')
        format=input('enter media format?')
        if format=='film':
            IMDB=input('enter IMDB:' )
            self.media_list.append({'id':id,'format':format , 'name':name, 'director':director ,'IMDB':IMDB , 'duration':duration})
        elif   format=='series':
            episod=input('Number of movie episodes:') 
            self.media_list.append({'id':id,'format':format , 'name':name, 'director':director ,'episod':episod , 'duration':duration}) 
        elif   format=='documentary':
            self.media_list.append({'id':id,'format':format , 'name':name, 'director':director ,'duration':duration})
        elif   format=='clip':
            self.media_list.append({'id':id,'format':format , 'name':name, 'director':director , 'duration':duration})  

    def Edit(self):
        name=input('enter name of media:')
        for i in range (len(self.media_list)):
            if self.media_list[i]['name']==name:
                info=input('which part of media want to edit?')
                self.media_list[i][info]=input()

    def Delete(self):
        name=input('enter name of media:')
        for i in range (len(self.media_list)):
            if self.media_list[i]['name']==name:
                del self.media_list [i]

    def Search(self):
        name=input('enter name of media:')
        for i in range (len(self.media_list)):
            if self.media_list[i]['name']==name:
                print(self.media_list[i])
                break

    def show_list(self):
        for i in range (len(self.media_list)):
            print(self.media_list[i])

    def Save(self):
        self.myfile=open('D:\py-class\OOP\media\data.txt','w')
        for i in range (len(self.media_list)):
            self.myfile.write(str(self.media_list[i]['id'])+","+str(self.media_list[i]['format'])+","+str(self.media_list[i]['name'])+","+str(self.media_list[i]['director']+','))
            if media_list[i]['format']=='film':
                self.myfile.write(str(self.media_list[i]['IMDB'])+","+str(self.media_list[i]['duration']))
            elif media_list[i]['format']=='series':
                self.myfile.write(str(self.media_list[i]['episod'])+","+str(self.media_list[i]['duration'])) 
            elif self.media_list[i]['format']=='documentary' or self.media_list[i]['format']=='clip':
                self.myfile.write(str(media_list[i]['duration']))      
            if i<(len(self.media_list)-1):
                self.myfile.write('\n')
        self.myfile.close()

def show_menu():
    print('1_ add media')
    print('2_ edit media info')
    print('3_ delete media')
    print('4_ search')
    print('5_ show list')
    print('6_ exit')

media_list=[]
media.loud()
show_menu()
choice= int(input('Please choose a number of menu:'))
while True:
    if choice==1:
        media.Add_media()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==2:
        media.Edit()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==3:
        media.Delete()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==4:
        media.Search()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==5:
        media.show_list()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==6:
        media.Save()
        exit()    