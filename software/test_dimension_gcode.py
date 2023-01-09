from load_cell.mass import measure_mass
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings
from gcode_sender.printcore_gcode_sender import send_gcode
from cv.dimensions import image_process, edges, analyze_edge, find_dim

iter = 3
mode = 'L'

# with open("./gcode_gen/test.gcode", "w") as f:
    
#     gcode = genStart(iter=iter, nozzleD=0.4, Te=230, Tb=0, Vp=settings['moveSpeed'])
#     gcode += gcode_gen(mode, iter, settings)
#     gcode += genEnd(iter)

#     f.write(gcode)

# send_gcode('./gcode_gen/test.gcode')

# Find Dimension of the Print
blurred = image_process() # Process Image
edge = edges(blurred) # Canny Edge Detection

distX = analyze_edge(edge) # Get the bed x-axis length in terms of pixels

# Calculate Print Location
if mode == 'L': 
    x = [(iter-1)*15/250*int(distX), int(iter*15/250*int(distX))]
    y = [0, 180]
# TBD
if mode == 'P' or mode == 'C': 
    x = [0, 0]
    y = [0, 0]

dimensions = find_dim(x, y, distX, edge) # Find dim
widths = dimensions[0]
lengths = dimensions[1]