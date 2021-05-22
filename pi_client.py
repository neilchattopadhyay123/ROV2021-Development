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
import ms5837
import time

RUNNING = True # Whether the client is running

def main ():
    ''' Main method '''
    
    global RUNNING
    # sensor = ms5837.MS5837_30BA()
    # # We must initialize the sensor before reading it
    # if not sensor.init():
    #     print("Sensor could not be initialized")
    #
    # # We have to read values from sensor to update pressure and temperature
    # if not sensor.read():
    #     print("Sensor read failed!")
    #
    # pressure = sensor.pressure(ms5837.UNITS_atm)
    # temperature = sensor.temperature(ms5837.UNITS_Centigrade)

    # Create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    PRINT('Connected to ' + ENC_VALUE(HOST + ':' + str(PORT)) + '.', SUCCESS)

    # Start the camera video thread
    stream = VideoStream().start()

    while RUNNING:
        # Get the current frame read by the video stream
        try:
            stream_frame = stream.read()
            _, frame = cv2.imencode('.jpg', stream_frame, ENCODE_PARAM)

            # Send data
            # send_pressure_and_temperature(s, pressure, temperature)
            send(s, [frame])
            
        except Exception as e: # Prints Error
            PRINT(str(e), ERROR)

        # Recieve data
        recv_data = recv(s)

        # print(recv_data[1])

        # Check if a command was sent
        if recv_data[DATA_IDX_COMMAND] == COMMAND_QUIT: # If quit command was recieved RUNNING = false
            PRINT('Recieved command ' + ENC_VALUE(COMMAND_QUIT) + '.', INFO)
            
            RUNNING = False

    s.close() # Closes socket
    stream.stop() # Stops stream

    PRINT('Quit.', SUCCESS)

if __name__ == '__main__':
    main()
