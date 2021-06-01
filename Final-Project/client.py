import http.client
import json

def server_request(connection, endpoint, parameters):

    connection.request("GET", endpoint + parameters)
    response = connection.getresponse()
    print("Response received!: ", response.status, response.reason)
    try:
        json_response = json.loads(response.read().decode())
        return json.dumps(json_response, indent=4, sort_keys=True), response.status
    except:
        if response.status == 200:
            return "Request to index does not return json", response.status
        else:
            return "The endpoint is not valid", response.status

limit = 10
species = 'mouse'
length = 18
gene_name = 'FRAT1'
SERVER = 'localhost:8080'
ENDPOINT_LS = ['/listSpecies', '/karyotype', '/chromosome_length', '/geneSeq', '/geneInfo', '/geneCalc']
PARAMETERS_LS = ['?limit={}&json=1'.format(limit), '?species={}&json=1'.format(species), '?species={}&length={}&json=1'.format(species, length), '?gene_name={}&json=1'.format(gene_name), '?gene_name={}&json=1'.format(gene_name), '?gene_name={}&json=1'.format(gene_name)]

connection = http.client.HTTPConnection(SERVER)
for endpoint, parameters in zip(ENDPOINT_LS, PARAMETERS_LS):
    print(endpoint)
    msg,status = server_request(connection, endpoint, parameters)
    print(msg)
    print(status)
# localhost:8080/listSpecies?limit=10&json=1
# http://localhost:8080/chromosome_length?species=mouse&length=18
# http://localhost:8080/geneSeq?gene_name=FRAT1