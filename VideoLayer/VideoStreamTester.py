import cv2
import Config.eye_shield_conf as conf

myrtmp_addr = conf.CAMERA_RTMP_ADDR
cap = cv2.VideoCapture(myrtmp_addr)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()