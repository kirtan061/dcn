# udp_client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello Server".encode(), ("localhost", 12346))

data, _ = client.recvfrom(1024)
print("Server:", data.decode())
