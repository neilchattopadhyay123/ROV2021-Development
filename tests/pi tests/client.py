import socket

host = '192.168.2.1'
port = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input('< ')

    if command == 'exit':
        s.send(str.encode(command))
        break
    elif command == 'kill':
        s.send(str.encode(command))
        break

    s.send(str.encode(command))

    reply = s.recv(1024)
    print('> ' + reply.decode('utf-8'))

s.close()
