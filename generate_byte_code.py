import click

from solc import compile_source


def convert_to_byte_code(file, contract):
    path_to_file = open(file, mode='r')
    compiled_sol = compile_source(path_to_file.read())

    contract_interface = compiled_sol['<stdin>:{}'.format(str(contract))]

    print(contract_interface['bin'])


def get_contract_names(file):
    path_to_file = open(file, mode='r')
    compiled_sol = compile_source(path_to_file.read())

    conracts_name = compiled_sol['<stdin>:SafeMath']['ast']['attributes']['exportedSymbols']
    print(conracts_name)
    # key = list(a.keys())


@click.command()
@click.option('-t', type=click.Choice(['bytecode', 'abi']), help="The flag define which type you need.")
@click.option('--solidity-file', '-s', help="The flag define path to solidity file.")
@click.option('--contract', '-c', help="The flag define which contract must be convert.")
def main(solidity_file, t, contract):
    if t == 'bytecode':
        convert_to_byte_code(solidity_file, contract)
    if not contract:
        get_contract_names(solidity_file)


if __name__ == '__main__':
    main()
