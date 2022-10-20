import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

msg = 'Hello, world!'
sock.send(msg.encode('utf-8'))

sock.close()
