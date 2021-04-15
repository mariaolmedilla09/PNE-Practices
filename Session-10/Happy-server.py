import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"   # the first thing I have to look at, is that this IP address is the right one.
                   # Localhost only attends requests from applications in the very same machine, but it will not attend requests running out of my computer.
                   # Third option is to leave IP empty: the issue is that  I am telling the OS that I want to listen in all the Ip addresses defined in the server machine.

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- OPTIONAL FOR AVOIDING THE PROBLEM OF PORT ALREADY IN USE
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
while True:
    # -- Waits for clients to connect
    print("Waiting for clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server")

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
        response = "HELLO. I am the Happy Server :-)\n"
        # -- The message has to be encoded into bytes
        cs.send(str(response).encode())

        # -- Close the socket
        cs.close()


