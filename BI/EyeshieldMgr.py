import cv2
import Config.eye_shield_conf as conf
from VideoLayer import FaceDetection
from VideoLayer import FaceRecognition
from DAL.MongoHelper import DbHelper
from Models.Image import Image
import time
import threading


class EyeShieldMgr(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
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
                im = Image(frame, "Tel Aviv", time.time())
                file_id = self.db.save_image(im)
                tz_list = FaceRecognition.find_match(frame)
                for tz in tz_list:
                    suspect = self.db.get_suspect_by_tz(tz)
                    suspect.add_image(file_id)
                    self.db.update_suspect(suspect)
                i = i+1

        cap.release()

    def stop_capture(self):
        self.isStart =False
