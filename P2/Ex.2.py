from Client0 import Client

print("-----| Practice 2, Exercise 2 |-----")

IP = "127.0.0.1"
PORT = 12000   # The port must always be an integer, not a string.
c = Client(IP, PORT)   # I create a client passing the port and the IP.
print(c)