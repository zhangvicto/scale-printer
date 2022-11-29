def gcode_gen(type): 
    gcode = ''
    start_gcode = ''
    end_gcode = ''

    gcode += start_gcode

    # generate line or plane
    if type == 'L': 
        gcode += genLine()
    elif type == 'P':
        gcode += genPlane()
    else:
        print('Enter L for Line or P for Plane.')

    gcode += end_gcode
    
    return gcode


def genLine(): 

    return ''

def genPlane(): 

    return ''
