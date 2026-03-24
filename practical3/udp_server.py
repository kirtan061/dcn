# udp_server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 12346))

print("UDP Server started...")

data, addr = server.recvfrom(1024)
print("Client:", data.decode())

server.sendto("Hello Client".encode(), addr)
