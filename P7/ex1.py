import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

# To create the query, first we establish the connection:

connection = http.client.HTTPConnection(SERVER)
# Now, once we have the connection, we can create the queries:
connection.request("GET", ENDPOINT + PARAMS) # As this already points to the server, we only need to add the endpoint and the parameters.
response = connection.getresponse()
print(response) # If we print this, we have a http response object, and that's not valid for us, because we cannot work with that (we need to transform it). We can also return "response.status" to see if it is running correctly or not.
answer_decoded = response.read().decode()  # The way to read and print objects is this one, because if we do not use that function, we are only printing where the object is located in memory.
print(type(answer_decoded), answer_decoded)
# As we have an string because we have decoded the bytes, we will tranform it into a dictionary to have json data.
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response) # Now, we can access the key to get the number.
if dict_response["ping"] == 1:
    print("PING OK!!! The database is running")
else:
    print("Database is down!!!!!")


# http://rest.ensembl.org/sequence/id/ENSG00000080603?content-type=application/json  IF WE USE THIS LINK, WE WILL GET THE BASES OF OUR GENE + SOME EXTRA INFORMATION, BUT IN A JSON FORMAT, BECAUSE WE ARE ADDING THAT PARAMETERS AFTER THE END OF THE NAME OF THE GENE.