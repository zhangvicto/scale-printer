#https://pypi.org/project/hx711-multi/

from hx711_multi import HX711
from time import perf_counter, sleep
import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

readings_to_average = 10
sck_pin = 6
dout_pins = [22, 4, 17, 27] # 1, 2, 3, 4
weight_multiples = [6561.210267857154, 6155.000297619006, 5987.672569444473, 6004.160069444496] # 128 gain

# create hx711 instance
hx711 = HX711(dout_pins=dout_pins,
            sck_pin=sck_pin,
            channel_A_gain=64,
            channel_select='A',
            all_or_nothing=False,
            log_level='CRITICAL')
hx711.set_weight_multiples(weight_multiples=weight_multiples)


def tare(): 
    # reset ADC, zero it
    hx711.reset()

    try:
        hx711.zero(readings_to_average*3) # 30 readings
        
        sleep(0.2)
        
        raw = hx711.read_raw(readings_to_average*3)

        while None in raw:
            raw = hx711.read_raw(readings_to_average)
        else: 
            weights = hx711.get_weight()

        return sum(weights) # actual 0

    except Exception as e: 
        print(e)

def measure_mass():
    values = []
    last_total = 0

    for i in range(2): # get 2 readings
        while None in hx711.read_raw(readings_to_average): # Average 10 readings
            continue
            # print("None in raw")
            
        else: 
            weights = hx711.get_weight() 
            total = sum(weights)
            while total > 300 or total - last_total > 1: # Filter out outliers and ensure that samples are with in 1g of each other
                print(total)
                weights = hx711.get_weight() 

                last_total = total
            else: 
                values.append(total) # Add measurement to array

        # start = perf_counter()

        # while perf_counter() - start <  3: # 4 sec timer
        #     # Read Raw Data
            
        #     raw_vals = hx711.read_raw(readings_to_average*3)
            
        #     sleep(0.2)

        #     weights = hx711.get_weight() 
        #     # print(weights)
            
        #     values.append(sum(weights)) # Add measurement to array

        #     # read_duration = perf_counter() - start

    print("Average Weight Measurement: {}".format(sum(values)/len(values)))
    # print(values)

    return sum(values)/len(values) # Avg of measurement over four seconds