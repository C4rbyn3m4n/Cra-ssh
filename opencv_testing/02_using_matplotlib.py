## By using matplotlib to plot pictures, we can learn the value of
## a color.
## Created on February 14, 2017
##
## The material was gathered from the following webpages:
## http://docs.opencv.org/3.2.0/dc/d2e/tutorial_py_image_display.html
##

import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = 'saitama_chibi.png'
# img = cv2.imread(filename,0)    # display in grayscale
img = cv2.imread(filename,1)[:,:,::-1] # display in color

# I don't know what cmap and interpolation options do.
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()