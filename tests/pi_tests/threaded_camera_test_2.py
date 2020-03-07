from threading import Thread
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

RES = (640, 480)

class VideoStream:
    def __init__(self):
        self.camera = PiCamera()
        self._rawCapture = PiRGBArray(self.camera, size=RES)

        self.camera.resolution = RES
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

stream = VideoStream().start()

while True:
    try:
        cv2.imshow('frame', stream.read())
    except:
        pass
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop()
