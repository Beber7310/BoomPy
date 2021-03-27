'''
Created on 27 mars 2021

@author: bdosd
'''
from guizero import App,Box,PushButton,os
 
import platform

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

#app = App(title="Hello world",layout="grid")
app = App(title="Hello world")

if(platform.system()=="Linux"):
    app.set_full_screen()

if(platform.system()=="Windows"):
    app.width=1280
    app.height=600

box_radio = Box(app, width="fill", align="top",layout="grid")
box_home  = Box(app, width="fill", align="bottom")


update_text = PushButton(box_home, command=radio_france_culture, image = "home.png",text="Back", align="bottom")

update_text = PushButton(box_radio, command=radio_fip,image = "fip.png", text="fip",grid=[0,0])
update_text = PushButton(box_radio, command=radio_france_inter, image = "franceinter.png",text="france inter",grid=[1,0])
update_text = PushButton(box_radio, command=radio_france_culture, image = "franceculture.png",text="france culture",grid=[2,0])


app.display()
