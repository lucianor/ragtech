import serial
# copy variables from devices.xml for Quadri 1200

# constants from XML (consts)
C_BATFACTOR = 0.7250
C_FINNOMINAL = 60.0000
C_FVOUTTAP0 = 1.2898
C_FVOUTTAP1 = 1.1558
C_FVOUTTAP2 = 1.0172
C_FVOUTTAP3 = 0.8812
C_VBATNOMINAL = 12.0000
C_VECFACTOR = 0.0500
C_VINMAX = 142.0000
C_VINMAX2 = 284.0000
C_VINMIN = 84.0000
C_VINMIN2 = 175.0000
C_VINNOMINAL = 115.0000
C_VINNOMINAL2 = 220.0000
C_VOUTNOMINAL = 115.0000
C_POUTNOMINAL = 500.0000

# decoder ring from XML (alias)
V_VERSION = 0x00
V_MODEL = 0x01
V_OSC53 = 0x02
V_OSC57 = 0x03
V_FOUTCALIB = 0x04
V_VBATCALIB = 0x05
V_VINCALIB = 0x06
V_VOUTCALIB = 0x07
V_IOUTCALIB = 0x09
V_ACTUALTAP = 0x11
V_VINPUT = 0x12
V_VOUTPUT = 0x13
V_IOUTPUT = 0x14
V_VBATTERY = 0x15
V_SHUTDOWNTIMER = 0x16
V_FOUTPUT = 0x17
V_TEMPER = 0x1A
# these are bits of info as part of a byte
F_VINSEL220 = 0x0A # bit=2
F_SYNCIN = 0x0C # bit=0
F_SHUTDOWNTIMERON = 0x0C # bit=4
F_MAXBATTERY = 0x0C # bit=7
F_NOVINPUT = 0x0D # bit=0
F_FENDBATTERY = 0x0E # bit=1
F_FOVERLOAD = 0x0E # bit=2
F_FSHORTCIRCUIT = 0x0E # bit=4
F_FABNORMALVOUT = 0x0E # bit=5
F_FABNORMALVBAT = 0x0E # bit=6
F_FINVERTER = 0x0E # bit=7
F_LOFINPUT = 0x0F # bit=1
F_HIFINPUT = 0x0F # bit=2
F_NOSYNCIN = 0x0F # bit=3
F_LOVINPUT = 0x0F # bit=4
F_HIVINPUT = 0x0F # bit=5
F_LOBATTERY = 0x0F # bit=6
F_NOISEIN = 0x0F # bit=7
F_OPBATTERY = 0x10 # bit=3
F_OPSTANDBY = 0x10 # bit=4
F_OPWARNING = 0x10 # bit=5
F_OPSTARTUP = 0x10 # bit=6
# byte reads for the flags above
FLAGS_0A = 0x0A
FLAGS_0C = 0x0C
FLAGS_0D = 0x0D
FLAGS_0E = 0x0E
FLAGS_0F = 0x0F
FLAGS_10 = 0x10

# sample message
message = b'\x99\x88\x77\x66\x55\x44\x99\x88\x77\x66\x55\x44\x99\x88\x77\x66\x55\x44\x99\x88\x77\x66\x55\x44\x99\x88\x77\x66\x55\x44\x99\x88\x77\x66\x55\x44'
# open serial connection
ser = serial.Serial('/dev/ttyACM0', 2400)
message = ser.read(33)

# read bytes
var_V_VERSION = message[V_VERSION]
var_V_MODEL = message[V_MODEL]
var_V_OSC53 = message[V_OSC53]
var_V_OSC57 = message[V_OSC57]
var_V_FOUTCALIB = message[V_FOUTCALIB]
var_V_VBATCALIB = message[V_VBATCALIB]
var_V_VINCALIB = message[V_VINCALIB]
var_V_VOUTCALIB = message[V_VOUTCALIB]
var_V_IOUTCALIB = message[V_IOUTCALIB]
var_V_ACTUALTAP = message[V_ACTUALTAP]
var_V_VINPUT = message[V_VINPUT]
var_V_VOUTPUT = message[V_VOUTPUT]
var_V_IOUTPUT = message[V_IOUTPUT]
var_V_VBATTERY = message[V_VBATTERY]
var_V_SHUTDOWNTIMER = message[V_SHUTDOWNTIMER]
var_V_FOUTPUT = message[V_FOUTPUT]
var_V_TEMPER = message[V_FOUTPUT]
# flags from bits on the bytes - not working
var_F_VINSEL220 = message[FLAGS_0A]&2
var_F_SYNCIN = message[FLAGS_0C]&0
var_F_SHUTDOWNTIMERON = message[FLAGS_0C]&4
var_F_MAXBATTERY = message[FLAGS_0C]&7
var_F_NOVINPUT = message[FLAGS_0D]&0
var_F_FENDBATTERY = message[FLAGS_0E]&1
var_F_FOVERLOAD = message[FLAGS_0E]&2
var_F_FSHORTCIRCUIT = message[FLAGS_0E]&4
var_F_FABNORMALVOUT = message[FLAGS_0E]&5
var_F_FABNORMALVBAT = message[FLAGS_0E]&6
var_F_FINVERTER = message[FLAGS_0E]&7
var_F_LOFINPUT = message[FLAGS_0F]&1
var_F_HIFINPUT = message[FLAGS_0F]&2
var_F_NOSYNCIN = message[FLAGS_0F]&3
var_F_LOVINPUT = message[FLAGS_0F]&4
var_F_HIVINPUT = message[FLAGS_0F]&5
var_F_LOBATTERY = message[FLAGS_0F]&6
var_F_NOISEIN = message[FLAGS_0F]&7
var_F_OPBATTERY = message[FLAGS_10]&3
var_F_OPSTANDBY = message[FLAGS_10]&4
var_F_OPWARNING = message[FLAGS_10]&5
var_F_OPSTARTUP = message[FLAGS_10]&6

# trasnformation from XML (vars)
model = var_V_MODEL
version = var_V_VERSION*0.1000
if not var_F_VINSEL220 or var_F_OPBATTERY:
    if var_F_NOVINPUT or not var_V_VINPUT or not var_V_VINCALIB:
        vInput = 0
    else:
        vInput = (var_V_VINPUT / var_V_VINCALIB) * 115
else:
    if var_F_NOVINPUT or not var_V_VINPUT or not var_V_VINCALIB or not var_V_IOUTCALIB:
        vInput = 0
    else:
        vInput = (var_V_VINPUT / var_V_VINCALIB) * 230 * ((var_V_IOUTPUT / var_V_IOUTCALIB) * C_VECFACTOR + 1)

if not var_V_VOUTCALIB or var_F_OPSTANDBY:
    vOutput = 0
else:
    if var_V_ACTUALTAP == 0:
        factor = C_FVOUTTAP0
    elif var_V_ACTUALTAP == 1:
        factor = C_FVOUTTAP1
    elif var_V_ACTUALTAP == 2:
        factor = C_FVOUTTAP2
    elif var_V_ACTUALTAP == 3:
        factor = C_FVOUTTAP3
    else:
        factor = 0

    vOutput = (var_V_VOUTPUT / var_V_VOUTCALIB) * factor * 115

if (var_V_OSC57 - var_V_OSC53):
    fOutput = ((53.0 + (4.0 * (var_V_FOUTPUT - var_V_OSC53) / (var_V_OSC57 - var_V_OSC53))) * 0.9806 + 1.46)
else:
    fOutput = 0

if not var_V_IOUTCALIB:
    pOutput = 0
else:
    pOutput = (var_V_IOUTPUT / var_V_IOUTCALIB) * 100

if not var_V_VBATCALIB:
    vBattery = 0
else:
    vBattery = (var_V_VBATTERY / var_V_VBATCALIB) * (C_VBATNOMINAL * 13.8 / 12)

cBattery_raw = (var_V_VBATTERY / var_V_VBATCALIB - C_BATFACTOR) / (1 - C_BATFACTOR) * 100
cBattery = 0 if cBattery_raw < 0 else cBattery_raw
temperature = var_V_TEMPER
shutdownTimer = var_V_SHUTDOWNTIMER if var_F_SHUTDOWNTIMERON else -1
nominalVInput = C_VINNOMINAL2 if var_F_VINSEL220 else C_VINNOMINAL
nominalVOutput = C_VOUTNOMINAL
nominalFOutput = C_FINNOMINAL
nominalPOutput = C_POUTNOMINAL
nominalVBattery = C_VBATNOMINAL


print(temperature)
print(cBaterry)

