from picamera.array import PiRGBArray
from picamera import PiCamera
from constants import *
from threading import Thread

class VideoStream:
    def __init__(self):
        self.camera = PiCamera()
        self._rawCapture = PiRGBArray(self.camera, size=CAMERA_RES)

        self.camera.resolution = CAMERA_RES
        self.camera.framerate = 20
        self.camera.shutter_speed = 1000
        self.camera.brightness = 65
        self.camera.awb_mode = 'incandescent'
        
        self.thread = Thread(target=self.update, args=())
        self.frame = None

    def start(self):
        self.thread.start()
        
        return self

    def update(self):
        while True:
            self.camera.capture(self._rawCapture, format="bgr", use_video_port=True)
            self.frame = self._rawCapture.array
            
            self._rawCapture.truncate(0)
            
    def read(self):
        return self.frame

    def stop(self):
        self.thread.join()
        self.camera.close()
