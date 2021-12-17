import os
import cv2 as cv

def LiveSnap():
    subName = input('Enter subject number : ')

    if not os.path.isdir('dataset/' + subName):
        os.makedirs('dataset/' + subName)
    else:
        print('Subject {} already exists'.format(subName))
        return

    pathImg = 'dataset/{}/'.format(subName)

    cap = cv.VideoCapture(2)
    cap.set(3,640)
    cap.set(4,480)
    count = 0
    while True:
        ret,img = cap.read()
        name = 'dataset/{}/{}_{}.jpg'.format(subName,subName,count)
        cv.imshow('camera' , img)
        k = cv.waitKey(33) & 0xff
        if k == 27:
            break
        elif k == 115:
            cv.imwrite(name, img)
            count += 1

    cap.release()
    cv.destroyAllWindows()

LiveSnap()
