"""
1.BT Serial -> MQTT Broker
 rpi: python3
 HC-06: Paring password: 1234
 sudo apt-get install python-serial
 sudo pip3 install paho-mqtt
 Connect BT: sudo rfcomm connect hci0 98:D3:32:20:6C:CE
 TLS: port 8883

2.rpi CPU Temp -> MQTT Broker

3.MQTT Broker -> rpi servo (cameara)
 Ref: http://abyz.me.uk/rpi/pigpio/
 Install Lib.
   wget https://github.com/joan2937/pigpio/archive/master.zip
   unzip master.zip
   cd pigpio-master
   make
   sudo make install
 start daemon: sudo pigpiod
 stop daemon: sudo killall pigpiod
 GPIO 17 - UP/DOWN
 GPIO 27 - LEFT/RIGHT
"""

import serial
from time import sleep
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import os
import constants
from subprocess import check_output
from re import findall
import pigpio

Broker = constants.MQTT_HOST

# Servo pin, time
VERTICAL_SERVO_PIN = 17
HORIZONTAL_SERVO_PIN = 27
MIN_WIDTH = 1000
MAX_WIDTH = 2000
STEP = 50

# Servo output width
v_width = 1500 # Vertical Center
h_width = 1500 # Horizontal Center

def get_cputemp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

# connect localhost PIGPIO
pi = pigpio.pi()

if not pi.connected:
    print("pigpio not connected")
    exit()
    
# connect BT serial
# Wait until being connected
while os.system("ls /dev/rfcomm0"):
    print("wait rfcomm0")
    sleep(1)

bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
print("rfcomm0 connected")
 
# MQTT Broker settings
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected")
    client.subscribe("home/camera1/camcontrol")

def on_message(client, userdata, msg):
    global v_width
    global h_width

    print(msg.topic+" "+str(msg.payload))
    cmd = msg.payload
    if (cmd == b'd'):
        v_width += STEP
    if (cmd == b'u'):
        v_width -= STEP
    if (cmd == b'l'):
        h_width += STEP
    if (cmd == b'r'):
        h_width -= STEP
    if (cmd == b'c'):
        v_width = 1500
        h_width = 1500

    # Limit
    if (v_width < MIN_WIDTH):
        v_width = MIN_WIDTH
    if (v_width > MAX_WIDTH):
        v_width = MAX_WIDTH
    if (h_width < MIN_WIDTH):
        h_width = MIN_WIDTH
    if (h_width > MAX_WIDTH):
        h_width = MAX_WIDTH
       
    pi.set_servo_pulsewidth(VERTICAL_SERVO_PIN, v_width)
    pi.set_servo_pulsewidth(HORIZONTAL_SERVO_PIN, h_width)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=constants.MQTT_USER, password=constants.MQTT_PASSWORD)
client.tls_set('certs/ca.crt')
#client.connect(Broker, 1883, 60)
client.connect(Broker, 8883, 60)
client.loop_start()

while True:
    try:
        if(bluetoothSerial.inWaiting != 0):
            input = str(bluetoothSerial.readline(), "ascii")
            print(input)
            inputs = input.split('/')
            topic = '/'.join(inputs[0:len(inputs)-1])
            client.publish(topic, inputs[len(inputs)-1])
            print(inputs)
            topic = "home/gateway/cputemp"
            temp = get_cputemp()
            client.publish(topic, temp)
            print(topic+'/'+temp)
    except KeyboardInterrupt:
        break
    
print("Exit")
# Stop Servo
pi.set_servo_pulsewidth(VERTICAL_SERVO_PIN, 0)
pi.set_servo_pulsewidth(HORIZONTAL_SERVO_PIN, 0)

# Disconnect PIGPIO
pi.stop()
