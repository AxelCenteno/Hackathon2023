from azure.storage.blob import BlobServiceClient, BlobClient

import random
from datetime import time
import requests
import pyaudio
import pydub
import numpy as np
from pytube import YouTube

pytube = 

#Funcion obtiene la hora aleatoria para reproducir musica
def horarepro(rtime1 = time(),rtime2 = time(),rtime3 = time(),i=0):
    
    while i != 3:
        random_time = time(random.randrange(24), random.randrange(60), random.randrange(60))
        if random_time < time(12,0,0) and random_time > time(8,0,0):
            rtime1 = random_time
            i=i+1
        elif random_time <  time(16,0,0) and random_time > time(12,0,0):
            rtime2 = random_time
            i=i+1
        elif random_time < time(22,0,0) and random_time > time(16,0,0):
            rtime3 = random_time
            i=i+1
        else:
                print("Hora no admitida")
        
    return rtime1,rtime2,rtime3

#Funcion obtiene la cancion de azure
def stream_music(url):
    response = requests.get(url, stream=True)
    return response.iter_content(chunk_size=1024)

seleccion = 1 #Introducir alerta de Azure

#Situaciones de reproduccion
if seleccion == 1:
    #Situacion accion audio cuidador
    p1 = pyaudio.PyAudio()
    stream1 = p1.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)        
    #Ejecuta stream de canciones
    for data in stream_music("url"):
         stream1.write(data)

    stream1.stop_stream()
    stream1.close()
    p1.terminate()
    print("Reproduciendo audio")

elif seleccion == 2:
    # Caso Reproduccion de Instruccion de como Ejecutar cierta accion
        #Situacion accion audio cuidador
    p2 = pyaudio.PyAudio()
    stream2 = p2.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)        
    #Ejecuta stream de canciones
    for data in stream_music("url"):
         stream2.write(data)

    stream2.stop_stream()
    stream2.close()
    p2.terminate()
    print("Reproduciendo audio")

# Caso Reproduccion de Musica Aleatoria Durante el Dia
rtime1,rtime2,rtime3=horarepro()

songs = np.array(["url de cada cancion","", "", "", "url"])

while int (f := 0) != 3:
    if rtime1 == time.now() or rtime2 == time.now() or rtime3 == time.now():
        
        #Obtiene la cancion de Youtube
        yt = YouTube(songs[x:=0])
        audio = yt.streams.filter(only_audio=True).first().stream_to_buffer()
        audio_bytes = audio.read()
        audio_data = AudioSegment.from_file(io.BytesIO(audio_bytes), format='webm')

        # Reproducir el audio
        play(audio_data)
        x+=1
        f+=1
    else:
        print("No es hora de musica")



