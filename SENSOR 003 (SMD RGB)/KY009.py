# Jonathan Lara Segovia 

import machine

sensor_pin = machine.ADC(26)  # El pin ADC utilizado es el GPIO 26

def read_color():
    red = sensor_pin.read_u16()
    green = sensor_pin.read_u16()
    blue = sensor_pin.read_u16()
    return red, green, blue

while True:
    red_value, green_value, blue_value = read_color()
    print("Valor de color: R={}, G={}, B={}".format(red_value, green_value, blue_value))
