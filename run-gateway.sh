#!/bin/bash
sudo rfcomm connect hci0 98:D3:32:20:6C:CE &
python3 /home/pi/iot-gateway-rpi/gateway.py
