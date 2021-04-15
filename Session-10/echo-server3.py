import socket

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ls.bind((IP, PORT))
count_connections = 0
client_address_list = []
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.appends(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Received Message: {msg}")
        try:
            response = "ECHO" + msg
            cs.send(response.encode())
        except ValueError:
            cs.send("We need a number".encode())

        cs.close()
        if count_connections == 5:
            for i in range(0, len(client_address_list)):
                print("Client " + str(i) + ":Client IP, PORT: " + str(client_address_list[i]))
            exit()

