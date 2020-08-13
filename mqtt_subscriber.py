#!/usr/bin/env python

###
## Bridge between EPICS and MQTT
####################################

from datetime import datetime
from pcaspy import Driver, SimpleServer 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from pyxtension.Json import Json

###
# MQTT brocker and topics
###
MQTT_SERVER = "localhost" #"129.129.130.80"
MQTT_TOPIC_01 = "dataV"
MQTT_TOPIC_02 = "dataP"
MQTT_TOPIC_03 = "dataC"   #

###
# Epics definitions
###
prefix = 'X10DA-ES-GMS:'
pvdb = {
    'SEND' : {'type' : 'int','scan' : 0.2,},
    'V1' : {'type' : 'int','scan' : 0.2,},
    'V2' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V3' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V4' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V5' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V6' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V7' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'V8' : {
        'type' : 'int',
        'scan' : 0.2,
    },

    'DATAC' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'DATAV' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'DATAP' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },

    'PRESSURE1' : {
        'type' : 'float',
        'scan' : 0.2,
        'prec' : 3,
        'unit' : 'bar',
    },

    'PRESSURE2' : {
        'type' : 'float',
        'scan' : 0.2,
        'prec' : 3,
        'unit' : 'bar',
    },

    'PRESSURE.SETPOINT' : {
        'type' : 'float',
        'scan' : 0.2,
        'prec' : 3,
        'unit' : 'bar',
    },
    'MIX1' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'MIX2' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'MIX3' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'MIX4' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 300,
    },
    'RECEIPT' : {
        'type' : 'enum',
	'enums' : ['0','1','2','3','4','5','6','7','8','9','10','11'],
    },
    'G1' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 10,
    },
    'PG1' : {
        'type' : 'float',
        'scan' : 0.2,
        'prec' : 3,
        'unit' : 'bar',
    },
    'G2' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 10,
    },
    'PG2' : {
        'type' : 'float',
        'scan' : 0.2,
        'prec' : 3,
        'unit' : 'bar',
    },
    'ENERGY' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 10,
    },
    'CORESPONDING' : {
        'type' : 'char',
        'scan' : 0.2,
        'count' : 10,
    },
    'IC' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'GAS1' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'GAS2' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'CYCLE.NO' : {
        'type' : 'int',
        'scan' : 0.2,
    },
    'STATUS' : {
        'type' : 'int',
        'scan' : 0.2,
    },




}

###
# Global variables to store the values for the bridge
###
msgData = ""; msgTest = ""; msgFill = 0;
msgV1 = 0; msgV2 = 0; msgV3 = 0; msgV4 = 0; msgV5 = 0; msgV6 = 0; msgV7 = 0; msgV8 = 0; 
msgMix1 = ""
msgMix2 = ""
msgMix3 = ""
msgMix4 = ""

receipt = []
msgGas1 = ""
msgGas2 = ""
msgPGas1 = 0
msgPGas2 = 0
energy = ""
coresponding = ""

msgDataC = ""
msgDataV = ""
msgDataP = ""

pressure1 = -1.0
pressure2 = -1.0
pressureSP = -1.0

class myDriver(Driver):
    def  __init__(self):
        super(myDriver, self).__init__()

    def read(self, reason):
        if reason == 'SEND':
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
        elif reason == 'V4':
           global msgV4
           value = msgV4        
	elif reason == 'V5':
           global msgV5
           value = msgV5
        elif reason == 'V6':
           global msgV6
           value = msgV6
        elif reason == 'V7':
           global msgV7
           value = msgV7
        elif reason == 'V8':
           global msgV8
           value = msgV8

	elif reason == 'DATAC':
           global msgDataC
           value = msgDataC
	elif reason == 'DATAV':
           global msgDataV
           value = msgDataV
	elif reason == 'DATAP':
           global msgDataP
           value = msgDataP

        elif reason == 'PRESSURE1':
           global pressure1
           value = pressure1
        elif reason == 'PRESSURE2':
           global pressure2
           value = pressure2
        elif reason == 'PRESSURE.SETPOINT':
           global pressureSP
           value = pressureSP

        elif reason == 'MIX1':
           global msgMix1
           value = msgMix1
        elif reason == 'MIX2':
           global msgMix2
           value = msgMix2
        elif reason == 'MIX3':
           global msgMix3
           value = msgMix3
        elif reason == 'MIX4':
           global msgMix4
           value = msgMix4

        elif reason == 'RECEIPT':
           global receipt
	   value = receipt

        elif reason == 'G1':
           global msgGas1
           value = msgGas1
        elif reason == 'G2':
           global msgGas2
           value = msgGas2        
	elif reason == 'PG1':
           global msgPGas1
           value = msgPGas1
        elif reason == 'PG2':
           global msgPGas2
           value = msgPGas2
        elif reason == 'ENERGY':
           global energy
           value = energy
        elif reason == 'CORESPONDING':
           global coresponding
           value = coresponding

  
	else:
	   value.self.getParam(reason)
	return value

    def write(self, reason, value):
        status = True
        if reason == 'DATA':
           global msgData
           msgData = value
           publish.single(MQTT_TOPIC_01, msgData, hostname=MQTT_SERVER)
	
	elif reason == 'TEST':
	   global msgTest
	   msgTest = value
           publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER)

	elif reason == 'FILL':
           global msgFill
           msgFill = value
           publish.single(MQTT_TOPIC_03, msgFill, hostname=MQTT_SERVER)
	elif reason == 'RECEIPT':
           global receipt, msgGas1, msgGas2, msgPGas1, msgPGas2, energy, coresponding
           receipt = value
 	   print(receipt)
           temp = Json(msgDataC)
	   msgGas1 = str(temp.dataC.pcGM[receipt].gas1)
	   msgGas2 = str(temp.dataC.pcGM[receipt].gas2)
	   msgPGas1 = int(temp.dataC.pcGM[receipt].pgas1)
	   msgPGas2 = int(temp.dataC.pcGM[receipt].pgas2)
	   energy = str(temp.dataC.pcGM[receipt].Energy)
           coresponding = str(temp.dataC.pcGM[receipt].Coresponding)
        
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

