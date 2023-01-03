import cv2
import time

cap = cv2.VideoCapture(0) #setup
ret, frame = cap.read() # take image and store in variable
time.sleep(1) # give time to prevent a green image
if ret:
    cv2.imwrite('test.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # write to a file

cap.release() # release

img = cv2.imread('test.jpg') 

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
new, edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

if new:
    cv2.imwrite('edges.jpg', edges, [cv2.IMWRITE_JPEG_QUALITY, 100]) # write to a file