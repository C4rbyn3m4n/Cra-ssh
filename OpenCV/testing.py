import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('rose.jpg')
img_mpl = img[:,:,::-1] # image for use with matplotlib (abbreviated mpl)
# print img
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print img_gray

plt.imshow(img_mpl, interpolation = 'bicubic')
# plt.imshow(img_mpl, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# new = [[[255%j,255%j,j] for j in i] for i in img_gray]
# dt = np.dtype('f8') # 64-bit floating-point number
# new = np.array(new,dtype=dt)

# cv2.imwrite('img.jpg',new)