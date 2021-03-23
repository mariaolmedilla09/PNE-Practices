from Client0 import Client

print("----- | Practice 2, Exercise 4 | -----")

PORT = 12000
IP = "127.0.0.1"

c = Client(IP, PORT)

c.debug_talk("Message 1--")
c.debug_talk("Message 2: Testing !!!")

