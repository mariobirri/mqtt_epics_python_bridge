from variables import *
from pcaspy import Driver

class myDriver(Driver):
    def __init__(self):
        super(myDriver, self).__init__()
    def read(self, reason):

	#DATAV
	if reason == 'V1': global V1; value = V1;
	elif reason == 'V2': global V2; value = V2;
	elif reason == 'V3': global V3; value = V3;
        elif reason == 'V4': global V4; value = V4;
	elif reason == 'V5': global V5; value = V5;
        elif reason == 'V6': global V6; value = V6;
        elif reason == 'V7': global V7; value = V7;
        elif reason == 'V8': global V8; value = V8;

	#DATAP
        elif reason == 'PPC': global ppc; value = ppc;
        elif reason == 'PPV': global ppv; value = ppv;

	#DATAC
	elif reason == 'IC': global ic; value = ic;
        elif reason == 'GAS1': global gas1; value = gas1;
        elif reason == 'GAS2': global gas2; value = gas2;
        elif reason == 'PGAS1': global pgas1; value = pgas1;
        elif reason == 'PGAS2': global pgas2; value = pgas2;
        elif reason == 'CYCLE': global cycle; value = cycle;
        elif reason == 'ACTCYCLE': global actcycle; value = actcycle;
        elif reason == 'STATUS': global status; value = status;
	elif reason == 'SETPOINT': global setpoint; value = setpoint;

	else: value = self.getParam(reason)
	return value

    def write(self, reason, value):
        status = True
        if reason == 'DATA': global msgData; msgData = value; publish.single(MQTT_TOPIC_01, msgData, hostname=MQTT_SERVER);
	elif reason == 'TEST': global msgTest; msgTest = value; publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER);
	elif reason == 'FILL': global msgFill; msgFill = value; publish.single(MQTT_TOPIC_03, msgFill, hostname=MQTT_SERVER);
	elif reason == 'RECEIPT':
		global receipt, msgGas1, msgGas2, msgPGas1, msgPGas2, energy, coresponding; 
		receipt = value; 
		temp = Json(msgDataC); 
		msgGas1 = str(temp.dataC.pcGM[receipt].gas1); 
		msgGas2 = str(temp.dataC.pcGM[receipt].gas2);
		msgPGas1 = int(temp.dataC.pcGM[receipt].pgas1)
		msgPGas2 = int(temp.dataC.pcGM[receipt].pgas2)
		energy = str(temp.dataC.pcGM[receipt].Energy)
		coresponding = str(temp.dataC.pcGM[receipt].Coresponding)

        if status:
           self.setParam(reason, value)
        return status
