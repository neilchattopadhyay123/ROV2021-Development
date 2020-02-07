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

RUNNING = True # Whether the client is running

def main ():
    global RUNNING

    # Create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    PRINT('Connected to ' + ENC_VALUE(HOST + ':'+ PORT) + '.', SUCCESS)

    # Start the camera video thread
    stream = VideoStream().start()

    while RUNNING:
        # Get the current frame read by the video stream
        _, frame = cv2.imencode('.jpg', stream.read(), ENCODE_PARAM)

        # Send data
        send(s, [frame])

        # Recieve data
        recv_data = recv(s)

        # Check if a command was sent
        if recv_data[DATA_IDX_COMMAND] == COMMAND_QUIT:
            PRINT('Recieved command ' + ENC_VALUE(COMMAND_QUIT) + '.', INFO)
            
            RUNNING = False

    s.close()
    stream.stop()

    PRINT('Quit.', SUCCESS)

if __name__ == '__main__':
    main()
