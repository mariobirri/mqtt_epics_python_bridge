###
# MQTT brocker and topics
###
MQTT_SERVER = "localhost" #MQTT_SERVER = "129.129.130.80"
MQTT_TOPIC_01 = "dataV"
MQTT_TOPIC_02 = "dataP"
MQTT_TOPIC_03 = "dataC"
MQTT_TOPIC_04 = "dataL"
MQTT_TOPIC_05 = "dataSet"
MQTT_TOPIC_06 = "vSet"
MQTT_TOPIC_07 = "stop"
MQTT_TOPIC_08 = "start"
MQTT_TOPIC_09 = "startEvac"


###
# Global variables to store the values for the bridge
###

#DATAV
V1 = 0;
V2 = 0;
V3 = 0;
V4 = 0;
V5 = 0;
V6 = 0;
V7 = 0;
V8 = 0;

#DATAP
global ppc, ppv
ppc = -1;
ppv = -1;

#DATAC
ic = 0;
gas1 = 0;
gas2 = 0;
pgas1 = 0;
pgas2 = 0;
cycle = 0;
actcycle = 0;
status = 0;
setpoint = 0;

#DATAL
listEntry = ['TI,V (5.0)','Ce,Cr (5.8)','2','3','4','5','6','7','8','9','10','11','12'];
dataL = ['','','','','','','','','','','','','']
row = "";
listnr = 0;

#DATASET
icEntry = ['1','2','3','All'];
setIc = 0;
setGas1 = 0;
setGas2 = 0;
setPgas1 = 0;
setPgas2 = 0;
setCycle = 0;
setSetpoint = 0.0;

sendMsg = "";

elements = [' ', 'AR', 'N2', 'HE', 'NE'] 
elementsArrGas1 = elements
elementsArrGas2 = elements
elementSelectedGas1 = 0;
elementSelectedGas2 = 0;

def numberToElement(inNumber):
	global elements
	return elements[inNumber]

def elementToNumber(inElement):
        global elements
	for x in range(len(elements)):
	        if elements[x] == inElement:
			return elements[inNumber]
	return 0
