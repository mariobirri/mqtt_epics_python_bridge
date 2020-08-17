###
# Epics definitions
###
prefix = 'X10DA-ES-GMS:' 
pvdb = {
    'DATAC' : {'type' : 'char', 'scan' : 0.2,'count' : 300},
    'DATAV' : {'type' : 'char', 'scan' : 0.2,'count' : 300},
    'DATAP' : {'type' : 'char', 'scan' : 0.2,'count' : 300},

    'V1' : {'type' : 'int', 'scan' : 0.2},
    'V2' : {'type' : 'int', 'scan' : 0.2},
    'V3' : {'type' : 'int', 'scan' : 0.2},
    'V4' : {'type' : 'int', 'scan' : 0.2},
    'V5' : {'type' : 'int', 'scan' : 0.2},
    'V6' : {'type' : 'int', 'scan' : 0.2},
    'V7' : {'type' : 'int', 'scan' : 0.2},
    'V8' : {'type' : 'int', 'scan' : 0.2},
    'PRESSURE1' : {'type' : 'float', 'scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},
    'PRESSURE2' : {'type' : 'float', 'scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},
    'PRESSURE.SETPOINT' : {'type' : 'float', 'scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},

    'MIX1' : {'type' : 'char', 'scan' : 0.2, 'count' : 300},
    'MIX2' : {'type' : 'char', 'scan' : 0.2, 'count' : 300},
    'MIX3' : {'type' : 'char', 'scan' : 0.2, 'count' : 300},
    'MIX4' : {'type' : 'char', 'scan' : 0.2, 'count' : 300},

    'RECEIPT' : {'type' : 'enum','enums' : ['0','1','2','3','4','5','6','7','8','9','10','11']},

    'G1' : {'type' : 'char','scan' : 0.2,'count' : 10},
    'PG1' : {'type' : 'float','scan' : 0.2,'prec' : 3,'unit' : 'bar'},
    'G2' : {'type' : 'char','scan' : 0.2,'count' : 10},
    'PG2' : {'type' : 'float','scan' : 0.2,'prec' : 3,'unit' : 'bar'},
    'ENERGY' : {'type' : 'char','scan' : 0.2,'count' : 10},
    'CORESPONDING' : {'type' : 'char','scan' : 0.2,'count' : 10},
    'IC' : {'type' : 'int','scan' : 0.2},
    'GAS1' : {'type' : 'int','scan' : 0.2},
    'GAS2' : {'type' : 'int','scan' : 0.2},
    'CYCLE.NO' : {'type' : 'int','scan' : 0.2},
    'STATUS' : {'type' : 'int','scan' : 0.2},
    'SEND' : {'type' : 'int','scan' : 0.2},
}
