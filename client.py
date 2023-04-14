import socket

host='localhost'
port=8080

# create socket to connect to the internet
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# search for this host and connect on this port
sock.connect((host,port))

# recieve message from connection of 1024 bytes
message = sock.recv(1024)

while message:
    print("Message: ",message.decode())
    message=sock.recv(1024)

sock.close()