import machine
import ssd1306
import time
from machine import Pin
from libx import NEC_16
from picozero import pico_led
from time import sleep

buzzer = machine.Pin(5, machine.Pin.OUT) # Asigna el Pin 5 como salida

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        #print('Data {:02x} Addr {:04x}'.format(data, addr))
        # Clear the display buffer
        display.fill(0)
        display.show()

        # Write some text to the display
        display.text('Data {:02x} Addr {:04x}'.format(data, addr), 0, 0)
        display.show()
        
        pico_led.on()
        buzzer.on() # Enciende el buzzer
        time.sleep(0.5) # Espera 0.5 segundos
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        time.sleep(0.5) # Espera 0.5 segundos

ir = NEC_16(Pin(28, Pin.IN), callback)


# Initialize I2C bus and SSD1306 display
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
