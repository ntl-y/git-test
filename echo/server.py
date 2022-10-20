import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn,addr=sock.accept()
print(addr)

data = conn.recv(1024).decode()
#while True:
#    data = conn.recv(1024)
#    if not data:
#        break
#    conn.send(data.upper())
print(data)

conn.close()
