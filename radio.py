import urllib.request
from datetime import datetime
from time import sleep
import vlc


SEMPRETOCAR = True # Colocar True se pretende que toque desde as 8 até às 18
SERVER_IP = "http://172.16.2.241"


def check():
    currenthour = datetime.now().hour
    currentmin = datetime.now().minute

    #reqoff = urllib.request.urlopen(f"{SERVER_IP}/off.html").getcode() # Verificar se é suposto estar off
    #while reqoff == 200:
    #    reqoff = urllib.request.urlopen(f"{SERVER_IP}/off.html").getcode() 
    #    sleep(60) # durante 1 minuto não toca nada

    if SEMPRETOCAR == True:
        if currenthour >= 8 and currenthour < 18:
            play(18,0)


    if currenthour == 8 and (currentmin < 28):
        play(8,28)

    if currenthour == 10 and (currentmin >= 1 and currentmin < 19):
        play(10,19)
    
    if currenthour == 11 and (currentmin >= 51 and currentmin < 59):
        play(11,59)

    if currenthour == 16 and (currentmin >= 1 and currentmin < 14):
        play(16,14)
    
    #reqon = urllib.request.urlopen(f"{SERVER_IP}/on.html").getcode() # Verificar o status da página on.html; Se for válida (200), tocar!
    #while reqon == 200:
    #    reqon = urllib.request.urlopen(f"{SERVER_IP}/on.html").getcode() # Parece repetitivo, mas serve para verificar novamente, após a primeira conexão fechar!
    #    play(currenthour, currentmin + 5) # tocar 5 min e depois verificar novamente
    
        


# A função play recebe uma hora e minuto em que deve terminar de trabalhar
def play(hora, min):

    # -----  VLC CODE ------ Colocado aqui para ser mais resiliente no caso de a conexão falhar num certo intervalo. - > Volta a executar o mesmo código
    #definir a VLC instancia
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    #Definir o player VLC
    player = instance.media_player_new()

    #Definir o VLC media
    media = instance.media_new(SERVER_IP + ":8000/airtime_128")

    #Definir a "media" do player
    player.set_media(media)

    # Tocar a Rádio
    player.play()    

    while True:
        currenthour = datetime.now().hour
        currentmin = datetime.now().minute
        if currenthour >= hora and currentmin >= min:
            player.stop()
            return True # Terminar a função


while True:
    diadasemana = datetime.now().weekday()
    if diadasemana < 5: # Se não for sábado ou domingo, trabalhar!
        check()
        sleep(60)
    else:
        sleep(21600) # Esperar 6 horas (É funcional, pois na segunda o programa apenas precisa de começar às 8:00, logo, mesmo que este código execute à meia noite de domingo, às 6h já estará funcional)