import click

from solc import compile_source


def convert_to_byte_code(file):
    path_to_file = open(file, mode='r')
    compiled_sol = compile_source(path_to_file.read())
    contract_interface = compiled_sol['<stdin>:{}'.format(str(file.split('.sol')[0]))]
    print(contract_interface['bin'])


@click.command()
@click.option('--type', help="format to convert")
@click.option('--file', help="file to convert")
def main(type, file):
    if type == 'byte':
        convert_to_byte_code(file)


if __name__ == '__main__':
    main()
