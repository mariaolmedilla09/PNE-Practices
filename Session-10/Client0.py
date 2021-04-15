import termcolor
import colorama
import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip     # We create the atributes.
        self.port = port

    def ping(self):    # This method is to test if a connection works.
        print("Ok")

    def advanced_ping(self):   # We are going to create a socket.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))    # If we try to connect a socket to something that is not running
            print("Server is up")
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the Port?")

    def __str__(self):  # If I didn't have the str, we wouldn't be able to print a string (We need to transform the class into a string)
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)   # Very important to convert the port into a string when concatenating it because it is an intege

    def talk(self, msg):
        colorama.init(strip="False")
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data. We're encoding the message.
        print(termcolor.colored("To Server: ", msg, "yellow"))
        s.send(msg.encode())
        # Receive data. We decode the message to a string.
        response = s.recv(2048).decode("utf-8")
        print("From server:", end="")
        print(termcolor.colored(response, "blue"))
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response  # We want to return the response to our main program

    def debug_talk(self, msg, response):
        termcolor.cprint("To server: {}".format(msg), 'blue')
        termcolor.cprint(response, 'green')

