#!/usr/bin/env python

###
## Bridge between EPICS and MQTT
####################################

from pcaspy import Driver, SimpleServer 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from pyxtension.Json import Json
from epicsDefinition import *
from variables import *
from epicsDriver import *	

###
# MQTT brocker and topics
###
MQTT_SERVER = "129.129.130.80"
MQTT_TOPIC_01 = "dataV"
MQTT_TOPIC_02 = "dataP"
MQTT_TOPIC_03 = "dataC"

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    myDriver()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC_01)
    client.subscribe(MQTT_TOPIC_02)
    client.subscribe(MQTT_TOPIC_03)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "data":
        global msgData 
	msgData = datetime.utcfromtimestamp(int(msg.payload[0:10])).strftime('%Y-%m-%d %H:%M:%S')
        #msgData = str(msg.payload)

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

    elif msg.topic == "dataP":
        global msgDataP, pressure1, pressure2, pressureSP
        msgDataP = str(msg.payload)
	temp = Json(msgDataP)
	pressure1 = float(temp.dataP.pressurePC)
        pressure2 = float(temp.dataP.pressurePV)
	pressureSP = float(temp.dataP.setpointPC)
    
    elif msg.topic == "dataV":
        global msgDataV, V1, V2, V3, V4, V5, V6, V7, V8
        msgDataV = str(msg.payload)
	temp = Json(msgDataV)
	msgV1 = int(temp.dataV.V1)
        msgV2 = int(temp.dataV.V2)
        msgV3 = int(temp.dataV.V3)
        msgV4 = int(temp.dataV.V4)
        msgV5 = int(temp.dataV.V5)
        msgV6 = int(temp.dataV.V6)
        msgV7 = int(temp.dataV.V7)
        msgV8 = int(temp.dataV.V8)

    elif msg.topic == "dataC":
        global msgDataC, receipt, msgMix1, msgMix2, msgMix3, msgMix4
        msgDataC = str(msg.payload)
	temp = Json(msgDataC)
	
	receipt = str(temp.dataC.pcGM)

	msgMix1 = str(temp.dataC.pcGM[0])
        msgMix2 = str(temp.dataC.pcGM[1])
        msgMix3 = str(temp.dataC.pcGM[2])
        msgMix4 = str(temp.dataC.pcGM[3])
	

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

