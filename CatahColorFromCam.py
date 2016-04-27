import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def to_hsv(r,g,b):
    color = np.uint8([[[b,g,r]]])
    hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
    return hsv_color
while(1):

    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # lower_blue  = np.array([G, B, R], dtype = "uint8")
    ''' Asia's skin color
    lower  = np.array([0, 0, 0], dtype = "uint8")
    upper  = np.array([100, 100, 255], dtype = "uint8")
    '''
    lower  = np.array([0, 0, 0], dtype = "uint8")
    upper  = np.array([100, 100, 255], dtype = "uint8")
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower, upper)
    
   
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print lower_blue
        print upper_blue
        break

cv2.destroyAllWindows()
