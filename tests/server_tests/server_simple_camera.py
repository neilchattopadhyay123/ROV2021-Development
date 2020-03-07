import socket
import pickle
import struct
import cv2

HOST = ''
PORT = 6969

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
def setup_server ():
    try:
        SERVER_SOCKET.bind((HOST, PORT))
    except socket.error as err:
        print(err)
    
    print('Socket bound.')
    
def setup_connection ():
    SERVER_SOCKET.listen(1)
    conn, address = SERVER_SOCKET.accept()
    
    print('Connected to: ' + str(address[0]) + ':' + str(address[1]))

    return conn

def recv (conn):
    data = b''
    payload_size = struct.calcsize('>L')
    
    while True:
        while len(data) < payload_size:
            data += conn.recv(2048)

        packed_img_size = data[:payload_size]
        data = data[payload_size:]
        img_size = struct.unpack('>L', packed_img_size)[0]

        while len(data) < img_size:
            data += conn.recv(2048)

        frame_data = data[:img_size]
        data = data[img_size:]

        frame = pickle.loads(frame_data, fix_imports=True, encoding='bytes')
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    conn.close()

def main ():
    setup_server()
    conn = setup_connection()
    
    recv(conn)

if __name__ == '__main__':
    main()
