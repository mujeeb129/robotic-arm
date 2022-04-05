import cv2 as cv
import numpy as np

class ReconAlgo:
    def StartDectection(self):
        self.faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        while True:
            self.ret, self.img = self.cap.read()
            self.grey = cv.cvtColor(self.img ,cv.COLOR_BG2GRAY )
            self.faces = self.faceCascade.detectMultiscale(gray,  1.3, 5)
            for (x ,y, w, h) in self.faces:
                self.cv.



def StartDetection():
    faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
        
    while True:
        ret, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0) , 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv.imshow('video', gray)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break

    cap.release()
    cv.destroyAllWindows()

StartDetection()
