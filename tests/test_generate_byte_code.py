import unittest
from scanner.generate_byte_code import *


class TestMethodsOfGenerate(unittest.TestCase):

    def test_convert_to_byte_code(self):
        file_to_assert = open('assert_with_name_test.txt', mode='r').read()
        convert = convert_to_byte_code('tests/neureal_token_test.sol', 'TESTToken')
        self.assertEqual(convert, file_to_assert)

    def test_get_contract_names(self):
        file_to_assert = open('assert_without_name_test.txt', mode='r').read()
        convert = get_contract_names('tests/neureal_token_test.sol')
        self.assertEqual(convert, file_to_assert)


if __name__ == '__main__':
    unittest.main()
