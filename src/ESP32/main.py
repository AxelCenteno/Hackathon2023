from machine import Pin, ADC, UART
from time import sleep
#Puerta infrarrojo
sensor_pin = Pin(4, Pin.IN) # Configurar el pin al que está conectado el sensor infrarrojo

#GAS
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
p2 = Pin(2, Pin.OUT)

#GPS
gpsModule = UART(2, baudrate=9600)
p2 = Pin(2, Pin.OUT)

while True:
    #LED infrarojo
    object_detected = sensor_pin.value() # Leer el valor del pin del sensor infrarrojo
    if object_detected:
        print("¡PuertaAaAaA!")
    else:
        print("¡Todo BIEN!")
    sleep(0.2)
    ## GPS
    # read from UART
    gpsModule.readline()
    data = str(gpsModule.readline())
    #data = gps.read()
    p2.off()
    #Gas
    pot_value = pot.read()

    print(pot_value)
    p2.on()
    sleep(0.1)
    # check if data is not empty
    if data:
        # convert bytes to string and print
        print(data)
        #print(data.decode('utf-8'))
        p2.on()
        #print('Data')
        sleep(0.3)

