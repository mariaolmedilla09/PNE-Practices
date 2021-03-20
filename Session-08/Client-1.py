# PROGRAMMING OUR OWN CLIENT WITH A PIECE OF CODE BY USING PYTHON (INSTEAD OF nc)
# For this to work, I need to have the appropiate python server for which this client is devoted.

import socket   # This is to communicate between applications.

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "192.168.124.179"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # We are creating a socket with this line (default socket-used in all our programes)

# establish the connection to the Server (IP, PORT)   # We execute the connect method with the given port and IP of the server we have running.
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necessary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))  # Encode is used to convert a string into a set of bytes.C

# Closing the socket
s.close()



