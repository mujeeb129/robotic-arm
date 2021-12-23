import cv2 as cv
import numpy as np

class FaceDetection():
    def startDetection():
        self.faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv.VideoCapture(2)
        self.cap.set(3,640)
        self.cap.set(4,480)
        
        while True:
            ret, img = self.cap.read()
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x,y,w,h) in faces:
                cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0) , 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv.imshow('video', img)
                k = cv.waitKey(30) & 0xff
                if k == 27:
                    break

        cap.release()
        cv.destroyAllWindows()

