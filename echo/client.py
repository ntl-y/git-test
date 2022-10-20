import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

msg = 'Hello, world!'
sock.send(msg.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode())