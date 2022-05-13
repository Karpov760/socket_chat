import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))


while True:
    #если новый ip присылает кодовую фразу, вернуть ему хост, добавть в список известных ip клиентов
    #может быть получать кодовую фразу + логин?

    #если знакомый ip парсить бродкаст или ptp и работать как с чатом
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    client.sendto(b'hello', addr)