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
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue') #to avoid splitting

        if self.path == "/":
            contents = read_html_file("./html/index.html")
        elif self.path == "/info/A":
            contents = read_html_file("./html/info/A.html")
        elif self.path == "/info/C":
            contents = read_html_file("./html/info/C.html")
        elif self.path == "/info/G":
            contents = read_html_file("./html/info/G.html")
        elif self.path == "/info/T":
            contents = read_html_file("./html/info/T.html")
        else:
            contents = read_html_file("./html/error.html")


        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return



# - Server MAIN program

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()