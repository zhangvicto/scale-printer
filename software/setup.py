import RPi.GPIO as GPIO
from pso.optimization import optimize 

# init GPIO (should be done outside HX711 module in case you are using other GPIO functionality)
GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

#MAIN BLOCK
# Choose Calibration Type GCODE (Line or Plane)
mode = input('Choose a calibration mode, L, P, or C')

if mode == "L": 
    numIterations = 20
elif mode == "P" or mode == "C": 
    numIterations = 10

for i in range(numIterations): 
    # Start print once the inputs are confirmed
    # Run through first PSO iteration
    optimize()

# Check for 

# Generate gcode for next iteration


GPIO.cleanup()