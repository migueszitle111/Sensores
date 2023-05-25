import machine
import utime

tap_pin = machine.ADC(0)

sensor_value = tap_pin.read_u16()

print("Valor del sensor KY-010:", sensor_value)
