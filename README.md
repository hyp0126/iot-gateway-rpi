# Home IoT Project (Iot Devices)

## Introduction
The IoT Gateway receive room temperature and humidity from IoT devices, and them send them to IoT Server.<br/>
* Servo motors (X, Y axis)<br/>
* Live streaming camera<br/>

## IoT Gateway
### Raspberry Pi
<p align="center">
<img src="https://github.com/hyp0126/Iot-gateway-rpi/blob/main/RPI_CAM_SG90_2.jpg?raw=true" width="700" />
</p>

## Technologies
* WiFi, Bluetooth, USART<br/>
* Camera, Servo motor<br/>
* MQTT + TLS/SSL

## IoT Devices
### NodeMCU(ESP8266), Arduino Uno
* IoT Device Project: https://github.com/hyp0126/iot-device

## Web Server
* Backend(AWS EC2): mosquitto, Express (https://github.com/hyp0126/react-home-iot)<br/>
* Frontend(GCP VM): React, NGINX (https://github.com/hyp0126/react-home-iot)<br/>

## Test (node-RED)
<p align="center">
<img src="https://github.com/hyp0126/Iot-gateway-rpi/blob/main/node-RED/node-RED.png?raw=true" width="700" />
</p>
