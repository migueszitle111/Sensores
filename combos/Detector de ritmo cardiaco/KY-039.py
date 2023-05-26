import ssd1306
from picozero import pico_led
from machine import ADC
from utime import sleep

sensor = ADC(26)

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

conversion_factor = 3.3 / (65535)

while True:
    lectura = sensor.read_u16() * conversion_factor
    
    pico_led.on()
    sleep(0.1)
    display.fill(0)
    display.text(str(lectura), 0, 0)
    display.show()
    pico_led.off()
    sleep(0.1)
