import cv2
import argparse

def framesFilter(frame):
    frontalFaceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    profileFaceCascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    #-- Detect faces
    faces = frontalFaceCascade.detectMultiScale(frame_gray, 1.3, 5)
    profileFaces = profileFaceCascade.detectMultiScale(frame_gray, 1.3, 5)
    # for (x,y,w,h) in faces:
    #     center = (x + w//2, y + h//2)
    #     frame = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    print(faces, profileFaces)
    if faces != () or profileFaces != ():
        print("Yes")
        return img
    return None



img = cv2.imread('C:\\Users\\tomharel\Desktop\Software Engineering\\4th Year\Final Project\\Face.jpg', 1)

isDetectFaces = framesFilter(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
