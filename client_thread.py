import pickle
import struct
import socket
import pygame
import time
from threading import Thread
from constants import *
from client_utils import *

class ClientThread:
    def __init__ (self, joystick):
        ''' Constructor '''


        self.joystick_thread = Thread(target=self.read_joystick, args=()) #Creates joystick thread object
        self.joystick = joystick #Initailizes Joystick

        if joystick != None: #If joystick exists initailizes axes, button, hats
            self.joystick_buttons = [False] * self.joystick.get_numbuttons()
            self.joystick_axes = [0.0] * self.joystick.get_numaxes()
            self.joystick_hats = [False] * self.joystick.get_numhats()

        else: # If joystick does not exist declare axes, buttons and hats
            self.joystick_buttons = []
            self.joystick_axes = []
            self.joystick_hats = []

        self.pressure = 0.001
        self.temperature = 0.001
        self.recv_data = [] # The data recieved
        self.command = '' # The command that is going to be sent to the client

        self.connection = None # The connection object
        self.address = [] # The address of the connected client

        self.running = True # Whether the thread is running or not

    def run (self, connection, address):
        ''' Main client loop '''

        # Sets connenection and address
        self.connection = connection
        self.address = address

        # Starts joystick thread if exists
        if self.joystick != None:
            self.joystick_thread.start()

        PRINT('Started client thread for ' + ENC_VALUE(self.address[0]) + '.', SUCCESS)

        while self.running:
            # Recieve data
            # self.pressure, self.temperature = recv_pressure_and_temperature(self.connection)
            # self.recv_data = recv(self.connection)

            # Send data
            send(self.connection, [self.command, [self.joystick_buttons, self.joystick_axes, self.joystick_hats]])

            # Check if the client is to be disconnected
            if self.command == COMMAND_QUIT:
                self.running = False

            # Reset the command so it doesn't send the same thing multiple times
            self.command = ''

        self.connection.close() # Close the connection if the thread ends
        self.joystick_thread.join() # Ends joystick_thread

        PRINT('Stopped client thread for ' + ENC_VALUE(self.address[0]) + '.', SUCCESS)


    def read_joystick (self):
        ''' Read joystick axes and buttons '''

        while self.running:
            for i in range(self.joystick.get_numbuttons()): # Update joystick button values
                self.joystick_buttons[i] = bool(self.joystick.get_button(i))

            for i in range(self.joystick.get_numaxes()): # Update joystick axis values
                self.joystick_axes[i] = self.joystick.get_axis(i)

            # for i in range(self.joystick.get_numhats()):  # Update joystick hat values
            #     if self.joystick.get_hat(i)[1] > 0:
            #         self.joystick_hats[DPAD_UP + (4 * i)] = True
            #     else:
            #         self.joystick_hats[DPAD_UP + (4 * i)] = False
            #
            #     if self.joystick.get_hat(i)[0] > 0:
            #         self.joystick_hats[DPAD_RIGHT + (4 * i)] = True
            #     else:
            #         self.joystick_hats[DPAD_RIGHT + (4 * i)] = False
            #
            #     if self.joystick.get_hat(i)[1] < 0:
            #         self.joystick_hats[DPAD_DOWN + (4 * i)] = True
            #     else:
            #         self.joystick_hats[DPAD_DOWN + (4 * i)] = False
            #
            #     if self.joystick.get_hat(i)[0] < 0:
            #         self.joystick_hats[DPAD_LEFT + (4 * i)] = True
            #     else:
            #         self.joystick_hats[DPAD_LEFT + (4 * i)] = False

            time.sleep(0.01) # Delay for controller data

    def push_command (self, command):
        ''' Send a command to the client '''

        # Sets command
        self.command = command

        PRINT('Sending command ' + ENC_VALUE(self.command) + ' to ' + ENC_VALUE(self.address[0]) + '...', INFO)
