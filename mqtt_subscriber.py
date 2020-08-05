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
MQTT_TOPIC_03 = "fill"
MQTT_TOPIC_04 = "v1"
MQTT_TOPIC_05 = "v2"
MQTT_TOPIC_06 = "v3"


###
# Epics definitions
###
prefix = 'X10DA-ES-GMS:'
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
    'FILL' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V1' : {
        'type' : 'int',
        'scan' : 0.2,
        'prec' : 5,
    },
    'V2' : {
        'type' : 'int',
        'scan' : 0.2,
        'prec' : 5,
    },
    'V3' : {
        'type' : 'int',
        'scan' : 0.2,
        'prec' : 5,
    },

}

###
# Global variables to store the values for the bridge
###
msgData = ""
msgTest = ""
msgFill = 0
msgV1 = 0
msgV2 = 0
msgV3 = 0

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
        elif reason == 'FILL':
           global msgFill
           value = msgFill
	elif reason == 'V1':
           global msgV1
           value = msgV1
	elif reason == 'V2':
           global msgV2
           value = msgV2
	elif reason == 'V3':
           global msgV3
           value = msgV3
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

	if reason == 'FILL':
           global msgFill
           msgFill = value
           publish.single(MQTT_TOPIC_03, msgFill, hostname=MQTT_SERVER)
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
    client.subscribe(MQTT_TOPIC_03)
    client.subscribe(MQTT_TOPIC_04)
    client.subscribe(MQTT_TOPIC_05)
    client.subscribe(MQTT_TOPIC_06)

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
    
    elif msg.topic == "fill":
        global msgFill
        msgFill = int(msg.payload)

    elif msg.topic == "v1":
        global msgV1
        msgV1 = int(msg.payload)
    elif msg.topic == "v2":
        global msgV2
        msgV2 = int(msg.payload)
    elif msg.topic == "v3":
        global msgV3
        msgV3 = int(msg.payload)

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

