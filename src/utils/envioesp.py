#Conexion con Azure IoTHub
from azure.iot.device import IoTHubDeviceClient, Message
import json

import serial

# Configuración del puerto serial

port = '/dev/COM#' # Cambiar a puerto serie
baudrate = 115200


# Conectar al puerto serial
ser = serial.Serial(port, baudrate)

line = ser.readline()

# Convertir los datos a un diccionario
data = {"value": line.strip().decode()}

# Configuracion IoT Hub
CONNECTION_STRING = ""
device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
device_client.connect()

#Mensaje

mesg = Message(data)

#Propiedades del Mensaje
mesg.content_encoding = "utf-8"
mesg.content_type = "application/json"
device_client.send_message(mesg)

#Cierra la conexion con Azure
device_client.disconnect()