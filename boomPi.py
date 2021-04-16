'''
Created on 27 mars 2021

@author: bdosd
'''
from guizero import App,Box,PushButton,os,Window
from PIL import Image
from os import path

import os.path
import platform
import wndDeezer
import time


if __name__ == '__main__':
    pass



def radio_fip():
    os.system("mpc clear")
    os.system("mpc add http://icecast.radiofrance.fr/fip-midfi.mp3")
    os.system("mpc play")

def radio_france_inter():
    os.system("mpc clear")
    os.system("mpc add http://direct.franceinter.fr/live/franceinter-midfi.mp3")
    os.system("mpc play")

def radio_france_culture():
    os.system("mpc clear")
    os.system("mpc add http://direct.franceculture.fr/live/franceculture-midfi.mp3")
    os.system("mpc play")

def radio_france_musique():
    os.system("mpc clear")
    os.system("mpc add http://direct.francemusique.fr/live/francemusique-midfi.mp3")
    os.system("mpc play")
 
def imgResize(imgName):
    im = Image.open("image/"+imgName) 
    newsize = (154,154)
    im = im.resize(newsize)
    im.save(imgName)     

    
def chicken_open():
    os.system("")
    
def chicken_close():
    os.system("")
    
def window_show_radio():
    appRadio.show()
    if(platform.system()=="Linux"):        
        appRadio.set_full_screen()
    if(platform.system()=="Windows"):
        appRadio.width=800
        appRadio.height=480        
        

def window_show_chicken():
    appChicken.show()
    if(platform.system()=="Linux"):        
        appChicken.set_full_screen()
    if(platform.system()=="Windows"):        
        appChicken.width=800
        appChicken.height=480
        
        
def window_show_album():
   wndAlbum.window_show_album()

def window_show_playlist():
   wndPlaylist.window_show_album()
            
            
            
def window_hide_radio():
    appRadio.hide()    
 
def window_hide_chicken():
    appChicken.hide()    
      
      
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

     
app = App(title="Main")
appRadio = Window(app)
appRadio.hide()
appChicken = Window(app)
appChicken.hide()


if(platform.system()=="Linux"):
    app.set_full_screen()
    appRadio.set_full_screen()
    appChicken.set_full_screen()
    while(not path.exists("/mnt/Music/")):
        time.sleep(5)
        os.system("sudo mount -a")

if(platform.system()=="Windows"):
    app.width=800
    app.height=480
    appRadio.width=800
    appRadio.height=480
    appChicken.width=800
    appChicken.height=480
    
    

wndAlbum = wndDeezer.WindowsTracks ();
wndAlbum.wndAlbumCreate(app,"album")

wndPlaylist = wndDeezer.WindowsTracks ();
wndPlaylist.wndAlbumCreate(app,"playlist")
    

imgResize("album.png")
imgResize("chicken.png")
imgResize("radio.png")
imgResize("playlist.png")

                
                
#----------------------------------------------------------------------------------------------------------
update_text = PushButton(app, command=window_show_chicken,  image = "chicken.png",align="left")
update_text = PushButton(app, command=window_show_radio,    image = "radio.png" ,align="left")
update_text = PushButton(app, command=window_show_album,    image = "album.png",align="left")
update_text = PushButton(app, command=window_show_playlist, image = "playlist.png",align="left")


#----------------------------------------------------------------------------------------------------------
box_radio = Box(appRadio, width="fill", align="top",layout="grid")
box_home  = Box(appRadio, width="fill", align="bottom")

update_text = PushButton(box_home, command=window_hide_radio,       image = "home.png",         text="Back", align="left")
update_text = PushButton(box_radio, command=radio_fip,              image = "fip.png",          text="fip",grid=[0,0])
update_text = PushButton(box_radio, command=radio_france_inter,     image = "franceinter.png",  text="france inter",grid=[1,0])
update_text = PushButton(box_radio, command=radio_france_culture,   image = "franceculture.png",text="france culture",grid=[2,0])
update_text = PushButton(box_radio, command=radio_france_musique,   image = "francemusique.png",text="france msique",grid=[3,0])


#----------------------------------------------------------------------------------------------------------
box_chicken_cmd     = Box(appChicken, width="fill", align="top",layout="grid")
box_chicken_home    = Box(appChicken, width="fill", align="bottom")

update_text = PushButton(box_chicken_home, command=window_hide_chicken,   image = "home.png",     text="Back", align="left")
update_text = PushButton(box_chicken_cmd, command=chicken_open,         image = "open.png",     grid=[0,0])
update_text = PushButton(box_chicken_cmd, command=chicken_close,        image = "close.png",    grid=[1,0])


#----------------------------------------------------------------------------------------------------------
 
app.display()
