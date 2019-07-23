import cv2
import Config.eye_shield_conf as conf


class VideoStream:
    def __init__(self):
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(conf.CAMERA_RTMP_ADDR)

    def get_frame(self):
        frame = None
        if self.cap:
            ret, frame = self.cap.read()

        return frame

    def stop(self):
        if self.cap:
            self.cap.release()
            self.cap = None
