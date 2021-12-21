import cv2 as cv
import numpy as np
import os

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv.FONT_HERSHEY_SIMPLEX

id = 0

name = ['admin']

cam = cv.VideoCapture(0)

cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW) ,int(minH))
    )
    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if confidence < 100:
            id = name[id]
            confidence = ' {0}%'.format(round(100-confidence))
        else:
            id = 'dunno'
            confidence = ' {0}%'.format(round(100-confidence))

        cv.putText(
            img,
            str(id),
            (x, y),
            font,
            1,
            (255 ,255, 255),
            2
        )
    cv.imshow('camera', img)
    k = cv.waitKey(10) & 0xff

    if k== 27:
        break
    
cam.release()
cv.destroyAllWindows()
