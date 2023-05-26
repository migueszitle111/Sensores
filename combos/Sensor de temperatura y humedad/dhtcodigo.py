import ssd1306
from machine import Pin
import utime 
from dht import DHT11

dhtPin = Pin(20, Pin.IN , Pin.PULL_DOWN)

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)



while True:
    dhtSensor = DHT11(dhtPin)
    
    temp_value = dhtSensor.temperature
    
    hum_value = dhtSensor.humidity
    
    display.fill(0)  # Limpiar la pantalla
    display.text("Temp: {}C".format(temp_value), 0, 0)
    display.text("Humidity: {}%".format(hum_value), 0, 10)
    display.show()
    utime.sleep(2)

