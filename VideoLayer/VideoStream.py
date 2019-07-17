import cv2
import Config.eye_shield_conf as conf
from VideoLayer import FaceDetection
from VideoLayer import FaceRecognition
from DAL.MongoHelper import DbHelper
from BI.Image import Image
import time

class VideoStream:
    def __init__(self):
        self.isStart = False
        self.rtmp_addr = conf.CAMERA_RTMP_ADDR
        self.db = DbHelper()

    def start_capture(self):
        self.isStart = True
        cap = cv2.VideoCapture(self.rtmp_addr)
        i=0
        while(i < 10):
        #while(self.isStart):
            ret, frame = cap.read()
            res = FaceDetection.framesFilter(frame)
            if(res):
                tz_list = FaceRecognition.find_match(frame)
                for tz in tz_list:
                    suspect = self.db.get_suspect_by_tz(tz)
                    im = Image(frame, "Tel Aviv", time.time())
                    suspect.add_image()
                    print(tz[0])

                i = i+1

        cap.release()

    def stop_capture(self):
        self.isStart =False


v = VideoStream()

v.start_capture()