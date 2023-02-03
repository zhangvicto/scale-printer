#https://pypi.org/project/hx711-multi/

from hx711_multi import HX711
from time import perf_counter, sleep
import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

readings_to_average = 10
sck_pin = 6
dout_pins = [22, 4, 17, 27] # 1, 2, 3, 4
weight_multiples = [13056.945625, 12197.703125, 11915.913035714253, 11894.808035714319] # 128 gain

# create hx711 instance
hx711 = HX711(dout_pins=dout_pins,
            sck_pin=sck_pin,
            channel_A_gain=128,
            channel_select='A',
            all_or_nothing=False,
            log_level='CRITICAL')
hx711.set_weight_multiples(weight_multiples=weight_multiples)


def tare(): 
    # reset ADC, zero it
    hx711.reset()

    try:
        hx711.zero(readings_to_average=readings_to_average*3) # 30 readings
        
        sleep(0.2)
        
        raw = hx711.read_raw(readings_to_average=readings_to_average*3)
        
        sleep(0.2)
        
        while None in raw:
            raw = hx711.read_raw(readings_to_average=readings_to_average*3)
        else: 
            weights = hx711.get_weight()

        return sum(weights) # actual 0

    except Exception as e: 
        print(e)


# need to add filtering...
def measure_mass():
    values = []

    try:
        for i in range(4): # get 4 readings
            while None in hx711.read_raw(readings_to_average*3):
                continue
                # print("None in raw")
                
            else: 
                weights = hx711.get_weight() 
                while sum(weights) > 300 or sum(weights) < 0: 
                    weights = hx711.get_weight() 
                
                else: 
                    values.append(sum(weights)) # Add measurement to array

        # start = perf_counter()

        # while perf_counter() - start <  3: # 4 sec timer
        #     # Read Raw Data
            
        #     raw_vals = hx711.read_raw(readings_to_average*3)
            
        #     sleep(0.2)

        #     weights = hx711.get_weight() 
        #     # print(weights)
            
        #     values.append(sum(weights)) # Add measurement to array

        #     # read_duration = perf_counter() - start

    except Exception as e:
        print(e)

    print("Average Weight Measurement: {}".format(sum(values)/len(values)))
    # print(values)

    return sum(values)/len(values) # Avg of measurement over four seconds