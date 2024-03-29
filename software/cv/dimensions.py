import cv2
import numpy as np
import time
import math
from scipy import ndimage

# Tuning parameters 
# LIGHTS ON/OFF
lights = True
if lights:
    cannyThres1 = 60
    cannyThres2 = 170
else: 
    cannyThres1 = 80
    cannyThres2 = 200

def capture(numCapture): 

    cap = cv2.VideoCapture(0) # Setup
    ret, frame = cap.read() # Take image and store in variable
    time.sleep(1.5) # Give time to prevent a green image
    if ret:
        cv2.imwrite('capture' + str(numCapture) + '.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100]) # Write to a file
        cap.release() # Release
    else: 
        cap.release() # Release

def image_process(): 
    # Capture 5 images
    numCapture = 1
    for i in range(0, numCapture): 
        capture(i)

    # Blending Images
    # images = []
    # for i in range(0, numCapture): 
    #     images.append(cv2.imread('capture'+str(numCapture)+'.jpg'))
    # cv2.imwrite('capture.jpg', blend(images))
    
    img = cv2.imread('capture0.jpg') # Read first Capture
    img_rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # Rotate by 90 DEG
    # print(img_rotate.shape[:2]) # Output dimensions
    img_cropped = img_rotate[118:515, 5:472] # Crop

    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)

    final = ndimage.rotate(img_gray, -0.3) # Rotate, next version use hough line to measurement angle of rotation
    cv2.imwrite('final.jpg', final) # Write to a file

    # View Edges
    # edges = cv2.Canny(image=img_blur, threshold1=cannyThres1, threshold2=cannyThres2) # Canny Edge Detection
    # cv2.imwrite('edges.jpg', edges) # write to a file

    # Draw Contours
    # contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img_cropped, contours[0], -1, color=(255,255,255), thickness=1)
    # time.sleep(1) # give time to prevent a green image
    # cv2.imwrite("output.jpg", img_cropped)

    return final

def edges(img):
    return cv2.Canny(img, threshold1=cannyThres1, threshold2=cannyThres2) # Canny Edge Detection

def analyze_edge(edges): 
    # Using Houghlines, Find Houghlines using Canny Edges
    lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

    # Draw the Hough Lines, find the max distance between any lines -- likely the dimenstion of the bed
    cEdges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) # covert color
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
                    return None # Distance is too small, likely not the bed

        print("Bed Pixel Size: " + str(max(difference)[0]))

    cv2.imwrite("lines.jpg", cEdges) # Store

    distanceX = max(difference)[0] if max(difference)[0] > 460 else 460 # this is now the distance to be used for calculating the size of 
    # 460 should be more or less the distance

    # print(cv2.imread("lines.jpg").shape)
    # print(distanceX)
    # Draw Probablistic Hough Lines
    # linesP = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None, 50, 10)

    # if linesP is not None: 
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0]
    #         cv2.line(cEdgesP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)

    # cv2.imwrite("plines.jpg", cEdgesP)
    
    return distanceX
    
# Find Dimension of the Printed Part  
def find_dim(x, y, distanceX, edges, iter): 

    length = 0
    width = 0
    
    # Crop the image so we only see the printed piece 
    printed = edges[y[0]:y[1], x[0]:x[1]] 

    # cv2.imwrite('printed.jpg', printed)
    # (x0, y0) and (x1, y1) are the coordinates that describe the opposite edges of the desired area for analysis

    # Find Hough Lines of the printed shape
    # printed_lines = cv2.Canny(image=printed,threshold1=cannyThres1, threshold2=cannyThres2)
    lines = cv2.HoughLines(printed, 0.5, np.pi/180, 20)
    # print(lines)

    # print(lines)
    draw_hough(lines, printed, 'printed-lines.jpg')

    # Draw Hough Lines
    if lines is not None:
        # draw_hough(lines, printed, 'printed-lines.jpg')
        # print('Drawing Hough Lines...')

        # Classify the lines (hori or verti) 
        linesH = []
        linesV = []
        for i in range(0, len(lines)):

            # rho = lines[i][0][0]
            theta = lines[i][0][1]
            print('Angle:{}'.format(math.degrees(theta)))

            if theta <= math.radians(0) and theta <= math.radians(10): 
                linesV.append(lines[i])
            elif theta >= math.radians(80) and theta <= math.radians(110):
                linesH.append(lines[i])
        
        draw_hough(linesH, printed, 'h-lines.jpg')
        draw_hough(linesV, printed, 'v-lines.jpg')

        # Find largest distance between lines. This is likely the outer edges
        differenceH = []
        differenceV = []

        for i in range(0, len(linesH)): 
            # Calculate distance between all lines
            for j in range(i+1, len(linesH)): 
                distXH = abs(hough_coord(linesH, j)[0] - hough_coord(linesH, i))[0]
                distYH = abs(hough_coord(linesH, j)[1] - hough_coord(linesH, i))[1]

                if distXH or distYH > 40: 
                    differenceH.append([max(distXH, distYH), i, j])
                else: 
                    return [None, None] # Distance too short, check the camera.

        for i in range(0, len(linesV)): 
            # Calculate distance between all lines
            for j in range(i+1, len(linesV)): 
                distXV = abs(hough_coord(linesV, j)[0] - hough_coord(linesV, i))[0]
                distYV = abs(hough_coord(linesV, j)[1] - hough_coord(linesV, i))[1]
                
                if distXV or distYV > 40: 
                    differenceV.append([max(distXV, distYV), i, j])
                else: 
                    return [None, None] # Distance too short, check the camera.
        
        # print(differenceH)
        # print(differenceV)


        if differenceH == [] or differenceV == []: # if empty
            width = None
            length = None

            return None
        else: 
            width = max(differenceV) #y
            length = max(differenceH) #x
            draw_hough([lines[width[1]], lines[length[1]], lines[width[2]], lines[length[2]]], printed, 'final-print' + str(iter) + '.jpg')

            ratio = distanceX/255
            print('Pixels: {},{}'.format(width[0], length[0]))
            print('Millimeters: {},{}'.format(width[0]/ratio, length[0]/ratio))

            return [width[0]/ratio, length[0]/ratio] # in mm
        
    # Using Contours - IGNORE
    # contours, h = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Draw ALL 
    # cv2.drawContours(edges, contours, -1, (0,0,255), 1)
    
    # contourArea = []
    # Draw Any Significant Contours
    # for i in range(0, len(contours)): 
        # print(cv2.contourArea(contours[i]))
        # Draw Contours that are big enough, maybe use a percentile calculation instead
        # if cv2.contourArea(contours[i]) > 100:  #and h[0][i][3] == maxH
        #     cv2.drawContours(edges, contours[i], -1, (255,255,255), 1)
        #     contourArea.append(cv2.contourArea(contours[i]))

    # print(contourArea)

    # cv2.imwrite("contours.jpg", edges)
    # Now we find the largest contour and highlight it 
    # cv2.drawContours(img, contours, -1, color=(255,255,255), thickness=1)

            
# Helper Functions
# ----------------------------------------------------------------------- # 

def draw_hough(lines, edges, filename): 
    cEdges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(0, len(lines)):
            x0 = hough_coord(lines, i)[0]
            y0 = hough_coord(lines, i)[1]
            a = hough_coord(lines, i)[2]
            b = hough_coord(lines, i)[3]
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(cEdges, pt1, pt2, (0,0,255), 1, cv2.LINE_AA) # Draw Hough Lines

    cv2.imwrite(filename, cEdges)
        
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

# Blend images equally
# def blend(list_images): 
#     equal_fraction = 1.0/(len(list_images))
#     output = np.zeros_like(list_images[0])
#     for img in list_images:
#         output += img * equal_fraction
#     return output


# Execute Script, comment on final
# ----------------------------------------------------------------------- # 
# iter = 2
# img = image_process() # Process Image
# edge = edges(img) # Canny Edge Detection
# distX = analyze_edge(edge) # Get the bed x-axis length in terms of pixels

# # Calculate Print Location
# square_size = 30
# x=[]
# y=[]

# if distX is not None:
#     ratio = distX/255 # Pixels per mm
#     print('Ratio: {}'.format(ratio))
#     # Pixel = mm * ratio

#     if distX: 
#         initial_gap = 10
#         gap = 10
#         x1 = round((initial_gap + gap/2 + (iter-1)*square_size)*ratio)
#         x2 = round(x1 + (square_size + gap)*ratio)
#         x = [x1, x2]
#         # print(x)
#         yOffset = -5
#         y1 = round((200 - (square_size + gap + yOffset))*ratio)
#         y2 = round((200- yOffset)*ratio)
#         y = [y1, y2]
#         # print(y)
#     else: 
#         x = [None, None]
#         y = [None, None]

# find_dim(x, y, distX, edge, iter)
