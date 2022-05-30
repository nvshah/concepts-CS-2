import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 55555))
#recieve message from server , specify how many bytes you wants to recieve
msg = s.recv(1024)
s.close()

print(msg.decode())