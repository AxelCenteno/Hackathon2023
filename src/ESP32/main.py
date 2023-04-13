from machine import Pin
from time import sleep

# Configurar el pin al que está conectado el sensor infrarrojo
sensor_pin = Pin(4, Pin.IN)
Led = Pin(2, Pin.OUT)

while True:
    # Leer el valor del pin del sensor infrarrojo
    object_detected = sensor_pin.value()
    Led.off()
    # Mostrar si hay un objeto enfrente o no
    if object_detected:
        print("¡PuertaAaAaA!")
        Led.on()
    else:
        print("¡Todo BIEN!")
        
        
    # Esperar un momento para evitar que el código se ejecute demasiado rápido
    sleep(0.2)
