#Luis
import machine

# Configuración del pin de entrada para el sensor KY-010
sensor_pin = machine.Pin(16, machine.Pin.IN)

# Bucle principal
while True:
    # Leer el valor del sensor
    sensor_value = sensor_pin.value()

    # Verificar si el sensor está bloqueado o no
    if sensor_value == 0:
        print("Sensor bloqueado")
    else:
        print("Sensor desbloqueado")
  
