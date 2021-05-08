import socket
import pickle
import struct
import cv2
import pygame
import os
import random
import sys
import numpy as np

sys.path.insert(1, 'gui')

from threading import Thread
from constants import * # Import all constants and functions in constants.py
from client_thread import ClientThread

from gui_utils import *
from dial import *
from menubar import MenuBar
from app import App

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

SERVER_SOCKET = None # The server socket object
PI_CLIENT = None # The client connection object
PI_CLIENT_CONNECTED = False # Whether the client is connected or not

FONT = pygame.font.Font('gui/unispace/unispace.ttf', 12)

IS_RUNNING = True # Whether the server is IS_RUNNING

def handle_connection (connection, address, joysticks):
    ''' Handle clients trying to connect to the server '''

    global PI_CLIENT
    global PI_CLIENT_CONNECTED

    PRINT('Handling connection from ' + ENC_VALUE(address[0]) + '...', INFO)

    # Create a new client thread for the incoming client
    PI_CLIENT = ClientThread(joysticks[0])
    PI_CLIENT_CONNECTED = True

    try:
        PRINT('Starting client thread for ' + ENC_VALUE(address[0]) + '...', INFO)

        # Create a thread for the client's run method (to send and recieve data)
        client_thread = Thread(target=PI_CLIENT.run, args=(connection, address))
        client_thread.start()
        client_thread.join() # Wait for the client to disconnect

        PRINT('Disconnected from ' + ENC_VALUE(address[0]) + '.', INFO)

        # Reset client variables
        connection.close()
        PI_CLIENT = None
        PI_CLIENT_CONNECTED = False
    except Exception as e:
        PRINT('Could not run client for ' + ENC_VALUE(address[0]) + '.', ERROR)
        PRINT('| ' + str(e), ERROR)

def connection_listener (joysticks):
    ''' Listens for incoming clients that want to connect to the server '''

    global IS_RUNNING
    global SERVER_SOCKET

    # Create socket object
    SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind socket to a specific port
        SERVER_SOCKET.bind(('', PORT))

        PRINT('Socket bound to port ' + ENC_VALUE(PORT) + '.', SUCCESS)
    except socket.error as err:
        PRINT('Socket failed to bind to port ' + ENC_VALUE(PORT) + '.', ERROR)
        PRINT('| ' + err, ERROR)

    PRINT('Listening for connections...', INFO)

    # Start listening for connections
    SERVER_SOCKET.listen(1)

    while IS_RUNNING:
        try:
            # If a client connects, get the connection object and the address
            conn, address = SERVER_SOCKET.accept()
            conn.settimeout(TIMEOUT)

            # Start a connection handler thread to begin reading and writing data
            connection_thread = Thread(target=handle_connection, args=(conn, address, joysticks))
            connection_thread.start()
            connection_thread.join() # Wait for the connection to disconnect
        except:
            pass

    PRINT('Socket closed.', SUCCESS)

def shutdown ():
    ''' Method that is called when the server is shutting down '''

    global PI_CLIENT
    global IS_RUNNING

    if PI_CLIENT != None:
        PI_CLIENT.push_command(COMMAND_QUIT)

    SERVER_SOCKET.close()

    IS_RUNNING = False

def main ():
    ''' The main method :o '''

    global PI_CLIENT
    global PI_CLIENT_CONNECTED
    global IS_RUNNING
    global pressure_ATM
    global temperature_C

    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    PRINT('Found ' + ENC_VALUE(len(joysticks)) + ' joysticks.', INFO)

    # Initialize detected joysticks
    if len(joysticks) > 0:
        for joystick in joysticks:
            joystick.init()
            PRINT('| ' + ENC_VALUE(joystick.get_id()) + ' ' + ENC_VALUE(joystick.get_name()), INFO)

    screen = pygame.display.set_mode(SCREEN_DIMENSION, pygame.RESIZABLE)
    screen.set_alpha(None)
    pygame.display.set_caption('LoggerheadROV Driver Station | ' + random.choice(QUOTES))
    pygame.display.set_icon(pygame.image.load('gui/images/loggerhead_logo.png'))

    clock = pygame.time.Clock()
    horizon = Horizon(screen.get_size()[0] - GAUGE_DIMENSION - UI_SCREEN_PADDING - UI_BORDER, screen.get_size()[1] - GAUGE_DIMENSION - UI_SCREEN_PADDING - UI_BORDER)

    menubar = MenuBar(screen, FONT)
    menubar.add_app(App("Do Thing", menubar))
    menubar.add_app(App("Do Other Thing", menubar))
    folder = App("Image Recognition", menubar, is_folder=True)
    folder.add_app(App("More Things", folder.sub_app_menubar))
    menubar.add_app(folder)

    # Create thread for the connection handler loop
    connection_handler = Thread(target=connection_listener, args=(joysticks,))
    connection_handler.start()

    while IS_RUNNING:
        mouse_data = [False] * len(pygame.mouse.get_pressed())
        key_data = [False] * len(pygame.key.get_pressed())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shutdown()

            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                horizon = Horizon(screen.get_size()[0] - GAUGE_DIMENSION - UI_SCREEN_PADDING - UI_BORDER, screen.get_size()[1] - GAUGE_DIMENSION - UI_SCREEN_PADDING - UI_BORDER)
                menubar.resize()

            if event.type == pygame.KEYDOWN:
                key_data = pygame.key.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_data = pygame.mouse.get_pressed()

        mouse_pos = pygame.mouse.get_pos()

        screen.fill(UI_COLOR_4)

        if PI_CLIENT_CONNECTED:
            try:
                # Get the video frame from the client and decode it
                frame = cv2.imdecode(PI_CLIENT.recv_data[DATA_IDX_VIDEO], cv2.IMREAD_COLOR)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = pygame.surfarray.make_surface(frame)

                frame = pygame.transform.scale(frame, screen.get_size())

                screen.blit(frame, (0, 0))

                # cv2.imshow('frame', frame)
            except:
                pass

        menubar.update(mouse_data, key_data)
        # horizon.update(screen, mouse_pos[0] - (screen.get_size()[0] / 2), mouse_pos[1] - (screen.get_size()[1] / 2)) # Draws gauge too

        menubar.draw()
        draw_text(screen, FONT, str(round(clock.get_fps(), 3)) + ' FPS', (screen.get_size()[0] - (UI_SCREEN_PADDING * 8), UI_SCREEN_PADDING), False)
        if PI_CLIENT_CONNECTED:
            draw_text(screen, FONT, str(PI_CLIENT.pressure) + ' atm', (screen.get_size()[0] - (UI_SCREEN_PADDING * 8), UI_SCREEN_PADDING + 30), False)
            draw_text(screen, FONT, str(PI_CLIENT.temperature) + ' C', (screen.get_size()[0] - (UI_SCREEN_PADDING * 8), UI_SCREEN_PADDING + 60), False)

        pygame.display.update()
        clock.tick(FPS)

    cv2.destroyAllWindows()
    connection_handler.join()

    PRINT('Quit.', SUCCESS)

if __name__ == '__main__':
    main()

pygame.quit()
