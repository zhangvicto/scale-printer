import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0) #setup
ret, frame = cap.read() # take image and store in variable
time.sleep(1) # give time to prevent a green image
if ret:
    cv2.imwrite('test.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # write to a file

cap.release() # release

img = cv2.imread('test.jpg')
img_rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
print(img_rotate.shape[:2])
img_cropped = img_rotate[0:1000, 0:1200] # crop
img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

cv2.imwrite('blur.jpg', img_blur) # write to a file

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

cv2.imwrite('edges.jpg', edges) # write to a file