from picamera.array import PiRGBArray
from picamera import PiCamera
from constants import *
from threading import Thread
import time

class VideoStream:
    def __init__(self):
        ''' Constructor '''

        self.camera = PiCamera() # Create PiCamera object
        self._rawCapture = PiRGBArray(self.camera, size=CAMERA_RES)

        # Setup camera settings
        self.camera.resolution = CAMERA_RES # Set camera resolution
        # self.camera.mode = CAMERA_MODE # Set the aspect ratio of the camera
        self.camera.framerate = CAMERA_FPS # Set camera fps
        # self.camera.shutter_speed = CAMERA_SHUTTER_SPEED # Set camera shutter speed
        # self.camera.brightness = CAMERA_BRIGHTNESS # Set camera brightness
        # self.camera.awb_mode = CAMERA_AWB_MODE # Set camera auto white balance

        # Create a thread for getting images from the camera
        self.thread = Thread(target=self.update, args=())
        self.frame = None
        self.running = False

        self.t0 = time.time()
        self.tt = self.t0;
        self.i = 0
        self.it = 0
        self.fps_list = []

        time.sleep(2) # Delay

    def start(self):
        ''' Begin reading the camera frames '''
        
        self.running = True # Sets main boolean to True
        
        self.thread.start()# Starts thread

        PRINT('Started video stream.', SUCCESS)
        
        return self

    def update(self):
        ''' The main thread loop for getting the current camera images '''

        # Main loop
        while self.running:
            self.i += 1
            self.it += 1
            
            # Get a picture from the camera and save it to a variable which can be accessed outside of the class
            self.camera.capture(self._rawCapture, format="bgr", use_video_port=True)
            self.frame = self._rawCapture.array

            # Clears stream for next frame
            self._rawCapture.truncate(0)

            # Updates t
            self.t = time.time()
            
            if self.t - self.t0 >= 1:
                self.fps_list += [self.i]
                
                # print(self.it / (self.t - self.t0), self.i, sum(self.fps_list) / len(self.fps_list))

                self.t0 = self.t
                self.i = 0

            time.sleep(0.02) # Delay
            
    def read(self):
        ''' Get the last frame the camera has read '''
        
        return self.frame

    def stop(self):
        ''' Stop capturing frames and stop running the thread '''
        
        self.running = False # Sets main boolean to False
        
        self.thread.join() # Ends thread
        self.camera.close() # Closes camera connection

        PRINT('Closed video stream.', SUCCESS)
