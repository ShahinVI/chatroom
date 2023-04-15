import socket
from threading import Thread

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

def broadcast(msg,prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8")+msg)

def handle_clients(conn, address):
    name = conn.recv(1024).decode
    welcome = "Welcome "+name+". You can type #quit if you ever want to leave the Chat Room"
    conn.recv(bytes(welcome, "utf8"))
    msg = name + "has joined the chat room"
    broadcast(bytes(msg),"utf8")
    clients[conn] = name

    while True:
        msg= conn.recv(1024)
        if msg!=bytes("#quit","utf8"):
            broadcast(msg, name+":")
        else:
            conn.semd(bytes("#quit","utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name+" has left the chat room"))

def listen_accept_connection(sock):
    while True:

        # when connection establish use sock.accept
        # this gives back connection and address
        client_conn, client_address = sock.accept()
        print(client_address," has connected")
        client_conn.send("\nWelcome to the ChatRomm, \nPlease Type your name to continue".encode('utf8'))

        addresses[client_conn] = client_address

        Thread(target = handle_clients, args=(client_conn, client_address)).start()

def send_message(client_conn,message):
    # send message over the coonnection
    client_conn.send(message.encode())

if __name__=="__main__":

    sock = establish_connection()
    # listening 5 request at one time for simplicity
    sock.listen(5)
    print("server is running and listening to clients request\n")

    t1 = Thread(target=listen_accept_connection(sock))
    t1.start()
    t1.join()