import machine
import time
import math

sensor_pin = machine.ADC(26)

while True:
    sensor_value = sensor_pin.read_u16()
    voltage = sensor_value * 3.3 / (2**16)
    resistance = (3.3 - voltage) * 10000 / voltage
    temperature = 1 / (1 / 298.15 + 1 / 3435 * (math.log(resistance / 10000) / math.log(10) + 1 / 25))
    print("Temperature: {:.2f} °C".format(temperature))
    time.sleep(1)
