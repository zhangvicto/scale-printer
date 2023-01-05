import cv2
import numpy as np
import time
import math

cannyThres1 = 40
cannyThres2 = 180

def capture(): 
    cap = cv2.VideoCapture(0) #setup
    ret, frame = cap.read() # take image and store in variable
    time.sleep(2) # give time to prevent a green image
    if ret:
        cv2.imwrite('test.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # write to a file
    cap.release() # release

def image_process(): 
    img = cv2.imread('test.jpg')
    img_rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # print(img_rotate.shape[:2]) # output dimensions
    img_cropped = img_rotate[0:400, 0:480] # crop

    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    cv2.imwrite('blur.jpg', img_blur) # write to a file

    edges = cv2.Canny(image=img_blur, threshold1=cannyThres1, threshold2=cannyThres2) # Canny Edge Detection
    # cv2.imwrite('edges.jpg', edges) # write to a file

    # img = cv2.imread('edges.jpg')
    contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img_cropped, contours[0], -1, color=(255,255,255), thickness=1)
    time.sleep(1) # give time to prevent a green image
    cv2.imwrite("output.jpg", img_cropped)

def analyze_edge(): 
    img = cv2.imread('blur.jpg')
    edges = cv2.Canny(img, threshold1=cannyThres1, threshold2=cannyThres2) # Canny Edge Detection
    
    # Using contours?
    # contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # for contour in contours: 
    #     print(cv2.contourArea(contour))
    # Now we find the largest contour and highlight it 
    # cv2.drawContours(img, contours, -1, color=(255,255,255), thickness=1)

    # Using Houghlines
    lines = cv2.HoughLines(edges, 1, np.pi/180, 150)
    linesP = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None, 50, 10)

    # cv2.imwrite("lines.jpg", lines)
    # Draw the lines
    cEdges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cEdgesP = np.copy(cEdges)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(cEdges, pt1, pt2, (0,0,255), 1, cv2.LINE_AA)
    
        # Find largest distance between lines. this could be the distance between the outer edges
        difference = []
        for i in range(0, len(lines)):
            # calculate distance between all lines
            for j in range(i+1, len(lines)): 
                distX = abs(hough_coord(lines, j)[0] - hough_coord(lines, i))[0]
                distY = abs(hough_coord(lines, j)[1] - hough_coord(lines, i))[1]

                difference.append(max(distX, distY))

        print(difference)
        print(max(difference))

    cv2.imwrite("lines.jpg", cEdges)

    # Draw Probablistic Hough Lines
    if linesP is not None: 
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cEdgesP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)

    cv2.imwrite("plines.jpg", cEdgesP)

    for line in linesP: 
        if line[0]-line[1] > 10:
            cv2.line(cEdgesP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)

    # find the two edges on the side and calculate their distance, X AXIS
    # distanceX = coordX2 - coordX1
    # distanceY = coordY2 - coordY1

    # length = # code here to find pixel size of the printed part

    # return width*distanceX/200, length*distanceY/200

# Compute Hough Line Coordinate
def hough_coord(lines, i):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho
    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

    return [x0, y0]

capture()
image_process()
analyze_edge()