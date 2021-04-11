'''
Created on 28 mars 2021

@author: bdosd
'''
from guizero import App,Box,PushButton,os,Window
from PIL import Image
 
import platform
import glob





        
class record():
    def __init__(self):
        self.artiste=""
        self.album=""
        self.cover=""
        self.genre =""
        self.songs =[]
        
        
    def loadFromFile(self,filePath):
        file = open(filePath, 'r')       
        try:
            line = file.readline()
            while line != '':  # The EOF char is an empty string
                print(line, end='')
                line = file.readline()                
                if "<COVER>" in line:                    
                    self.cover=line.replace("<COVER>","") 
                    self.cover=self.cover.rstrip()
                elif "<ARTISTE>" in line:                    
                    self.artiste=line.replace("<ARTISTE>","") 
                    self.artiste=self.artiste.rstrip()   
                elif "<ALBUM>" in line:                    
                    self.album=line.replace("<ALBUM>","") 
                    self.album=self.album.rstrip()
                elif "mp3/" in line:                    
                    self.songs.append(line.rstrip())
                         
        finally:
            file.close()


class WindowsTracks():
    def __init__(self):
        self.arrayAlbum=[];
        self.arrayAlbumIdx=0;
        self.box_album=0
        self.appAlbum =None;
        self.albumPathDesc =""
        self.basePathDesc = ""   
        self.arrayButton=[];
        
        
    def nextAlbum(self):        
        if(self.arrayAlbumIdx+10 < len(self.arrayAlbum)):
            self.arrayAlbumIdx+=10;
        self.UpdateButton(self.box_album)   
    
    def prevAlbum(self):
        if(self.arrayAlbumIdx >=10):
            self.arrayAlbumIdx-=10
        if(self.arrayAlbumIdx<0):
            self.arrayAlbumIdx=0
        self.UpdateButton(self.box_album)      
    

    def wndAlbumCreate(self, parent,type):

        self.appAlbum = Window(parent)
        if(platform.system()=="Linux"):
            self.appAlbum.set_full_screen()
            self.basePathDesc  = "/mnt/Music/"
            
            
          
        if(platform.system()=="Windows"):
            self.appAlbum.width=800
            self.appAlbum.height=480
            self.basePathDesc = "//OPENMEDIAVAULT/Music/"
                    
        
        if(type=="album"):
            self.albumPathDesc = self.basePathDesc+"album/"
        if(type=="playlist"):
            self.albumPathDesc = self.basePathDesc+"playlists/"
            
        self.box_album = Box(self.appAlbum, width="fill", align="top",layout="grid")
        box_home  = Box(self.appAlbum, width="fill", align="bottom")
    
        PushButton(box_home,command=self.nextAlbum, text =">", align="right",width=20,height="fill")
        PushButton(box_home,command=self.prevAlbum, text ="<", align="right",width=20,height="fill")    
        PushButton(box_home, command=self.window_hide_album,       image = "home.png",         text="Back", align="left")
        
        for filename in glob.glob(os.path.join(self.albumPathDesc, '*.piz')):
            albumInst = record();
            albumInst.loadFromFile(filename)
            
            if(not os.path.exists(self.basePathDesc + albumInst.cover+"thumb")):
                print("Creating " + self.basePathDesc + albumInst.cover+"thumb" , end='')
                im = Image.open(self.basePathDesc + albumInst.cover) 
                newsize = (154,154)
                im = im.resize(newsize)
                im.save( self.basePathDesc + albumInst.cover+"thumb", "GIF")     
            else:
                print("Skip creating " + self.basePathDesc + albumInst.cover+"thumb" , end='')
            
            self.arrayAlbum.append(albumInst)
        
        self.UpdateButton(self.box_album)     
        self.appAlbum.hide()  
    
    def window_hide_album(self):
        self.appAlbum.hide()  
    
    def window_show_album(self):
        self.appAlbum.show()  
        
  
    
    def mpcPlay(self,m3u :record ):
        os.system("mpc clear")   
        for song in m3u.songs:
            mp3Path=self.basePathDesc +song.split(" ")[0]        
            print("mpc add " + mp3Path , end=' ')            
            os.system("mpc add "+ mp3Path)
            
        os.system("mpc play")
        
    def UpdateButton(self,parent):    
        
        for x in self.arrayButton:
            x.destroy()
            
        self.arrayButton.clear()   
    
        if(self.arrayAlbumIdx+0 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+0]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+0].cover+"thumb",grid=[0,0]))
        if(self.arrayAlbumIdx+1 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+1]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+1].cover+"thumb",grid=[1,0]))
        if(self.arrayAlbumIdx+2 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+2]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+2].cover+"thumb",grid=[2,0]))
        if(self.arrayAlbumIdx+3 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+3]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+3].cover+"thumb",grid=[3,0]))
        if(self.arrayAlbumIdx+4 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+4]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+4].cover+"thumb",grid=[4,0]))
        
        if(self.arrayAlbumIdx+5 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+5]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+5].cover+"thumb",grid=[0,1]))
        if(self.arrayAlbumIdx+6 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+6]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+6].cover+"thumb",grid=[1,1]))
        if(self.arrayAlbumIdx+7 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+7]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+7].cover+"thumb",grid=[2,1]))
        if(self.arrayAlbumIdx+8 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+8]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+8].cover+"thumb",grid=[3,1]))
        if(self.arrayAlbumIdx+9 < len(self.arrayAlbum)): self.arrayButton.append(PushButton(parent, command=self.mpcPlay,args=[self.arrayAlbum[self.arrayAlbumIdx+9]],  image = self.basePathDesc+ self.arrayAlbum[self.arrayAlbumIdx+9].cover+"thumb",grid=[4,1]))
        
        
    
    

