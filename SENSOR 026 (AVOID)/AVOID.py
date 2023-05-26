from machine import Pin
import utime

sensor = Pin(15, Pin.IN)

while True:
    if sensor.value() == 1:
        print("Obstáculo no detectado")
    else:
        print("Obstáculo detectado")
    utime.sleep_ms(500)
