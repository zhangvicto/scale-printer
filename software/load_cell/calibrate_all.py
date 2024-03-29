from hx711_multi import HX711
import statistics
import time
import RPi.GPIO as GPIO  # import GPIO
import numpy as np

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

readings_to_average = 10
sck_pin = 6
dout_pins = [22, 4, 17, 27]

hx711 = HX711(dout_pins=dout_pins,
              sck_pin=sck_pin,
              channel_A_gain=128,
              channel_select='A',
              all_or_nothing=False,
              log_level='CRITICAL')

# reset ADC, zero it
hx711.reset()

try:
    hx711.zero(readings_to_average)
except Exception as e:
    print(e)

# Function to Calibrate all Load Cells Together
def calibrate_all(known_weights): 
    avg_multiples = []
    individual_multiples = []
    i = 0 
    for weight_ref in known_weights: 
        # Tare
        hx711.reset()

        try:
            hx711.zero(readings_to_average)
        except Exception as e:
            print(e)
            
        # Input Prompt
        input("Please put {}g weight on the bed.".format(weight_ref))
        time.sleep(1) # sleep to prevent none values

        raw = hx711.read_raw(readings_to_average*3) # Read the Raw Values of Each Load Cell

        # prevent none values
        while None in raw: 
            raw = hx711.read_raw(readings_to_average*3)

        weight_sum = sum(raw) # Sum up all weight readings
        avg_multiples.append((weight_sum/(weight_ref))) # Calculate the multiple

        individual_cell_multiple = []
        for value in raw: 
            multiple_diff = (avg_multiples[i] - value/weight_ref)/avg_multiples[i] # Relative difference of individual load cell vs. the average
            individual_cell_multiple.append(avg_multiples[i]*(1 + multiple_diff))  # Adjustment to the individual multiple

        individual_multiples.append(individual_cell_multiple) # Add all four multiples with adjustment

        i += 1 # Next calibration weight

        input("Please take the weight off.\n")

    # Standard Dev of Values in Multiples
    # print(statistics.stdev(avg_multiples)) # Avg Value of the multiple across four cells

    # Avg the individual Weights and Print
    individual = np.transpose(individual_multiples)

    print("Average Multiples: {}".format(avg_multiples))
    print("Average: {}".format(sum(avg_multiples)/len(avg_multiples)))

    i = 1
    for multiple in individual: 
        print("Load Cell-{}: {}. Stddev: {}".format(i, sum(multiple)/len(multiple), statistics.stdev(multiple)))
        i+=1
        

# Run Script to find best, for future auto run calibration at start
weights = [1, 2, 5, 10]
calibrate_all(weights)