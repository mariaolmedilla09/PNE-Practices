# The difference with the Client-1 is that in this case I am connecting to the server, sending information and later on I am sending something else (I want to receive information from the server and I store it in the message).
# What we are doing is exchanging information.

import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.124.179"

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

# Closing the socket
s.close()


