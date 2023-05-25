import machine
import utime

relay_pin = machine.Pin(0, machine.Pin.OUT)

relay_pin.value(1)

relay_pin.value(0)

relay_pin.value(1)  # Activa el relé
utime.sleep(2)     # Espera 2 segundos
relay_pin.value(0)  # Desactiva el relé
