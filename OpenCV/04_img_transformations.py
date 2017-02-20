## This script shows the effect of matrix transformations on an image.
## Created on February 14, 2017.
##
## The material was gathered from the following webpages:
## http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748
##

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in
filename = 'saitama_chibi.png'
img = cv2.imread(filename)

# Perform matrix transformations
img2 = img[:,:,::-1]                # covert from bgr to rgb
img3 = img[:,::-1,:]                # flip image along vertical axis
img4 = img[::-1,:,:]                # flip image along horizontal axis
img5 = img[::-1,::-1,:]             # flip image along both x and y axes

# Write images out
cv2.imwrite('saitama_bgr_to_rgb.png',img2)
cv2.imwrite('saitama_flip_ver.png',img3)
cv2.imwrite('saitama_flip_hor.png',img4)
cv2.imwrite('saitama_flip_both_axes.png',img5)

plt.subplot(121);plt.imshow(img)    # expects distorted color
plt.subplot(122);plt.imshow(img2)   # expect true color
plt.show()

cv2.imshow('bgr image',img)         # expects true color
cv2.imshow('rgb image',img2)        # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()