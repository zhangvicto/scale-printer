from load_cell.mass import measure_mass
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings
from gcode_sender.printcore_gcode_sender import send_gcode
from cv.dimensions import image_process, edges, analyze_edge, find_dim

iter = 1

gcode = genStart(nozzleD=0.4, Te=230, Tb=0, Vp=settings['moveSpeed'])
gcode += gcode_gen('L', iter, settings)
gcode += genEnd() # need to add iter as a parameter
gcode += open("./gcode_gen/end.txt", "r").read()

send_gcode(gcode)