import os
import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
count = 0
while True:
    ret,img = cap.read()
    name = 'dataset/'+str(count) + '.jpg'
    cv.imshow('camera' , img)
    k = cv.waitKey(33) & 0xff
    if k == 27:
        break
    elif k == 115:
        cv.imwrite(name, img)
        count += 1

cap.release()
cv.destroyAllWindows()
    
    

