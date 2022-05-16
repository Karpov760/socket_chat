import socket
import time


CODE = b"code_phrase"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)

server.sendto(CODE, ('<broadcast>', 37020))
data, addr = server.recvfrom(1024)
print("received message: %s" % data)
