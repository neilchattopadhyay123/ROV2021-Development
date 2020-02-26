import socket
import pickle
import struct
import cv2

from threading import Thread
from constants import * # Import all constants and functions in constants.py
from client_thread import ClientThread

SERVER_SOCKET = None # The server socket object
PI_CLIENT = None # The client connection object
PI_CLIENT_CONNECTED = False # Whether the client is connected or not

RUNNING = True # Whether the server is running

def handle_connection (connection, address):
    ''' Handle clients trying to connect to the server '''
    
    global PI_CLIENT
    global PI_CLIENT_CONNECTED
    
    PRINT('Handling connection from ' + ENC_VALUE(address[0]) + '...', INFO)

    # Create a new client thread for the incoming client
    PI_CLIENT = ClientThread()
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
        
    except Exception as e: # Prints Error
        
        PRINT('Could not run client for ' + ENC_VALUE(address[0]) + '.', ERROR)
        PRINT('| ' + str(e), ERROR)
        
def connection_listener ():
    ''' Listens for incoming clients that want to connect to the server '''
    
    global RUNNING
    global SERVER_SOCKET

    # Create socket object
    SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind socket to a specific port
        SERVER_SOCKET.bind(('', PORT))
        
        PRINT('Socket bound to port ' + ENC_VALUE(PORT) + '.', SUCCESS)
        
    except socket.error as err: # Prints Error
        
        PRINT('Socket failed to bind to port ' + ENC_VALUE(PORT) + '.', ERROR)
        PRINT('| ' + err, ERROR)

    PRINT('Listening for connections...', INFO)

    # Start listening for connections
    SERVER_SOCKET.listen(1)

    while RUNNING:
        try:
            # If a client connects, get the connection object and the address
            conn, address = SERVER_SOCKET.accept()
            conn.settimeout(TIMEOUT)

            # Start a connection handler thread to begin reading and writing data
            connection_thread = Thread(target=handle_connection, args=(conn, address))
            connection_thread.start()
            connection_thread.join() # Wait for the connection to disconnect
        except:
            pass

    SERVER_SOCKET.close() # Closes server socket
    
    PRINT('Socket closed.', SUCCESS)

def main ():
    ''' The main method :o '''
    
    global PI_CLIENT
    global PI_CLIENT_CONNECTED
    global RUNNING

    # Create thread for the connection handler loop
    connection_handler = Thread(target=connection_listener, args=())
    connection_handler.start()

    while RUNNING: # Main loop
        if PI_CLIENT_CONNECTED:
            try:
                # Get the video frame from the client and decode it
                frame = cv2.imdecode(PI_CLIENT.recv_data[DATA_IDX_VIDEO], cv2.IMREAD_COLOR)

                # Display camera feed on 'frame'
                cv2.imshow('frame', frame)

                # If the 'q' key is pressed, shut down the server
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    PI_CLIENT.push_command(COMMAND_QUIT)
                    
                    RUNNING = False
            except:
                pass

    cv2.destroyAllWindows() # Closes all cv2 widows
    connection_handler.join() # Ends connection

    PRINT('Quit.', SUCCESS)

if __name__ == '__main__':
    main()
