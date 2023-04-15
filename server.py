import socket
#################################################
host = '127.0.0.1'                              #
port = 8080                                     #
message = "Hey connection established"          #
# dict of clients holding connection ############
clients = {}                                    #
# dict of address holding address of clients ####
addresses = {}                                    #
#################################################

def establish_connection():
    # TCP connecttion use SOCK_STREAM. SOCK_DGRAM using UDP connection
    # AF_INET uses internet 4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # passing the host and port number as a tuple
    sock.bind((host, port))
    return sock

def listen_accept_connection(sock):
    while True:
        # listening 5 request at one time for simplicity
        sock.listen(5)
        print("server is running and listening to clients request\n")
        # when connection establish use sock.accept
        # this gives back connection and address
        conn, address = sock.accept()
        if conn:
            return conn, address

def send_message(sock,message):
    # send message over the coonnection
    conn.send(message.encode())

if __name__=="__main__":
    sock = establish_connection()
    conn, address = listen_accept_connection(sock)
    send_message(sock, message)
    conn.close()