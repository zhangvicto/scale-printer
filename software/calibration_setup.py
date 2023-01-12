import RPi.GPIO as GPIO
from optimization import optimize, fitness
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

def calibrate(mode, numIterations): 
    # Input Sequence
    # Choose Calibration Type GCODE (Line or Plane)
    mode = input('Choose a calibration mode, L, P, or C: \n')


    if mode == "L": 
        numIterations = 15
    elif mode == "P" or mode == "C": 
        numIterations = 10

    desired_mass = input('Enter the Theoretical Mass of the Pattern: \n')


    # Run Iterations
    for i in range(0, numIterations): 
        # Tare Load Cells
        tare()
        mass = measure_mass()
        print(mass) # Should be 0 

        # Tare until we get a value that is less than 0.3g
        # while abs(mass) > 0.3: 
        #     tare()
        
        # Run through first PSO iteration and generate parameter
        optimize(func=fitness, xmax=xmax, xmin=xmin, xguess=xguess, numDimensions=numDimensions, iter=i, mode=mode)

GPIO.cleanup()