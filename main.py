import socket

host='localhost'
port=8080

# TCP connecttion use SOCK_STREAM. SOCK_DGRAM using UDP connection
# AF_INET uses internet 4
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# passing the host and port number as a tuple
sock.bind((host,port))

# listening 1 request at one time
sock.listen(1)

# when connection establish use sock.accept
# this gives back connection and address
conn,address = sock.accept()

message = "Hey connection established"

# send message over the coonnection
conn.send(message.encode())

conn.close()