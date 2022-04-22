import cv2


classFile = 'coco.names'
classNames = []

with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)
