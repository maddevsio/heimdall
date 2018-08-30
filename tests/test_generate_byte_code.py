import unittest
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
scanner = os.path.normpath(os.path.join(current_dir,  '../scanner'))
sys.path.append(scanner)

from generate_byte_code import *


class TestMethodsOfGenerate(unittest.TestCase):
    def test_extract_bytecode(self):    
        compiled = {
                            'TESTToken':{'bin': {123}, 'abi': {'test1'}}, 
                            'SafeMath':{'bin': {123}, 'abi':{ 'test2'}}
                            }       
        contract_name = ['TESTToken', 'SafeMath']
        output = extract_bytecode(compiled, contract_name)
        self.assertEqual(output, [{'TESTToken': {'bytecode': {123}, 'abi': {'test1'}}}, {'SafeMath': {'bytecode': {123}, 'abi': {'test2'}}}])
    
    def test_get_contracts(self):
        output = get_contracts({'test': 123, 'test2': 321})
        self.assertEqual(list(output), ['test', 'test2'])

    def test_compiled_smart_contract(self):
        output = compiled_smart_contract('tests/neureal_token_test.sol')
        self.assertTrue('<stdin>:SafeMath' in output)
    

if __name__ == '__main__':
    unittest.main()
