import click

from solc import compile_source


def convert_to_byte_code(file, contract_name):
    report = {}
    with open(file, 'r') as f:
        content = f.read()
    compiled_sol = compile_source(content)
    if type(contract_name) is list:
        for contract in contract_name:
            contract_interface = compiled_sol[str(contract)]
            report[str(contract).split('<stdin>:')[1]] = {'bytecode': contract_interface['bin'],
                                                          'abi': compiled_sol[str(contract)]['abi']}
        print(report)
    else:
        contract_interface = compiled_sol['<stdin>:{}'.format(str(contract_name))]
        report[str(contract_name)] = {'bytecode': contract_interface['bin'], 'abi': compiled_sol['<stdin>:' +
                                                                                                 str(contract_name)]
                                                                                                ['abi']}
        print(report)


def get_contract_names(file):
    with open(file, 'r') as f:
        content = f.read()
    compiled_sol = compile_source(content)
    return convert_to_byte_code(file, contract_name=list(compiled_sol.keys()))


@click.command()
@click.option('-t', type=click.Choice(['bytecode', 'abi']), help="The flag define which type you need.")
@click.option('--solidity-file', '-s', help="The flag define path to solidity file.")
@click.option('--contract', '-c', help="The flag define which contract must be convert.")
def main(solidity_file, t, contract):
    if t == 'bytecode':
        if not contract:
            return get_contract_names(solidity_file)
        convert_to_byte_code(solidity_file, contract)


if __name__ == '__main__':
    main()
