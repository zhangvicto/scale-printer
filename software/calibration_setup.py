import RPi.GPIO as GPIO
from optimization import optimize, fitness
from load_cell.mass import tare, measure_mass

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

#MAIN BLOCK
# Settings

# Variables MIN MAX
# Extruder Temp

TeMax = 260
TeMin = 190

# Bed Temp - unused due to broken bed
TbMax = 80
TbMin = 40

# Print Speed - feedrate
VpMax = 200
VpMin = 20

# Extrusion Flow Multiplier
EfMax = 2
EfMin = 0.8

xmax = [TeMax, VpMax*60, EfMax]
xmin = [TeMin, VpMin*60, EfMin]
# xguess = [190, 60, 40]

numDimensions = len(xmax)

# Desired Mass
mass_desired = 1.07 # in grams, includes weight of wipe

def calibrate(numIterations): 
    # Input Sequence
    # Choose Calibration Type GCODE (Line or Plane)
    mode = input('Choose a calibration mode, L, P, or C: \n')

    if mode == "L": 
        numIterations = 15
    elif mode == "P" or mode == "C": 
        numIterations = 10

    # Initial Guess, and if out of bounds, use default
    Te_guess = input('Enter the initial extruder temperature guess: \n')
    if int(Te_guess) < 190 or int(Te_guess) > 260: 
        print("Invalid temperature guess, using 190")
        Te_guess = 190
    Vp_guess = input('Enter the initial print speed guess: \n')
    
    if int(Vp_guess) < 20 or int(Vp_guess) > 200: 
        print("Invalid print speed guess, using 50")
        Vp_guess = 50
    Ef_guess = input('Enter the initial extrusion flow guess: \n')
    
    if int(Ef_guess) < 0.8 or int(Ef_guess) > 2: 
        print("Invalid extrusion flow guess, using 1")
        Ef_guess = 1

    xguess = [int(Te_guess), int(Vp_guess)*60, int(Ef_guess)]
    
    last_guess = []

    # Run Iterations
    for i in range(0, numIterations): 

        print('Starting Iteration {}'.format(i))
        
        # Tare Load Cells
        tare()
        mass = measure_mass()
        print("Tared Mass: {}".format(mass)) # Should be near 0 

        if i == 0: 
            xguess_i = xguess
        elif last_guess is not None and not xguess:
            xguess_i = last_guess

        # Run through first PSO iteration and generate parameter
        last_guess = optimize(mode, xmax, xmin, xguess_i, mass_desired, numDimensions, i)

        print(last_guess)

        input('Please remove prints and press enter to continue: \n')

calibrate(10)

GPIO.cleanup()