# For having a dinamic page:

import http.server
import socketserver
import termcolor
import pathlib
import jinja2

PORT = 8080
#dict for general.html
BASES_INFORMATION = {
    "A":{"link": "https://en.wikipedia.org/wiki/Adenine", "formula": "C5H5N5", "name": "ADENINE", "color": "lightgreen"},
"C":{"link": "https://en.wikipedia.org/wiki/Cytosine", "formula": "C4H5N30", "name": "CYTOSINE", "color": "yellow"},
"G":{"link": "https://en.wikipedia.org/wiki/Guanine", "formula": "C5H5N50", "name": "GUANINE", "color": "lightskyblue"},
"T":{"link": "https://en.wikipedia.org/wiki/Thymine", "formula": "C5H6N202", "name": "THYMINE", "color": "pink"}
}

socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content
def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content
#the template object cannot be sent directly, so we need the render function to generate the html code

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)
        print(self.path)  # to avoid splitting

        if self.path == "/":
            contents = read_html_file("./html/index.html")
        elif "/info/" in self.path:
            base = self.path.split("/")[-1]
            context = BASES_INFORMATION[base]
            context["letter"] = base
            contents = read_template_html_file("./html/info/general.html").render(base_information=context)
            # the name of the arguments are the variables of general.html
            """contents = read_html_file("./html/info/general.html").render(name=BASES_INFORMATION[base]["name"],
                                                                    formula=BASES_INFORMATION[base]["formula"],
                                                                    letter=base,
                                                                    link=BASES_INFORMATION[base]["link"])"""

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