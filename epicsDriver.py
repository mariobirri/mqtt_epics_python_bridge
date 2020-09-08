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
        elif reason == 'DATAL.SOLLWERT' and str(var.row) != "": temp = Json(str(var.row)); value = temp.sollwert;

        #DATASET
        elif reason == 'SET.IC': value = var.setIc;
        elif reason == 'SET.GAS1': value = str(var.numberToElement(var.setGas1));
        elif reason == 'SET.GAS2': value = str(var.numberToElement(var.setGas2));
        elif reason == 'SET.PGAS1': value = var.setPgas1;
        elif reason == 'SET.PGAS2': value = var.setPgas2;
        elif reason == 'SET.CYCLE': value = var.setCycle;
        elif reason == 'SET.SETPOINT': value = float(var.setSetpoint);



	else: value = self.getParam(reason)
	return value

    def write(self, reason, value):
        status = True
        if reason == 'LISTNR': var.listnr = value; var.row = str(var.dataL[value]);  #publish.single(MQTT_TOPIC_01, msgData, hostname=MQTT_SERVER);
        elif reason == 'COPY' and str(var.row) != "": 
		temp = Json(str(var.row)); 
		var.setGas1 = temp.gas1;
		var.setGas2 = temp.gas2;
		var.setPgas1 = temp.pgas1;
		var.setPgas2 = temp.pgas2;
		var.setSetpoint = temp.sollwert;
        elif reason == 'SET.IC': var.setIc = value;
        elif reason == 'SET.GAS1': var.setGas1 = var.elementToNumber(value); #print(var.setGas1);
        elif reason == 'SET.GAS2': var.setGas2 = var.elementToNumber(value); #print(var.setGas2);
        elif reason == 'SET.PGAS1': var.setPgas1 = value;
        elif reason == 'SET.PGAS2': var.setPgas2 = value;
        elif reason == 'SET.CYCLE': var.setCycle = value;
        elif reason == 'SET.SETPOINT': var.setSetpoint = value;

	elif reason == 'SEND':
		var.sendMsg = Json( ('ic',var.setIc),('gas1',var.setGas1),('gas2',var.setGas2), ('pgas1',var.setPgas1), ('pgas2',var.setPgas2), ('zyklus',var.setCycle), ('sollwert',var.setSetpoint)); 
		#print(str(var.setGas1))
		#print(str(var.setGas2))
		publish.single(var.MQTT_TOPIC_05, str(var.sendMsg), hostname=var.MQTT_SERVER);

	elif reason == 'STOP': var.status = false; print(var.status); #publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER);

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
