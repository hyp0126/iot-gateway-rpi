#rpi: python3
#HC-06: Paring password: 1234
#sudo apt-get install python-serial
#sudo pip3 install paho-mqtt
#Connect BT: sudo rfcomm connect hci0 98:D3:32:20:6C:CE

import serial
from time import sleep
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import os

Broker = "localhost"

while os.system("ls /dev/rfcomm0"):
    print("wait rfcomm0")
    sleep(1000)

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
 
client = mqtt.Client()
client.connect(Broker, 1883, 60)
client.loop_start()

while True:
    input = str(bluetoothSerial.readline(), "ascii")
    print(input)
    inputs = input.split('/')
    topic = '/'.join(inputs[0:len(inputs)-1])
    client.publish(topic, inputs[len(inputs)-1])
    print(inputs)
