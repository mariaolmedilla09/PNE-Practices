import http.server
import socketserver
import termcolor
import pathlib

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)
        print(self.path)  # to avoid splitting

        if self.path == "/":
            contents = read_html_file("./html/index.html")
        elif self.path == "/info/A":
            contents = read_html_file("./html/A.html")
        elif self.path == "/info/C":
            contents = read_html_file("./html/C.html")
        elif self.path == "/info/G":
            contents = read_html_file("./html/G.html")
        elif self.path == "/info/T":
            contents = read_html_file("./html/T.html")
        elif self.path.endswith(".html"):
            try:
                contents = read_html_file("./html" + self.path)
            except FileNotFoundError:
                contents = read_html_file("./html/error.html")
        else:
            contents = read_html_file("./html/error.html")

        # Generating the response message
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(contents.encode())
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()