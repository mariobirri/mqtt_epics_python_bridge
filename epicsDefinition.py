###
# Epics definitions
###
prefix = 'X10DA-ES-GMS:' 
pvdb = {


    #DATA
    'DATAC' : {'type' : 'char', 'scan' : 0.2,'count' : 300},
    'DATAV' : {'type' : 'char', 'scan' : 0.2,'count' : 300},
    'DATAP' : {'type' : 'char', 'scan' : 0.2,'count' : 300},

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
    'GAS1' : {'type' : 'int','scan' : 0.2},
    'GAS2' : {'type' : 'int','scan' : 0.2},
    'PGAS1' : {'type' : 'int','scan' : 0.2},
    'PGAS2' : {'type' : 'int','scan' : 0.2},
    'CYCLE' : {'type' : 'int','scan' : 0.2},
    'ACTCYCLE' : {'type' : 'int','scan' : 0.2},
    'STATUS' : {'type' : 'int','scan' : 0.2},
    'SETPOINT' : {'type' : 'int','scan' : 0.2},




#    'ENERGY' : {'type' : 'char','scan' : 0.2,'count' : 10},
#    'CORESPONDING' : {'type' : 'char','scan' : 0.2,'count' : 10},
#    'SEND' : {'type' : 'int','scan' : 0.2},
}
