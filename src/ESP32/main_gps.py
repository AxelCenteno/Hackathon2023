## ESP32 GPS Module

from machine import UART, Pin 
from time import sleep

gpsModule = UART(2, baudrate=9600) 

buff = bytearray(255)

p2 = Pin(2, Pin.OUT)

latitude = ""
longitude = ""
satellites = ""
GPStime = ""

while True:
    # read from UART 
    gpsModule.readline()
    buff = str(gpsModule.readline())
    data = str(gpsModule.readline())
    
    parts = buff.split(',')
    
    if ((parts[0] == "b'$GPGGA")):
        print(buff)