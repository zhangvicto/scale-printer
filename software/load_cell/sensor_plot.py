import matplotlib.pyplot as plt
from hx711_multi import HX711
from time import perf_counter, sleep
import RPi.GPIO as GPIO  # import GPIO
import numpy as np

# init GPIO (should be done outside HX711 module in case you are using other GPIO functionality)
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
# reset ADC, zero it
hx711.reset()
sleep(0.2)
hx711.reset()

# Try Zeroing ADC
try:
    hx711.zero(readings_to_average)
except Exception as e:
    print(e)

# Set multiple 
hx711.set_weight_multiples(weight_multiples=weight_multiples)

measurements = []
cell1 = []
cell2 = []
cell3 = []
cell4 = []
time = []

# separate each cell into its own array of measurements 

# plot all with legends 
plt.plot([cell1, time])
plt.ylabel('Mass (g)')
plt.xlabel('Time (s)')