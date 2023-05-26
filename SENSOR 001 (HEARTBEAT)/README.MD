# KY-039 Heartbeat Sensor <img src="logo.jfif" alt="diagrama" width="200"/>

El KY-039 Heartbeat Sensor es un módulo utilizado para medir la frecuencia cardíaca a través de la detección de pulsos sanguíneos. Es ampliamente utilizado en proyectos de monitoreo de salud y aplicaciones relacionadas con la frecuencia cardíaca.

## Características

- Permite la medición de la frecuencia cardíaca a través de los pulsos sanguíneos.
- Salida analógica que proporciona una señal proporcional a la frecuencia cardíaca.
- Fácil de integrar con microcontroladores y placas de desarrollo.
- Bajo consumo de energía.

## Conexiones

El KY-039 Heartbeat Sensor se puede conectar a una placa de desarrollo o microcontrolador utilizando los siguientes pines:

- VCC: Conectar a la alimentación de 5V.
- GND: Conectar a la tierra (GND).
- OUT: Proporciona una señal analógica que representa la frecuencia cardíaca medida.

## Uso

1. Conecta el KY-039 Heartbeat Sensor a tu placa de desarrollo o microcontrolador según las conexiones mencionadas anteriormente.

2. Configura tu placa de desarrollo o microcontrolador para leer la señal analógica del pin OUT del KY-039.

3. Realiza la conversión necesaria de la señal analógica a la frecuencia cardíaca según la resolución del sensor y el rango de frecuencia deseado.

4. Realiza las acciones necesarias basadas en la frecuencia cardíaca medida, como mostrarla en una pantalla, enviarla a un servidor o activar una alarma, entre otras posibilidades.

## Ejemplo de código

Aquí tienes un ejemplo básico de código en Arduino para leer la frecuencia cardíaca medida por el KY-039 Heartbeat Sensor:

```arduino
int sensorPin = A0;
int heartRate;

void setup() {
  Serial.begin(9600);
}

void loop() {
  heartRate = analogRead(sensorPin);
  Serial.print("Heart Rate: ");
  Serial.println(heartRate);
  delay(1000);
}

