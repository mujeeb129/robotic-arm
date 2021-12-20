import cv2 as cv
import os
from PIL import Image
import numpy as np

path = 'dataset'
recognizer = cv.face.LBPHFaceRecognizer_create()
detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml");


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        print(os.path.split(imagePath)[-1].split('_')[1].split('.')[0])
        id = int(os.path.split(imagePath)[-1].split('_')[1].split('.')[0])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples,ids

print('[info] Training faces, please wait for few seconds')

faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer.yml')
print('[info] {0} faces trained. Exiting Program'.format(len(np.unique(ids))))
