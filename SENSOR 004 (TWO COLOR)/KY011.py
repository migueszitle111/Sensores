#Jonathan Lara Segovia 

import machine
import utime

sensor_pin = machine.Pin(7, machine.Pin.IN)

while True:
    if sensor_pin.value() == 0:
        print("Detectado color Rojo")
    else:
        print("Detectado color Verde")
    
    utime.sleep(1)
