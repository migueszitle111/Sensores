# Codigo hecho y verificado por Alvarez Espinoza Raul - 18212141
import ssd1306
from picozero import pico_led
from machine import Pin, ADC
import time
import utime

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

buzzer = machine.Pin(5, machine.Pin.OUT) # Asigna el Pin 5 como salida

digital = Pin(18, Pin.IN)
analog = ADC(26)

while True:
    
    display.fill(0)
    display.text(str(digital.value()) + ' - ' + str(analog.read_u16()), 0, 0)
    display.show()
    buzzer.on() # Enciende el buzzer
    pico_led.on()
    utime.sleep(0.1)
    buzzer.off() # Apaga el buzzer
    pico_led.off()
    utime.sleep(0.1)
    time.sleep(1)
