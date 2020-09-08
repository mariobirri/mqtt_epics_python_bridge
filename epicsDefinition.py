###
# Epics definitions
###
prefix = 'X10DA-ES-GMS:' 
pvdb = {

    #DATAV
    'V1' : {'type' : 'int', 'scan' : 0.2},
    'V2' : {'type' : 'int', 'scan' : 0.2},
    'V3' : {'type' : 'int', 'scan' : 0.2},
    'V4' : {'type' : 'int', 'scan' : 0.2},
    'V5' : {'type' : 'int', 'scan' : 0.2},
    'V6' : {'type' : 'int', 'scan' : 0.2},
    'V7' : {'type' : 'int', 'scan' : 0.2},
    'V8' : {'type' : 'int', 'scan' : 0.2},

    #DATAP
    'PPC' : {'type' : 'float', 'scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},
    'PPV' : {'type' : 'float', 'scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},

    #DATAC
    'IC' : {'type' : 'int','scan' : 0.2},
    'GAS1' : {'type' : 'char','scan' : 0.2, 'count' : 5},
    'GAS2' : {'type' : 'char','scan' : 0.2, 'count' : 5},
    'PGAS1' : {'type' : 'int','scan' : 0.2},
    'PGAS2' : {'type' : 'int','scan' : 0.2},
    'CYCLE' : {'type' : 'int','scan' : 0.2},
    'ACTCYCLE' : {'type' : 'int','scan' : 0.2},
    'STATUS' : {'type' : 'int','scan' : 0.2},
    'SETPOINT' : {'type' : 'float','scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},

    #DATAL
    'ROW' : {'type' : 'char', 'scan' : 0.2, 'count' : 300},
    'LISTNR' : {'type' : 'enum', 'enums' : ['0','1','2','3','4','5','6','7','8','9','10','11','12']},
    'DATAL.CORESPONDING' : {'type' : 'char', 'scan' : 0.2, 'count' : 20},
    'DATAL.ENERGY' : {'type' : 'char', 'scan' : 0.2, 'count' : 20},
    'DATAL.GAS1' : {'type' : 'char', 'scan' : 0.2, 'count' : 20},
    'DATAL.GAS2' : {'type' : 'char', 'scan' : 0.2, 'count' : 20},
    'DATAL.PGAS1' : {'type' : 'char', 'scan' : 0.2, 'count' : 20},
    'DATAL.PGAS2' : {'type' : 'char', 'scan' : 0.2, 'count' : 20},
    'DATAL.SOLLWERT' : {'type' : 'float', 'scan' : 0.2, 'prec' : 3, 'unit' : 'bar'},

    #DATASET
    'SET.IC' : {'type' : 'int','scan' : 0.2},
    'SET.GAS1' : {'type' : 'char','scan' : 0.2, 'count' : 2},
    'SET.GAS2' : {'type' : 'char','scan' : 0.2, 'count' : 2},
    'SET.PGAS1' : {'type' : 'int','scan' : 0.2},
    'SET.PGAS2' : {'type' : 'int','scan' : 0.2},
    'SET.CYCLE' : {'type' : 'int','scan' : 0.2},
    'SET.SETPOINT' : {'type' : 'float','scan' : 0.2, 'prec' : 3},
    'COPY' : {'type' : 'int','scan' : 0.2},
    'SEND' : {'type' : 'int','scan' : 0.2},

    'STOP' : {'type' : 'int','scan' : 0.2},

#    'ENERGY' : {'type' : 'char','scan' : 0.2,'count' : 10},
#    'CORESPONDING' : {'type' : 'char','scan' : 0.2,'count' : 10},
#    'SEND' : {'type' : 'int','scan' : 0.2},
}
