import pickle
import struct
import socket
from threading import Thread
from constants import *
from client_utils import *

class ClientThread:
    def __init__ (self, joystick):
        ''' Constructor '''

        self.joystick = joystick
        if joystick != None:
            self.joystick_buttons = [False] * self.joystick.get_numbuttons()
            self.joystick_axes = [0.0] * self.joystick.get_numaxes()
            self.joystick_hats = [False] * (self.joystick.get_numhats() * 4) # 0 = TOP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
        
        self.recv_data = [] # The data recieved
        self.command = '' # The command that is going to be sent to the client

        self.connection = None # The connection object
        self.address = [] # The address of the connected client

        self.running = True # Whether the thread is running or not

    def run (self, connection, address):
        ''' Main client loop '''
        
        self.connection = connection
        self.address = address

        PRINT('Started client thread for ' + ENC_VALUE(self.address[0]) + '.', SUCCESS)
        
        while self.running:
            # Recieve data
            self.recv_data = recv(self.connection)

            # Get joystick value
            try:
                for i in range(self.joystick.get_numbuttons()): # Update joystick button values
                    self.joystick_buttons[i] = bool(self.joystick.get_button(i))
                for i in range(self.joystick.get_numaxes()): # Update joystick axis values
                    self.joystick_axes[i] = smooth_input(self.joystick.get_axis(i))
                for i in range(self.joystick.get_numhats()):  # Update joystick hat values
                    if self.joystick.get_hat(i)[1] > 0:
                        self.joystick_hats[DPAD_UP + (4 * i)] = True
                    else:
                        self.joystick_hats[DPAD_UP + (4 * i)] = False
                    if self.joystick.get_hat(i)[0] > 0:
                        self.joystick_hats[DPAD_RIGHT + (4 * i)] = True
                    else:
                        self.joystick_hats[DPAD_RIGHT + (4 * i)] = False
                    if self.joystick.get_hat(i)[1] < 0:
                        self.joystick_hats[DPAD_DOWN + (4 * i)] = True
                    else:
                        self.joystick_hats[DPAD_DOWN + (4 * i)] = False
                    if self.joystick.get_hat(i)[0] < 0:
                        self.joystick_hats[DPAD_LEFT + (4 * i)] = True
                    else:
                        self.joystick_hats[DPAD_LEFT + (4 * i)] = False
            except:
                pass

            # Send data
            send(self.connection, [self.command, [self.joystick_buttons, self.joystick_axes, self.joystick_hats]])

            # Check if the client is to be disconnected
            if self.command == COMMAND_QUIT:
                self.running = False

            # Reset the command so it doesn't send the same thing multiple times
            self.command = ''
        
        self.connection.close() # Close the connection if the thread ends

        PRINT('Stopped client thread for ' + ENC_VALUE(self.address[0]) + '.', SUCCESS)

    def push_command (self, command):
        ''' Send a command to the client '''
        
        self.command = command
        
        PRINT('Sending command ' + ENC_VALUE(self.command) + ' to ' + ENC_VALUE(self.address[0]) + '...', INFO)
