import http.server
import socketserver
import termcolor
#import pathlib   As we are not using these ones, we can comment them.
#import jinja2
from urllib.parse import urlparse, parse_qs
import server_utils as su


"""def read_html_file(filename):  # We're not using this function anymore, and instead I'm using the following one.
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    #Estamos creando un template object que contenga un html file y tenemos que añadir el valor
    # de esos valores en ese template
    return content"""  # We're not needing this function anymore here.

# Define the Server's port
PORT = 8081

LIST_SEQUENCES = ["AGCTGATCGATGGGTAGCATGCT", "AGCTAGTGTGTTGGTTACTGATCGCAT", "AGCTGTTTGATGCTAGTCGATCA", "CATGATGCTGATAGATGATCGTAGTAGGCTA", "CATGTAGTCGTAGTCGTATCGATGCTAGTAGCT"]

LIST_GENES = ["ADA", "FRAT", "FNX", "RNU6_269P", "U5"]
BASES_INFORMATION = {
    'A':{'link': "https://en.wikipedia.org/wiki/Adenine",'formula': 'C5H5N5', 'name': 'ADENINE', 'colour':'green'}, #The value of A is a dictionary at the same time.
    'C': {'link': "https://en.wikipedia.org/wiki/Citosine", 'formula': 'C5H5N5', 'name': 'CITOSINE', 'colour':'yellow'},
    'G': {'link': "https://en.wikipedia.org/wiki/Guanine", 'formula': 'C5H5N5', 'name': 'GUANINE', 'colour':'blue'},
    'T': {'link': "https://en.wikipedia.org/wiki/Timine",'formula': 'C5H5N5','name': 'TIMINE','colour':'pink'}
} # It is a dictionary with dictionaries as values.

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #Get all the requests
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green') #GET /info/A HTTP/1.1
        termcolor.cprint(self.path, 'blue') #/info/A

        # We're using this for replacing self.path and use path_name. This will work for every path want to use.
        o = urlparse(self.path) #Creating urlparse object --- #/test
        path_name = o.path #get the path and store it. Our path is going to be stored here.
        arguments = parse_qs(o.query) #parse the arguments.
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        # In this simple server version we are not processing the client's request. It is a happy server: It always returns a message saying that everything is fine.
        context = {}   # This is better for the case in which we have to pass more than one value. We have to inizialize this and each of the variables that we use before using them.

        if path_name == '/':
            context["n_sequences"] = len(LIST_SEQUENCES)
            context["list_genes"] = LIST_GENES
            contents = su.read_template_html_file('./html/Index.html').render(context=context)
        elif path_name == "/test":
            contents = su.read_template_html_file("./html/test.html").render()
        elif path_name == "/ping":
            contents = su.read_template_html_file("./html/ping.html").render()
        elif path_name == "/get":
            number_sequence = arguments["Sequence"][0]
            contents = su.get(LIST_SEQUENCES, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            if arguments["results"][0] == "Rev":
                sequence = arguments["results"][0]
                contents = su.rev(sequence)
            elif arguments["results"][0] == "Comp":
                sequence = arguments["sequence"][0]
                contents = su.comp(sequence)
            elif arguments["results"][0] == "Info":
                sequence = arguments["sequence"][0]
                contents = su.comp(sequence)
        else:
            contents = su.read_template_html_file("./html/Error.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') # Here we specify the content that we are sending.
        self.send_header('Content-Length', str(len(contents.encode())))

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