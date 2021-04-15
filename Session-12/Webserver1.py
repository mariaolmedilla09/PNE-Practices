





PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req.raw.decode()

    print("Message FROM CLIENT: ")
    # --