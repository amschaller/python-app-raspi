import json
import math
import time
import paho.mqtt.client as mqtt 
import socket
import time
import grovepi

timestamp = math.trunc(time.time())
localhost = socket.gethostbyname(socket.gethostname())
print (localhost)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_publish(client, userdata, mid):
    print("Message published")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# connect to localhost
print("Connecting to server")
client.connect(localhost)

# starting loop
client.loop_start()
print ("Starting for loop")


# Connect the Grove Light Sensor to analog port A0
light_sensor = 0
grovepi.pinMode(light_sensor, "INPUT")

for i in range(1,20):

	sensor_value = grovepi.analogRead(light_sensor)
	print "temperature value = %d: ", sensor_value
	client.publish("TestTopic1", sensor_value)
	sleep(60)
	

client.loop_stop()

