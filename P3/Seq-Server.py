import socket
import server_utils

list_sequences = ["AGCTGATCGATGGGTAGCATGCT", "AGCTAGTGTGTTGGTTACTGATCGCAT", "AGCTGTTTGATGCTAGTCGATCA", "CATGATGCTGATAGATGATCGTAGTAGGCTA", "CATGTAGTCGTAGTCGTATCGATGCTAGTAGCT"]

PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ls.bind((IP, PORT))
count_connections = 0
ls.listen()
client_address_list = []
print("The server is configured!")

while True:

    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()


    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()

    formatted_message = server_utils.format_command(msg) # To eliminate \n \r
    formatted_message = formatted_message.split(" ")   # For creating a list of the division.

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command= formatted_message[0]
        argument = formatted_message[1]

    if command == "PING":
        server_utils.ping(cs)
        cs.close()
    elif command == "GET":
        server_utils.get(cs, list_sequences, argument)
        cs.close()
    elif command == "INFO":
        server_utils.info(cs, argument)
        cs.close()
    elif command == "COMP":
        server_utils.comp(cs,argument)
        cs.close()
    elif command == "REV":
        server_utils.rev(cs,argument)
        cs.close()
    elif command == "GENE":
        server_utils.gene(cs,argument)
        cs.close()
    else:
        response = "Not available command"
        cs.send(response.encode())

ls.close()
if count_connections == 5:
    for i in range(0, len(client_address_list)):
        print("Client" + str(i) + ":Client IP, PORT: " + str(client_address_list[i]))
    exit()