#JOnathan Lara Segovia 
import machine

sensor_pin = machine.Pin(2, machine.Pin.IN)  # Pin GP2

while True:
    if sensor_pin.value() == 0:
        print("Línea detectada")
    else:
        print("No se detecta línea")
