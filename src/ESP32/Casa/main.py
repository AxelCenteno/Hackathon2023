## ESP32 Modulos de gas y puerta
from machine import Pin, ADC
from time import sleep
#Puerta infrarrojo
sensor_pin = Pin(4, Pin.IN) # Configurar el pin al que está conectado el sensor infrarrojo

#GAS
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
p2 = Pin(2, Pin.OUT)

while True:
    p2.off()
    #LED infrarojo
    object_detected = sensor_pin.value() # Leer el valor del pin del sensor infrarrojo
    if object_detected:
        print("¡PuertaAaAaA!")
    else:
        print("¡Todo BIEN!")
        sleep(0.2)
    
    #Gas
    pot_value = pot.read()

    print(pot_value)
    sleep(0.2)
    


