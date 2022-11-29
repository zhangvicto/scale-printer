import RPi.GPIO as GPIO

# init GPIO (should be done outside HX711 module in case you are using other GPIO functionality)
GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering



#MAIN BLOCK

# Choose Gcode (Line or Plane)

# Start print once the inputs are confirmed

# Run through first PSO iteration
    # Once print finishes, check weight, check dimensions
    # 

# Check for 

# Generate gcode for next iteration



GPIO.cleanup()