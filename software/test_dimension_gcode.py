from load_cell.mass import measure_mass
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings, square_size
from gcode_sender.printcore_gcode_sender import send_gcode
from cv.dimensions import image_process, edges, analyze_edge, find_dim


mode = 'P'

for i in range(1,2):

    iter = i

    # with open("./gcode_gen/test.gcode", "w") as f:
        
    #     gcode = genStart(iter=iter, nozzleD=0.4, Te=230, Tb=0, Vp=settings['moveSpeed'])
    #     gcode += gcode_gen(mode, iter, settings)
    #     gcode += genEnd(iter)

    #     f.write(gcode)

    # send_gcode('./gcode_gen/test.gcode')

    # # Find Dimension of the Print
    blurred = image_process() # Process Image
    edge = edges(blurred) # Canny Edge Detection

    distX = analyze_edge(edge) # Get the bed x-axis length in terms of pixels

    # Calculate Print Location
    ratio = distX/250 # Pixels per mm
    print(ratio)
    # Pixel = mm * ratio

    if mode == 'L': 
        if distX > 0: 
            xOffset = 20
            x1 = xOffset + round((iter-1)*15*ratio)
            x2 = round(x1 + 10*ratio)
            x = [x1, x2]
            print(x)
            print(x)
            y1 = round(180*ratio) - 20
            y2 = round(180*ratio)
            y = [y1, y2]
        else: 
            x = [None, None]
            y = [None, None]

    if mode == 'P': 
        if distX: 
            xOffset = 10
            y1 = xOffset + round((iter-1)*square_size*ratio)
            y2 = round(y1 + square_size*ratio)
            y = [y1, y2]
            print(y)
            x1 = round((180 - (square_size + 5))*ratio)
            x2 = round(square_size*ratio + distX/250*200)
            x = [x1, x2]
            print(x)
        else: 
            x = [None, None]
            y = [None, None]
    if mode == 'C': 
        x = [None, None]
        y = [None, None]

    dimensions = find_dim(x, y, distX, edge) # Find dim
    widths = dimensions[0]
    lengths = dimensions[1]