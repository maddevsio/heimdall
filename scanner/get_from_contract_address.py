import requests
import json
import click

URL = 'https://api.infura.io/v1/jsonrpc/'
METHOD  =  'eth_getCode' 


def get_bytecode(address, network):
    NETWORK = network + '/'
    endpoint = URL + NETWORK + METHOD 
    payload = {'params': json.dumps(["{}".format(address), "latest"])}

    response = requests.get(endpoint, params=payload)
    if 400 <= response.status_code < 404:
        return print("No data was found")

    return response.json()['result']


@click.command()
@click.option('--address', '-a',  required=True, help="Set address to get the bytecode")
@click.option('--network', '-n',  required=True, help="Set network")
def main(address, network):
    bytecode = get_bytecode(address, network)
    print(bytecode)

if __name__ == '__main__':
    main()