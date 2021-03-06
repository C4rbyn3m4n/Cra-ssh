## The program below loads an image in grayscale, displays it, save the image
## if you press 's' and exit, or simply exit without saving if you press
## ESC key.
## Created February 14, 2017.
##
## The material was gathered from the following website(s):
## http://docs.opencv.org/3.2.0/dc/d2e/tutorial_py_image_display.html
##

import numpy as np
import cv2

filename = 'saitama_chibi.png'
img = cv2.imread(filename, 0)

cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:                     # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):             # wait for 's' key to save and exit
    cv2.imwrite('grayscale_'+filename, img)
    cv2.destroyAllWindows()
