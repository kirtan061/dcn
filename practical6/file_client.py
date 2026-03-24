 # file_client.py

import socket

client = socket.socket()
client.connect(("localhost", 12347))

data = client.recv(1024)

file = open("received.txt", "wb")
file.write(data)

file.close()
client.close()

print("File received successfully")
