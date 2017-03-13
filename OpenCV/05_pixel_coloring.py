## This program shows the effect of pixel coloring on a picture of a rose.
## It finds all the white pixels and changes them to red pixels.
## Created February 17, 2017.
##
## Sites visited:
## http://stackoverflow.com/questions/29125349/change-color-of-a-pixel-with-opencv
##

import cv2
import numpy as np

img = cv2.imread('rose.jpg')
# print img # debug
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print img_gray # debug

# new = [[[0,0,155%j] for j in i] for i in img_gray]
new = [[[255%j,255%j,j] for j in i] for i in img_gray]
dt = np.dtype('f8')
new = np.array(new,dtype=dt)

cv2.imwrite('img.jpg',new)
