from variables import *
from pcaspy import Driver

class myDriver(Driver):
    def __init__(self):
        super(myDriver, self).__init__()
    def read(self, reason):
        if reason == 'SEND': global msgFill; value = msgFill;
	elif reason == 'V1': global msgV1; value = msgV1;
	elif reason == 'V2': global msgV2; value = msgV2;
	elif reason == 'V3': global msgV3; value = msgV3;
        elif reason == 'V4': global msgV4; value = msgV4;
	elif reason == 'V5': global msgV5; value = msgV5;
        elif reason == 'V6': global msgV6; value = msgV6;
        elif reason == 'V7': global msgV7; value = msgV7;
        elif reason == 'V8': global msgV8; value = msgV8;
	elif reason == 'DATAC': global msgDataC; value = msgDataC;
	elif reason == 'DATAV': global msgDataV; value = msgDataV;
	elif reason == 'DATAP': global msgDataP; value = msgDataP;
        elif reason == 'PRESSURE1': global pressure1; value = pressure1;
        elif reason == 'PRESSURE2': global pressure2; value = pressure2;
        elif reason == 'PRESSURE.SETPOINT': global pressureSP; value = pressureSP;
        elif reason == 'MIX1': global msgMix1; value = msgMix1;
        elif reason == 'MIX2': global msgMix2; value = msgMix2;
        elif reason == 'MIX3': global msgMix3; value = msgMix3;
        elif reason == 'MIX4': global msgMix4; value = msgMix4;
        elif reason == 'RECEIPT': global receipt; value = receipt;
        elif reason == 'G1': global msgGas1; value = msgGas1;
        elif reason == 'G2': global msgGas2; value = msgGas2;
	elif reason == 'PG1': global msgPGas1; value = msgPGas1;
        elif reason == 'PG2': global msgPGas2; value = msgPGas2;
        elif reason == 'ENERGY': global energy; value = energy;
        elif reason == 'CORESPONDING': global coresponding; value = coresponding;
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
