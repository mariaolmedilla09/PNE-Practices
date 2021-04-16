# This is the main programme for the client used in ex.7.

from Client0 import Client

gene_list = {"ADA", "FRAT1", "FXN", "RNU6_269P", "U5"}

IP = "127.0.0.1"
PORT = 8080

client = Client(IP, PORT)
command = input("Type the command you want to execute: ")

if command == "PING":
    print(" * Testing PING...")
    client.talk(command)
elif command == "GET":
    print(" * Testing GET...")
    for a in range(0,5):
        client.talk(command + " " + str(a))
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
    for i in gene_list:
        client.talk(command + " " + i)

