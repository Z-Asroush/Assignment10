from film import film
from series import series
from Actor import Actor
from clip import clip
from documentary import documentary


class main():
 
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
        for i in range (len(media_list)):
            print(media_list[i])

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

def loud():
    print('louding...')    
    myfile=open('D:\py-class\OOP\media\data.txt','r')
    data=myfile.read().split('\n')
    for i in range (len(data)):
        detail_list=data[i].split(',')
        if detail_list[1]=='film':
            media_list.append({'id':detail_list[0], 'format':detail_list[1] ,'name':detail_list[2], 'director':detail_list[3] , 'IMDB':detail_list[4],'duration':detail_list[5]})
        elif detail_list[1]=='series':
            media_list.append({'id':detail_list[0], 'format':detail_list[1] ,'name':detail_list[2], 'director':detail_list[3]  ,'episod':detail_list[4],'duration':detail_list[5]}) 
        elif   detail_list[1]=='documentary':
            media_list.append({'id':detail_list[0], 'format':detail_list[1] ,'name':detail_list[2], 'director':detail_list[3],'duration':detail_list[4]})
        elif   detail_list[1]=='clip':
            media_list.append({'id':detail_list[0], 'format':detail_list[1] ,'name':detail_list[2], 'director':detail_list[3],'duration':detail_list[4]})      
    myfile.close()

def show_menu():
    print('1_ add media')
    print('2_ edit media info')
    print('3_ delete media')
    print('4_ search')
    print('5_ show list')
    print('6_ exit')

a=(input('name:'), input('format:'), input('director'),input('url:'),input('duration:'),input('cast:'))

media_list=[]
loud()
show_menu()
choice= int(input('Please choose a number of menu:'))
while True:
    if choice==1:
        a.Add_media()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==2:
        a.Edit()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==3:
        a.Delete()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==4:
        a.Search()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==5:
        a.show_list()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==6:
        a.Save()
        exit()    