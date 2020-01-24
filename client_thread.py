import pickle
import struct
import socket
from threading import Thread
from constants import *

class ClientThread:
    def __init__ (self):
        self.send_data = []
        self.recv_data = []

        self.connection = None
        self.address = []

        self.running = True
        self.data = b''

    def recv (self):
        try: # Receive the image from the camera
            while len(self.data) < PAYLOAD_SIZE:
                self.data += self.connection.recv(PACKET_SIZE)

            packed_img_size = self.data[:PAYLOAD_SIZE]
            self.data = self.data[PAYLOAD_SIZE:]
            img_size = struct.unpack('>L', packed_img_size)[0]

            while len(self.data) < img_size:
                self.data += self.connection.recv(PACKET_SIZE)

            loaded_data = self.data[:img_size]
            self.data = self.data[img_size:]

            self.recv_data = pickle.loads(loaded_data, fix_imports=True, encoding='bytes')
        except Exception as e:
            PRINT('Could not receive data.', ERROR)
            PRINT('| ' + str(e), ERROR)
            
            self.running = False
            
    def send (self):
        try:
            self.send_data = pickle.dumps([self.command], 0)

            self.connection.sendall(struct.pack('>L', len(self.send_data)) + self.send_data)

            self.command = ''
        except Exception as e:
            PRINT('Could not send data.', ERROR)
            PRINT('| ' + str(e), ERROR)

            self.running = False
            
    def run (self, connection, address):
        self.connection = connection
        self.address = address
        
        while self.running:
            self.recv()
            self.send()
        
        self.connection.close() # Close the connection if the thread ends

    def push_command (self, command):
        self.command = command
        
        PRINT('Sending command ' + ENC_VALUE(command) + ' to ' + ENC_VALUE(address[0]) + '...')
