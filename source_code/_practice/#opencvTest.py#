    
# importing cv2 
import cv2
  
imcap = cv2.VideoCapture(0)
imcap.set(3, 640) 
imcap.set(4, 480) 

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    success, img = imcap.read()  
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)

    cv2.imshow('face_detect', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow('face_detect')



#while(True):
      
    # Capture the video frame
    # by frame
    #ret, frame = vid.read()
  
    # Display the resulting frame
   # cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
 #   if cv2.waitKey(1) & 0xFF == ord('q'):
  #      break
  
# After the loop release the cap object
#vid.release()
# Destroy all the windows
#cv2.destroyAllWindows()
# Opening image
#img = cv2.imread("image.jpg")
#cv2.imshow("Name",img)
#cv2.waitkey(1)  
# OpenCV opens images as BRG 
# but we want it as RGB and 
# we also need a grayscale 
# version
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
# Creates the environment 
# of the picture and shows it
#plt.subplot(1, 1, 1)
#plt.imshow(img_rgb)
#plt.show()
