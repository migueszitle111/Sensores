#Jonathan Lara Segovia 
import machine

button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

def button_pressed(pin):
    print("Botón presionado")

button_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed)

while True:
    pass
