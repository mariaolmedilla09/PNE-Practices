import http.server
import socketserver
import pathlib
import jinja2
import json
from urllib.parse import urlparse, parse_qs
import server_utils as su


PORT = 8080

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
            contents = su.read_template_html_file("./html/index.html").render(context=context)

        elif path_name == "/geneSeq":
            if 'gene_name' in arguments and not 'json' in arguments:
                contents = su.gene_sequence(arguments['gene_name'][0], True)
            elif 'gene_name' in arguments and 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = su.gene_sequence(arguments['gene_name'][0], False)
                else:
                    contents = {'ERROR': 'json argument must be 1 to return json output'}
            else:
                contents = {'ERROR': 'endpoint arguments are not correct for this endpoint'}

        elif path_name == "/geneInfo":
            if 'gene_name' in arguments and not 'json' in arguments:
                contents = su.gene_info(arguments['gene_name'][0], True)
            elif 'gene_name' in arguments and 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = su.gene_info(arguments['gene_name'][0], False)
                else:
                    contents = {'ERROR': "json argument must be 1 to return json output"}
            else:
                contents = {'ERROR': 'endpoint arguments are not correct for this endpoint'}

        elif path_name == "/geneCalc":
            if 'gene_name' in arguments and not 'json' in arguments:
                contents = su.gene_calc(arguments['gene_name'][0], True)
            elif 'gene_name' in arguments and 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = su.gene_calc(arguments['gene_name'][0], False)
                else:
                    contents = {'ERROR': "json argument must be 1 to return json output"}
            else:
                contents = {'ERROR': 'endpoint arguments are not correct for this endpoint'}

        elif path_name == "/listSpecies":
            if 'limit' in arguments and not 'json' in arguments:
                contents = su.list_species(arguments['limit'][0], True)
            elif 'limit' in arguments and 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = su.list_species(arguments['limit'][0], False)
                else:
                    contents = {'ERROR': 'json argument must be 1 to return json output'}
            else:
                contents = {'ERROR': 'endpoint arguments are not correct for this endpoint (Check you introduced a limit also!'}

        elif path_name == "/karyotype":
            if 'species' in arguments and not 'json' in arguments:
                contents = su.karyotype_by_specie(arguments['species'][0], True)
            elif 'species' in arguments and 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = su.karyotype_by_specie(arguments['species'][0], False)
                else:
                    contents = {'ERROR': 'json argument must be 1 to return json output'}
            else:
                contents = {'ERROR': 'endpoint arguments are not correct for this endpoint'}

        elif path_name == "/chromosome_length":
            if 'species' in arguments and 'length' in arguments and not 'json' in arguments:
                contents = su.chromosome_length(arguments['species'][0],
                                                  arguments['length'][0], True)
            elif 'species' in arguments and 'length' in arguments and 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = su.chromosome_length(arguments['species'][0],
                                                  arguments['length'][0], False)
                else:
                    contents = {'ERROR': 'json argument must be 1 to return json output'}
            else:
                contents = {'ERROR': 'endpoint arguments are not correct for this endpoint'}

        else:
            contents = su.read_template_html_file("./html/error.html").render()

        # Generating the response message
        if type(contents) == str:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            # The header is finished
            self.end_headers()
            # Send the response message
            self.wfile.write(contents.encode())
        elif type(contents) == dict:
            contents_str = json.dumps(contents)
            self.send_response(200)
            self.send_header('Content-Type', 'text/json')
            self.send_header('Content-Length', len(contents_str.encode()))
            # The header is finished
            self.end_headers()
            # Send the response message
            self.wfile.write(contents_str.encode())
        else:
            pass

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