# file_server.py

import socket

server = socket.socket()
server.bind(("localhost", 12347))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected:", addr)

file = open("sample.txt", "rb")
data = file.read()

conn.send(data)

file.close()
conn.close()
server.close()
