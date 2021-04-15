# This is the main programme for the client used in ex.7.

from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

client = Client(IP, PORT)
command = input("Type the command you want to execute: ")
if command == "PING":
    print(" * Testing PING...")
    client.talk(command)
elif command == "GET":
    print(" * Testing GET...")
    argument = input("Enter an argument: ")
    client.talk(command + " " + argument)
elif command == "INFO":
    print(" * Testing INFO...")
    client.talk(command + " " + "AGCTGATCGATGGGTAGCATGCT")
elif command == "COMP":
    print(" * Testing COMP...")
    client.talk(command + " " + "AGCTGATCGATGGGTAGCATGCT")
elif command == "REV":
    print(" * Testing REV...")
    client.talk(command + " " + "AGCTGATCGATGGGTAGCATGCT")
elif command == "GENE":
    print(" * Testing GENE...")
    argument = input("Enter an argument: ")
    client.talk(command + " " + argument)

