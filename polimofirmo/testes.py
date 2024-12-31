import unittest
from polimofirmo.model.formas_geometricas.quadrado import Quadrado

class MyTestCase(unittest.TestCase):
    def test_something(self):
        quadrado = Quadrado(2)
        print('Area : %d' % quadrado.area())
        print('Perimetro: %d' % quadrado.perimetro())




if __name__ == '__main__':
    unittest.main()
