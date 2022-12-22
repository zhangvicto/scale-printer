import RPi.GPIO as GPIO  # import GPIO

# init GPIO (should be done outside HX711 module in case you are using other GPIO functionality)
GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering

from hx711 import HX711

try:
    hx711 = HX711(
        dout_pin=20,
        pd_sck_pin=26,
        channel='A',
        gain=64
    )

    # hx711.reset()   # Before we start, reset the HX711 (not obligate)
    measures = hx711.get_raw_data(num_measures=3)
finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!
    print("\n".join(measures))