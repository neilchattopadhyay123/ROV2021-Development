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
import serial
import time

RUNNING = True  # Whether the client is running


def main():
    ''' Main method '''

    global RUNNING

    # Create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    PRINT('Connected to ' + ENC_VALUE(HOST + ':' + str(PORT)) + '.', SUCCESS)

    # connect to the arduino via serial
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    cr = '\n'

    # Start the camera video thread
    stream = VideoStream().start()
    last_serial_time = time.time()  # stores the last time a serial value was sent

    while RUNNING:
        # Get the current frame read by the video stream
        try:
            stream_frame = stream.read()
            _, frame = cv2.imencode('.jpg', stream_frame, ENCODE_PARAM)

            # Send data
            send(s, [frame])

        except Exception as e:  # Prints Error
            PRINT(str(e), ERROR)

        # Recieve data
        recv_data = recv(s)

        # Check if a command was sent
        if recv_data[DATA_IDX_COMMAND] == COMMAND_QUIT:  # If quit command was recieved RUNNING = false
            PRINT('Recieved command ' + ENC_VALUE(COMMAND_QUIT) + '.', INFO)

            joy_vrt = round(4 * (1 - 0))
            joy_fwd = round(4 * (1 - 0))
            joy_rot = round(4 * (1 + 0))

            submit = str(joy_vrt * 100 + joy_fwd * 10 + joy_rot)

            ser.write(submit.encode('utf-8'))
            ser.write(cr.encode('utf-8'))

            RUNNING = False
        elif time.time() - last_serial_time >= 1:
            if recv_data and len(recv_data) == 3:  # checks if recv data is empty
                joy_vrt = round(4 * (1 - recv_data[1][3]))
                joy_fwd = round(4 * (1 - recv_data[1][1]))
                joy_rot = round(4 * (1 + recv_data[1][2]))

                submit = str(joy_vrt * 100 + joy_fwd * 10 + joy_rot)
                print(submit)

                ser.write(submit.encode('utf-8'))
                ser.write(cr.encode('utf-8'))
                line = ser.readline().decode('utf-8').rstrip()
                print(line)

            last_serial_time = time.time()

    s.close()  # Closes socket
    stream.stop()  # Stops stream

    PRINT('Quit.', SUCCESS)


if __name__ == '__main__':
    main()
