import paho.mqtt.publish as publish
import variables as var
from pcaspy import Driver
from pyxtension.Json import Json

class myDriver(Driver):
    def __init__(self):
        super(myDriver, self).__init__()
    def read(self, reason):

	#DATAV
	if reason == 'V1': value = var.V1;
	elif reason == 'V2': value = var.V2;
	elif reason == 'V3': value = var.V3;
        elif reason == 'V4': value = var.V4;
	elif reason == 'V5': value = var.V5;
        elif reason == 'V6': value = var.V6;
        elif reason == 'V7': value = var.V7;
        elif reason == 'V8': value = var.V8;

	#DATAP
        elif reason == 'PPC': value = var.ppc;
        elif reason == 'PPV': value = var.ppv;
	elif reason == 'SP.PC': value = var.sppc;

	#DATAC
	elif reason == 'IC': value = var.ic;
        elif reason == 'GAS1': value = var.numberToElement(var.gas1);
        elif reason == 'GAS2': value = var.numberToElement(var.gas2);
        elif reason == 'PGAS1': value = var.pgas1;
        elif reason == 'PGAS2': value = var.pgas2;
        elif reason == 'CYCLE': value = var.cycle;
        elif reason == 'ACTCYCLE': value = var.actcycle;
        elif reason == 'STATUS': value = var.status;
	elif reason == 'SETPOINT': value = var.setpoint;

	#DATAL
	elif reason == 'ROW': value = str(var.dataL[var.listnr]); var.row = value;
	elif reason == 'LISTNR' : value = var.listnr;
	elif reason == 'DATAL.CORESPONDING' and str(var.row) != "": temp = Json(str(var.row)); value = str(temp.Coresponding);
        elif reason == 'DATAL.ENERGY' and str(var.row) != "": temp = Json(str(var.row)); value = str(temp.Energy);
        elif reason == 'DATAL.GAS1' and str(var.row) != "": temp = Json(str(var.row)); value = str(var.numberToElement(int(temp.gas1)));
        elif reason == 'DATAL.GAS2' and str(var.row) != "": temp = Json(str(var.row)); value = str(var.numberToElement(int(temp.gas2)));
        elif reason == 'DATAL.PGAS1' and str(var.row) != "": temp = Json(str(var.row)); value = str(temp.pgas1);
        elif reason == 'DATAL.PGAS2' and str(var.row) != "": temp = Json(str(var.row)); value = str(temp.pgas2);
        elif reason == 'DATAL.SOLLWERT' and str(var.row) != "": temp = Json(str(var.row)); value = temp.setpoint;

        #DATASET
        elif reason == 'SET.IC': value = var.setIc;
        elif reason == 'SET.GAS1': value = str(var.numberToElement(var.setGas1));
        elif reason == 'SET.GAS2': value = str(var.numberToElement(var.setGas2));
        elif reason == 'SET.PGAS1': value = var.setPgas1;
        elif reason == 'SET.PGAS2': value = var.setPgas2;
        elif reason == 'SET.CYCLE': value = var.setCycle;
        elif reason == 'SET.SETPOINT': value = var.setSetpoint;

	#OTHERS
	elif reason == 'ELEMENT.G1': value = var.elementSelectedGas1; 
	elif reason == 'ELEMENT.G2': value = var.elementSelectedGas2;
        elif reason == 'SETPOINT.PC': value = var.setpointPC;

	else: value = self.getParam(reason)
	return value

    def write(self, reason, value):
        status = True
        if reason == 'LISTNR': 
		var.listnr = value; var.row = str(var.dataL[value]);  #publish.single(MQTT_TOPIC_01, msgData, hostname=MQTT_SERVER);
		temp = Json(str(var.row));
                var.setGas1 = temp.gas1;
                var.setGas2 = temp.gas2;
                var.setPgas1 = temp.pgas1;
                var.setPgas2 = temp.pgas2;
                var.setSetpoint = temp.setpoint;
        elif reason == 'COPY' and str(var.row) != "": 
		temp = Json(str(var.row)); 
		var.setGas1 = temp.gas1; 
		var.setGas2 = temp.gas2;
		var.setPgas1 = temp.pgas1;
		var.setPgas2 = temp.pgas2;
		var.setSetpoint = temp.setpoint;
        elif reason == 'SET.IC': var.setIc = value;
        elif reason == 'SET.GAS1': var.setGas1 = var.elementToNumber(value); #print(var.setGas1);
        elif reason == 'SET.GAS2': var.setGas2 = var.elementToNumber(value); #print(var.setGas2);
        elif reason == 'SET.PGAS1': var.setPgas1 = value; var.setPgas2 = 100 - value;
        elif reason == 'SET.PGAS2': var.setPgas2 = value;
        elif reason == 'SET.CYCLE': var.setCycle = value;
        elif reason == 'SET.SETPOINT': var.setSetpoint = value;
	
        elif reason == 'ELEMENT.G1': var.elementSelectedGas1 = value; var.setGas1 = value;
        elif reason == 'ELEMENT.G2': var.elementSelectedGas2 = value; var.setGas2 = value;


	elif reason == 'SEND':
		var.sendMsg = Json( ('ic',var.setIc),('gas1',var.setGas1),('gas2',var.setGas2), ('pgas1',var.setPgas1), ('pgas2',var.setPgas2), ('zyklus',var.setCycle), ('sollwert',var.setSetpoint)); 
		#print(str(var.setGas1))
		#print(str(var.setGas2))
		publish.single(var.MQTT_TOPIC_05, str(var.sendMsg), hostname=var.MQTT_SERVER);

	elif reason == 'STOP': publish.single(var.MQTT_TOPIC_07, "1", hostname=var.MQTT_SERVER); 
        elif reason == 'START': publish.single(var.MQTT_TOPIC_08, "1", hostname=var.MQTT_SERVER);
        elif reason == 'STARTEVAC': publish.single(var.MQTT_TOPIC_09, "1", hostname=var.MQTT_SERVER);
        elif reason == 'SETPOINT.PC': var.setpointPC = value;  publish.single(var.MQTT_TOPIC_10, var.setpointPC, hostname=var.MQTT_SERVER);

        #DATAV
        elif reason == 'V1': 
		var.V1 = value;
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V2': 
		var.V2 = value; 
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V3': 
		var.V3 = value; 
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
		publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V4': 
		var.V4 = value;
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V5': 
		var.V5 = value;
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V6': 
		var.V6 = value;
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V7': 
		var.V7 = value;
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);
        elif reason == 'V8': 
		var.V8 = value;
		msg = Json(('V1',var.V1),('V2',var.V2),('V3',var.V3),('V4',var.V4),('V5',var.V5),('V6',var.V6),('V7',var.V7),('V8',var.V8));
                publish.single(var.MQTT_TOPIC_06, str(msg), hostname=var.MQTT_SERVER);


#publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER);

	#elif reason == 'TEST': global msgTest; msgTest = value; publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER);
	#elif reason == 'FILL': global msgFill; msgFill = value; publish.single(MQTT_TOPIC_03, msgFill, hostname=MQTT_SERVER);
	#elif reason == 'RECEIPT':
#		global receipt, msgGas1, msgGas2, msgPGas1, msgPGas2, energy, coresponding; 
#		receipt = value; 
#		temp = Json(msgDataC); 
#		msgGas1 = str(temp.dataC.pcGM[receipt].gas1); 
#		msgGas2 = str(temp.dataC.pcGM[receipt].gas2);
#		msgPGas1 = int(temp.dataC.pcGM[receipt].pgas1)
#		msgPGas2 = int(temp.dataC.pcGM[receipt].pgas2)
#		energy = str(temp.dataC.pcGM[receipt].Energy)
#		coresponding = str(temp.dataC.pcGM[receipt].Coresponding)

        if status:
           self.setParam(reason, value)
        return status
