import cv2

image = cv2.imread("image.jpg")
imgBlur = cv2.GaussianBlur
imgGray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)


cv2.imshow("grey" , image)
cv2.waitKey(0)


