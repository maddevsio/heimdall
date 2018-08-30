import click
import json

from solc import compile_source


def extract_bytecode(compiled, contract_name):
    """
    :compiled - content from smart contract file
    :contract_name - list / empty of contract names
    """
    return [{
        contract: {
            'bytecode': compiled[contract]['bin'],
            'abi': compiled[contract]['abi']
        }
    } for contract in contract_name]


def get_contracts(compiled):
    return compiled.keys()

def compiled_smart_contract(solidity_file):
    with open(solidity_file, 'r') as f:
        smart_contract = f.read()
        return compile_source(smart_contract)


@click.command()
@click.option('--solidity-file', '-s', help="The flag define path to solidity file.")
@click.option('--contract', '-c', help="The flag define which contract must be convert.")
@click.option('--output', '-o', help="Print to stdout.")
def main(solidity_file, output, contract):
    compiled = compiled_smart_contract(solidity_file)

    if not contract:
        contract = list(get_contracts(compiled))
    else:
        contract = ['<stdin>:' + contract, ]

    result = extract_bytecode(compiled, contract)
    return resolve_output(result, output)


def resolve_output(result, output):
    if output == 'stdout':
        print(result)
        return
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()