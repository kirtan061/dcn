# tcp_client.py

import socket

client = socket.socket()
client.connect(("localhost", 12345))

client.send("Hello Server".encode())

data = client.recv(1024).decode()
print("Server:", data)

client.close()
