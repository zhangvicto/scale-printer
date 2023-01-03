import cv2
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
time.sleep(1)
if ret:
    cv2.imwrite('test.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

cap.release()