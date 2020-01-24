from constants import *
import socket
import pickle
import struct

def recv (connection):
    data = b''
    
    try:
        while len(data) < PAYLOAD_SIZE:
            data += connection.recv(PACKET_SIZE)

        packed_size = data[:PAYLOAD_SIZE]
        data = data[PAYLOAD_SIZE:]
        size = struct.unpack('>L', packed_size)[0]

        while len(data) < size:
            data += connection.recv(PACKET_SIZE)

        loaded_data = data[:size]
        data = data[size:]

        return pickle.loads(loaded_data, fix_imports=True, encoding='bytes')
    except Exception as e:
        PRINT('Could not receive data.', ERROR)
        PRINT('| ' + str(e), ERROR)

    return []
            
def send (connection, semd_data):
    try:
        data = pickle.dumps(send_data, 0)

        connection.sendall(struct.pack('>L', len(data)) + data)
    except Exception as e:
        PRINT('Could not send data.', ERROR)
        PRINT('| ' + str(e), ERROR)
