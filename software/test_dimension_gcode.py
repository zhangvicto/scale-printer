from load_cell.mass import measure_mass
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings
from gcode_sender.printcore_gcode_sender import send_gcode
from cv.dimensions import image_process, edges, analyze_edge, find_dim

iter = 3

with open("./gcode_gen/test.gcode", "w") as f:
    
    gcode = genStart(nozzleD=0.4, Te=230, Tb=0, Vp=settings['moveSpeed'])
    gcode += gcode_gen('L', iter, settings)
    gcode += genEnd(iter)
    # gcode += open("./gcode_gen/end.txt", "r").read()

    f.write(gcode)

send_gcode('./gcode_gen/test.gcode')