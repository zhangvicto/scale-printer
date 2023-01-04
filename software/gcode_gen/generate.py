import math

# Global Vars
CUR_X = 0
CUR_Y = 0 
CUR_Z = 0

RETRACTED = False

# Variables
BED_X = 200
BED_Y = 250
FILAMENT_DIAMETER = 0.75 # mm
NOZZLE_DIAMETER = 0.4 # mm
LINE_WIDTH = 0.5 # mm
SPEED_FIRSTLAYER = 40*60
SPEED_TRAVEL = 180*60
SPEED_PERIMETER = 50*60
SPEED_RETRACT = 30*60
SPEED_UNRETRACT = 30*60
PRINT_DIR = 0 
HEIGHT_LAYER = 0.3
HEIGHT_FIRSTLAYER = 0.2

EXTRUSION_RATIO = LINE_WIDTH * HEIGHT_LAYER / (pow(FILAMENT_DIAMETER / 2, 2) * math.pi)
RETRACT_DIST = 0.8
EXTRUDER_NAME = "PSO Printer"
ZHOP_ENABLE = True
ZHOP_HEIGHT = 0.1
ANCHOR_LAYER_LINE_RATIO = 1
XY_ROUND = 4
Z_ROUND = 3

CENTER_X = BED_X/2
CENTER_Y = BED_Y/2
LINE_SPACING = LINE_WIDTH - HEIGHT_LAYER * (1 - math.pi / 4)
ANCHOR_LAYER_LINE_SPACING = LINE_WIDTH - HEIGHT_LAYER * (1 - math.pi / 4)
EXT_MULT = 1
ANCHOR_LAYER_LINE_WIDTH = NOZZLE_DIAMETER * (ANCHOR_LAYER_LINE_RATIO / 100)
ANCHOR_LAYER_LINE_RATIO = ANCHOR_LAYER_LINE_WIDTH * HEIGHT_FIRSTLAYER /  (pow(FILAMENT_DIAMETER / 2, 2) * math.pi)

# UNUSED
# NUM_PATTERNS = 0 
# LINE_RATIO = 
# PA_START = 
# PA_END = 
# PA_STEP = 
# LINE_WIDTH = NOZZLE_DIAMETER * (LINE_RATIO / 100)
# ANCHOR_PERIMETERS = 


settings = {
    'firstLayerSpeed': SPEED_FIRSTLAYER,
    'moveSpeed': SPEED_TRAVEL,
    # 'numPatterns': NUM_PATTERNS,
    'perimSpeed': SPEED_PERIMETER,
    'centerX': CENTER_X,
    'centerY': CENTER_Y,
    'printDir': PRINT_DIR,
    'layerHeight': HEIGHT_LAYER,
    'firstLayerHeight': HEIGHT_FIRSTLAYER,
    'lineWidth': LINE_WIDTH,
    'lineSpacing': LINE_SPACING,
    'extRatio': EXTRUSION_RATIO,
    'extMult': EXT_MULT,
    # 'anchorExtRatio': ANCHOR_LAYER_EXTRUSION_RATIO,
    'anchorLineWidth': ANCHOR_LAYER_LINE_WIDTH,
    'anchorLineSpacing': ANCHOR_LAYER_LINE_SPACING,
    # 'anchorPerimeters': ANCHOR_PERIMETERS,
    'retractDist': RETRACT_DIST,
    'retractSpeed': SPEED_RETRACT,
    'unretractSpeed': SPEED_UNRETRACT,
    'extruderName': EXTRUDER_NAME,
    'xyRound': XY_ROUND,
    'zRound': Z_ROUND,
    'zhopEnable': ZHOP_ENABLE,
    'zhopHeight': ZHOP_HEIGHT,
    # 'paStart': PA_START,
    # 'paEnd': PA_END,
    # 'paStep': PA_STEP
}

# Gcode generation

# LINE
# |||||||||||||||
# |||||||||||||||
# |||||||||||||||
# |||||||||||||||
# |||||||||||||||

# PLANE
# [ ] [ ] [ ] [ ] 
# [ ] [ ] [ ] [ ]
# [ ] [ ] [ ] [ ]
# [ ] [ ] [ ] [ ]
# [ ] [ ] [ ] [ ]

# Cube
# [ ]         [ ] 
#    [ ]   [ ]
#       [ ] 
#    [ ]   [ ]
# [ ]         [ ]

def gcode_gen(type, iter, settings): #x, y, indicate the position of the print

    gcode = ''

    # generate line or plane
    if type == 'L': 
        gcode += genLine(iter,settings)
    elif type == 'P':
        gcode += genPlane()
    elif type == 'C':
        gcode += genCube()
    else:
        print('Enter L for Line, P for Plane, C for Cube')
    
    return gcode

# PRUSA SPECIFIC GCODE GENERATION
def genStart(nozzleD, Te, Tb, Vp): 
    gcode = ";START_GCODE\n"

    # Setting Accelerations etc
    gcode += "M73 P0 R24 \nM73 Q0 S24 \nM201 X1000 Y1000 Z200 E5000 ; sets maximum accelerations, mm/sec^2 \n"
    gcode += "M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm / sec\n"
    gcode += "M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2 \n"
    gcode += "M205 X8.00 Y8.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec\n"
    gcode += "M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec \n"
    gcode += "M107\n"
    # NO LINEAR ADVANCE IS SET

    # Basic Settings
    gcode += 'M862.3 P "MK3S" ; printer model check\n'
    gcode += "M862.1 P{} ; nozzle diameter check\n".format(nozzleD)
    gcode += "M115 U3.11.0 ; tell printer latest fw version\n"
    gcode += "G90 ; use absolute coordinates\n"
    gcode += "M83 ; extruder relative mode\n"
    gcode += "M104 S{} ; set extruder temp\n".format(Te)
    gcode += "M140 S{} ; set bed temp\n".format(Tb)
    # gcode += "M190 S{} ; wait for bed temp\n".format(Tb)
    gcode += "M109 S{} ; wait for extruder temp\n".format(Te)
    gcode += "G28 W ; home all without mesh bed level\n"
    gcode += "G80 ; mesh bed leveling\n\n"

    # Intro line
    gcode += "G1 Z0.3 F720 \nG1 Y-3 F1000 ; go outside print area \nG92 E0 \nG1 X60 E9 F1000 ; intro line \nG1 X100 E9 F1000 ; intro line\n\n"

    # Level again, set flow
    gcode += "G92 E0 \nM221 S95 ; Set flow\n\n"

    return gcode

def genEnd(): 
    gcode = ";END_GCODE\n"
    # # Wipe
    # gcode += ";WIPE_START \nG1 F8640;_WIPE \nG1 X106.746 Y118.207 E-.76 \n;WIPE_END \nG1 E-.04 F2100 \nG1 Z8.4 F720 \nM107\n"
    
    # Park and Reset Flow
    gcode += "G1 Z9 F720 ; Move print head up \nG1 X0 Y200 F3600 ; park \nG1 Z57 F720 ; Move print head further up \nG4 ; wait \nM221 S100 ; reset flow\n\n"

    # Turn Everything Off
    gcode += "M104 S0 ; turn off temperature\n"
    # gcode += "M140 S0 ; turn off heatbed"
    gcode += "M107 ; turn off fan \nM84 ; disable motors \nM73 P100 R0 \nM73 Q100 S0"

    return gcode

def genLine(iter, settings): 
    TO_X = iter*10
    TO_Y = settings['lineSpacing']
    TO_Z = HEIGHT_FIRSTLAYER
    line_length = 200

    gcode = ''

    # initial z position
    gcode += moveToZ(TO_Z ,settings)

    # initial xy pos
    # START_X = CENTER_X - (250 / 2)
    # START_Y = CENTER_Y - (210 / 2)
    gcode += moveToXY(to_x=TO_X, to_y=TO_Y, settings=settings, optional={'comment': '; Moving to line position\n'})

    # print line 
    gcode += createLine(to_x=TO_X, to_y=line_length, settings=settings, optional={'comment': '; Create Line \n'})

    gcode += "\n"

    return gcode

def genPlane(): 
    gcode = ''
    return ''

def genCube(): 
    gcode = ''
    return ''


def moveToZ(to_z, settings): 

    global CUR_Z

    gcode = ''
    gcode += 'G0 Z' + str(round(to_z, 3)) + ' F' + str(settings['moveSpeed']) + ' ; Move to z height\n'
    CUR_Z = to_z # Update global position

    return gcode

def moveToXY(to_x, to_y, settings, optional): 

    global CUR_X 
    global CUR_Y

    gcode = ''
    distance = getDistance(CUR_X, CUR_Y, to_x, to_y)

    defaults = {
      'comment': ' ; Move\n'
    }

    optArgs = dict()
    optArgs.update(defaults)
    optArgs.update(optional)

    if distance > 2: # don't retract for travels under 2mm
        gcode += doEfeed('-', settings) #retract

    gcode += 'G0 X' + str(round(rotateX(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), settings['xyRound'])) + ' Y' + str(round(rotateY(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), settings['xyRound'])) +' F' + str(settings['moveSpeed']) + optArgs['comment']
  


    CUR_X = to_x # update global position vars
    CUR_Y = to_y

    if distance >= 2: 
        gcode += doEfeed('+', settings)  #un-retract

    return gcode

# Rotate X
def rotateX(x, xm, y, ym, a): 
    a *= math.degrees(math.pi/180) # Convert to radians
    cos = math.cos(a)
    sin = math.sin(a)
    # Subtract midpoints, so that midpoint is translated to origin
    # and add it in the end again
    # xr = (x - xm) * cos - (y - ym) * sin + xm; # CCW
    xr = (cos * (x - xm)) + (sin * (y - ym)) + xm; # CW
    return xr

# Rotate Y
def rotateY(x, xm, y, ym, a): 
    a *= math.degrees(math.pi/180) # Convert to radians
    cos = math.cos(a)
    sin = math.sin(a)
    # Subtract midpoints, so that midpoint is translated to origin
    # and add it in the end again
    # yr = (x - xm) * sin + (y - ym) * cos + ym # CCW
    yr = (cos * (y - ym)) - (sin * (x - xm)) + ym # CW
    return yr


# get distance
def getDistance(cur_x, cur_y, to_x, to_y): 
  return math.hypot((to_x - cur_x), (to_y - cur_y))

# extruder feed gcode
def doEfeed(dir, settings): 
    global RETRACTED, CUR_Z, Z_ROUND

    gcode = ''

    if dir == '+' and RETRACTED and not settings['zhopEnable']:
        gcode += 'G1 E' + str(round(settings['retractDist'], 5)) + ' F' + str(settings['unretractSpeed']) + ' ; Un-retract\n'
        RETRACTED = False
        return gcode
    elif dir == '-' and not RETRACTED and not settings['zhopEnable']:
        gcode += 'G1 E-' + str(round(settings['retractDist'], 5)) + ' F' + str(settings['retractSpeed']) + ' ; Retract\n'
        RETRACTED = True
        return gcode
    elif dir == '+' and RETRACTED and settings['zhopEnable']:
        gcode += 'G1 Z' + str(round(CUR_Z, Z_ROUND)) + ' F' + str(settings['moveSpeed']) + ' ; Z hop return\n' + 'G1 E' + str(round(settings['retractDist'], 5)) + ' F' + str(settings['unretractSpeed']) + ' ; Un-retract\n'
        RETRACTED = False
        return gcode
    elif dir == '-' and not RETRACTED and settings['zhopEnable']:
        gcode += 'G1 E-' + str(round(settings['retractDist'], 5)) + ' F' + str(settings['retractSpeed']) + ' ; Retract\n' + 'G1 Z' + str(round((CUR_Z + settings['zhopHeight']), settings['zRound'])) + ' F' + str(settings['moveSpeed']) + ' ; Z hop\n'
        RETRACTED = True
        return gcode


def createLine(to_x, to_y, settings, optional): 

    global CUR_X, CUR_Y

    # handle optional function arguments passed as object
    defaults = {
        'extMult': settings['extMult'],
        'extRatio': settings['extRatio'],
        'speed': settings['firstLayerSpeed'],
        'comment': ' ; Print line\n'
    }

    optArgs = dict()
    optArgs.update(defaults)
    optArgs.update(optional)

    # change speed if first layer
    if round(CUR_Z, 3) == settings['firstLayerHeight']: 
        optArgs['speed'] = settings['firstLayerSpeed']
    else: 
        optArgs['speed'] = settings['perimSpeed']

    length = getDistance(CUR_X, CUR_Y, to_x, to_y)
    ext = round(optArgs['extRatio'] * optArgs['extMult'] * abs(length), 5)
    print(ext)
    gcode = 'G1 X' + str(round(rotateX(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), 4)) + ' Y' + str(round(rotateY(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), 4)) + ' E' + str(ext) + ' F' + str(optArgs['speed']) + optArgs['comment']

    CUR_X = to_x # update global position vars
    CUR_Y = to_y

    return gcode

with open("test.gcode", "w") as f:
    f.write(genStart(0.4, 230, 0, settings['moveSpeed']))
    f.write(gcode_gen('L', 1, settings))
    f.write(genEnd())

    f.close()