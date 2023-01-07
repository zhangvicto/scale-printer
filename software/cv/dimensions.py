import cv2
import numpy as np
import time
import math

cannyThres1 = 40
cannyThres2 = 180

def capture(numCapture): 

    cap = cv2.VideoCapture(0) #setup
    ret, frame = cap.read() # take image and store in variable
    time.sleep(1.5) # give time to prevent a green image
    if ret:
        cv2.imwrite('capture' + str(numCapture) + '.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # write to a file
        cap.release() # release
    else: 
        cap.release() # release
    

# def blend(list_images): # Blend images equally
#     equal_fraction = 1.0/(len(list_images))
#     output = np.zeros_like(list_images[0])
#     for img in list_images:
#         output += img * equal_fraction
#     return output


def image_process(): 
    # Capture x images
    numCapture = 5
    for i in range(0, numCapture): 
        capture(i)

    # Blending Images
    # images = []
    # for i in range(0, numCapture): 
    #     images.append(cv2.imread('capture'+str(numCapture)+'.jpg'))
    # cv2.imwrite('capture.jpg', blend(images))
    
    img = cv2.imread('capture0.jpg')
    img_rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # print(img_rotate.shape[:2]) # output dimensions
    img_cropped = img_rotate[0:440, 0:480] # crop

    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    cv2.imwrite('blur.jpg', img_blur) # write to a file

    # View Edges
    # edges = cv2.Canny(image=img_blur, threshold1=cannyThres1, threshold2=cannyThres2) # Canny Edge Detection
    # cv2.imwrite('edges.jpg', edges) # write to a file

    # Draw Contours
    # contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img_cropped, contours[0], -1, color=(255,255,255), thickness=1)
    # time.sleep(1) # give time to prevent a green image
    # cv2.imwrite("output.jpg", img_cropped)

    return img_blur

def edges(img):
    return cv2.Canny(img, threshold1=cannyThres1, threshold2=cannyThres2) # Canny Edge Detection

def analyze_edge(edges): 
    # Using Houghlines, Find Houghlines using Canny Edges
    lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

    # Draw the Hough Lines
    cEdges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    # cEdgesP = np.copy(cEdges)

    difference = [] # Array for Distances Between All Hough Lines

    # Draw the lines
    if lines is not None:
        for i in range(0, len(lines)):
            x0 = hough_coord(lines, i)[0]
            y0 = hough_coord(lines, i)[1]
            a = hough_coord(lines, i)[2]
            b = hough_coord(lines, i)[3]
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(cEdges, pt1, pt2, (0,0,255), 1, cv2.LINE_AA) # Draw Hough Lines
    
        # Find largest distance between lines. this is likely distance between the outer edges
        for i in range(0, len(lines)):
            # Calculate distance between all lines
            for j in range(i+1, len(lines)): 
                distX = abs(hough_coord(lines, j)[0] - hough_coord(lines, i))[0]
                distY = abs(hough_coord(lines, j)[1] - hough_coord(lines, i))[1]

                if distX or distY > 400: 
                    difference.append([max(distX, distY), i if distX > distY else j])
                else: 
                    return 'Distance too short, check your camera.'

        print(max(difference)[0])

    cv2.imwrite("lines.jpg", cEdges) # Send to file 

    distanceX = max(difference[0]) # this is now the distance to be used for calculating the size of 

    # Draw Probablistic Hough Lines

    # linesP = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None, 50, 10)

    # if linesP is not None: 
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0]
    #         cv2.line(cEdgesP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)

    # cv2.imwrite("plines.jpg", cEdgesP)
    return distanceX
    
# Find Dimension of the Printed Part  
def find_dim(distanceX, edges): 

    length = 0 # code here to find pixel size of the printed part
    width = 0
    
    # Using Contours
    contours, h = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # Find Highest Hierarchy
    maxH = find_maxH(h)

    # Draw ALL 
    # cv2.drawContours(edges, contours, -1, (0,0,255), 1)
    
    contourArea = []
    # Draw Any Significant Contours
    for i in range(0, len(contours)): 
        # print(cv2.contourArea(contours[i]))
        # Using RETER_TREE 
        # Remove any contour that are 
        print(maxH)
        print(h[0][0])
        # Draw Contours that are big enough, maybe use a percentile calculation instead
        if cv2.contourArea(contours[i]) > 100 and h[0][i][3] == maxH: 
            cv2.drawContours(edges, contours[i], -1, (255,255,255), 1)
            contourArea.append(cv2.contourArea(contours[i]))

    print(contourArea)

    cv2.imwrite("contours.jpg", edges)
    # Now we find the largest contour and highlight it 
    # cv2.drawContours(img, contours, -1, color=(255,255,255), thickness=1)

    return [width*distanceX/250, length*distanceX/250] # in mm


# Helper Functions
# ----------------------------------------------------------------------- # 

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

    return [x0, y0, a, b]

# Recursively Find Max in a List 
def find_maxH(h):
    array = h[0]
    m = []
    if len(array) == 1:
        return array[3]
    else:
        for i in range(0, len(array)): 
            m.append(array[3]) 
        return max(m)


# Execute Script
# ----------------------------------------------------------------------- # 
blurred = image_process()
edge = edges(blurred)
find_dim(analyze_edge(edge), edge)
