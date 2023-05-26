import machine
import utime

# Configuración de pines
sound_pin = machine.Pin(26)  # Pin GPIO26 (D26) para la entrada del sensor de sonido (OUT)
adc = machine.ADC(0)  # Configurar el ADC en el canal 0
umbral = 1650  # Ajusta el umbral según tus necesidades

# Función para detectar sonido
def detectar_sonido(pin):
    valor_analogico = adc.read_u16()
    if valor_analogico > umbral:
        print("¡Sonido detectado!")
    else:
        print("No se detecta sonido")

# Bucle principal
while True:
    detectar_sonido(sound_pin)
    utime.sleep(2)  # Esperar 2 segundos antes de la próxima detección de sonido
