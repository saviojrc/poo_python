import datetime
import unittest
from metodos_abstratos_e_metodos_de_classe.data import Data

class MyTestCase(unittest.TestCase):
    def test_something(self):
        data_string = '31-12-2024'

        data = Data(31,12,2024)
        print(data)
        outra_data = Data.de_string(data_string)
        print(outra_data)
        valido = data.is_data_valid(data_string)
        print(valido)

if __name__ == '__main__':
    unittest.main()
