#!/usr/bin/env python

###
## Bridge between EPICS and MQTT
####################################

from datetime import datetime
from pcaspy import Driver, SimpleServer
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

###
# MQTT brocker and topics
###
MQTT_SERVER = "129.129.130.80"
MQTT_TOPIC_01 = "data"
MQTT_TOPIC_02 = "test"


###
# Epics definitions
###
prefix = 'MTEST:'
pvdb = {
    'DATA' : {
	'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'TEST' : {
        'type' : 'string',
        'scan' : 0.2,
    },
}

###
# Global variables to store the values for the bridge
###
msgData = ""
msgTest = ""

class myDriver(Driver):
    def  __init__(self):
        super(myDriver, self).__init__()

    def read(self, reason):
        if reason == 'DATA':
           global msgData
	   value = str(msgData)
        elif reason == 'TEST':
           global msgTest
           value = msgTest
	else:
	   value.self.getParam(reason)
	return value

    def write(self, reason, value):
        status = True
        if reason == 'DATA':
           global msgData
           msgData = value
           publish.single(MQTT_TOPIC_01, msgData, hostname=MQTT_SERVER)
	
	if reason == 'TEST':
	   global msgTest
	   msgTest = value
           publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER)
        if status:
           self.setParam(reason, value)

        return status


if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = myDriver()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC_01)
    client.subscribe(MQTT_TOPIC_02)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "data":
        global msgData 
	msgData = datetime.utcfromtimestamp(int(msg.payload[0:10])).strftime('%Y-%m-%d %H:%M:%S')
        #msgData = str(msg.payload)

    elif msg.topic == "test":
	global msgTest
	msgTest = msg.payload
    else:
        print("unknown topic: "+msg.topic)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()
#client.loop_forever()

while True:
	server.process(0.1)

