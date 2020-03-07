from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from threading import Thread

SIZE_DOESNT_MATTER = (640, 480)

camera = PiCamera()
rawCapture = PiRGBArray(camera, size=SIZE_DOESNT_MATTER)

camera.resolution = SIZE_DOESNT_MATTER
camera.framerate = 32
camera.shutter_speed = 1000
camera.brightness = 60
camera.awb_mode = 'incandescent'

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break

camera.close()
