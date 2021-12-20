import cv2 as cv
import numpy as np
import os

recognizer = cv.face.LBHFaceRecognizer_create()
recognizer.read('trainer.yml')

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv.FONT_HERSHEY_SIMPLEX

id = 0

name = ['admin']

cam = cv.VideoCapture(2)

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
        minNeigbours = 5,
        minSize = (int(minW) ,int(minH))
    )
    for (x,y,w,h) in faces:
        cv.rectangle(img(x,))
