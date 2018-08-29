import click

from solc import compile_source


def convert_to_byte_code(file, contract_name):
    report = {}
    compiled_sol = compile_source(open(file, mode='r').read())
    if type(contract_name) is list:
        for contract in contract_name:
            contract_interface = compiled_sol['<stdin>:{}'.format(str(contract))]
            report[str(contract)] = {'bytecode': contract_interface['bin'], 'abi': compiled_sol['<stdin>:' +
                                                                                                str(contract)]['abi']}
        print(report)
    else:
        contract_interface = compiled_sol['<stdin>:{}'.format(str(contract_name))]
        report[str(contract_name)] = {'bytecode': contract_interface['bin'], 'abi': compiled_sol['<stdin>:' +
                                                                                                 str(contract_name)]
                                                                                                ['abi']}
        print(report)


def get_contract_names(file):
    path_to_file = open(file, mode='r')
    compiled_sol = compile_source(path_to_file.read())

    name_of_contract = compiled_sol['<stdin>:SafeMath']['ast']['attributes']['exportedSymbols']
    return convert_to_byte_code(file, contract_name=list(name_of_contract.keys()))


@click.command()
@click.option('-t', type=click.Choice(['bytecode', 'abi']), help="The flag define which type you need.")
@click.option('--solidity-file', '-s', help="The flag define path to solidity file.")
@click.option('--contract', '-c', help="The flag define which contract must be convert.")
def main(solidity_file, t, contract):
    if t == 'bytecode':
        if not contract:
            get_contract_names(solidity_file)
        else:
            convert_to_byte_code(solidity_file, contract)


if __name__ == '__main__':
    main()
