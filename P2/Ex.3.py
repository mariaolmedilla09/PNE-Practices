from Client0 import Client

print("-----| Practice 2, Exercise 3 |-----")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
# response = c.talk("Message")  It's better to write these two lines in a single one.
# print(response)
print("Response: ", c.talk("This is something random"))




