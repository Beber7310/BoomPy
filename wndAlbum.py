'''
Created on 28 mars 2021

@author: bdosd
'''
from guizero import App,Box,PushButton,os,Window
from PIL import Image
 
import platform
import glob

arrayAlbum=[];
arrayAlbumIdx=0;
box_album=0

arrayButton=[];

albumPathDesc =""
basePathDesc = ""
        
class record():
    artiste=""
    album=""
    cover=""
    genre =""
    songs =[]
    
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
                    
                    print("cover=" + self.cover, end='')                   
        finally:
            file.close()
    
def nextAlbum():
    global box_album
    global arrayAlbumIdx
    if(arrayAlbumIdx+10 < len(arrayAlbum)):
        arrayAlbumIdx+=10;
    UpdateButton(box_album)   
    
def prevAlbum():
    global box_album
    global arrayAlbumIdx
    if(arrayAlbumIdx >=10):
        arrayAlbumIdx-=10
    if(arrayAlbumIdx<0):
        arrayAlbumIdx=0
    UpdateButton(box_album)      
    
def wndAlbumCreate(parent):
    global albumPathDesc
    global basePathDesc
    global box_album
    
    appAlbum = Window(parent)
    if(platform.system()=="Linux"):
        appAlbum.set_full_screen()
        albumPathDesc = "/mnt/Music/album/"
        basePathDesc  = "/mnt/Music/"
      
    if(platform.system()=="Windows"):
        appAlbum.width=800
        appAlbum.height=480
        albumPathDesc ="//OPENMEDIAVAULT/Music/album/"
        basePathDesc = "//OPENMEDIAVAULT/Music/"
    
    box_album = Box(appAlbum, width="fill", align="top",layout="grid")
    box_home  = Box(appAlbum, width="fill", align="bottom")

    PushButton(box_home,command=prevAlbum, text ="<", align="left")
    PushButton(box_home,command=nextAlbum, text =">", align="right")
    
    for filename in glob.glob(os.path.join(albumPathDesc, '*.piz')):
        albumInst = record();
        albumInst.loadFromFile(filename)
        
        if(not os.path.exists(basePathDesc + albumInst.cover+"thumb")):
            print("Creating " + basePathDesc + albumInst.cover+"thumb" , end='')
            im = Image.open(basePathDesc + albumInst.cover) 
            newsize = (154,154)
            im = im.resize(newsize)
            im.save( basePathDesc + albumInst.cover+"thumb", "GIF")     
        else:
            print("Skip creating " + basePathDesc + albumInst.cover+"thumb" , end='')
        
        arrayAlbum.append(albumInst)
    
    UpdateButton(box_album)     
    
def UpdateButton(parent):    
    global albumPathDesc
    global basePathDesc
    global arrayAlbum;
    global arrayAlbumIdx;
    
    
    for x in arrayButton:
        x.destroy()
        
    arrayButton.clear()   

    if(arrayAlbumIdx+0 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+0].cover+"thumb",grid=[0,0]))
    if(arrayAlbumIdx+1 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+1].cover+"thumb",grid=[1,0]))
    if(arrayAlbumIdx+2 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+2].cover+"thumb",grid=[2,0]))
    if(arrayAlbumIdx+3 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+3].cover+"thumb",grid=[3,0]))
    if(arrayAlbumIdx+4 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+4].cover+"thumb",grid=[4,0]))
    
    if(arrayAlbumIdx+5 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+5].cover+"thumb",grid=[0,1]))
    if(arrayAlbumIdx+6 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+6].cover+"thumb",grid=[1,1]))
    if(arrayAlbumIdx+7 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+7].cover+"thumb",grid=[2,1]))
    if(arrayAlbumIdx+8 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+8].cover+"thumb",grid=[3,1]))
    if(arrayAlbumIdx+9 < len(arrayAlbum)): arrayButton.append(PushButton(parent,  image = basePathDesc+ arrayAlbum[arrayAlbumIdx+9].cover+"thumb",grid=[4,1]))
    
    
    
    

