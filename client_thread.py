import pickle
import struct
import socket
from threading import Thread
from constants import *
from client_utils import *

class ClientThread:
    def __init__ (self):
        ''' Constructor '''
        
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

            # Send data
            send(self.connection, [self.command])

            # Check if the client is to be disconnected
            if self.command == COMMAND_QUIT:
                self.running = false

            # Reset the command so it doesn't send the same thing multiple times
            self.command = ''
        
        self.connection.close() # Close the connection if the thread ends

        PRINT('Stopped client thread for ' + ENC_VALUE(self.address[0]) + '.', SUCCESS)

    def push_command (self, command):
        ''' Send a command to the client '''
        
        self.command = command
        
        PRINT('Sending command ' + ENC_VALUE(self.command) + ' to ' + ENC_VALUE(address[0]) + '...', INFO)
