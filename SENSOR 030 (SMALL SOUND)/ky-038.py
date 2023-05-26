import machine

adc = machine.ADC(machine.Pin(26))  # Configura el pin GP26 como entrada analógica

while True:
    sound_value = adc.read_u16()  # Lee el valor analógico del pin ADC
    print("Valor de sonido:", sound_value)

