import http.server
import socketserver
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
import server_utils as su

PORT = 8080
#dict for general.html
BASES_INFORMATION = {
    "A":{"link": "https://en.wikipedia.org/wiki/Adenine", "formula": "C5H5N5", "name": "ADENINE", "color": "lightgreen"},
"C":{"link": "https://en.wikipedia.org/wiki/Cytosine", "formula": "C4H5N30", "name": "CYTOSINE", "color": "yellow"},
"G":{"link": "https://en.wikipedia.org/wiki/Guanine", "formula": "C5H5N50", "name": "GUANINE", "color": "lightskyblue"},
"T":{"link": "https://en.wikipedia.org/wiki/Thymine", "formula": "C5H6N202", "name": "THYMINE", "color": "pink"}
}

LIST_SEQUENCES = ["AAGCTGCTACGTACGTACAGCT", "ACGGATCGCATCGATCGTACGATCGATCATC", "CGATAGCTGATCGATCATGCTACGTGTACG", "AGTAGCTAGTGCTACGATTATCGATCA", "CAGTCGATCGATTACG"]
LIST_GENES = ["ADA", "FRAT1", "U5", "FXN", "RNU6_269P"]
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
        print(self.path)

        o = urlparse(self.path) #we create a urlparse object
        path_name = o.path  #create a path for the object, it will be like self.path but without the question mark
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        context = {}
        if path_name == "/":
            context["n_sequences"] = len(LIST_SEQUENCES)
            context["list_genes"] = LIST_GENES
            contents = su.read_template_html_file("./html/index.html").render(context=context)
        elif path_name == "/test":
            contents = su.read_template_html_file("./html/test.html").render()
        elif path_name == "/ping":
            contents = su.read_template_html_file("./html/ping.html").render()
        elif path_name == "/get":
            number_sequence = arguments["sequence"][0]
            contents = su.get(LIST_SEQUENCES, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            if arguments['calculation'][0] == 'Rev':
                seq = arguments['sequence'][0]
                contents = su.rev(seq)
            elif arguments['calculation'][0] == 'Info':
                seq = arguments['sequence'][0]
                contents = su.info(seq)
            elif arguments['calculation'][0] == 'Comp':
                seq = arguments['sequence'][0]
                contents = su.comp(seq)
            else:
                pass
        else:
            contents = su.read_template_html_file("./html/error.html").render()

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
        print("Stopped by the user")
        httpd.server_close()