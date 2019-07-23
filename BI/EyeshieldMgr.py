from VideoLayer import FaceDetection
from VideoLayer import FaceRecognition
from VideoLayer import VideoStream
from DAL.MongoHelper import DbHelper
from Models.Image import Image
import time
import threading


class EyeShieldMgr(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.isStart = False
        self.db = DbHelper()
        self.video_stream = VideoStream.VideoStream()

    def start_capture(self):
        self.isStart = True
        while self.isStart:
            self.video_stream.start()
            frame = self.video_stream.get_frame()
            if frame is None:
                print("invalid frame")
                continue
            res = FaceDetection.framesFilter(frame)
            if res:
                im = Image(frame, "Raanana", time.time())
                file_id = self.db.save_image(im)
                tz_list = FaceRecognition.find_match(frame)
                for tz in tz_list:
                    print(tz)
                    suspect = self.db.get_suspect_by_tz(tz)
                    suspect.add_image(file_id)
                    self.db.update_suspect(suspect)
                    im.tag()
                    self.db.update_image_metadata(im)

    def run(self):
        self.start_capture()

    def stop(self):
        self.stop_capture()

    def stop_capture(self):
        self.isStart = False
        self.video_stream.stop()
