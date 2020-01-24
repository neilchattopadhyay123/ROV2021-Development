import socket

host = ''
port = 6969

value = 'Slick beans'

def setup_server ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created.')

    try:
        s.bind((host, port))
    except socket.error as err:
        print(err)
    print('Socket bound.')

    return s

def setup_connection ():
    s.listen(1) # Allow 1 person
    conn, address = s.accept()
    print('Connected to: ' + str(address[0]) + ':' + str(address[1]))

    return conn

def GET ():
    reply = value

    return reply

def REPEAT (data_message):
    reply = data_message[1]

    return reply

def data_transfer (conn):
    # A big loop that sends and recieves data until told not to

    while True:
        # Recieve the data
        data = conn.recv(1024)
        data = data.decode('utf-8')
        # Split command line into the command and the words that follow it
        data_message = data.split(' ', 1)
        command = data_message[0]

        if command == 'get':
            reply = GET()
        elif command == 'repeat':
            reply = REPEAT(data_message)
        elif command == 'exit':
            print('Client disconnected.')
            break
        elif command == 'kill':
            print('Client requested to shut down the server')
            s.close()
            break
        else:
            reply = 'Unknown command.'

        # Send the reply
        conn.sendall(str.encode(reply))
        print('Data has been sent!')

    conn.close()

s = setup_server()

while True:
    try:
        conn = setup_connection()
        data_transfer(conn)
    except:
        break
