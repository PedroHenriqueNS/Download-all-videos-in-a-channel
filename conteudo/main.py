from datetime import date, time, datetime
from xmlrpc.client import boolean
from pytube import YouTube, Channel, Playlist, exceptions
from importlib.resources import path

import os

#url = input('Link do video')
#path = input('path: ')

#yt = YouTube(url)

# infoVideo = {
#     "Titulo": yt.title,
#     "Número de views": yt.views,
#     "Tamanho do vídeo": yt.length,
#     "Aaliação do vídeo": yt.rating
# }

# print(infoVideo)

# ys = yt.streams.get_highest_resolution()

#print('Baixando...')

#ys.download(path)

#print('Download concluído!!')

def verificarExistencia(titulo) -> boolean:
    actualPath = os.getcwd()
    path = actualPath + r"\Videos\{titulo}.mp4"

    return os.path.exists(path)

def downloadVideo(url, path):
    yt = YouTube(url)
    infoVideo = {
        "Titulo": yt.title,
        "Descrição": yt.description,
        #"Número de views": yt.views,
        #"Tamanho do vídeo": yt.length,
        #"Avaliação do vídeo": yt.rating
    }
    #print(infoVideo)

    data = yt.publish_date
    strData = str(data.year) + "-" + str(data.month) + "-" + str(data.day) + " -- "
    #print(strData)

    if verificarExistencia(infoVideo["Titulo"]) == False:

        try:
            ys = yt.streams.get_highest_resolution()
            print(f'Baixando ({infoVideo["Titulo"]}) | Por favor aguarde')
            ys.download(path, filename_prefix=strData)

        except:
            print("Erro: video está ao vivo ou não está disponível")

    else:
        print("Erro: este vídeo já foi baixado.")

#def verificar


c = Channel('https://www.youtube.com/c/CanalBarueriLive')
path = os.getcwd() + "\Videos"

for url in c.video_urls:
    downloadVideo(url, path)