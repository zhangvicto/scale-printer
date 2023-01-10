from load_cell.mass import measure_mass
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings
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
    ratio = round(distX/250) # Pixels per mm
    # Pixel = mm * ratio

    if mode == 'L': 
        if distX > 0: 
            x1 = round((iter-1)*15*ratio)
            x2 = round(x1 + 10*ratio)
            x = [x1, x2]
            print(x)
            y = [0, 180*ratio]
        else: 
            x = [0, 0]
            y = [0, 0]

    if mode == 'P': 
        if distX > 0: 
            x1 = round((iter-1)*20*ratio)
            x2 = round(x1 + 20*ratio)
            x = [x1, x2]
            print(x)
            y = [0, 180*ratio]
        else: 
            x = [0, 0]
            y = [0, 0]
    if mode == 'C': 
        x = [0, 0]
        y = [0, 0]

    dimensions = find_dim(x, y, distX, edge) # Find dim
    widths = dimensions[0]
    lengths = dimensions[1]