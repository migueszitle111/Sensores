# JOnathan Lara Segovia #19210515

from machine import Pin
import time


sensorPin = Pin(19, Pin.OUT)

while(True):
    print("Prendido")
    sensorPin.on()
    time.sleep(1)
    sensorPin.off()
    print("Apagado")
    time.sleep(1)
