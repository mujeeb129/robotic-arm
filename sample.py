import cv2 as cv
import numpy as np

#to start capturing video
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while(True):
    ret,frame = cap.read()
    print(ret)
    #frame = cv.flip(frame,-1) #flip vertically
    

    cv.imshow('frame', frame)
    

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()


