import socket
import pickle
import struct
import cv2
from threading import Thread
from constants import *
from client_thread import ClientThread

SERVER_SOCKET = None
PI_CLIENT = None
PI_CLIENT_CONNECTED = False

RUNNING = True

def handle_connection (connection, address):
    global PI_CLIENT
    global PI_CLIENT_CONNECTED
    
    PRINT('Handling connection from ' + ENC_VALUE(address[0]) + '...', INFO)
    
    PI_CLIENT = ClientThread()
    PI_CLIENT_CONNECTED = True

    try:
        client_thread = Thread(target=PI_CLIENT.run, args=(connection, address))
        client_thread.start()
        client_thread.join()

        PRINT('Disconnected from ' + ENC_VALUE(address[0]) + '.', INFO)

        connection.close()
        PI_CLIENT = None
        PI_CLIENT_CONNECTED = False
    except Exception as e:
        PRINT('Could not run client for ' + ENC_VALUE(address[0]) + '.', ERROR)
        PRINT('| ' + str(e), ERROR)
        
def connection_listener ():
    global RUNNING
    global SERVER_SOCKET
    
    SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        SERVER_SOCKET.bind(('', PORT))
        
        PRINT('Socket bound to port ' + ENC_VALUE(PORT) + '.', SUCCESS)
    except socket.error as err:
        PRINT('Socket failed to bind to port ' + ENC_VALUE(PORT) + '.', ERROR)
        PRINT('| ' + err, ERROR)

    SERVER_SOCKET.listen(1)

    while RUNNING:
        try:
            conn, address = SERVER_SOCKET.accept()
            conn.settimeout(TIMEOUT)
            
            connection_thread = Thread(target=handle_connection, args=(conn, address))
            connection_thread.start()
            connection_thread.join()
        except:
            pass

def main ():
    global PI_CLIENT
    global PI_CLIENT_CONNECTED
    global RUNNING
    
    connection_handler = Thread(target=connection_listener, args=())
    connection_handler.start()

    while RUNNING:
        if PI_CLIENT_CONNECTED:
            try:
                frame = cv2.imdecode(PI_CLIENT.recv_data[0], cv2.IMREAD_COLOR)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    RUNNING = False
            except:
                pass

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
