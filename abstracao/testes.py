import unittest
from abstracao.cachorro import Cachorro

class MyTestCase(unittest.TestCase):
    def test_something(self):
        cachorro = Cachorro()
        print(cachorro.dizer_algo())
        assert "AU AU" , cachorro.dizer_algo()


if __name__ == '__main__':
    unittest.main()
