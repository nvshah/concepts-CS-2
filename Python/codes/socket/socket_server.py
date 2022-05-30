import socket

#-----SERVER

#TCP socket for Internet
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind() & listen() are req for server

# Host for socket to run is provided by 2 configs - Ip address & port number
# Here treating local machine as host so localhost = `127.0.0.1`
# & port number = `55555`
s.bind(('127.0.0.1', 55555))
s.listen() #socket will start listening 

while True:
    client, address = s.accept() #listen any input on socket
    print("connected to {}".format(address)) 
    client.send("You are connected !".encode())
    client.close()