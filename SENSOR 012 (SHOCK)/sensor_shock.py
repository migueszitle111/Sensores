import machine

shock_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if shock_pin.value() == 1:
        print("¡Se detectó un golpe o vibración!")
    else:
        print("Sin golpe o vibración.")
