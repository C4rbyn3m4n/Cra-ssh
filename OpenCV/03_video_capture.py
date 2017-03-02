## Created on February 14, 2017
##
## The material was gathered from the following webpages:
## http://docs.opencv.org/3.2.0/dd/d43/tutorial_py_video_display.html
##

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    # smurf_filter = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Display the resulting frame. To display in color, comment
    # out the line above 'gray = ...' and change the word 'gray'
    # below to 'frame'
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
