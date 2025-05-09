

import socket
import threading
import time
import tkinter as tk

client = socket.socket()
client.connect(('localhost', 63453))
root = tk.Tk()

def send():
    data_send = get_message.get()
    if data_send != "":
        data_send = str(data_send)
        try:
            client.send(data_send.encode())
        except socket.error as e:
            print(f"Socket error: {e}")
        lbl = tk.Label(root, text=data_send, bg="red", fg="white")
        get_message.delete(0, tk.END)
        lbl.pack(fill='x', side='top')

def recv():
    while True:
        try:
            data_recv = client.recv(1024)
            if data_recv != b"":
                lbl = tk.Label(root, text=data_recv.decode(), bg="blue", fg="white")
                lbl.pack(fill='x', side='top')
        except socket.error as e:
            print(f"Socket error: {e}")
            break

get_message = tk.Entry(root)
send_message = tk.Button(root, text="Send", command=send)

send_message.pack(fill='x', side='bottom')
get_message.pack(fill='x', side='bottom')

threading.Thread(target=recv).start()

root.title("Chat Client")
root.geometry("500x700")
root.resizable(width=False, height=False)

root.mainloop()