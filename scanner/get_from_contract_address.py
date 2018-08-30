import requests
import json
import click

def get_bytecode(address):
    endpoint = 'https://api.infura.io/v1/jsonrpc/mainnet/eth_getCode' + \
                            '?params=["%s", "latest"]' % address
    response = requests.get(endpoint).json()
    return response['result']

@click.command()
@click.option('--address', '-a',  required=True, help="Set address to get the bytecode")
def main(address):
    bytecode = get_bytecode(address)
    print(bytecode)

if __name__ == '__main__':
    main()