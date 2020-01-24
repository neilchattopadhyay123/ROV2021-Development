import socket
import pickle
import struct
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread

HOST = '192.168.2.1'
PORT = 6969
RES = (640, 480)

ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

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

def main ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    stream = VideoStream().start()

    while True:
        try:
            frame = stream.read()
            _, frame = cv2.imencode('.jpg', frame, ENCODE_PARAM)
            frame_data = pickle.dumps([frame], 0)

            s.sendall(struct.pack('>L', len(frame_data)) + frame_data)
            print('sending...')
        except Exception as e:
            print(e)

    s.close()
    stream.stop()

if __name__ == '__main__':
    main()
