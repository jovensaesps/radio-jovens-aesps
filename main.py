import urllib.request
from datetime import datetime
from time import sleep
import vlc


SEMPRETOCAR = True # Colocar True se pretende que toque desde as 8 até às 18
SERVER_IP = "http://172.16.2.241"

def check():
    currenthour = datetime.now().hour
    currentmin = datetime.now().minute

    if SEMPRETOCAR:
        if currenthour >= 8 and currenthour < 18:
            play(18,0)

    req = urllib.request.urlopen(f"{SERVER_IP}/on.html").getcode() # Verificar o status da página on.html; Se for válida (200), tocar!
    while req == 200:
        req = urllib.request.urlopen(f"{SERVER_IP}/on.html").getcode() # Parece repetitivo, mas serve para verificar novamente, após a primeira conexão fechar!
        play(currenthour, currentmin + 5) # tocar 5 min e depois verificar novamente

    if currenthour == 8 and (currentmin < 28):
        play(8,28)

    if currenthour == 10 and (currentmin >= 1 and currentmin < 19):
        play(10,19)
    
    if currenthour == 11 and (currentmin >= 51 and currentmin < 59):
        play(11,59)

    if currenthour == 16 and (currentmin >= 1 and currentmin < 14):
        play(16,14)
    
        


# A função play recebe uma hora e minuto em que deve terminar de trabalhar
def play(hora, min):
    # Implement
    
    #define VLC instance
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    #Define VLC player
    player=instance.media_player_new()

    #Define VLC media
    media=instance.media_new(SERVER_IP + ":8000/airtime_128")

    #Set player media
    player.set_media(media)

    #Play the media
    player.play()    

    while True:
        currenthour = datetime.now().hour
        currentmin = datetime.now().minute
        if currenthour >= hora and currentmin >= min:
            player.stop()
            return True # Terminar a função



while True:
    check()
    sleep(60)




"""

import urllib.request
from datetime import datetime
from time import sleep

from gi.repository import Gst, GLib, GObject


SEMPRETOCAR = True # Colocar True se pretende que toque desde as 8 até às 18
SERVER_IP = "http://172.16.2.241"

def check():
    currenthour = datetime.now().hour
    currentmin = datetime.now().minute

    if SEMPRETOCAR:
        if currenthour >= 8 and currenthour <= 18:
            play(18,0)

    req = urllib.request.urlopen(f"{SERVER_IP}/on.html").getcode() # Verificar o status da página on.html; Se for válida (200), tocar!
    while req == 200:
        req = urllib.request.urlopen(f"{SERVER_IP}/on.html").getcode() # Parece repetitivo, mas serve para verificar novamente, após a primeira conexão fechar!
        play(currenthour, currentmin + 5) # tocar 5 min e depois verificar novamente

    if currenthour == 8 and (currentmin <= 28):
        play(8,28)

    if currenthour == 10 and (currentmin >= 1 and currentmin <= 19):
        play(10,19)
    
    if currenthour == 11 and (currentmin >= 51 and currentmin <= 59):
        play(11,59)

    if currenthour == 16 and (currentmin >= 1 and currentmin <= 14):
        play(16,14)
    
        


# A função play recebe uma hora e minuto em que deve terminar de trabalhar
def play(hora, min):
    # Implement
    Gst.init(None)
    player = Gst.ElementFactory.make("playbin", "player")
    player.set_property("uri", SERVER_IP + ":8000/airtime_128")
    



    print("Playing!")
    

    while True:
        currenthour = datetime.now().hour
        currentmin = datetime.now().minute
        if currenthour >= hora and currentmin >= min:
            print("Stop!")
            return True # Terminar a função



while True:
    check()
    sleep(60)



"""