# import cv2
import time
from picamera2 import Picamera2

picam2 = Picamera2()

time.sleep(2)

picam2.start_and_capture_file('test.jpg', 'rgb')

