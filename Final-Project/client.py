import http.client
import json

SERVER = "rest.ensembl.org"
action = input("Choose an endpoint: ")

if action == "list_especies":
    endpoint = "/info/species"
    parameters = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", endpoint + parameters)
    response = connection.getresponse()
    response = json.loads(response.read().decode())
    print(json.dumps(response, indent=4, sort_keys=True))



