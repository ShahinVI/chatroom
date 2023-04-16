import socket
import tkinter  # gui module
from tkinter import *
from threading import Thread, Lock
import sys
import time
from queue import Queue

host = '127.0.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

END_PROGRAM = False
msg_queue = Queue()


def receive_message():
    global END_PROGRAM
    while not END_PROGRAM:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_queue.put(msg)
        except:
            print("There is an Error Receiving the Message")


def update_msg_list():
    if not msg_queue.empty():
        msg = msg_queue.get()
        msg_list.insert(tkinter.END, msg)

    if not END_PROGRAM:
        window.after(100, update_msg_list)


def send_message():
    global END_PROGRAM
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))
    if msg == "#quit":
        END_PROGRAM = True
        receive_Thread.join()
        s.close()
        window.destroy()
        window.quit()


def on_closing():
    my_msg.set("#quit")
    send_message()


# instance of GUI
window = Tk()
window.title("Chat Room Application")
window.configure(bg="black")

message_frame = Frame(window, height=100, width=100, bg="white")
message_frame.pack()  # adjust window to hold message frame

my_msg = StringVar()
my_msg.set("")

# add scroll bar to message frame
scroll_bar = Scrollbar(message_frame)
# create a list box for message, add scroll bar in y axis in msg list
msg_list = Listbox(message_frame, height=15, width=100, bg="white", yscrollcommand=scroll_bar.set)
# scroll bar on right
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg='blue', font='Aeria', bg='red')
label.pack()

entry_field = Entry(window, textvariable=my_msg, fg='black', width=50)
entry_field.pack()

send_button = Button(window, text="Send", font="Aerial", fg='black', command=send_message)
send_button.pack()

quit_button = Button(window, text="Quit", font="Aerial", fg='black', command=on_closing)
quit_button.pack()

if not END_PROGRAM:
    receive_Thread = Thread(target=receive_message)
    receive_Thread.start()

window.after(100, update_msg_list)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
print("exited")
