# Jonathan Lara segovia 
import machine
import time

relay_pin = machine.Pin(7, machine.Pin.OUT)  # Configura el pin del relé como salida

while True:
    relay_pin.on()  # Enciende el relé
    print("Relé encendido")
    time.sleep(1)  # Espera 1 segundo
    
    relay_pin.off()  # Apaga el relé
    print("Relé apagado")
    time.sleep(1)  # Espera 1 segundo
