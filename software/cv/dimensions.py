import cv2
import time
from picamera import PiCamera

camera = PiCamera()
time.sleep(2)
camera.capture("/dimensions.jpg")

