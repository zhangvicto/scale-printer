import cv2
import time
import picamera2

picam2 = picamera2.PiCamera()
time.sleep(2)
picam2.start_and_capture_file("test.jpg")

