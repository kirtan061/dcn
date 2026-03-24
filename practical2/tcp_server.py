# tcp_server.py

import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)

print("Server started...")

conn, addr = server.accept()
print("Connected:", addr)

data = conn.recv(1024).decode()
print("Client:", data)

conn.send("Hello Client".encode())

conn.close()
server.close()
