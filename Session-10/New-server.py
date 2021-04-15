import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"  # the first thing I have to look at, is that this IP address is the right one.
# Localhost only attends requests from applications in the very same machine, but it will not attend requests running out of my computer.
# Third option is to leave IP empty: the issue is that  I am telling the OS that I want to listen in all the Ip addresses defined in the server machine.

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- OPTIONAL FOR AVOIDING THE PROBLEM OF PORT ALREADY IN USE
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
count_connections = 0
# -- Step 3: Configure the socket for listening
ls.listen()
client_address_list = []
print("The server is configured!")

while True:
    # -- Waits for clients to connect
    print("Waiting for clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        # -- Close the listening socket
        ls.close()
        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Received Message: {msg}")

        # -- Send a response message to the client
        response = "ECHO" + msg
        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the socket
        cs.close()
        if count_connections == 5:
            for i in range(0, len(client_address_list)):
                print("Client " + str(i) + ":Client IP, PORT: " + str(client_address_list[i]))
            exit()

