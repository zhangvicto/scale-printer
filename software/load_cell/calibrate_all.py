from hx711_multi import HX711
import statistics
import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

readings_to_average = 10
sck_pin = 6
dout_pins = [22, 4, 17, 27]

hx711 = HX711(dout_pins=dout_pins,
              sck_pin=sck_pin,
              channel_A_gain=64,
              channel_select='A',
              all_or_nothing=False,
              log_level='CRITICAL')

# reset ADC, zero it
hx711.reset()

def calibrate_all(known_weights): 
    avg_multiples = []
    individual_multiples = []
    i = 0 
    for weight in known_weights: 
        raw = hx711.read_raw(readings_to_average=readings_to_average) # Read the Raw Values of Each Load Cell
        print(sum(raw))
        raw_sum = sum(raw) # Sum up all raw readings
        avg_multiples += weight/raw_sum # Find the multiple

        individual_cell_multiple = []
        for value in raw: 
            multiple_diff = (avg_multiples[i] - weight/value)/avg_multiples[i] # Relative difference of individual load cell vs. the average
            individual_cell_multiple += avg_multiples[i](1 + multiple_diff) # Adjustment to the individual multiple

        individual_multiples.append(individual_cell_multiple) # Add all four multiples with adjustment
        i += 1 # Next calibration weight

        input("Please put {}g weight on the bed.".format(weight))
    

    # Standard Dev of Values in Multiples
    print(statistics.stdev(avg_multiples)) # Avg Value of the multiple across four cells

    # Avg the individual Weights
    i = 1
    for multiple in individual_multiples: 
        print("Load Cell{}: {}. Stddev: {}".format(i, sum(multiple)/len(multiple), statistics.stdev(multiple)))

# Run Script to find best, for future auto run calibration at start
calibrate_all(known_weights=[1, 2, 5, 10, 20, 100])