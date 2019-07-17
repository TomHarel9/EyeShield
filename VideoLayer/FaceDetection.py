import cv2

def framesFilter(frame):
    frontalFaceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    profileFaceCascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    #-- Detect faces
    faces = frontalFaceCascade.detectMultiScale(frame_gray, 1.3, 5)
    profileFaces = profileFaceCascade.detectMultiScale(frame_gray, 1.3, 5)

    #print(faces, profileFaces)
    if faces != () or profileFaces != ():
        #print("Face detected!")
        return True
    #print("No face detected")
    return False
