from constants import *
import socket
import pickle
import struct


def recv_pressure_and_temperature(connection):
    try:
        # Receive pressure and temperature
        pressure = connection.recv(PAYLOAD_SIZE)
        temperature = connection.recv(PAYLOAD_SIZE)

        return pressure, temperature

    except Exception as e:
        # Print error if thrown
        PRINT('Could not receive temp and pressure data.', ERROR)
        PRINT('| ' + str(e), ERROR)


def recv(connection):
    ''' Recieve data method '''

    data = b''  # The incoming data from the client

    try:
        # Load the incoming data and decode it into a python array
        while len(data) < PAYLOAD_SIZE:
            data += connection.recv(PACKET_SIZE)

        # Unpacks data recieved
        packed_size = data[:PAYLOAD_SIZE]
        data = data[PAYLOAD_SIZE:]
        size = struct.unpack('>L', packed_size)[0]

        while len(data) < size:
            data += connection.recv(PACKET_SIZE)

        loaded_data = data[:size]
        data = data[size:]

        return pickle.loads(loaded_data, fix_imports=True, encoding='bytes')

    except Exception as e:
        # Print error if thrown
        PRINT('Could not receive data.', ERROR)
        PRINT('| ' + str(e), ERROR)

    # Return '[]' if error is thrown
    return []


def send_pressure_and_temperature(connection, pressure, temperature):
    try:
        # Pack the data so its smaller
        data = struct.pack('>L', pressure) + struct.pack('>L', temperature)

        # Send the data to the client
        connection.sendall(data)

    except Exception as e:
        # Print error if thrown
        PRINT('Could not send temp and pressure data.', ERROR)
        PRINT('| ' + str(e), ERROR)


def send(connection, send_data):
    ''' Send data method '''

    try:
        # Pack the data so its smaller
        data = pickle.dumps(send_data, 0)

        # Send the data to the client
        connection.sendall(struct.pack('>L', len(data)) + data)

    except Exception as e:
        # Print error if thrown
        PRINT('Could not send data.', ERROR)
        PRINT('| ' + str(e), ERROR)
