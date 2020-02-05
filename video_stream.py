from picamera.array import PiRGBArray
from picamera import PiCamera
from constants import *
from threading import Thread

class VideoStream:
    def __init__(self):
        ''' Constructor '''

        self.camera = PiCamera() # Create PiCamera object
        self._rawCapture = PiRGBArray(self.camera, size=CAMERA_RES)

        # Setup camera settings
        self.camera.resolution = CAMERA_RES # Set camera resolution
        self.camera.framerate = 20 # Set camera fps
        self.camera.shutter_speed = 1000 # Set camera shutter speed
        self.camera.brightness = 65 # Set camera brightness
        self.camera.awb_mode = 'incandescent' # Set camera auto white balance

        # Create a thread for getting images from the camera
        self.thread = Thread(target=self.update, args=())
        self.frame = None

    def start(self):
        ''' Begin reading the camera frames '''
        
        self.thread.start()

        PRINT('Started video stream.', SUCCESS)
        
        return self

    def update(self):
        ''' The main thread loop for getting the current camera images '''
        
        while True:
            # Get a picture from the camera and save it to a variable which can be accessed outside of the class
            self.camera.capture(self._rawCapture, format="bgr", use_video_port=True)
            self.frame = self._rawCapture.array
            
            self._rawCapture.truncate(0)
            
    def read(self):
        ''' Get the last frame the camera has read '''
        
        return self.frame

    def stop(self):
        ''' Stop capturing frames and stop running the thread '''
        
        self.thread.join()
        self.camera.close()

        PRINT('Closed video stream.', SUCCESS)
