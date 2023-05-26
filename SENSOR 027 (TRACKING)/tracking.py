from machine import Pin
import utime

sensor = Pin(20, Pin.IN)
utime.sleep(2)

while True:
    if sensor.value() == 1:
        print("Libre")
    else:
        print("Línea")
    utime.sleep(2)