import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "\static\grabacion.wav" #si no funciona quitar static

audio = pyaudio.PyAudio()

# Configura la grabación
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Grabando...")
frames = []

# Graba el audio
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Fin de la grabación")

# Detiene la grabación y libera los recursos
stream.stop_stream()
stream.close()
audio.terminate()

# Guarda la grabación en un archivo WAV
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

#Subir audio a Azure
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Configura la conexión con Azure Blob Storage
connect_str = '<Tu cadena de conexión a Azure Blob Storage>'
container_name = '<Nombre del contenedor>'
blob_name = '<Nombre del archivo de audio en Azure>'

# Crea un cliente de servicio de blobs
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Crea un cliente de contenedor
container_client = blob_service_client.get_container_client(container_name)

# Sube el archivo de audio a Azure Blob Storage
with open('<Ruta del archivo de audio local>', 'rb') as data:
    container_client.upload_blob(name=blob_name, data=data)
    
print('Archivo de audio subido exitosamente a Azure Blob Storage')
