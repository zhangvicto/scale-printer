import RPi.GPIO as GPIO
from optimization import optimize, fitness
from load_cell.mass import tare, measure_mass

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

def calibrate(numIterations): 
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

        print('Starting Iteration {}'.format(i))
        
        # Tare Load Cells
        tare()
        mass = measure_mass()
        print(mass) # Should be 0 

        # Tare until we get a value that is less than 0.3g
        # while abs(mass) > 0.3: 
        #     tare()
        if i == 0: 
            xguess_i = xguess
        elif last_guess is not None and not xguess:
            xguess_i = last_guess

        # Run through first PSO iteration and generate parameter
        last_guess = optimize(mode, xmax, xmin, xguess_i, numDimensions, i)

        input('Please remove prints and press enter to continue: \n')

calibrate(10)

GPIO.cleanup()