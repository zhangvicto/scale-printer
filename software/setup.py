import RPi.GPIO as GPIO
from optimization import optimize, fitness
from gcode_gen.generate import gcode_gen
from gcode_sender.printcore_gcode_sender import send_gcode
from load_cell.mass import tare, measure_mass

# init GPIO (should be done outside HX711 module in case you are using other GPIO functionality)
GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

#MAIN BLOCK
# Settings

# Variables MIN MAX
# Extruder Temp
TeMax = 260
TeMin = 200

# Bed Temp - unused due to broken bed
TbMax = 90
TbMin = 40

# Print Speed
VpMax = 200
VpMin = 20

# Extrusion Flow Multiplier
EfMax = 2
EfMin = 0.8

xmax = [TeMax, VpMax, EfMax]
xmin = [TeMin, VpMin, EfMin]
xguess = [230, 60, 40]

numDimensions = len(xmax)

# Choose Calibration Type GCODE (Line or Plane)
mode = input('Choose a calibration mode, L, P, or C: \n')

if mode == "L": 
    numIterations = 15
elif mode == "P" or mode == "C": 
    numIterations = 10

# Run Iterations
for i in range(numIterations): 
    # Tare Load Cells
    tare()
    mass = measure_mass()
    print(mass) # Should be 0 

    # Tare until we get a value that is less than 0.3g
    # while abs(mass) > 0.3: 
    #     tare()
    
    
    # Start print once the inputs are confirmed

    # Run through first PSO iteration and generate parameter
    gcode_gen(optimize(fitness, xmax, xmin, xguess, numDimensions, i), i, )

    # Send to Printer
    send_gcode(gcode_file=gcode)

    # Check for 

    # Generate gcode for next iteration

GPIO.cleanup()