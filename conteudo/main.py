from datetime import date, time, datetime
from xmlrpc.client import boolean
from pytube import YouTube, Channel, Playlist, exceptions
from importlib.resources import path

import os

def start_verificarPastaVideos():
    actualPath = os.getcwd()
    path = actualPath + r"\Videos"

    return os.path.exists(path)

def criarPastaVideos():
    actualPath = os.getcwd()
    path = actualPath + r"\Videos"
    
    os.mkdir(path)

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

if start_verificarPastaVideos() == False:
    criarPastaVideos()

c = Channel('LINK DO CANAL DO YOUTUBE') ## TODO: Substitua com o link de um canal do YouTube
path = os.getcwd() + "\Videos"

for url in c.video_urls:
    downloadVideo(url, path)