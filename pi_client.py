import socket
import pickle
import struct
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from constants import *
from threading import Thread
from video_stream import VideoStream
from client_utils import *

RUNNING = True

def main ():
    global RUNNING
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    stream = VideoStream().start()

    while RUNNING:
        _, frame = cv2.imencode('.jpg', stream.read(), ENCODE_PARAM)
        
        send(s, [frame])]

        recv_data = recv(s)

        if recv_data[DATA_IDX_COMMAND] == COMMAND_QUIT:
            PRINT('Recieved command ' + ENC_VALUE(COMMAND_QUIT) + '.', INFO)
            
            RUNNING = False

    s.close()
    stream.stop()

if __name__ == '__main__':
    main()
