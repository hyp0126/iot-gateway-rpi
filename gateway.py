
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
import constants
from subprocess import check_output
from re import findall

def get_cputemp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

Broker = constants.MQTT_HOST

while os.system("ls /dev/rfcomm0"):
    print("wait rfcomm0")
    sleep(1000)

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
 
client = mqtt.Client()
client.username_pw_set(username=constants.MQTT_USER, password=constants.MQTT_PASSWORD)
client.connect(Broker, 1883, 60)
client.loop_start()

while True:
    input = str(bluetoothSerial.readline(), "ascii")
    print(input)
    inputs = input.split('/')
    topic = '/'.join(inputs[0:len(inputs)-1])
    client.publish(topic, inputs[len(inputs)-1])
    print(inputs)
    topic = "home/rpi/cputemperature"
    temp = get_cputemp()
    client.publish(topic, temp)
    print(topic+'/'+temp)

