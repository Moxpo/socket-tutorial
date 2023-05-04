import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file = open("tango.pdf", "rb")
file_size = os.path.getsize("tango.pdf")

client.send("recieved_tango.pdf".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()