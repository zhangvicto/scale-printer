from hx711_multi import HX711
from time import perf_counter
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

weight_multiple = hx711.run_calibration(known_weights=[1, 2, 5, 10])
print(f'Weight multiple = {weight_multiple}')