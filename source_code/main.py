import cv2 as cv
import numpy as np

#to start capturing video
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

faceCascade = cv.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20,20)
    )
    for(x,y,w,h) in faces:
