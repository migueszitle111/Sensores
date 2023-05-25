#JOnathan Lara Segovia 
import machine

sensor_pin = machine.Pin(7, machine.Pin.IN)

def detect_line():
    return sensor_pin.value()

while True:
    if detect_line():
        print("Línea detectada")
    else:
        print("No se detecta línea")
