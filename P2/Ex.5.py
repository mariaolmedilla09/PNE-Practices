from Client0 import Client
from pathlib import Path

print("-----| Practice 2, Exercise 5 |-----")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
print(c.talk("Sending the U5 Gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))

