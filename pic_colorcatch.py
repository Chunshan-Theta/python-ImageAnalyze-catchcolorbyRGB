import cv2
import numpy as np
import sys

def to_hsv(r,g,b):
    color = np.uint8([[[b,g,r]]])
    hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
    return hsv_color

'''
'''
#img = cv2.imread(dir/pic.jpg)
img = cv2.imread('./t.png')
img = np.asarray(img)
    
   

    
#
# np.array([G, B, R], dtype = "uint8")
lower  = np.array([0, 0, 130], dtype = "uint8")
upper  = np.array([100, 100, 250], dtype = "uint8")
    
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(img, lower, upper)

output = cv2.bitwise_and(img, img, mask = mask)    
 

    
    
#Bitwise-AND mask and original image
#res = cv2.bitwise_and(img,img, mask= mask)


cv2.imshow("images", np.hstack([img, output]))
cv2.waitKey(0)    
