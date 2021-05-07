# We will follow the same procedure than in Ex.1

import http.client
import json

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSMUSG00000062960",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"  # We need to add something else afterwards.
ID = DICT_GENES["MIR633"]
PARAMETERS = "?content-type=application/json"

# We carry out the request, by establishing the connection with the server.

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + ID + PARAMETERS)
response = connection.getresponse()
print("Response received!: ", response.status, response.reason)
if response.status == 200:
    # Now, we need to get the response:
    response = json.loads(response.read().decode())
    #print(response)

    # In order to print that dictionary in a better format, we will use the following, that will be transforming back the dictionary to a string. We can also use the argument "indent=4,sort_keys=True" to print a dictionary properly formatted.
    print(json.dumps(response, indent=4, sort_keys=True))

    # As we need to print it in different lines and I can access to the keys of the dictionary I have obatained previously:

    print("Gene: ", ID)
    print("Description: ", response["desc"])
    print("Bases: ", response["seq"])
elif response.status == 404:
    print("Check if the ENDPOINT was correctly written !!!!!!!!!!!!!!!!!")

