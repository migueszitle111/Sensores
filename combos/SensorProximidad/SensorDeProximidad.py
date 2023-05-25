import ssd1306
from picozero import pico_led
from machine import Pin
import utime

buzzer = machine.Pin(5, machine.Pin.OUT) # Asigna el Pin 5 como salida

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

sensor = Pin(18, Pin.IN)
utime.sleep(0.1)

while True:
# Se imprime un mensaje en función del valor del sensor
    if sensor.value() == 1:
        display.fill(0)
        display.text("Libre", 0, 0)
        display.show()
    else:
        display.fill(0)
        buzzer.on() # Enciende el buzzer
        utime.sleep(0.5)
        pico_led.on()
        display.text("Detectado", 0, 0)
        display.show()
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        utime.sleep(0.5)
