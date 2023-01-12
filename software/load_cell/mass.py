#https://pypi.org/project/hx711-multi/

from hx711_multi import HX711
from time import perf_counter
import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

readings_to_average = 10
sck_pin = 6
dout_pins = [22, 4, 17, 27] # 1, 2, 3, 4
weight_multiples = [498.01008928572116, 474.10257936507116, 459.4241071428569, 459.72] # 128 gain
# weight_multiples = [249.2455357142855, 239.83, 227.31, 237.63] # 64 gain

# create hx711 instance
hx711 = HX711(dout_pins=dout_pins,
            sck_pin=sck_pin,
            channel_A_gain=128,
            channel_select='A',
            all_or_nothing=False,
            log_level='CRITICAL')
hx711.set_weight_multiples(weight_multiples=weight_multiples)


def tare(): 
    try:
        hx711.zero(readings_to_average=readings_to_average*3) # 30 readings
    except Exception as e:
        print(e)

def measure_mass():
    values = []
    mass = []

    try:
        start = perf_counter()

        while perf_counter() - start <  4: # 4 sec timer
            # Read Raw Data
            raw_vals = hx711.read_raw(readings_to_average=readings_to_average)

            # This function call will not perform a new measurement, it will just use what was acquired during read_raw()
            while not None in raw_vals: 
                weights = hx711.get_weight() 
                values.append(weights) # Add measurement to array

            # read_duration = perf_counter() - start

    except Exception as e:
        print(e)

    # print(values) # weight
    if values: 
        for value in values: 
            mass.append(sum(value))

    return sum(mass)/len(mass) # Avg of measurement over four seconds