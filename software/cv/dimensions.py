import cv2
import time
from picamera2 import PiCamera2

picam2 = PiCamera2()
time.sleep(2)
picam2.start_and_capture_file("test.jpg")

