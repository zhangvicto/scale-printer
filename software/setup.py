import RPi.GPIO as GPIO
from optimization import optimize, fitness
from gcode_gen.generate import gcode_gen

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
mode = input('Choose a calibration mode, L, P, or C')

if mode == "L": 
    numIterations = 20
elif mode == "P" or mode == "C": 
    numIterations = 10

for i in range(numIterations): 
    # Start print once the inputs are confirmed
    # Run through first PSO iteration
    gcode_gen(optimize(fitness, xmax, xmin, xguess, numDimensions, i))

# Check for 

# Generate gcode for next iteration


GPIO.cleanup()