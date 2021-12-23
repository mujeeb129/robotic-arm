import cv2 as cv
import numpy as np

class FaceDetection():
    def startDetection(self):
        self.faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        
        while True:
            self.ret, self.img = cap.read()
            self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
            self.faces = self.faceCascade.detectMultiScale(self.gray, 1.2, 5)
            for (x,y,w,h) in self.faces:
                cv.rectangle(self.img, (x,y), (x+w,y+h), (255,0,0) , 2)
                roi_gray = self.gray[y:y+h, x:x+w]
                roi_color = self.img[y:y+h, x:x+w]
                cv.imshow('video', self.img)
                self.k = cv.waitKey(30) & 0xff
                if self.k == 27:
                    break

        cap.release()
        cv.destroyAllWindows()

x = FaceDetection()
x.startDetection()
