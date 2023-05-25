while True:
    if sensor_pin.value() == 1:
        print("Campo magnético detectado")
    else:
        print("Campo magnético no detectado")
    utime.sleep(0.1)  # Espera breve para evitar lecturas repetitivas
