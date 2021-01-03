# Iot-gateway-rpi

<p align="center">
<img src="https://github.com/hyp0126/Iot-gateway-rpi/blob/main/RPI_CAM_SG90_2.jpg?raw=true" width="700" />
</p>

1. ARDUINO UNO + Temperature sensor + HC-06(Bluetooth) -> <b>rpi (BT to MQTT)</b> -> rpi (Mosquitto, Node-RED) 

2. ARDUINO UNO + Temperature sensor + HC-06(Bluetooth) -> <b>rpi (BT to MQTT)</b> -> GCP (Ubuntu: Mosquitto, Node-RED) 

3. UNO BT -> <b>rpi (BT to MQTT)</b> -> (TLS/SSL) -> GCP (Compute Engine: Mosquitto) -> GCP (Node-RED / https)

4. <b>rpi (Node-RED)</b> -> GCP (Mosquitto) -> rpi SG90 (Servo)
