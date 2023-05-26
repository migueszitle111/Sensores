# Importar los módulos importantes - Pin, ADC y Utime
import ssd1306
from picozero import pico_led
from machine import Pin, ADC
import utime

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
buzzer = machine.Pin(5, machine.Pin.OUT) # Asigna el Pin 5 como salida

utime.sleep(0.1)

# Crea las variables x y yAxis. Luego, asignarlas a los pines GPIO. xAxis se asignará al pin 27 y yAxis se asignará al pin 26. 
xAxis = ADC (Pin (27))
yAxis = ADC (Pin (26))

#  Crea una variable de botón. Esto ayuda a alternar el joystick y a enviar señales.
button = Pin (16,Pin.IN, Pin.PULL_UP)

# Comprueba e imprime el valor de x, y y botón a través de un bucle continuo. 
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value ()
    xStatus = "M"
    yStatus = "M"
    buttonStatus = "NP"
    # etiquetar el estado del joystick y de los botones dentro del bucle mediante sentencias if/then.
    if xValue <= 600:
        xStatus = "I"
        pico_led.on()
        buzzer.on() # Enciende el buzzer
        utime.sleep(0.1)
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        utime.sleep(0.1)
    elif xValue >= 60000:
        xStatus = "D"
        pico_led.on()
        buzzer.on() # Enciende el buzzer
        utime.sleep(0.1)
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        utime.sleep(0.1)
    if yValue <= 600:
        yStatus = "Ar"
        pico_led.on()
        buzzer.on() # Enciende el buzzer
        utime.sleep(0.1)
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        utime.sleep(0.1)
    elif yValue >= 60000:
        yStatus = "Ab"
        pico_led.on()
        buzzer.on() # Enciende el buzzer
        utime.sleep(0.1)
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        utime.sleep(0.1)
    if buttonValue == 0:
        buttonStatus = "P"
        pico_led.on()
        buzzer.on() # Enciende el buzzer
        utime.sleep(0.1)
        pico_led.off()
        buzzer.off() # Apaga el buzzer
        utime.sleep(0.1)
      # por encima del comando sleep, se escribe una sentencia print para mostrar las variables.
      
    display.fill(0)
    display.text("X: " + xStatus + ", Y: " + yStatus + " -- " + buttonStatus, 0, 0)
    display.show()

    utime.sleep(0.1)
