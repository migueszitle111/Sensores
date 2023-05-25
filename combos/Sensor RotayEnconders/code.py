import ssd1306
from picozero import pico_led
import machine
import utime

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

buzzer = machine.Pin(5, machine.Pin.OUT) # Asigna el Pin 5 como salida

# Pines del Rotary Encoder
clk_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
dt_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Variables para almacenar el estado anterior de los pines
prev_clk_state = clk_pin.value()
prev_dt_state = dt_pin.value()

# Variable para almacenar la posición actual del encoder
encoder_pos = 0

# Función de interrupción para manejar los cambios del Rotary Encoder
def handle_interrupt(pin):
    global encoder_pos, prev_clk_state, prev_dt_state

    clk_state = clk_pin.value()
    dt_state = dt_pin.value()

    if dt_state != prev_dt_state:
        if clk_state != dt_state:
            encoder_pos += 1
        else:
            encoder_pos -= 1

        buzzer.on() # Enciende el buzzer
        pico_led.on()
        utime.sleep(0.1)
        display.fill(0)
        display.text("Position:", 0, 0)
        display.text(str(encoder_pos), 0, 10)
        display.show()
        buzzer.off()
        pico_led.off()
        utime.sleep(0.1)

    prev_clk_state = clk_state
    prev_dt_state = dt_state

# Configurar interrupciones en los pines del Rotary Encoder
clk_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_interrupt)
dt_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_interrupt)

# Bucle principal
while True:
    utime.sleep(1)
