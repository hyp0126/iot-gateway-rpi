# Iot-gateway-rpi
1. ARDUINO UNO + Temperature sensor + HC-06(Bluetooth) -> rpi (BT to MQTT) -> rpi (Mosquitto, Node-RED) 

2. ARDUINO UNO + Temperature sensor + HC-06(Bluetooth) -> rpi (BT to MQTT) -> GCP (Ubuntu: Mosquitto, Node-RED) 

3. UNO BT -> rpi (BT to MQTT) -> (TLS/SSL) -> GCP (Compute Engine: Mosquitto) -> GCP (Node-RED / https)
