import math
# global vars
CUR_X = 0
CUR_Y = 0 
CUR_Z = 0
RETRACTED = False


# Variables
SPEED_FIRSTLAYER = 0 
SPEED_TRAVEL = 0 
SPEED_PERIMETER = 0 
# NUM_PATTERNS = 0 
CENTER_X = 0 
CENTER_Y = 0 
PRINT_DIR = 0 
HEIGHT_LAYER = 0.3
HEIGHT_FIRSTLAYER = 0.2
LINE_WIDTH = 0.5
LINE_SPACING = 0
EXTRUSION_RATIO = 1 # exxtrusion width
EXT_MULT = 0 
ANCHOR_LAYER_LINE_WIDTH = 
ANCHOR_LAYER_LINE_SPACING = 
ANCHOR_PERIMETERS = 
RETRACT_DIST = 0.56
SPEED_RETRACT = 
SPEED_UNRETRACT = 
EXTRUDER_NAME = "PSO Printer"
ZHOP_ENABLE = True
ZHOP_HEIGHT = 
# PA_START = 
# PA_END = 
# PA_STEP = 

settings = {
    'firstLayerSpeed': SPEED_FIRSTLAYER,
    'moveSpeed': SPEED_TRAVEL,
    'numPatterns': NUM_PATTERNS,
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
    'anchorExtRatio': ANCHOR_LAYER_EXTRUSION_RATIO,
    'anchorLineWidth': ANCHOR_LAYER_LINE_WIDTH,
    'anchorLineSpacing': ANCHOR_LAYER_LINE_SPACING,
    'anchorPerimeters': ANCHOR_PERIMETERS,
    'retractDist': RETRACT_DIST,
    'retractSpeed': SPEED_RETRACT,
    'unretractSpeed': SPEED_UNRETRACT,
    'extruderName': EXTRUDER_NAME,
    'zhopEnable': ZHOP_ENABLE,
    'zhopHeight': ZHOP_HEIGHT,
    'paStart': PA_START,
    'paEnd': PA_END,
    'paStep': PA_STEP
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

def gcode_gen(type, x, y, settings): #x, y, indicate the position of the print
    gcode = ''
    start_gcode = ''
    end_gcode = ''

    gcode += start_gcode

    # generate line or plane
    if type == 'L': 
        gcode += genLine(x,y,settings)
    elif type == 'P':
        gcode += genPlane()
    elif type == 'C':
        gcode += genCube()
    else:
        print('Enter L for Line, P for Plane, C for Cube')

    gcode += end_gcode
    
    return gcode


def genLine(x, y, settings): 
    # initial z position
    moveToZ( ,settings)

    # print line 
    createLine(x,y,settings)

    return ''

def genPlane(): 

    return ''

def genCube(): 

    return ''


def moveToZ(to_z, settings): 
    gcode = ''
    gcode += 'G0 Z' + round(to_z, -3) + ' F' + settings['speed'] + ' Move to z height\n'
    UR_Z = to_z # Update global position
    return gcode

def moveToXY(to_x, to_y, settings, optional): 
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

    gcode += 'G0 X' + round(rotateX(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), XY_round) + ' Y' + round(rotateY(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), XY_round) +' F' + setting['moveSpeed'] + optArgs['comment']
  
    CUR_X = to_x # update global position vars
    CUR_Y = to_y

    if distance >= 2: 
        gcode += doEfeed('+', settings)  #un-retract

    return gcode

# Rotate X
def rotateX(x, xm, y, ym, a): 
    a = math.degrees(math.pi / 180)*a # Convert to radians
    cos = math.cos(a)
    sin = math.sin(a)
    # Subtract midpoints, so that midpoint is translated to origin
    # and add it in the end again
    # xr = (x - xm) * cos - (y - ym) * sin + xm; # CCW
    xr = (cos * (x - xm)) + (sin * (y - ym)) + xm; # CW

    return xr

# Rotate Y
def rotateY(x, xm, y, ym, a): 
    a = math.degrees(math.pi / 180)*a # Convert to radians
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
    gcode = ''

    if dir == '+' and RETRACTED and not settings['zhopEnable']:
        gcode += 'G1 E' + round(settings['retractDist'], -5) + ' F' + settings['unretractSpeed'] + ' ; Un-retract\n'
        RETRACTED = False
        return gcode
    elif dir == '-' and not RETRACTED and not settings['zhopEnable']:
        gcode += 'G1 E-' + round(settings['retractDist'], -5) + ' F' + settings['retractSpeed'] + ' ; Retract\n'
        RETRACTED = True
        return gcode
    elif dir == '+' and RETRACTED and settings['zhopEnable']:
        gcode += 'G1 Z' + round(CUR_Z, -3) + ' F' + settings['moveSpeed'] + ' ; Z hop return\n' + 'G1 E' + round(settings['retractDist'], -5) + ' F' + settings['unretractSpeed'] + ' ; Un-retract\n'
        RETRACTED = False
        return gcode
    elif dir == '-' and not RETRACTED and settings['zhopEnable']:
        gcode += 'G1 E-' + round(settings['retractDist'], -5) + ' F' + settings['retractSpeed'] + ' ; Retract\n' + 'G1 Z' + round((CUR_Z + settings['zhopHeight']), Z_round) + ' F' + settings['moveSpeed'] + ' ; Z hop\n'
        RETRACTED = True
        return gcode


def createLine(to_x, to_y, settings, optional): 
    ext = 0
    length = 0
    gcode = ''

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
    if round(CUR_Z, -3) == settings['firstLayerHeight']: 
        optArgs['speed'] = settings['firstLayerSpeed']
    else: 
        optArgs['speed'] = settings['perimSpeed']

    length = getDistance(CUR_X, CUR_Y, to_x, to_y)
    ext = round(optArgs['extRatio'] * optArgs['extMult'] * abs(length), -5)

    gcode += 'G1 X' + round(rotateX(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), -4) + ' Y' + round(rotateY(to_x, settings['centerX'], to_y, settings['centerY'], settings['printDir']), -4) + ' E' + ext + ' F' + optArgs['speed'] + optArgs['comment']

    CUR_X = to_x # update global position vars
    CUR_Y = to_y

    return gcode

with open("test.gcode", "w") as f:
    f.write(gcode_gen('line', settings))